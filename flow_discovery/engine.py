"""The deterministic Flow Discovery Engine.

Pipeline
--------
1. Load artifacts and flatten them into :class:`Signal` evidence (see
   :mod:`flow_discovery.artifacts`).
2. Group evidence by domain-model entity.
3. For every entity, activate each journey :class:`Archetype` whose trigger
   verbs are evidenced, producing an end-to-end :class:`BusinessFlow`.
4. Compute QA metadata (complexity, criticality, touchpoints) and a confidence
   score from the supporting evidence.
5. Sort deterministically and assign stable ``FLOW-NNN`` identifiers.

The whole pipeline is pure and deterministic: identical artifacts always yield
identical output. No randomness, timestamps, network calls or LLM usage.
"""

from __future__ import annotations

import re
from typing import Dict, List, Optional, Tuple

from .artifacts import ArtifactBundle, load_bundle
from .models import (
    BusinessFlow,
    DiscoveryResult,
    FlowStep,
    QAMetadata,
    Signal,
)
from .patterns import (
    ARCHETYPES,
    Archetype,
    VERB_BY_KEY,
    resolve_category,
)

_CRIT_SCORE = {"low": 1, "medium": 2, "high": 3, "critical": 4}
_CRIT_LABEL = {1: "Low", 2: "Medium", 3: "High", 4: "Critical"}

_INTEGRATION_KEYWORDS = (
    "integration", "sync", "synchron", "planner", "primavera", "erp",
    "webhook", "import", "export", "interface", "external system",
)
_DOCUMENT_KEYWORDS = (
    "document", "attachment", "file", "upload", "download", "drawing",
    "submittal", "transmittal", "report",
)

# A flow needs at least this many supporting signals to be reported. This keeps
# the engine from inventing journeys for entities that barely appear.
_MIN_SUPPORTING_SIGNALS = 2


