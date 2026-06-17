"""Repository discovery service.

Clones a repository and runs deterministic analysis over its contents. No AI is
used — detection is purely structure/regex based.
"""

from __future__ import annotations

from pathlib import Path

from app.discovery.analyzer import analyze_repository
from app.discovery.artifacts import load_application, save_application
from app.discovery.cloner import (
    CloneError,
    clone_repository,
    derive_application_name,
)
from app.models.discovery import DiscoveryResult, Repository


class DiscoveryService:
    """Discovers repositories and analyzes their technology/structure."""

    def list_repositories(self) -> list[Repository]:
        """Return the set of known repositories.

        Currently returns an empty list as a placeholder.
        """

        return []

    def discover(self, repo_url: str, branch: str | None = None) -> DiscoveryResult:
        """Clone ``repo_url``, analyze it, and persist ``outputs/application.json``.

        The artifact is written so later stages can consume it instead of
        re-reading the repository. Raises ``CloneError`` if cloning fails.
        """

        application = derive_application_name(repo_url)
        with clone_repository(repo_url, branch=branch) as path:
            result = analyze_repository(path, application)
        save_application(result)
        return result

    def load_artifact(self) -> DiscoveryResult | None:
        """Return the last persisted discovery artifact, if any."""

        return load_application()

    def artifact_path(self) -> Path:
        """Return the path to the discovery artifact."""

        from app.discovery.artifacts import application_artifact_path

        return application_artifact_path()


__all__ = ["DiscoveryService", "CloneError"]
