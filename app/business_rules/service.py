"""Business rule discovery service.

Consumes existing artifacts only and produces ``business-rules.json``. The
service never reads or clones repositories and makes no LLM calls.
"""

from __future__ import annotations

from pathlib import Path

from app import pipeline
from app.business_rules.artifacts import (
    business_rules_artifact_path,
    load_business_rules,
    save_business_rules,
)
from app.business_rules.engine import build_business_rules
from app.discovery.artifacts import load_application
from app.domains.artifacts import load_domain_model
from app.features.artifacts import load_inventory
from app.models.business_rules import BusinessRulesModel
from app.traceability.artifacts import load_traceability


class BusinessRulesInputError(RuntimeError):
    """Raised when a required upstream artifact is missing."""


class BusinessRulesService:
    """Builds and serves deterministic business rules from pipeline artifacts."""

    STAGE = "business-rules"

    def build(self) -> BusinessRulesModel:
        """Build ``business-rules.json`` from existing upstream artifacts.

        Enforces the Artifact First Rule via the immediate upstream artifact
        (``traceability.json``) and additionally requires the earlier artifacts
        used for context. Raises ``BusinessRulesInputError`` if any are missing.
        """

        try:
            pipeline.require_previous_artifact(self.STAGE)
        except pipeline.MissingArtifactError as exc:
            raise BusinessRulesInputError(str(exc)) from exc

        application = load_application()
        inventory = load_inventory()
        domain_model = load_domain_model()
        traceability = load_traceability()

        missing = [
            name
            for name, value in (
                ("application.json", application),
                ("feature-inventory.json", inventory),
                ("domain-model.json", domain_model),
                ("traceability.json", traceability),
            )
            if value is None
        ]
        if missing:
            raise BusinessRulesInputError(
                f"Missing required artifact(s): {', '.join(missing)}."
            )

        model = build_business_rules(application, inventory, domain_model, traceability)
        save_business_rules(model)
        return model

    def load(self) -> BusinessRulesModel | None:
        """Return the last persisted business rules artifact, if any."""

        return load_business_rules()

    def artifact_path(self) -> Path:
        """Return the path to the business rules artifact."""

        return business_rules_artifact_path()
