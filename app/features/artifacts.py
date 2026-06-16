"""Persistence for the feature inventory artifact (``feature-inventory.json``).

File naming and JSON I/O are delegated to :mod:`app.pipeline`, the single source
of truth for the Artifact First Rule.
"""

from __future__ import annotations

from pathlib import Path

from app import pipeline
from app.config import Settings
from app.models.feature import FeatureInventory

FEATURE_ARTIFACT = pipeline.stage_artifact("features")


def feature_artifact_path(settings: Settings | None = None) -> Path:
    """Return the path to ``feature-inventory.json``."""

    return pipeline.artifact_path(FEATURE_ARTIFACT, settings)


def save_inventory(inventory: FeatureInventory, settings: Settings | None = None) -> Path:
    """Write ``inventory`` to ``outputs/feature-inventory.json`` and return its path."""

    return pipeline.save_model(FEATURE_ARTIFACT, inventory, settings)


def load_inventory(settings: Settings | None = None) -> FeatureInventory | None:
    """Load the saved feature inventory, or ``None`` if it does not exist."""

    return pipeline.load_model(FEATURE_ARTIFACT, FeatureInventory, settings)