class FlowDiscoveryEngine:
    """Discovers business flows from a directory of QA Architect artifacts."""

    def __init__(self, bundle: ArtifactBundle) -> None:
        self.bundle = bundle

    @classmethod
    def from_directory(cls, artifact_dir: str) -> "FlowDiscoveryEngine":
        return cls(load_bundle(artifact_dir))

    # ------------------------------------------------------------------
    def discover(self) -> DiscoveryResult:
        entity_index = self._index_entities()
        flows: List[BusinessFlow] = []

        for entity in self.bundle.entities:
            signals = entity_index.get(entity["name"], [])
            if len(signals) < _MIN_SUPPORTING_SIGNALS:
                continue
            entity_verbs = self._aggregate_verbs(signals)
            primary_verbs = self._primary_verbs(signals)
            gate_text = f"{entity['name']} {entity.get('domain', '')}".lower()
            for archetype in ARCHETYPES:
                if not _triggered(archetype, primary_verbs):
                    continue
                if archetype.gate_keywords and not any(
                    kw in gate_text for kw in archetype.gate_keywords
                ):
                    continue
                flow = self._build_flow(entity, signals, entity_verbs, archetype)
                if flow is not None:
                    flows.append(flow)

        flows = self._finalize(flows)
        summary = self._summarize(flows)
        return DiscoveryResult(
            flows=flows,
            summary=summary,
            source_artifacts=self.bundle.loaded_files,
        )

    # ------------------------------------------------------------------
    # Entity indexing
    # ------------------------------------------------------------------
    def _index_entities(self) -> Dict[str, List[Signal]]:
        index: Dict[str, List[Signal]] = {e["name"]: [] for e in self.bundle.entities}
        name_by_lower = {e["name"].lower(): e["name"] for e in self.bundle.entities}
        matchers = {e["name"]: _entity_matcher(e["name"]) for e in self.bundle.entities}

        for signal in self.bundle.signals:
            declared = (signal.entity or "").strip().lower()
            if declared and declared in name_by_lower:
                # A declared entity is authoritative - attach only there so a
                # signal that merely mentions another entity in prose does not
                # leak into that other entity's flows.
                index[name_by_lower[declared]].append(signal)
                continue
            lowered_text = signal.text.lower()
            for entity in self.bundle.entities:
                if matchers[entity["name"]].search(lowered_text):
                    index[entity["name"]].append(signal)
        return index

    @staticmethod
    def _aggregate_verbs(signals: List[Signal]) -> List[str]:
        verbs: set = set()
        for signal in signals:
            verbs.update(signal.verbs)
        return [k for k in VERB_BY_KEY if k in verbs]

    @staticmethod
    def _primary_verbs(signals: List[Signal]) -> List[str]:
        """Verbs that are the *primary action* of a signal (taken from names).

        Using the signal name rather than its full description keeps incidental
        verbs ("...and notify stakeholders") from spawning unrelated flows.
        """

        verbs: set = set()
        for signal in signals:
            # Business rules are constraints, not actions - they must not start
            # a journey, only reinforce one that features/APIs already imply.
            if signal.kind == "rule":
                continue
            verbs.update(signal.name_verbs)
        return [k for k in VERB_BY_KEY if k in verbs]

    # ------------------------------------------------------------------
    # Flow construction
    # ------------------------------------------------------------------
    def _build_flow(self, entity: Dict[str, str], signals: List[Signal],
                    entity_verbs: List[str], archetype: Archetype) -> Optional[BusinessFlow]:
        steps = _build_steps(archetype, entity_verbs)
        if not steps:
            return None

        relevant = _relevant_signals(archetype, signals)
        if not relevant:
            relevant = signals

        domain = entity.get("domain") or _dominant_domain(relevant)
        category = resolve_category(
            f"{entity['name']} {domain}", archetype.default_category
        )
        flow_name = _flow_name(entity["name"], archetype.suffix)
        purpose = archetype.purpose.format(entity=entity["name"])

        qa = self._qa_metadata(entity, steps, relevant, archetype)
        confidence = self._confidence(entity, archetype, steps, relevant)
        sources = _build_sources(relevant)
        dependencies = self._dependencies(entity, relevant, qa)

        return BusinessFlow(
            flow_id="",  # assigned during finalize()
            domain=domain or "General",
            flow_name=flow_name,
            category=category,
            confidence=confidence,
            purpose=purpose,
            steps=steps,
            sources=sources,
            qa_metadata=qa,
            dependencies=dependencies,
        )

    # ------------------------------------------------------------------
    # QA metadata + scoring
    # ------------------------------------------------------------------
    def _qa_metadata(self, entity: Dict[str, str], steps: List[FlowStep],
                     signals: List[Signal], archetype: Archetype) -> QAMetadata:
        integration_points = _count_signals(signals, _INTEGRATION_KEYWORDS)
        document_touchpoints = _count_signals(signals, _DOCUMENT_KEYWORDS)
        approval_touchpoints = sum(
            1 for s in signals
            if {"approve", "review", "reject"} & set(s.verbs)
        )
        step_count = len(steps)

        complexity = _complexity(step_count, integration_points, document_touchpoints)
        criticality = self._criticality(entity, archetype, integration_points,
                                        approval_touchpoints)

        return QAMetadata(
            complexity=complexity,
            criticality=criticality,
            step_count=step_count,
            integration_points=integration_points,
            document_touchpoints=document_touchpoints,
            approval_touchpoints=approval_touchpoints,
        )

    @staticmethod
    def _criticality(entity: Dict[str, str], archetype: Archetype,
                     integration_points: int, approval_touchpoints: int) -> str:
        score = _CRIT_SCORE.get(archetype.base_criticality.lower(), 2)
        ent_crit = _CRIT_SCORE.get((entity.get("criticality") or "").lower(), 0)
        score = max(score, ent_crit)
        if integration_points >= 2:
            score = max(score, 3)
        if approval_touchpoints >= 2:
            score = max(score, 3)
        score = min(score, 4)
        return _CRIT_LABEL[score]

    def _confidence(self, entity: Dict[str, str], archetype: Archetype,
                    steps: List[FlowStep], signals: List[Signal]) -> float:
        score = 0.50
        if entity.get("criticality"):
            score += 0.05
        evidenced = sum(1 for s in steps if s.evidenced)
        if steps:
            score += 0.25 * (evidenced / len(steps))
        distinct_sources = len({(s.artifact, s.kind, s.ref_id) for s in signals})
        score += min(0.15, 0.03 * distinct_sources)
        triggered = len(set(archetype.trigger_verbs) &
                        set(self._aggregate_verbs(signals)))
        score += min(0.10, 0.05 * triggered)
        if self._has_traceability(entity):
            score += 0.05
        return round(min(score, 0.99), 2)

    def _has_traceability(self, entity: Dict[str, str]) -> bool:
        name = entity["name"].lower()
        for link in self.bundle.traceability:
            blob = " ".join(str(v) for v in link.values()).lower()
            if name in blob:
                return True
        return False

    def _dependencies(self, entity: Dict[str, str], signals: List[Signal],
                      qa: QAMetadata) -> List[str]:
        deps: set = set()
        if qa.integration_points > 0:
            for integration in _integrations(self.bundle):
                deps.add(integration)
        # Other entities referenced by the supporting evidence.
        self_name = entity["name"].lower()
        for other in self.bundle.entities:
            oname = other["name"]
            if oname.lower() == self_name:
                continue
            pat = _entity_matcher(oname)
            for signal in signals:
                if pat.search(signal.text.lower()):
                    deps.add(oname)
                    break
        return sorted(deps)

    # ------------------------------------------------------------------
    # Finalization + summary
    # ------------------------------------------------------------------
    @staticmethod
    def _finalize(flows: List[BusinessFlow]) -> List[BusinessFlow]:
        # Deduplicate by flow name, keeping the highest-confidence variant.
        best: Dict[str, BusinessFlow] = {}
        for flow in flows:
            existing = best.get(flow.flow_name)
            if existing is None or flow.confidence > existing.confidence:
                best[flow.flow_name] = flow
        unique = list(best.values())
        unique.sort(key=lambda f: (f.domain.lower(), f.flow_name.lower()))
        for idx, flow in enumerate(unique, start=1):
            flow.flow_id = f"FLOW-{idx:03d}"
        return unique

    @staticmethod
    def _summarize(flows: List[BusinessFlow]) -> Dict:
        total = len(flows)
        per_domain: Dict[str, int] = {}
        per_category: Dict[str, int] = {}
        step_total = 0
        for flow in flows:
            per_domain[flow.domain] = per_domain.get(flow.domain, 0) + 1
            per_category[flow.category] = per_category.get(flow.category, 0) + 1
            step_total += flow.qa_metadata.step_count

        avg_steps = round(step_total / total, 2) if total else 0.0

        complexity_rank = {"High": 3, "Medium": 2, "Low": 1}
        criticality_rank = {"Critical": 4, "High": 3, "Medium": 2, "Low": 1}

        highest_complexity = [
            f.flow_name for f in sorted(
                flows,
                key=lambda f: (complexity_rank.get(f.qa_metadata.complexity, 0),
                               f.confidence),
                reverse=True,
            )
            if f.qa_metadata.complexity == "High"
        ]
        highest_criticality = [
            f.flow_name for f in sorted(
                flows,
                key=lambda f: (criticality_rank.get(f.qa_metadata.criticality, 0),
                               f.confidence),
                reverse=True,
            )
            if f.qa_metadata.criticality == "Critical"
        ]

        return {
            "total_flows": total,
            "flows_per_domain": dict(sorted(per_domain.items())),
            "flows_per_category": dict(sorted(per_category.items())),
            "average_steps_per_flow": avg_steps,
            "highest_complexity_flows": highest_complexity,
            "highest_criticality_flows": highest_criticality,
        }


