"""Deterministic QA-focused business rule enrichment.

The engine consumes existing artifacts only. It filters and consolidates
low-value CRUD rules, preserves source traceability, and adds high-value rules
from PMWebX workflow/RACI/document patterns found in artifact names.
"""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from collections.abc import Iterable

from app.models.discovery import DiscoveryResult
from app.models.domain import DomainModel
from app.models.enriched_business_rules import (
    EnrichedBusinessRule,
    EnrichedBusinessRulesModel,
    QualityReport,
    RuleClassification,
)
from app.models.feature import FeatureInventory
from app.models.rule_catalog import CatalogRule, RuleCatalogModel
from app.models.traceability import FeatureTrace, TraceabilityModel

_TOKEN_RE = re.compile(r"[A-Za-z]+|\d+")

_VALUE_BY_CLASSIFICATION: dict[RuleClassification, int] = {
    "CRUD": 2,
    "Authorization": 8,
    "Workflow": 10,
    "State Transition": 10,
    "Validation": 9,
    "Calculation": 8,
    "Notification": 8,
    "Integration": 7,
    "Audit": 8,
    "RACI": 10,
    "Document Management": 8,
    "Scheduling": 8,
    "Configuration": 6,
}


def build_enriched_business_rules(
    application: DiscoveryResult,
    inventory: FeatureInventory,
    domain_model: DomainModel,
    traceability: TraceabilityModel,
    catalog: RuleCatalogModel,
) -> tuple[EnrichedBusinessRulesModel, QualityReport]:
    """Build enriched rules and quality metrics from existing artifacts."""

    del application, inventory, domain_model  # Context remains explicit in the signature.
    source_rules = list(catalog.rules)
    source_crud_rules = [rule for rule in source_rules if classify_rule(rule) == "CRUD"]
    enriched: list[EnrichedBusinessRule] = []

    enriched.extend(_consolidate_crud_rules(source_crud_rules))
    enriched.extend(_non_crud_catalog_rules(source_rules))
    enriched.extend(_implicit_pattern_rules(traceability, source_rules))

    enriched = _dedupe_enriched_rules(enriched)
    for index, rule in enumerate(sorted(enriched, key=_rule_sort_key), start=1):
        rule.id = f"EBR-{index:04d}"

    model = EnrichedBusinessRulesModel(rules=sorted(enriched, key=lambda rule: rule.id))
    report = build_quality_report(model, len(source_rules), len(source_crud_rules))
    return model, report


def build_quality_report(
    model: EnrichedBusinessRulesModel,
    source_catalog_rules: int,
    source_crud_rules: int,
) -> QualityReport:
    """Calculate deterministic quality metrics for enriched rules."""

    total = len(model.rules)
    counts = Counter(rule.classification for rule in model.rules)
    consolidated = sum(1 for rule in model.rules if "consolidated-crud" in rule.tags)
    average_score = (
        round(sum(rule.testing_value_score for rule in model.rules) / total, 2)
        if total
        else 0.0
    )
    crud_reduction = (
        round((source_crud_rules - counts["CRUD"]) / source_crud_rules * 100, 2)
        if source_crud_rules
        else 0.0
    )
    top_100 = sorted(
        model.rules,
        key=lambda rule: (-rule.testing_value_score, -rule.confidence, rule.domain, rule.rule),
    )[:100]
    return QualityReport(
        total_rules=total,
        source_catalog_rules=source_catalog_rules,
        source_crud_rules=source_crud_rules,
        crud_rules=counts["CRUD"],
        workflow_rules=counts["Workflow"] + counts["State Transition"],
        authorization_rules=counts["Authorization"],
        validation_rules=counts["Validation"],
        raci_rules=counts["RACI"],
        consolidated_rules=consolidated,
        average_testing_value_score=average_score,
        crud_reduction_percentage=crud_reduction,
        top_100_highest_value_rules=top_100,
    )


def render_enriched_markdown(model: EnrichedBusinessRulesModel, report: QualityReport) -> str:
    """Render QA-focused rules in a human-readable format."""

    lines = [
        "# Enriched Business Rules",
        "",
        f"Total rules: {report.total_rules}",
        f"Average testing value score: {report.average_testing_value_score}",
        f"CRUD reduction: {report.crud_reduction_percentage}%",
        "",
    ]
    for domain in sorted({rule.domain for rule in model.rules}, key=str.lower):
        lines.extend([f"## {domain}", ""])
        for rule in [item for item in model.rules if item.domain == domain]:
            lines.extend(
                [
                    f"### {rule.id}",
                    "",
                    rule.rule,
                    "",
                    f"Classification: {rule.classification}",
                    f"Testing Value Score: {rule.testing_value_score}",
                    f"Business Criticality: {rule.business_criticality}",
                    f"Confidence: {rule.confidence}",
                    f"Source Rule IDs: {', '.join(rule.source_rule_ids) if rule.source_rule_ids else 'None'}",
                    f"Evidence: {'; '.join(rule.evidence) if rule.evidence else 'None'}",
                    f"Tags: {', '.join(rule.tags) if rule.tags else 'None'}",
                    "",
                ]
            )
    return "\n".join(lines).rstrip() + "\n"


