"""Persistence for QA-focused business rule enrichment artifacts."""

from __future__ import annotations

from pathlib import Path

from app import pipeline
from app.config import Settings
from app.models.enriched_business_rules import EnrichedBusinessRulesModel, QualityReport

ENRICHED_RULES_ARTIFACT = pipeline.stage_artifact("rule-enrichment")
ENRICHED_RULES_MARKDOWN = "enriched-business-rules.md"
QUALITY_REPORT_ARTIFACT = "quality-report.json"


def enriched_rules_artifact_path(settings: Settings | None = None) -> Path:
    """Return the path to ``enriched-business-rules.json``."""

    return pipeline.artifact_path(ENRICHED_RULES_ARTIFACT, settings)


def enriched_rules_markdown_path(settings: Settings | None = None) -> Path:
    """Return the path to ``enriched-business-rules.md``."""

    return pipeline.artifact_path(ENRICHED_RULES_MARKDOWN, settings)


def quality_report_artifact_path(settings: Settings | None = None) -> Path:
    """Return the path to ``quality-report.json``."""

    return pipeline.artifact_path(QUALITY_REPORT_ARTIFACT, settings)


def save_enriched_rules(
    model: EnrichedBusinessRulesModel,
    settings: Settings | None = None,
) -> Path:
    """Write ``enriched-business-rules.json`` and return its path."""

    return pipeline.save_model(ENRICHED_RULES_ARTIFACT, model, settings)


def load_enriched_rules(
    settings: Settings | None = None,
) -> EnrichedBusinessRulesModel | None:
    """Load enriched rules, or ``None`` if absent."""

    return pipeline.load_model(ENRICHED_RULES_ARTIFACT, EnrichedBusinessRulesModel, settings)


def save_quality_report(report: QualityReport, settings: Settings | None = None) -> Path:
    """Write ``quality-report.json`` and return its path."""

    return pipeline.save_model(QUALITY_REPORT_ARTIFACT, report, settings)


def load_quality_report(settings: Settings | None = None) -> QualityReport | None:
    """Load quality report, or ``None`` if absent."""

    return pipeline.load_model(QUALITY_REPORT_ARTIFACT, QualityReport, settings)


def save_markdown(markdown: str, settings: Settings | None = None) -> Path:
    """Write ``enriched-business-rules.md`` and return its path."""

    path = enriched_rules_markdown_path(settings)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(markdown, encoding="utf-8")
    return path


def load_markdown(settings: Settings | None = None) -> str | None:
    """Load enriched rules Markdown, or ``None`` if absent."""

    path = enriched_rules_markdown_path(settings)
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")
