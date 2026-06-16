"""Persistence for the feature inventory artifact (``feature-inventory.json``)."""

from __future__ import annotations

from pathlib import Path

from app.config import Settings, get_settings
from app.models.feature import FeatureInventory

FEATURE_ARTIFACT = "feature-inventory.json"


def feature_artifact_path(settings: Settings | None = None) -> Path:
    """Return the path to ``feature-inventory.json``."""

    settings = settings or get_settings()
    return Path(settings.output_dir) / FEATURE_ARTIFACT


def save_inventory(inventory: FeatureInventory, settings: Settings | None = None) -> Path:
    """Write ``inventory`` to ``outputs/feature-inventory.json`` and return its path."""

    path = feature_artifact_path(settings)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(inventory.model_dump_json(indent=2) + "\n", encoding="utf-8")
    return path


def load_inventory(settings: Settings | None = None) -> FeatureInventory | None:
    """Load the saved feature inventory, or ``None`` if it does not exist."""

    path = feature_artifact_path(settings)
    if not path.is_file():
        return None
    return FeatureInventory.model_validate_json(path.read_text(encoding="utf-8"))
