"""Traceability service.

Consumes the discovery, feature, and domain artifacts and produces the
traceability graph (``traceability.json``). It never reads or clones
repositories — all input comes from previously generated artifacts.
"""

from __future__ import annotations

from pathlib import Path

from app import pipeline
from app.discovery.artifacts import load_application
from app.domains.artifacts import load_domain_model
from app.features.artifacts import load_inventory
from app.models.traceability import TraceabilityModel
from app.traceability.artifacts import (
    load_traceability,
    save_traceability,
    traceability_artifact_path,
)
from app.traceability.engine import build_traceability


class TraceabilityInputError(RuntimeError):
    """Raised when a required upstream artifact is missing."""


class TraceabilityService:
    """Builds and serves the traceability graph from upstream artifacts."""

    STAGE = "traceability"

    def build(self) -> TraceabilityModel:
        """Build ``traceability.json`` from the discovery/feature/domain artifacts.

        Enforces the Artifact First Rule via the immediate upstream artifact
        (``domain-model.json``) and additionally requires the discovery and
        feature artifacts it joins. Raises ``TraceabilityInputError`` if any are
        missing.
        """

        try:
            pipeline.require_previous_artifact(self.STAGE)
        except pipeline.MissingArtifactError as exc:
            raise TraceabilityInputError(str(exc)) from exc

        application = load_application()
        inventory = load_inventory()
        domain_model = load_domain_model()

        missing = [
            name
            for name, value in (
                ("application.json", application),
                ("feature-inventory.json", inventory),
                ("domain-model.json", domain_model),
            )
            if value is None
        ]
        if missing:
            raise TraceabilityInputError(
                f"Missing required artifact(s): {', '.join(missing)}."
            )

        model = build_traceability(application, inventory, domain_model)
        save_traceability(model)
        return model

    def load(self) -> TraceabilityModel | None:
        """Return the last persisted traceability model, if any."""

        return load_traceability()

    def artifact_path(self) -> Path:
        """Return the path to the traceability artifact."""

        return traceability_artifact_path()
