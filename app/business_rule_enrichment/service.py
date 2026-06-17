"""Business rule enrichment service."""

from __future__ import annotations

from pathlib import Path

from app import pipeline
from app.business_rule_enrichment.artifacts import (
    enriched_rules_artifact_path,
    load_enriched_rules,
    load_markdown,
    load_quality_report,
    quality_report_artifact_path,
    save_enriched_rules,
    save_markdown,
    save_quality_report,
)
from app.business_rule_enrichment.engine import (
    build_enriched_business_rules,
    render_enriched_markdown,
)
from app.discovery.artifacts import load_application
from app.domains.artifacts import load_domain_model
from app.features.artifacts import load_inventory
from app.models.enriched_business_rules import EnrichedBusinessRulesModel, QualityReport
from app.rule_catalog.artifacts import load_catalog
from app.traceability.artifacts import load_traceability


class BusinessRuleEnrichmentInputError(RuntimeError):
    """Raised when a required enrichment input artifact is missing."""


class BusinessRuleEnrichmentService:
    """Builds QA-focused enriched business rules from existing artifacts."""

    STAGE = "rule-enrichment"

    def build(self) -> EnrichedBusinessRulesModel:
        """Build enriched rules, Markdown, and quality report artifacts."""

        try:
            pipeline.require_previous_artifact(self.STAGE)
        except pipeline.MissingArtifactError as exc:
            raise BusinessRuleEnrichmentInputError(str(exc)) from exc

        application = load_application()
        inventory = load_inventory()
        domain_model = load_domain_model()
        traceability = load_traceability()
        catalog = load_catalog()

        missing = [
            name
            for name, value in (
                ("application.json", application),
                ("feature-inventory.json", inventory),
                ("domain-model.json", domain_model),
                ("traceability.json", traceability),
                ("business-rule-catalog.json", catalog),
            )
            if value is None
        ]
        if missing:
            raise BusinessRuleEnrichmentInputError(
                f"Missing required artifact(s): {', '.join(missing)}."
            )

        model, report = build_enriched_business_rules(
            application,
            inventory,
            domain_model,
            traceability,
            catalog,
        )
        save_enriched_rules(model)
        save_quality_report(report)
        save_markdown(render_enriched_markdown(model, report))
        return model

    def load(self) -> EnrichedBusinessRulesModel | None:
        """Return the persisted enriched rules artifact, if any."""

        return load_enriched_rules()

    def load_quality_report(self) -> QualityReport | None:
        """Return the persisted quality report artifact, if any."""

        return load_quality_report()

    def load_markdown(self) -> str | None:
        """Return the persisted enriched rules Markdown artifact, if any."""

        return load_markdown()

    def artifact_path(self) -> Path:
        """Return the enriched rules artifact path."""

        return enriched_rules_artifact_path()

    def quality_report_path(self) -> Path:
        """Return the quality report artifact path."""

        return quality_report_artifact_path()
