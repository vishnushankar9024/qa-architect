"""A thin GitHub client wrapper.

This is a placeholder integration layer. It wraps configuration and exposes a
small surface used by the rest of the app. Network calls are kept minimal and
optional so the service can run without credentials during scaffolding.
"""

from __future__ import annotations

from app.config import Settings, get_settings


class GitHubClient:
    """Lightweight wrapper around GitHub configuration.

    Real API interactions (via PyGithub or httpx) will be added later. For now
    this exposes whether the client is configured with a token.
    """

    def __init__(self, settings: Settings | None = None) -> None:
        self._settings = settings or get_settings()

    @property
    def is_configured(self) -> bool:
        """Whether a GitHub token is available."""

        return bool(self._settings.github_token)

    @property
    def api_url(self) -> str:
        """Base GitHub API URL."""

        return self._settings.github_api_url
