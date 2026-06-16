"""Persistence for the discovery artifact (``outputs/application.json``).

The discovery stage writes a single, deterministic JSON artifact that later QA
Architect stages consume **instead of re-reading the repository**. This keeps the
expensive source parsing in one place.
"""

from __future__ import annotations

from pathlib import Path

from app.config import Settings, get_settings
from app.models.discovery import DiscoveryResult

APPLICATION_ARTIFACT = "application.json"


def output_dir(settings: Settings | None = None) -> Path:
    """Return the configured output directory as a ``Path``."""

    settings = settings or get_settings()
    return Path(settings.output_dir)


def application_artifact_path(settings: Settings | None = None) -> Path:
    """Return the path to ``application.json``."""

    return output_dir(settings) / APPLICATION_ARTIFACT


def save_application(result: DiscoveryResult, settings: Settings | None = None) -> Path:
    """Write ``result`` to ``outputs/application.json`` and return its path."""

    path = application_artifact_path(settings)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        result.model_dump_json(indent=2) + "\n",
        encoding="utf-8",
    )
    return path


def load_application(settings: Settings | None = None) -> DiscoveryResult | None:
    """Load the saved discovery artifact, or ``None`` if it does not exist."""

    path = application_artifact_path(settings)
    if not path.is_file():
        return None
    return DiscoveryResult.model_validate_json(path.read_text(encoding="utf-8"))
