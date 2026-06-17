"""Application configuration.

Settings are loaded from environment variables (and an optional ``.env`` file).
No AI provider configuration is wired up yet; this only covers the basics needed
to run the API and talk to GitHub.
"""

from __future__ import annotations

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime settings for the QA Architect service."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="QA_ARCHITECT_",
        extra="ignore",
    )

    app_name: str = "QA Architect"
    environment: str = "development"
    debug: bool = True

    # Directory where QA Architect writes reusable artifacts (e.g.
    # ``application.json`` produced by repository discovery). Relative paths are
    # resolved against the current working directory.
    output_dir: str = "outputs"

    # GitHub integration. Token is optional so the app can boot without it;
    # endpoints that need it will report that it is missing.
    github_token: str | None = None
    github_api_url: str = "https://api.github.com"


@lru_cache
def get_settings() -> Settings:
    """Return a cached ``Settings`` instance."""

    return Settings()
