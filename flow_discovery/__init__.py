"""QA Architect - Flow Discovery Engine.

A deterministic, artifact-first engine that discovers end-to-end business
workflows (flows) from previously generated QA Architect artifacts.

The engine never clones or re-scans repositories and never calls an LLM. It
consumes existing artifacts exclusively and produces ``business-flows.json``
and ``business-flows.md``.
"""

from .engine import FlowDiscoveryEngine
from .models import BusinessFlow, DiscoveryResult, FlowStep

__all__ = [
    "FlowDiscoveryEngine",
    "BusinessFlow",
    "FlowStep",
    "DiscoveryResult",
]

__version__ = "1.0.0"
