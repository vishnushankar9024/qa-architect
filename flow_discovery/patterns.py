"""PMWebX workflow pattern vocabulary, flow categories and journey archetypes.

Everything in this module is a *static, deterministic* definition. There are no
runtime decisions here - the engine consumes these tables to turn artifact text
into ordered business flows. Keeping the vocabulary in one place makes the
discovery behaviour auditable and reproducible.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class PatternVerb:
    """A canonical PMWebX workflow concept (verb).

    ``key``      canonical identifier used internally.
    ``display``  human readable noun used when rendering a step.
    ``order``    global ordering weight; smaller runs earlier in a journey.
    ``synonyms`` surface forms detected in artifact text (whole-word match).
    """

    key: str
    display: str
    order: int
    synonyms: Tuple[str, ...]


# Canonical PMWebX workflow verbs. The list intentionally covers the concepts
# called out in the specification (initiate, review, approve, reject, resend,
# close, publish, activate, assign, delegate, notify, upload, download, map,
# sync) plus a few common lifecycle verbs (create, submit, execute, complete)
# that make discovered journeys read as genuine end-to-end workflows.
PATTERN_VERBS: Tuple[PatternVerb, ...] = (
    PatternVerb("initiate", "Initiate", 10,
                ("initiate", "initiation", "start", "begin", "open", "raise", "trigger")),
    PatternVerb("create", "Create", 12,
                ("create", "creation", "add", "register", "registration", "draft",
                 "define", "setup", "set up", "new")),
    PatternVerb("submit", "Submission", 20,
                ("submit", "submission", "send", "forward")),
    PatternVerb("upload", "Upload", 22,
                ("upload", "attach", "attachment")),
    PatternVerb("map", "Mapping", 24,
                ("map", "mapping", "match", "link")),
    PatternVerb("assign", "Assignment", 30,
                ("assign", "assignment", "allocate", "allocation", "designate")),
    PatternVerb("delegate", "Delegation", 32,
                ("delegate", "delegation", "reassign")),
    PatternVerb("review", "Review", 40,
                ("review", "verify", "verification", "validate", "validation", "check")),
    PatternVerb("approve", "Approval", 50,
                ("approve", "approval", "authorize", "authorise", "authorization",
                 "sign-off", "sign off", "accept")),
    PatternVerb("reject", "Rejection", 52,
                ("reject", "rejection", "decline", "return")),
    PatternVerb("resend", "Resend", 54,
                ("resend", "resubmit", "resubmission")),
    PatternVerb("activate", "Activation", 60,
                ("activate", "activation", "enable", "go live")),
    PatternVerb("execute", "Execution", 62,
                ("execute", "execution", "perform", "run", "process", "processing")),
    PatternVerb("complete", "Completion", 64,
                ("complete", "completion", "finish", "fill", "fill out", "inspect", "inspection")),
    PatternVerb("sync", "Synchronization", 66,
                ("sync", "synchronize", "synchronise", "synchronization", "integrate",
                 "integration", "import", "export")),
    PatternVerb("publish", "Publish", 70,
                ("publish", "publication", "release", "issue")),
    PatternVerb("notify", "Notification", 72,
                ("notify", "notification", "alert", "remind", "reminder", "email")),
    PatternVerb("download", "Download", 74,
                ("download",)),
    PatternVerb("close", "Closure", 80,
                ("close", "closure", "archive", "finalize", "finalise", "complete workflow")),
)

VERB_BY_KEY: Dict[str, PatternVerb] = {v.key: v for v in PATTERN_VERBS}

# Pre-compiled whole-word detectors for every synonym, mapped to the canonical
# verb key. Sorted by descending synonym length so multi-word forms win.
_DETECTORS: Tuple[Tuple[re.Pattern, str], ...] = tuple(
    (re.compile(r"\b" + re.escape(syn) + r"\b", re.IGNORECASE), verb.key)
    for verb in PATTERN_VERBS
    for syn in sorted(verb.synonyms, key=len, reverse=True)
)


def detect_verbs(text: str) -> List[str]:
    """Return the canonical verb keys present in ``text`` (whole-word match).

    Deterministic: the result is ordered by each verb's global ``order`` weight
    so callers always receive the same sequence for the same input.
    """

    if not text:
        return []
    found = set()
    for pattern, key in _DETECTORS:
        if pattern.search(text):
            found.add(key)
    return [v.key for v in PATTERN_VERBS if v.key in found]


# ---------------------------------------------------------------------------
# Flow categories (specification requirement #4)
# ---------------------------------------------------------------------------

# Ordered list - earlier entries win ties during category resolution.
CATEGORY_KEYWORDS: Tuple[Tuple[str, Tuple[str, ...]], ...] = (
    ("RACI Flow", ("raci", "responsible", "accountable", "consulted", "informed")),
    ("Approval Flow", ("approval", "approve", "sign-off", "sign off", "authorize",
                       "authorise", "authorization")),
    ("Template Flow", ("template", "blueprint", "preset")),
    ("Checklist Flow", ("checklist", "inspection", "punch list", "punch", "quality check")),
    ("Document Flow", ("document", "attachment", "drawing", "submittal", "transmittal",
                       "rfi", "report")),
    ("Notification Flow", ("notification", "notify", "alert", "reminder")),
    ("Integration Flow", ("integration", "planner", "primavera", "erp", "interface",
                          "webhook", "sync", "import", "export")),
    ("Vendor Management Flow", ("vendor", "supplier", "contractor", "subcontractor",
                                "procurement")),
    ("User Management Flow", ("user", "role", "permission", "access control", "login",
                              "account", "authentication")),
    ("Project Flow", ("project", "portfolio", "program", "programme")),
    ("Activity Flow", ("activity", "task", "workstation", "work order")),
    ("Workflow Flow", ("workflow", "stage", "transition", "lifecycle", "status")),
)

# The complete, ordered set of valid categories (used for validation / fallbacks).
ALL_CATEGORIES: Tuple[str, ...] = tuple(name for name, _ in CATEGORY_KEYWORDS)


def resolve_category(text: str, fallback: str) -> str:
    """Classify ``text`` into one of the 12 flow categories.

    Scores every category by the number of keyword hits and returns the highest
    scoring one. Ties are broken by the declaration order in
    ``CATEGORY_KEYWORDS``. When nothing matches, ``fallback`` (the archetype's
    default category) is returned.
    """

    lowered = (text or "").lower()
    best_name = fallback
    best_score = 0
    for name, keywords in CATEGORY_KEYWORDS:
        score = sum(1 for kw in keywords if kw in lowered)
        if score > best_score:
            best_score = score
            best_name = name
    return best_name


# ---------------------------------------------------------------------------
# Journey archetypes - the shape of an end-to-end business flow
# ---------------------------------------------------------------------------


@dataclass(frozen=True)
class Archetype:
    """A reusable end-to-end journey shape.

    ``suffix``           the journey noun used to name the flow
                         (``"{Entity} {suffix} Flow"``).
    ``trigger_verbs``    if one of these verbs is the *primary action* of any
                         signal for an entity, the archetype activates.
    ``step_verbs``       canonical, ordered verbs that make up the journey.
    ``default_category`` category used when entity/domain text is ambiguous.
    ``base_criticality`` baseline business criticality for the journey.
    ``gate_keywords``    if set, the archetype only activates when the
                         entity/domain text contains one of these keywords.
                         Used to keep "side-effect" verbs (e.g. ``notify``)
                         from generating noise on unrelated entities.
    """

    name: str
    suffix: str
    trigger_verbs: Tuple[str, ...]
    step_verbs: Tuple[str, ...]
    default_category: str
    base_criticality: str
    purpose: str
    gate_keywords: Tuple[str, ...] = ()


ARCHETYPES: Tuple[Archetype, ...] = (
    Archetype(
        name="Creation",
        suffix="Creation",
        trigger_verbs=("create", "initiate"),
        step_verbs=("initiate", "submit", "review", "approve", "activate"),
        default_category="Workflow Flow",
        base_criticality="High",
        purpose="Capture, validate and activate a new {entity}.",
    ),
    Archetype(
        name="Approval",
        suffix="Approval",
        trigger_verbs=("approve", "review", "reject"),
        step_verbs=("initiate", "submit", "review", "approve", "close"),
        default_category="Approval Flow",
        base_criticality="Critical",
        purpose="Route a {entity} through review and approval to a final decision.",
    ),
    Archetype(
        name="Assignment",
        suffix="Assignment",
        trigger_verbs=("assign", "delegate"),
        step_verbs=("initiate", "assign", "delegate", "notify"),
        default_category="RACI Flow",
        base_criticality="High",
        purpose="Allocate ownership and responsibility for a {entity}.",
    ),
    Archetype(
        name="Execution",
        suffix="Execution",
        trigger_verbs=("execute",),
        step_verbs=("initiate", "assign", "execute", "complete", "close"),
        default_category="Activity Flow",
        base_criticality="High",
        purpose="Carry out and complete the work associated with a {entity}.",
    ),
    Archetype(
        name="Completion",
        suffix="Completion",
        trigger_verbs=("complete",),
        step_verbs=("initiate", "complete", "review", "approve"),
        default_category="Checklist Flow",
        base_criticality="High",
        purpose="Fill in, verify and sign off a {entity}.",
    ),
    Archetype(
        name="Synchronization",
        suffix="Synchronization",
        trigger_verbs=("sync",),
        step_verbs=("map", "sync", "notify"),
        default_category="Integration Flow",
        base_criticality="High",
        purpose="Exchange and reconcile {entity} data with an external system.",
    ),
    Archetype(
        name="Publishing",
        suffix="Publishing",
        trigger_verbs=("upload", "publish", "download"),
        step_verbs=("upload", "review", "approve", "publish", "download"),
        default_category="Document Flow",
        base_criticality="High",
        purpose="Upload, control and publish a {entity}.",
        gate_keywords=("document", "file", "attachment", "drawing", "submittal",
                       "transmittal", "report"),
    ),
    Archetype(
        name="Notification",
        suffix="Notification",
        trigger_verbs=("notify",),
        step_verbs=("initiate", "notify", "close"),
        default_category="Notification Flow",
        base_criticality="Medium",
        purpose="Detect an event and notify the relevant stakeholders for a {entity}.",
        gate_keywords=("notification", "notify", "alert", "reminder"),
    ),
)
