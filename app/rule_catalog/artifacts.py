"""Persistence for governed business rule catalog artifacts."""

from __future__ import annotations

from pathlib import Path

from app import pipeline
from app.config import Settings
from app.models.rule_catalog import RuleCatalogModel, RuleOverridesModel

RULE_OVERRIDES_ARTIFACT = "business-rule-overrides.json"
RULE_CATALOG_ARTIFACT = pipeline.stage_artifact("rule-catalog")
RULE_CATALOG_MARKDOWN = "business-rule-catalog.md"


def rule_overrides_artifact_path(settings: Settings | None = None) -> Path:
    """Return the path to ``business-rule-overrides.json``."""

    return pipeline.artifact_path(RULE_OVERRIDES_ARTIFACT, settings)


def rule_catalog_artifact_path(settings: Settings | None = None) -> Path:
    """Return the path to ``business-rule-catalog.json``."""

    return pipeline.artifact_path(RULE_CATALOG_ARTIFACT, settings)


def rule_catalog_markdown_path(settings: Settings | None = None) -> Path:
    """Return the path to ``business-rule-catalog.md``."""

    return pipeline.artifact_path(RULE_CATALOG_MARKDOWN, settings)


def load_overrides(settings: Settings | None = None) -> RuleOverridesModel | None:
    """Load human rule overrides, or ``None`` if the artifact does not exist."""

    return pipeline.load_model(RULE_OVERRIDES_ARTIFACT, RuleOverridesModel, settings)


def save_overrides(model: RuleOverridesModel, settings: Settings | None = None) -> Path:
    """Write human rule overrides and return the artifact path."""

    return pipeline.save_model(RULE_OVERRIDES_ARTIFACT, model, settings)


def ensure_overrides(settings: Settings | None = None) -> RuleOverridesModel:
    """Load overrides or create an empty governed overrides artifact."""

    overrides = load_overrides(settings)
    if overrides is not None:
        return overrides
    empty = RuleOverridesModel()
    save_overrides(empty, settings)
    return empty


def load_catalog(settings: Settings | None = None) -> RuleCatalogModel | None:
    """Load the merged rule catalog, or ``None`` if it does not exist."""

    return pipeline.load_model(RULE_CATALOG_ARTIFACT, RuleCatalogModel, settings)


def save_catalog(model: RuleCatalogModel, settings: Settings | None = None) -> Path:
    """Write the merged rule catalog and return the artifact path."""

    return pipeline.save_model(RULE_CATALOG_ARTIFACT, model, settings)


def load_markdown(settings: Settings | None = None) -> str | None:
    """Load the human-readable Markdown catalog, or ``None`` if absent."""

    path = rule_catalog_markdown_path(settings)
    if not path.is_file():
        return None
    return path.read_text(encoding="utf-8")


def save_markdown(markdown: str, settings: Settings | None = None) -> Path:
    """Write the human-readable Markdown catalog and return the artifact path."""

    path = rule_catalog_markdown_path(settings)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(markdown, encoding="utf-8")
    return path
