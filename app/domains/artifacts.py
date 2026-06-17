"""Persistence for the domain model artifact (``domain-model.json``).

File naming and JSON I/O are delegated to :mod:`app.pipeline`, the single source
of truth for the Artifact First Rule.
"""

from __future__ import annotations

from pathlib import Path

from app import pipeline
from app.config import Settings
from app.models.domain import DomainModel

DOMAIN_ARTIFACT = pipeline.stage_artifact("domains")


def domain_artifact_path(settings: Settings | None = None) -> Path:
    """Return the path to ``domain-model.json``."""

    return pipeline.artifact_path(DOMAIN_ARTIFACT, settings)


def save_domain_model(model: DomainModel, settings: Settings | None = None) -> Path:
    """Write ``model`` to ``outputs/domain-model.json`` and return its path."""

    return pipeline.save_model(DOMAIN_ARTIFACT, model, settings)


def load_domain_model(settings: Settings | None = None) -> DomainModel | None:
    """Load the saved domain model, or ``None`` if it does not exist."""

    return pipeline.load_model(DOMAIN_ARTIFACT, DomainModel, settings)
