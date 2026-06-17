"""Dataclasses for the flow discovery domain model."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Signal:
    """A normalized piece of evidence drawn from an input artifact.

    Signals are the common currency the engine works with: features, API
    operations, routes, Postman collection requests and business rules are all
    flattened into ``Signal`` objects so the discovery logic can treat them
    uniformly.
    """

    artifact: str          # source artifact file, e.g. "feature-inventory.json"
    kind: str              # feature | api | route | collection | rule
    ref_id: str            # identifier within the artifact (best effort)
    name: str              # display name
    text: str              # full searchable text (name + description + path)
    domain: str = ""       # declared domain, if any
    entity: str = ""       # declared entity, if any
    verbs: List[str] = field(default_factory=list)       # verbs in full text
    name_verbs: List[str] = field(default_factory=list)  # verbs in the name only


@dataclass
class FlowStep:
    sequence: int
    name: str
    verb: str
    evidenced: bool = False  # True when an artifact signal supports this step

    def to_dict(self) -> Dict[str, Any]:
        return {"sequence": self.sequence, "name": self.name}


@dataclass
class QAMetadata:
    complexity: str
    criticality: str
    step_count: int
    integration_points: int
    document_touchpoints: int
    approval_touchpoints: int

    def to_dict(self) -> Dict[str, Any]:
        return {
            "complexity": self.complexity,
            "criticality": self.criticality,
            "step_count": self.step_count,
            "integration_points": self.integration_points,
            "document_touchpoints": self.document_touchpoints,
            "approval_touchpoints": self.approval_touchpoints,
        }


@dataclass
class BusinessFlow:
    flow_id: str
    domain: str
    flow_name: str
    category: str
    confidence: float
    purpose: str
    steps: List[FlowStep]
    sources: List[Dict[str, Any]]
    qa_metadata: QAMetadata
    dependencies: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "flow_id": self.flow_id,
            "domain": self.domain,
            "flow_name": self.flow_name,
            "category": self.category,
            "confidence": self.confidence,
            "purpose": self.purpose,
            "qa_metadata": self.qa_metadata.to_dict(),
            "steps": [s.to_dict() for s in self.steps],
            "dependencies": self.dependencies,
            "sources": self.sources,
        }


@dataclass
class DiscoveryResult:
    flows: List[BusinessFlow]
    summary: Dict[str, Any]
    source_artifacts: List[str]

    def to_dict(self) -> Dict[str, Any]:
        return {
            "generated_by": "QA Architect - Flow Discovery Engine",
            "engine": "deterministic / artifact-first",
            "source_artifacts": self.source_artifacts,
            "summary": self.summary,
            "flows": [f.to_dict() for f in self.flows],
        }
