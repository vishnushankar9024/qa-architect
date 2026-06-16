"""Persistence for the discovery artifact (``outputs/application.json``).

The discovery stage writes a single, deterministic JSON artifact that later QA
Architect stages consume **instead of re-reading the repository**. File naming
and JSON I/O are delegated to :mod:`app.pipeline`, the single source of truth
for the Artifact First Rule.
"""

from __future__ import annotations

from pathlib import Path

from app import pipeline
from app.config import Settings
from app.models.discovery import DiscoveryResult

APPLICATION_ARTIFACT = pipeline.stage_artifact("discovery")


def output_dir(settings: Settings | None = None) -> Path:
    """Return the configured output directory as a ``Path``."""

    return pipeline.output_dir(settings)


def application_artifact_path(settings: Settings | None = None) -> Path:
    """Return the path to ``application.json``."""

    return pipeline.artifact_path(APPLICATION_ARTIFACT, settings)


def save_application(result: DiscoveryResult, settings: Settings | None = None) -> Path:
    """Write ``result`` to ``outputs/application.json`` and return its path."""

    return pipeline.save_model(APPLICATION_ARTIFACT, result, settings)


def load_application(settings: Settings | None = None) -> DiscoveryResult | None:
    """Load the saved discovery artifact, or ``None`` if it does not exist."""

    return pipeline.load_model(APPLICATION_ARTIFACT, DiscoveryResult, settings)
