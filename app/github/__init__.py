"""GitHub integration module.

Provides a thin client wrapper and a router exposing GitHub-backed endpoints.
AI features are intentionally not implemented yet.
"""

from app.github.client import GitHubClient
from app.github.router import router

__all__ = ["GitHubClient", "router"]