def classify_rule(rule: CatalogRule) -> RuleClassification:
    """Classify a catalog rule into QA enrichment categories."""

    text = f"{rule.domain} {rule.feature} {rule.title} {rule.description} {' '.join(rule.tags)}".lower()
    if _is_crud_text(text):
        return "CRUD"
    if _has(text, "accountable", "responsible", "consulted", "informed", "raci", "assignee", "delegate", "delegation"):
        return "RACI"
    if _has(text, "review", "state", "status", "transition", "progression", "progress", "stagegate", "stage gate", "closure", "close", "reopen"):
        return "State Transition"
    if _has(text, "mandatory", "required", "cannot", "must be completed", "before", "validation", "validate"):
        return "Validation"
    if _has(text, "notification", "notify", "message", "email", "alert"):
        return "Notification"
    if _has(text, "audit", "log", "history", "revision", "version"):
        return "Audit"
    if _has(text, "authenticate", "authorization", "authorized", "permission", "role", "access", "login", "password", "otp"):
        return "Authorization"
    if _has(text, "document", "attachment", "file", "template", "upload", "download"):
        return "Document Management"
    if _has(text, "milestone", "schedule", "planner", "calendar", "timeline"):
        return "Scheduling"
    if _has(text, "integration", "sync", "callback", "redis", "primavera", "pmweb"):
        return "Integration"
    if _has(text, "calculate", "calculation", "score", "amount", "cost", "price"):
        return "Calculation"
    if _has(text, "config", "configuration", "setting", "master", "mapping", "definition"):
        return "Configuration"
    if _has(text, "workflow", "approval", "approve", "reject", "submit", "complete", "checklist", "activity"):
        return "Workflow"
    return "Workflow" if rule.rule_type == "Workflow" else "Validation"


def _non_crud_catalog_rules(source_rules: list[CatalogRule]) -> list[EnrichedBusinessRule]:
    enriched: list[EnrichedBusinessRule] = []
    for rule in source_rules:
        classification = classify_rule(rule)
        if classification == "CRUD":
            continue
        enriched.append(
            _enriched_rule(
                source_rule_ids=[rule.id],
                classification=classification,
                confidence=rule.confidence or 0.7,
                rule=_rewrite_rule(rule, classification),
                domain=rule.domain,
                feature=rule.feature,
                evidence=list(rule.evidence),
                tags=list(rule.tags),
            )
        )
    return enriched


def _consolidate_crud_rules(source_rules: list[CatalogRule]) -> list[EnrichedBusinessRule]:
    buckets: dict[tuple[str, str], list[CatalogRule]] = defaultdict(list)
    for rule in source_rules:
        buckets[(rule.domain, _crud_action(rule))].append(rule)

    enriched: list[EnrichedBusinessRule] = []
    for (domain, action), rules in sorted(buckets.items()):
        concept = _domain_concept(domain)
        verb = {
            "create": "created",
            "retrieve": "retrieved",
            "update": "updated",
            "delete": "deleted only through explicit authorization",
        }[action]
        score = 1 if action == "retrieve" else 2
        criticality = "Low" if action == "retrieve" else "Medium"
        enriched.append(
            EnrichedBusinessRule(
                id="",
                source_rule_ids=sorted(rule.id for rule in rules),
                classification="CRUD",
                testing_value_score=score,
                business_criticality=criticality,
                confidence=round(max((rule.confidence or 0.5) for rule in rules), 2),
                rule=f"{concept} records must be {verb} through controlled system actions.",
                domain=domain,
                feature=concept,
                evidence=[f"Consolidated {len(rules)} repetitive CRUD rule(s)."],
                tags=["crud", "consolidated-crud", action],
            )
        )
    return enriched


