"""Feature discovery service.

Consumes the discovery artifact (``application.json``) and produces the feature
inventory (``feature-inventory.json``). It never reads or clones repositories —
all input comes from the previously generated discovery artifact.
"""

from __future__ import annotations

from pathlib import Path

from app.discovery.artifacts import load_application
from app.features.artifacts import feature_artifact_path, load_inventory, save_inventory
from app.features.grouping import build_feature_inventory
from app.models.feature import FeatureInventory


class FeatureInputError(RuntimeError):
    """Raised when the required discovery artifact is missing."""


class FeatureService:
    """Builds and serves the feature inventory from discovery artifacts."""

    def build(self) -> FeatureInventory:
        """Build ``feature-inventory.json`` from ``application.json``.

        Raises ``FeatureInputError`` if the discovery artifact is missing.
        """

        application = load_application()
        if application is None:
            raise FeatureInputError(
                "application.json not found. Run POST /discover before feature discovery."
            )
        inventory = build_feature_inventory(application)
        save_inventory(inventory)
        return inventory

    def load(self) -> FeatureInventory | None:
        """Return the last persisted feature inventory, if any."""

        return load_inventory()

    def artifact_path(self) -> Path:
        """Return the path to the feature inventory artifact."""

        return feature_artifact_path()
