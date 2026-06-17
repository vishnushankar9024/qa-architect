"""Deterministic grouping of features into business domains.

Input is a :class:`~app.models.feature.FeatureInventory` (loaded from
``feature-inventory.json``). Each feature is matched against a fixed keyword
taxonomy using the artifact fields already present in the inventory. Features
that match no domain are collected under "General".

No LLMs, no repository access — pure rule-based processing.
"""

from __future__ import annotations

import re

from app.models.domain import Domain, DomainModel
from collections.abc import Iterable

from app.models.feature import Feature, FeatureInventory

# Ordered taxonomy of business domains -> matching keyword tokens (singular,
# lowercased). Order is used as a deterministic tie-breaker.
_DOMAIN_TAXONOMY: tuple[tuple[str, set[str]], ...] = (
    (
        "Identity and Access Management",
        {
            "auth",
            "authentication",
            "login",
            "logout",
            "register",
            "registration",
            "signin",
            "signup",
            "session",
            "token",
            "oauth",
            "jwt",
            "credential",
            "rbac",
            "role",
            "permission",
            "user",
            "userlist",
            "usermanagement",
            "usermapping",
            "profile",
            "identity",
            "access",
            "allocated",
            "allocatedto",
            "approver",
            "createdby",
            "department",
            "designation",
            "linemanager",
            "manager",
            "otp",
            "password",
            "vendorlogin",
        },
    ),
    (
        "Opportunity and Procurement Lifecycle",
        {
            "opportunity",
            "opportunityhub",
            "opportunityconfiguration",
            "opportunitystructure",
            "enquiry",
            "enquiries",
            "enquiryhub",
            "enquirydetail",
            "eoi",
            "rfp",
            "award",
            "bid",
            "bidder",
            "commercial",
            "procurement",
            "quote",
            "quotation",
            "tender",
            "technicalbid",
            "vendorbid",
            "proposal",
            "lead",
            "deal",
        },
    ),
    (
        "Vendor and Organization Management",
        {
            "onboarding",
            "afteronboarding",
            "vendor",
            "company",
            "businessunit",
            "consultant",
            "contact",
            "organization",
            "organisation",
            "partner",
            "supplier",
            "replacement",
            "newreplacement",
            "accountsetup",
            "accountsetupsuccess",
        },
    ),
    (
        "Evaluation and Scoring",
        {
            "evaluation",
            "evaluator",
            "evaluatorhub",
            "score",
            "scoring",
            "evaluate",
            "ptc",
            "ptchub",
            "ptcdetail",
            "ptccounter",
            "raci",
        },
    ),
    (
        "Project and Activity Management",
        {
            "activity",
            "activitychecklist",
            "activityraci",
            "activityrelationship",
            "calendar",
            "dependency",
            "milestone",
            "phase",
            "primavera",
            "project",
            "projectallocation",
            "schedule",
            "stage",
            "stagegate",
            "task",
            "timeline",
        },
    ),
    (
        "Workflow, Approval and RACI",
        {
            "accountable",
            "accountableinput",
            "action",
            "actionitem",
            "approval",
            "approve",
            "assignee",
            "assignment",
            "cancel",
            "checklist",
            "close",
            "complete",
            "consult",
            "delegate",
            "delegation",
            "execute",
            "execution",
            "executionapproval",
            "informed",
            "initiate",
            "publish",
            "raci",
            "reject",
            "release",
            "reopen",
            "responsible",
            "restore",
            "return",
            "skip",
            "state",
            "status",
            "step",
            "submit",
            "workflow",
        },
    ),
    (
        "Document, File and Template Management",
        {
            "document",
            "documentmanager",
            "file",
            "activityfile",
            "attachment",
            "blueprint",
            "template",
            "formtemplate",
            "addendum",
            "blob",
            "download",
            "folder",
            "form",
            "getform",
            "image",
            "media",
            "pdf",
            "s3",
            "signedurl",
            "storage",
            "upload",
        },
    ),
    (
        "Configuration and Master Data",
        {
            "configuration",
            "config",
            "masterconfiguration",
            "setting",
            "setup",
            "administration",
            "admin",
            "addmapping",
            "mapping",
            "definition",
            "function",
            "appmodule",
            "capability",
            "category",
            "counter",
            "customfield",
            "field",
            "group",
            "listvalue",
            "lookup",
            "master",
            "metadata",
            "module",
            "process",
            "property",
            "section",
            "setting",
            "type",
        },
    ),
    (
        "Collaboration and Communication",
        {
            "notification",
            "chat",
            "thread",
            "threadscenter",
            "discussion",
            "comment",
            "email",
            "message",
            "community",
            "ask",
            "mail",
            "mention",
            "note",
            "question",
            "reply",
            "send",
            "subscriber",
        },
    ),
    (
        "Reporting, Audit and Logs",
        {
            "activitylog",
            "alldelegationlog",
            "analytics",
            "audit",
            "dashboard",
            "delegationlog",
            "export",
            "history",
            "log",
            "range",
            "report",
            "revision",
            "summary",
            "version",
        },
    ),
    (
        "Location and Asset Management",
        {
            "allocation",
            "area",
            "asset",
            "city",
            "country",
            "equipment",
            "location",
            "region",
            "site",
            "unit",
            "zone",
        },
    ),
)

