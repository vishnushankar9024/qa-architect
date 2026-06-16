"""Domain discovery service.

Consumes the feature inventory (``feature-inventory.json``) and produces the
domain model (``domain-model.json``). It never reads or clones repositories —
all input comes from the upstream feature artifact.
"""

from __future__ import annotations

from pathlib import Path

from app import pipeline
from app.domains.artifacts import (
    domain_artifact_path,
    load_domain_model,
    save_domain_model,
)
from app.domains.grouping import build_domain_model
from app.features.artifacts import load_inventory
from app.models.domain import DomainModel


class DomainInputError(RuntimeError):
    """Raised when the required feature inventory artifact is missing."""


class DomainService:
    """Builds and serves the domain model from the feature inventory."""

    STAGE = "domains"

    def build(self) -> DomainModel:
        """Build ``domain-model.json`` from ``feature-inventory.json``.

        Enforces the Artifact First Rule: consumes the feature inventory only and
        never reads the repository. Raises ``DomainInputError`` if the upstream
        artifact is missing.
        """

        try:
            pipeline.require_previous_artifact(self.STAGE)
        except pipeline.MissingArtifactError as exc:
            raise DomainInputError(str(exc)) from exc

        inventory = load_inventory()
        if inventory is None:  # pragma: no cover - guarded by require_previous_artifact
            raise DomainInputError("feature-inventory.json could not be loaded.")
        model = build_domain_model(inventory)
        save_domain_model(model)
        return model

    def load(self) -> DomainModel | None:
        """Return the last persisted domain model, if any."""

        return load_domain_model()

    def artifact_path(self) -> Path:
        """Return the path to the domain model artifact."""

        return domain_artifact_path()
