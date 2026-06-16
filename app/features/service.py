"""Feature discovery service.

Consumes the discovery artifact (``application.json``) and produces the feature
inventory (``feature-inventory.json``). It never reads or clones repositories —
all input comes from the previously generated discovery artifact.
"""

from __future__ import annotations

from pathlib import Path

from app import pipeline
from app.discovery.artifacts import load_application
from app.features.artifacts import feature_artifact_path, load_inventory, save_inventory
from app.features.grouping import build_feature_inventory
from app.models.feature import FeatureInventory


class FeatureInputError(RuntimeError):
    """Raised when the required discovery artifact is missing."""


class FeatureService:
    """Builds and serves the feature inventory from discovery artifacts."""

    STAGE = "features"

    def build(self) -> FeatureInventory:
        """Build ``feature-inventory.json`` from ``application.json``.

        Enforces the Artifact First Rule: the feature stage consumes the
        discovery artifact only and never reads the repository. Raises
        ``FeatureInputError`` if the upstream artifact is missing.
        """

        try:
            pipeline.require_previous_artifact(self.STAGE)
        except pipeline.MissingArtifactError as exc:
            raise FeatureInputError(str(exc)) from exc

        application = load_application()
        if application is None:  # pragma: no cover - guarded by require_previous_artifact
            raise FeatureInputError("application.json could not be loaded.")
        inventory = build_feature_inventory(application)
        save_inventory(inventory)
        return inventory

    def load(self) -> FeatureInventory | None:
        """Return the last persisted feature inventory, if any."""

        return load_inventory()

    def artifact_path(self) -> Path:
        """Return the path to the feature inventory artifact."""

        return feature_artifact_path()
