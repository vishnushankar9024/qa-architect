"""Repository discovery service.

Clones a repository and runs deterministic analysis over its contents. No AI is
used — detection is purely structure/regex based.
"""

from __future__ import annotations

from app.discovery.analyzer import analyze_repository
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
        """Clone ``repo_url`` and produce a deterministic discovery result.

        Raises ``CloneError`` if the repository cannot be cloned.
        """

        application = derive_application_name(repo_url)
        with clone_repository(repo_url, branch=branch) as path:
            result = analyze_repository(path, application)
        return result


__all__ = ["DiscoveryService", "CloneError"]
