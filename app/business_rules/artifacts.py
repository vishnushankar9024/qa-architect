"""Persistence for the business rules artifact (``business-rules.json``).

File naming and JSON I/O are delegated to :mod:`app.pipeline`, the single source
of truth for the Artifact First Rule.
"""

from __future__ import annotations

from pathlib import Path

from app import pipeline
from app.config import Settings
from app.models.business_rules import BusinessRulesModel

BUSINESS_RULES_ARTIFACT = pipeline.stage_artifact("business-rules")


def business_rules_artifact_path(settings: Settings | None = None) -> Path:
    """Return the path to ``business-rules.json``."""

    return pipeline.artifact_path(BUSINESS_RULES_ARTIFACT, settings)


def save_business_rules(model: BusinessRulesModel, settings: Settings | None = None) -> Path:
    """Write ``model`` to ``outputs/business-rules.json`` and return its path."""

    return pipeline.save_model(BUSINESS_RULES_ARTIFACT, model, settings)


def load_business_rules(settings: Settings | None = None) -> BusinessRulesModel | None:
    """Load the saved business rules model, or ``None`` if it does not exist."""

    return pipeline.load_model(BUSINESS_RULES_ARTIFACT, BusinessRulesModel, settings)