# ---------------------------------------------------------------------------
# Pure helpers
# ---------------------------------------------------------------------------


def _entity_matcher(name: str) -> "re.Pattern":
    lowered = name.lower()
    forms = {lowered, lowered + "s"}
    if lowered.endswith("s") and len(lowered) > 3:
        forms.add(lowered[:-1])
    alternation = "|".join(re.escape(f) for f in sorted(forms, key=len, reverse=True))
    return re.compile(r"\b(" + alternation + r")\b")


def _triggered(archetype: Archetype, primary_verbs: List[str]) -> bool:
    return bool(set(archetype.trigger_verbs) & set(primary_verbs))


def _build_steps(archetype: Archetype, entity_verbs: List[str]) -> List[FlowStep]:
    verb_set = set(entity_verbs)
    steps: List[FlowStep] = []
    for sequence, verb_key in enumerate(archetype.step_verbs, start=1):
        verb = VERB_BY_KEY[verb_key]
        steps.append(FlowStep(
            sequence=sequence,
            name=verb.display,
            verb=verb_key,
            evidenced=verb_key in verb_set,
        ))
    return steps


def _relevant_signals(archetype: Archetype, signals: List[Signal]) -> List[Signal]:
    relevant_verbs = set(archetype.step_verbs) | set(archetype.trigger_verbs)
    return [s for s in signals if relevant_verbs & set(s.verbs)]


def _dominant_domain(signals: List[Signal]) -> str:
    counts: Dict[str, int] = {}
    for signal in signals:
        if signal.domain:
            counts[signal.domain] = counts.get(signal.domain, 0) + 1
    if not counts:
        return ""
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[0][0]


def _flow_name(entity_name: str, suffix: str) -> str:
    words = entity_name.split()
    if words and words[-1].lower() == suffix.lower():
        return f"{entity_name} Flow"
    return f"{entity_name} {suffix} Flow"


def _count_signals(signals: List[Signal], keywords: Tuple[str, ...]) -> int:
    count = 0
    for signal in signals:
        lowered = signal.text.lower()
        if any(kw in lowered for kw in keywords):
            count += 1
    return count


def _complexity(step_count: int, integration_points: int,
                document_touchpoints: int) -> str:
    if step_count >= 5 or integration_points >= 2:
        return "High"
    if step_count <= 3 and integration_points == 0 and document_touchpoints == 0:
        return "Low"
    return "Medium"


def _build_sources(signals: List[Signal]) -> List[Dict[str, str]]:
    seen = set()
    sources: List[Dict[str, str]] = []
    for signal in signals:
        key = (signal.artifact, signal.kind, signal.ref_id)
        if key in seen:
            continue
        seen.add(key)
        sources.append({
            "artifact": signal.artifact,
            "type": signal.kind,
            "id": signal.ref_id,
            "name": signal.name,
        })
    sources.sort(key=lambda s: (s["artifact"], s["type"], s["id"]))
    return sources


def _integrations(bundle: ArtifactBundle) -> List[str]:
    names: List[str] = []
    app = bundle.application or {}
    raw = app.get("integrations") or app.get("external_systems") or app.get("integration") or []
    if isinstance(raw, dict):
        raw = [raw]
    for item in raw or []:
        if isinstance(item, dict):
            name = item.get("name") or item.get("system") or item.get("title")
            if name:
                names.append(str(name))
        elif isinstance(item, str):
            names.append(item)
    return names


def discover_flows(artifact_dir: str) -> DiscoveryResult:
    """Convenience wrapper: load ``artifact_dir`` and run discovery."""

    return FlowDiscoveryEngine.from_directory(artifact_dir).discover()
