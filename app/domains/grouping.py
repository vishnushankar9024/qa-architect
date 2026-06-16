"""Deterministic grouping of features into business domains.

Input is a :class:`~app.models.feature.FeatureInventory` (loaded from
``feature-inventory.json``). Each feature is matched against a fixed keyword
taxonomy and assigned to the best-matching business domain. Features that match
no domain are collected under "General".

No LLMs, no repository access — pure rule-based processing.
"""

from __future__ import annotations

import re

from app.models.domain import Domain, DomainModel
from app.models.feature import FeatureInventory

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
            "account",
            "profile",
            "identity",
            "access",
            "delegation",
            "newdelegation",
        },
    ),
    (
        "Opportunity Management",
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
            "tender",
            "proposal",
            "lead",
            "deal",
        },
    ),
    (
        "Onboarding and Vendor Management",
        {
            "onboarding",
            "afteronboarding",
            "vendor",
            "company",
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
            "ptc",
            "ptchub",
            "ptcdetail",
            "raci",
        },
    ),
    (
        "Document and Template Management",
        {
            "document",
            "documentmanager",
            "file",
            "attachment",
            "blueprint",
            "template",
            "formtemplate",
            "addendum",
        },
    ),
    (
        "Configuration and Administration",
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
            "message",
            "community",
        },
    ),
    (
        "Workflow and Execution",
        {
            "workflow",
            "execution",
            "timeline",
            "step",
            "instruction",
            "approval",
            "projectallocation",
            "structure",
            "itemboard",
            "myitem",
            "preview",
            "group",
            "cost",
            "blueprinthub",
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


def _feature_tokens(name: str) -> set[str]:
    """Tokenize a feature name into normalized, singularized keyword tokens."""

    parts = re.split(r"[^a-z0-9]+", name.lower())
    tokens: set[str] = set()
    for part in parts:
        if not part or part in _STOPWORDS:
            continue
        tokens.add(part)
        tokens.add(_singularize(part))
        # Also add the collapsed/compact form (e.g. "user-management" pieces).
    # Compact form of the whole name (no separators) helps match composite keys
    # like "opportunityhub" / "usermanagement".
    compact = re.sub(r"[^a-z0-9]", "", name.lower())
    if compact and compact not in _STOPWORDS:
        tokens.add(compact)
        tokens.add(_singularize(compact))
    return tokens


def _match_domain(feature_name: str) -> str | None:
    """Return the best-matching domain name for a feature, or ``None``."""

    tokens = _feature_tokens(feature_name)
    best_domain: str | None = None
    best_score = 0
    for domain_name, keywords in _DOMAIN_TAXONOMY:
        score = len(tokens & keywords)
        if score > best_score:
            best_score = score
            best_domain = domain_name
    return best_domain


def build_domain_model(inventory: FeatureInventory) -> DomainModel:
    """Group ``inventory`` features into deterministic business domains."""

    grouped: dict[str, set[str]] = {}
    for feature in inventory.features:
        domain = _match_domain(feature.name) or _GENERAL_DOMAIN
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