def _implicit_pattern_rules(
    traceability: TraceabilityModel,
    source_rules: list[CatalogRule],
) -> list[EnrichedBusinessRule]:
    source_by_domain = _source_rules_by_domain(source_rules)
    enriched: list[EnrichedBusinessRule] = []
    for domain in traceability.domains:
        for feature in domain.features:
            tokens = _feature_tokens(feature)
            source_ids = _source_ids_for_feature(source_by_domain[domain.name], feature)
            if not source_ids:
                continue
            feature_label = _feature_label(feature.name)
            evidence = _feature_evidence(feature)

            if "checklist" in tokens:
                enriched.append(
                    _pattern_rule(
                        source_ids,
                        "Validation",
                        "Critical",
                        0.88,
                        "Mandatory checklist items must be completed before workflow progression.",
                        domain.name,
                        feature_label,
                        evidence,
                        ["checklist", "mandatory", "workflow"],
                    )
                )
            if tokens & {"approval", "approve", "raci", "accountable", "responsible"}:
                enriched.append(
                    _pattern_rule(
                        source_ids,
                        "RACI",
                        "Critical",
                        0.9,
                        "Only Accountable users may approve workflow items.",
                        domain.name,
                        feature_label,
                        evidence,
                        ["raci", "approval", "accountable"],
                    )
                )
            if tokens & {"activity", "workflow", "stagegate", "stage", "status", "state", "approval"}:
                enriched.append(
                    _pattern_rule(
                        source_ids,
                        "State Transition",
                        "Critical",
                        0.86,
                        f"{feature_label} must progress through defined workflow states.",
                        domain.name,
                        feature_label,
                        evidence,
                        ["workflow", "state-transition"],
                    )
                )
            if "activity" in tokens and tokens & {"document", "file", "attachment", "upload"}:
                enriched.append(
                    _pattern_rule(
                        source_ids,
                        "Validation",
                        "Critical",
                        0.84,
                        "Activity status cannot move to Review without required documents.",
                        domain.name,
                        feature_label,
                        evidence,
                        ["activity", "document", "review"],
                    )
                )
            if tokens & {"notification", "notify", "message"}:
                enriched.append(
                    _pattern_rule(
                        source_ids,
                        "Notification",
                        "High",
                        0.82,
                        "Notifications must be generated on workflow state changes.",
                        domain.name,
                        feature_label,
                        evidence,
                        ["notification", "workflow"],
                    )
                )
            if tokens & {"thread", "comment", "discussion"}:
                enriched.append(
                    _pattern_rule(
                        source_ids,
                        "Audit",
                        "High",
                        0.78,
                        "Collaboration threads must preserve comments and attachments with the related business record.",
                        domain.name,
                        feature_label,
                        evidence,
                        ["collaboration", "audit"],
                    )
                )
            if tokens & {"delegation", "delegate"}:
                enriched.append(
                    _pattern_rule(
                        source_ids,
                        "RACI",
                        "High",
                        0.82,
                        "Delegation changes must preserve original accountability and audit history.",
                        domain.name,
                        feature_label,
                        evidence,
                        ["delegation", "raci", "audit"],
                    )
                )
            if tokens & {"milestone", "planner", "schedule", "timeline", "stagegate"}:
                enriched.append(
                    _pattern_rule(
                        source_ids,
                        "Scheduling",
                        "High",
                        0.8,
                        "Milestones and stage gates must be completed before the next project phase starts.",
                        domain.name,
                        feature_label,
                        evidence,
                        ["scheduling", "stagegate"],
                    )
                )
            if tokens & {"version", "revision"}:
                enriched.append(
                    _pattern_rule(
                        source_ids,
                        "Audit",
                        "High",
                        0.8,
                        "Version and revision changes must preserve audit history.",
                        domain.name,
                        feature_label,
                        evidence,
                        ["version", "audit"],
                    )
                )
    return enriched


def _enriched_rule(
    source_rule_ids: list[str],
    classification: RuleClassification,
    confidence: float,
    rule: str,
    domain: str,
    feature: str,
    evidence: list[str],
    tags: list[str],
) -> EnrichedBusinessRule:
    score = _VALUE_BY_CLASSIFICATION[classification]
    return EnrichedBusinessRule(
        id="",
        source_rule_ids=sorted(set(source_rule_ids)),
        classification=classification,
        testing_value_score=score,
        business_criticality=_criticality(classification, score, rule),
        confidence=round(confidence, 2),
        rule=rule,
        domain=domain,
        feature=feature,
        evidence=evidence,
        tags=_dedupe([classification.lower(), *tags]),
    )


def _pattern_rule(
    source_rule_ids: list[str],
    classification: RuleClassification,
    criticality: str,
    confidence: float,
    rule: str,
    domain: str,
    feature: str,
    evidence: list[str],
    tags: list[str],
) -> EnrichedBusinessRule:
    enriched = _enriched_rule(
        source_rule_ids,
        classification,
        confidence,
        rule,
        domain,
        feature,
        evidence,
        tags,
    )
    enriched.business_criticality = criticality  # type: ignore[assignment]
    return enriched


