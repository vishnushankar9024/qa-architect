"""Governed business rule catalog service.

Builds a single source of truth from generated rules plus human-authored
overrides. The service consumes artifacts only and never reads or clones
repositories.
"""

from __future__ import annotations

import re
from collections import Counter
from pathlib import Path

from app import pipeline
from app.business_rules.artifacts import load_business_rules
from app.models.business_rules import BusinessRule, BusinessRulesModel, DomainBusinessRules
from app.models.rule_catalog import (
    CatalogRule,
    RuleCatalogModel,
    RuleCatalogSummary,
    RuleOverridesModel,
    RulePriority,
    RuleType,
)
from app.rule_catalog.artifacts import (
    ensure_overrides,
    load_catalog,
    load_markdown,
    rule_catalog_artifact_path,
    rule_catalog_markdown_path,
    save_catalog,
    save_markdown,
)


class RuleCatalogInputError(RuntimeError):
    """Raised when a required upstream catalog artifact is missing."""


class RuleCatalogService:
    """Builds and serves the governed business rule catalog."""

    STAGE = "rule-catalog"

    def build(self) -> RuleCatalogModel:
        """Merge generated rules and human overrides into catalog artifacts."""

        try:
            pipeline.require_previous_artifact(self.STAGE)
        except pipeline.MissingArtifactError as exc:
            raise RuleCatalogInputError(str(exc)) from exc

        generated = load_business_rules()
        if generated is None:  # pragma: no cover - guarded by require_previous_artifact
            raise RuleCatalogInputError("business-rules.json could not be loaded.")

        overrides = ensure_overrides()
        catalog = build_rule_catalog(generated, overrides)
        save_catalog(catalog)
        save_markdown(render_catalog_markdown(catalog))
        return catalog

    def load(self) -> RuleCatalogModel | None:
        """Return the last persisted rule catalog artifact, if any."""

        return load_catalog()

    def load_markdown(self) -> str | None:
        """Return the last persisted Markdown catalog, if any."""

        return load_markdown()

    def artifact_path(self) -> Path:
        """Return the path to the merged catalog artifact."""

        return rule_catalog_artifact_path()

    def markdown_path(self) -> Path:
        """Return the path to the Markdown catalog artifact."""

        return rule_catalog_markdown_path()


def build_rule_catalog(
    generated: BusinessRulesModel,
    overrides: RuleOverridesModel,
) -> RuleCatalogModel:
    """Merge generated and human rules into a governed catalog."""

    generated_rules = _catalog_generated_rules(generated)
    merged_by_id: dict[str, CatalogRule] = {rule.id: rule for rule in generated_rules}

    # Overrides use the same ID to replace generated values. A distinct ID is a
    # durable human rule that is appended and preserved across rebuilds.
    for override in overrides.rules:
        base = merged_by_id.get(override.id)
        merged_by_id[override.id] = _merge_override(base, override)

    rules = sorted(
        merged_by_id.values(),
        key=lambda rule: (rule.domain.lower(), rule.id.lower()),
    )
    summary = RuleCatalogSummary(
        total_generated_rules=len(generated_rules),
        total_human_rules=len(overrides.rules),
        total_merged_rules=len(rules),
        rules_by_status=dict(Counter(rule.status for rule in rules)),
        rules_by_domain=dict(Counter(rule.domain for rule in rules)),
    )
    return RuleCatalogModel(summary=summary, rules=rules)


def render_catalog_markdown(catalog: RuleCatalogModel) -> str:
    """Render a deterministic human-readable rule catalog."""

    lines: list[str] = []
    domains = sorted({rule.domain for rule in catalog.rules}, key=str.lower)
    for domain in domains:
        lines.append(f"# {domain}")
        lines.append("")
        for rule in [r for r in catalog.rules if r.domain == domain]:
            lines.extend(
                [
                    f"## {rule.id}",
                    "",
                    rule.title,
                    "",
                    rule.description,
                    "",
                    f"Priority: {rule.priority}",
                    "",
                    f"Status: {rule.status}",
                    "",
                    f"Source: {rule.source}",
                    "",
                    "Evidence:",
                ]
            )
            if rule.evidence:
                lines.extend(f"- {item}" for item in rule.evidence)
            else:
                lines.append("- None")
            lines.extend(
                [
                    "",
                    f"Tags: {', '.join(rule.tags) if rule.tags else 'None'}",
                    "",
                ]
            )
    return "\n".join(lines).rstrip() + "\n"


def _catalog_generated_rules(generated: BusinessRulesModel) -> list[CatalogRule]:
    rules: list[CatalogRule] = []
    for domain in generated.domains:
        for generated_rule in domain.rules:
            rules.append(_generated_to_catalog_rule(domain, generated_rule))
    return rules


def _generated_to_catalog_rule(
    domain: DomainBusinessRules,
    rule: BusinessRule,
) -> CatalogRule:
    rule_type = _classify_rule(rule.rule)
    return CatalogRule(
        id=rule.id,
        domain=domain.domain,
        feature=_feature_from_rule(rule.rule),
        title=_title_from_rule(rule.rule),
        description=rule.rule,
        rule_type=rule_type,
        priority=_priority_from_confidence(rule.confidence),
        source="Generated",
        author=None,
        status="Generated",
        evidence=[f"Generated from business-rules.json rule {rule.id}"],
        tags=_tags(domain.domain, rule.rule, rule_type),
        confidence=rule.confidence,
        generated_rule_id=rule.id,
    )


def _merge_override(base: CatalogRule | None, override: CatalogRule) -> CatalogRule:
    if base is None:
        return override
    return override.model_copy(
        update={
            "generated_rule_id": override.generated_rule_id or base.generated_rule_id or base.id,
            "confidence": override.confidence if override.confidence is not None else base.confidence,
            "evidence": _dedupe(base.evidence + override.evidence),
            "tags": _dedupe(base.tags + override.tags),
        }
    )


def _classify_rule(rule: str) -> RuleType:
    text = rule.lower()
    if any(word in text for word in ("authenticate", "authorization", "authorized", "access", "roles", "permissions", "accountable users")):
        return "Authorization"
    if any(word in text for word in ("approval", "approve", "workflow", "lifecycle", "states", "status", "progress", "onboarding", "completion")):
        return "Workflow"
    if any(word in text for word in ("source data", "records must be", "documents", "stored", "retrievable", "select an existing")):
        return "Data"
    if any(word in text for word in ("api", "endpoint", "import", "export", "upload", "download", "application surface")):
        return "Technical"
    return "Business"


def _priority_from_confidence(confidence: float) -> RulePriority:
    if confidence >= 0.85:
        return "High"
    if confidence >= 0.7:
        return "Medium"
    return "Low"


def _title_from_rule(rule: str) -> str:
    title = rule.strip().rstrip(".")
    return title[:120]


def _feature_from_rule(rule: str) -> str:
    words = re.split(r"\s+", rule.strip())
    if not words:
        return ""
    stop = {"the", "system", "users", "only", "access", "identity"}
    feature_words: list[str] = []
    for word in words[:4]:
        cleaned = re.sub(r"[^A-Za-z0-9]", "", word)
        if not cleaned or cleaned.lower() in stop:
            continue
        feature_words.append(cleaned)
        if len(feature_words) == 2:
            break
    return " ".join(feature_words)


def _tags(domain: str, rule: str, rule_type: RuleType) -> list[str]:
    values = [rule_type.lower()]
    values.extend(
        token
        for token in re.split(r"[^a-z0-9]+", f"{domain} {rule}".lower())
        if token and len(token) > 3
    )
    return _dedupe(values)[:12]


def _dedupe(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result
