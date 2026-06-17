"""Deterministic business rule inference.

Consumes existing pipeline artifacts only:

* ``application.json``         — application context such as detected roles.
* ``feature-inventory.json``   — canonical business features.
* ``domain-model.json``        — domain ordering and feature grouping.
* ``traceability.json``        — domain -> feature -> relationships graph.

No LLMs, repository reads, or repository clones are performed here.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from app.models.business_rules import BusinessRule, BusinessRulesModel, DomainBusinessRules
from app.models.discovery import DiscoveryResult
from app.models.domain import DomainModel
from app.models.feature import FeatureInventory
from app.models.traceability import FeatureTrace, TraceabilityModel

_TOKEN_RE = re.compile(r"[A-Za-z]+|\d+")
_API_RE = re.compile(r"^([A-Z]+)\s+(.+)$")

_ACCESS_TOKENS = {"auth", "authentication", "login", "logout", "password", "session"}
_ROLE_TOKENS = {"role", "roles", "permission", "permissions", "user", "users", "access"}
_APPROVAL_TOKENS = {"approval", "approve", "approved", "approver", "reject", "rejected"}
_OWNERSHIP_TOKENS = {
    "accountable",
    "assignee",
    "assignment",
    "delegate",
    "delegation",
    "owner",
    "raci",
    "responsible",
}
_WORKFLOW_TOKENS = {
    "checklist",
    "complete",
    "execution",
    "stage",
    "state",
    "status",
    "step",
    "submit",
    "timeline",
    "workflow",
}
_DOCUMENT_TOKENS = {
    "attachment",
    "document",
    "documentmanager",
    "file",
    "form",
    "formtemplate",
    "template",
    "upload",
}
_COLLABORATION_TOKENS = {
    "chat",
    "comment",
    "discussion",
    "message",
    "notification",
    "thread",
}
_VENDOR_TOKENS = {"onboarding", "vendor", "supplier"}
_OPPORTUNITY_TOKENS = {"award", "enquiry", "eoi", "opportunity", "rfp"}
_CONFIG_TOKENS = {
    "admin",
    "config",
    "configuration",
    "definition",
    "function",
    "mapping",
    "master",
}


def _split_camel(value: str) -> str:
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", value)


def _tokens(values: Iterable[str]) -> set[str]:
    tokens: set[str] = set()
    for value in values:
        normalized = _split_camel(value).lower()
        tokens.update(token for token in _TOKEN_RE.findall(normalized) if token)
    return tokens


def _feature_label(name: str) -> str:
    label = name.replace(" Management", "").replace(" management", "")
    label = _split_camel(label)
    label = re.sub(r"[^A-Za-z0-9]+", " ", label).strip()
    return label or name


def _collection_label(name: str) -> str:
    label = _split_camel(name)
    label = re.sub(r"[^A-Za-z0-9]+", " ", label).strip()
    return label or name


def _api_parts(api: str) -> tuple[str, str] | None:
    match = _API_RE.match(api.strip())
    if not match:
        return None
    return match.group(1).upper(), match.group(2)


def _add_rule(candidates: dict[str, float], rule: str, confidence: float) -> None:
    candidates[rule] = max(round(confidence, 2), candidates.get(rule, 0.0))


def _has(tokens: set[str], expected: set[str]) -> bool:
    return bool(tokens & expected)


def _api_methods(feature: FeatureTrace) -> set[str]:
    methods: set[str] = set()
    for api in feature.apis:
        parts = _api_parts(api)
        if parts:
            methods.add(parts[0])
    return methods


def _route_tokens(feature: FeatureTrace) -> set[str]:
    return _tokens(feature.routes + feature.apis)


def _infer_feature_rules(feature: FeatureTrace, domain_name: str) -> dict[str, float]:
    candidates: dict[str, float] = {}
    label = _feature_label(feature.name)
    signal_tokens = _tokens(
        [feature.name]
        + feature.routes
        + feature.apis
        + feature.collections
        + feature.components
        + feature.services
    )
    route_tokens = _route_tokens(feature)
    methods = _api_methods(feature)

    if _has(signal_tokens, _ACCESS_TOKENS):
        _add_rule(
            candidates,
            f"{label} actions must authenticate users before access is granted.",
            0.86,
        )
    if _has(signal_tokens, _ROLE_TOKENS):
        _add_rule(
            candidates,
            f"Access to {label} must be governed by user roles and permissions.",
            0.84,
        )
    if _has(signal_tokens, _APPROVAL_TOKENS):
        _add_rule(
            candidates,
            f"{label} items require an approval decision before completion.",
            0.86,
        )
    if _has(signal_tokens, _OWNERSHIP_TOKENS):
        _add_rule(
            candidates,
            f"{label} work must have clear ownership before it can progress.",
            0.82,
        )
    if _has(signal_tokens, _APPROVAL_TOKENS) and _has(signal_tokens, _OWNERSHIP_TOKENS):
        _add_rule(
            candidates,
            f"Only accountable users should approve items in {label}.",
            0.88,
        )
    if _has(signal_tokens, _WORKFLOW_TOKENS):
        _add_rule(
            candidates,
            f"{label} records must move through defined workflow states.",
            0.78,
        )
    if _has(signal_tokens, _DOCUMENT_TOKENS):
        _add_rule(
            candidates,
            f"{label} documents must be created, stored, or updated through controlled document processes.",
            0.8,
        )
    if _has(signal_tokens, _COLLABORATION_TOKENS):
        _add_rule(
            candidates,
            f"{label} collaboration must keep messages and notifications linked to the related business record.",
            0.77,
        )
    if _has(signal_tokens, _VENDOR_TOKENS):
        _add_rule(
            candidates,
            f"{label} onboarding must be completed before active vendor participation.",
            0.83,
        )
    if _has(signal_tokens, _OPPORTUNITY_TOKENS):
        _add_rule(
            candidates,
            f"{label} records must follow the applicable opportunity lifecycle.",
            0.8,
        )
    if _has(signal_tokens, _CONFIG_TOKENS):
        _add_rule(
            candidates,
            f"{label} changes must be managed through administrative controls.",
            0.74,
        )

    if "POST" in methods:
        _add_rule(candidates, f"{label} records must be created through controlled API actions.", 0.72)
    if methods & {"PUT", "PATCH"}:
        _add_rule(candidates, f"{label} records must be updated through controlled API actions.", 0.72)
    if "DELETE" in methods:
        _add_rule(candidates, f"{label} deletion must be explicit and authorized.", 0.8)
    if "GET" in methods:
        _add_rule(candidates, f"{label} records must be retrievable for authorized users.", 0.64)

    if route_tokens & {"approve", "submit", "complete", "close", "cancel", "reject"}:
        _add_rule(
            candidates,
            f"{label} lifecycle actions must be enforced through workflow endpoints.",
            0.82,
        )
    if route_tokens & {"status", "state"}:
        _add_rule(candidates, f"{label} status must be maintained for each tracked record.", 0.78)
    if route_tokens & {"upload", "download", "import", "export"}:
        _add_rule(candidates, f"{label} file movement must use controlled import, export, upload, or download actions.", 0.76)

    if any(":id" in route or "/id" in route.lower() for route in feature.routes + feature.apis):
        _add_rule(
            candidates,
            f"Users must select an existing {label} record before detail actions are performed.",
            0.66,
        )
    if route_tokens & {"list", "search", "explorer", "browse"}:
        _add_rule(candidates, f"Users must be able to find {label} records before selecting detail actions.", 0.62)

    for collection in sorted(feature.collections, key=str.lower):
        _add_rule(
            candidates,
            f"The system must maintain {_collection_label(collection)} records as source data for {label}.",
            0.7,
        )

    if not candidates and (feature.routes or feature.apis or feature.collections):
        _add_rule(
            candidates,
            f"{label} business actions should be handled through the traced {domain_name} application surface.",
            0.55,
        )

    return candidates


def build_business_rules(
    application: DiscoveryResult,
    inventory: FeatureInventory,
    domain_model: DomainModel,
    traceability: TraceabilityModel,
) -> BusinessRulesModel:
    """Infer deterministic business rule candidates from existing artifacts."""

    feature_names = {feature.name for feature in inventory.features}
    domain_names = {domain.name for domain in domain_model.domains}
    emitted = 1
    domains: list[DomainBusinessRules] = []

    for domain in traceability.domains:
        candidates: dict[str, float] = {}

        if domain.name in domain_names and domain.name == "Identity and Access Management":
            _add_rule(candidates, "Identity actions must enforce authentication and authorization controls.", 0.86)
        if application.roles and domain.name == "Identity and Access Management":
            _add_rule(candidates, "Configured application roles must be used when evaluating protected actions.", 0.79)

        for feature in domain.features:
            if feature.name not in feature_names:
                continue
            for rule, confidence in _infer_feature_rules(feature, domain.name).items():
                _add_rule(candidates, rule, confidence)

        rules = [
            BusinessRule(id=f"BR-{index:03d}", rule=rule, confidence=confidence)
            for index, (rule, confidence) in enumerate(
                sorted(candidates.items(), key=lambda item: (-item[1], item[0].lower())),
                start=emitted,
            )
        ]
        emitted += len(rules)
        domains.append(DomainBusinessRules(domain=domain.name, rules=rules))

    return BusinessRulesModel(domains=domains)