_GENERAL_DOMAIN = "General"

# Tokens to ignore when tokenizing a feature name.
_STOPWORDS = {"management", "and", "the", "of", "for", "a", "an"}


def _singularize(word: str) -> str:
    w = word.lower()
    if len(w) <= 3:
        return w
    if w.endswith("ies"):
        return w[:-3] + "y"
    for suffix in ("ches", "shes", "sses", "xes", "zes"):
        if w.endswith(suffix):
            return w[:-2]
    if w.endswith("ss"):
        return w
    if w.endswith("s"):
        return w[:-1]
    return w


def _split_camel(value: str) -> str:
    """Add token boundaries to camel/Pascal case names."""

    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", value)


def _feature_values(feature: Feature) -> list[str]:
    """Return artifact fields that can carry business-domain signals."""

    values = [feature.name]
    values.extend(feature.modules)
    values.extend(feature.routes)
    values.extend(feature.apis)
    values.extend(feature.collections)
    return values


def _tokens(values: Iterable[str]) -> set[str]:
    """Tokenize artifact values into normalized, singularized keyword tokens."""

    tokens: set[str] = set()
    for value in values:
        normalized = _split_camel(value).lower()
        parts = re.split(r"[^a-z0-9]+", normalized)
        for part in parts:
            if not part or part in _STOPWORDS:
                continue
            tokens.add(part)
            tokens.add(_singularize(part))
        compact = re.sub(r"[^a-z0-9]", "", normalized)
        if compact and compact not in _STOPWORDS:
            tokens.add(compact)
            tokens.add(_singularize(compact))
    return tokens


def _keyword_score(tokens: set[str], keyword: str) -> int:
    """Score one taxonomy keyword against observed feature tokens."""

    if keyword in tokens:
        return 3
    if len(keyword) < 4:
        return 0
    for token in tokens:
        if len(token) >= 4 and (keyword in token or token in keyword):
            return 2 if len(keyword) >= 6 else 1
    return 0


def _match_domain(feature: Feature) -> str | None:
    """Return the best-matching domain name for a feature, or ``None``."""

    tokens = _tokens(_feature_values(feature))
    best_domain: str | None = None
    best_score = 0
    for domain_name, keywords in _DOMAIN_TAXONOMY:
        score = sum(_keyword_score(tokens, keyword) for keyword in keywords)
        if score > best_score:
            best_score = score
            best_domain = domain_name
    return best_domain


def build_domain_model(inventory: FeatureInventory) -> DomainModel:
    """Group ``inventory`` features into deterministic business domains."""

    grouped: dict[str, set[str]] = {}
    for feature in inventory.features:
        domain = _match_domain(feature) or _GENERAL_DOMAIN
        grouped.setdefault(domain, set()).add(feature.name)

    # Emit domains in taxonomy order, then any extras alphabetically, General last.
    order = {name: i for i, (name, _) in enumerate(_DOMAIN_TAXONOMY)}

    def sort_key(domain_name: str) -> tuple[int, str]:
        if domain_name == _GENERAL_DOMAIN:
            return (len(order) + 1, domain_name)
        return (order.get(domain_name, len(order)), domain_name.lower())

    domains = [
        Domain(name=name, features=sorted(grouped[name]))
        for name in sorted(grouped, key=sort_key)
    ]
    return DomainModel(domains=domains)
