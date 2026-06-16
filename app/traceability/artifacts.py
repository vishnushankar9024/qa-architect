"""Persistence for the traceability artifact (``traceability.json``).

File naming and JSON I/O are delegated to :mod:`app.pipeline`, the single source
of truth for the Artifact First Rule.
"""

from __future__ import annotations

from pathlib import Path

from app import pipeline
from app.config import Settings
from app.models.traceability import TraceabilityModel

TRACEABILITY_ARTIFACT = pipeline.stage_artifact("traceability")


def traceability_artifact_path(settings: Settings | None = None) -> Path:
    """Return the path to ``traceability.json``."""

    return pipeline.artifact_path(TRACEABILITY_ARTIFACT, settings)


def save_traceability(model: TraceabilityModel, settings: Settings | None = None) -> Path:
    """Write ``model`` to ``outputs/traceability.json`` and return its path."""

    return pipeline.save_model(TRACEABILITY_ARTIFACT, model, settings)


def load_traceability(settings: Settings | None = None) -> TraceabilityModel | None:
    """Load the saved traceability model, or ``None`` if it does not exist."""

    return pipeline.load_model(TRACEABILITY_ARTIFACT, TraceabilityModel, settings)
