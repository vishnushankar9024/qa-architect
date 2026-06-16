"""GitHub integration endpoints."""

from __future__ import annotations

from fastapi import APIRouter

from app.github.client import GitHubClient
from app.models.common import Message

router = APIRouter(prefix="/github", tags=["github"])


@router.get("/status", response_model=Message)
def github_status() -> Message:
    """Report whether GitHub integration is configured."""

    client = GitHubClient()
    if client.is_configured:
        return Message(detail="GitHub integration is configured.")
    return Message(detail="GitHub integration is not configured (no token set).")
