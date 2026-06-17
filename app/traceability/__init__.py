"""Traceability stage.

Joins the discovery, feature, and domain artifacts into a single
Domain -> Feature -> (routes/components/services/apis/collections) graph
(``traceability.json``). No repositories are read or cloned and no LLM calls are
made — the join is purely deterministic.
"""

from app.traceability.engine import build_traceability
from app.traceability.router import router
from app.traceability.service import TraceabilityInputError, TraceabilityService

__all__ = [
    "build_traceability",
    "router",
    "TraceabilityService",
    "TraceabilityInputError",
]
