"""Repository discovery service (placeholder)."""

from __future__ import annotations

from app.models.discovery import Repository


class DiscoveryService:
    """Discovers repositories available to QA Architect.

    This is a scaffold. Real discovery (e.g. via the GitHub API or local
    filesystem scanning) will be implemented later.
    """

    def list_repositories(self) -> list[Repository]:
        """Return the set of known repositories.

        Currently returns an empty list as a placeholder.
        """

        return []