def _rewrite_rule(rule: CatalogRule, classification: RuleClassification) -> str:
    text = rule.description.rstrip(".")
    if classification == "Workflow" and "records must move through defined workflow states" in text:
        return f"{rule.feature or 'Records'} must progress through defined workflow states."
    return text + "."


def _is_crud_text(text: str) -> bool:
    return (
        "records must be created through controlled api actions" in text
        or "records must be updated through controlled api actions" in text
        or "records must be retrievable for authorized users" in text
        or "deletion must be explicit and authorized" in text
        or "created through controlled system actions" in text
    )


def _crud_action(rule: CatalogRule) -> str:
    text = f"{rule.title} {rule.description}".lower()
    if "retrievable" in text:
        return "retrieve"
    if "updated" in text:
        return "update"
    if "deletion" in text or "deleted" in text:
        return "delete"
    return "create"


def _criticality(classification: RuleClassification, score: int, rule: str) -> str:
    text = rule.lower()
    if score >= 10 or "login" in text or "mandatory checklist" in text:
        return "Critical"
    if score >= 8:
        return "High"
    if score >= 6:
        return "Medium"
    return "Low"


def _feature_tokens(feature: FeatureTrace) -> set[str]:
    return _tokens(
        [feature.name]
        + feature.routes
        + feature.apis
        + feature.collections
        + feature.components
        + feature.services
    )


def _tokens(values: Iterable[str]) -> set[str]:
    tokens: set[str] = set()
    for value in values:
        normalized = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", value).lower()
        tokens.update(token for token in _TOKEN_RE.findall(normalized) if token)
    return tokens


def _feature_label(feature_name: str) -> str:
    label = feature_name.replace(" Management", "")
    label = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", label)
    return re.sub(r"[^A-Za-z0-9]+", " ", label).strip() or feature_name


def _feature_evidence(feature: FeatureTrace) -> list[str]:
    evidence: list[str] = [f"Feature: {feature.name}"]
    if feature.apis:
        evidence.append(f"APIs: {', '.join(feature.apis[:8])}")
    if feature.collections:
        evidence.append(f"Collections: {', '.join(feature.collections[:8])}")
    if feature.routes:
        evidence.append(f"Routes: {', '.join(feature.routes[:8])}")
    return evidence


def _source_rules_by_domain(source_rules: list[CatalogRule]) -> dict[str, list[CatalogRule]]:
    by_domain: dict[str, list[CatalogRule]] = defaultdict(list)
    for rule in source_rules:
        by_domain[rule.domain].append(rule)
    return by_domain


def _source_ids_for_feature(source_rules: list[CatalogRule], feature: FeatureTrace) -> list[str]:
    feature_key = _normalize(feature.name)
    ids: list[str] = []
    for rule in source_rules:
        if _normalize(rule.feature) and (
            _normalize(rule.feature) in feature_key or feature_key in _normalize(rule.feature)
        ):
            ids.append(rule.id)
            continue
        if any(token in _normalize(rule.description) for token in _feature_tokens(feature)):
            ids.append(rule.id)
    return sorted(set(ids))[:50]


def _normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]", "", value.lower().replace("management", ""))


def _dedupe_enriched_rules(rules: list[EnrichedBusinessRule]) -> list[EnrichedBusinessRule]:
    by_key: dict[tuple[str, str, str], EnrichedBusinessRule] = {}
    for rule in rules:
        key = (rule.domain, rule.classification, rule.rule.lower())
        existing = by_key.get(key)
        if existing is None:
            by_key[key] = rule
            continue
        existing.source_rule_ids = sorted(set(existing.source_rule_ids + rule.source_rule_ids))
        existing.evidence = _dedupe(existing.evidence + rule.evidence)
        existing.tags = _dedupe(existing.tags + rule.tags)
        existing.confidence = max(existing.confidence, rule.confidence)
    return list(by_key.values())


def _rule_sort_key(rule: EnrichedBusinessRule) -> tuple[str, int, str]:
    return (rule.domain.lower(), -rule.testing_value_score, rule.rule.lower())


def _domain_concept(domain: str) -> str:
    return domain.replace(" Management", "").replace("Lifecycle", "lifecycle")


def _has(text: str, *values: str) -> bool:
    return any(value in text for value in values)


def _dedupe(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value and value not in seen:
            seen.add(value)
            result.append(value)
    return result
