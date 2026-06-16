"""Repository discovery endpoints."""

from __future__ import annotations

from fastapi import APIRouter

from app.discovery.service import DiscoveryService
from app.models.discovery import Repository

router = APIRouter(prefix="/discovery", tags=["discovery"])


@router.get("/repositories", response_model=list[Repository])
def list_repositories() -> list[Repository]:
    """List repositories known to QA Architect (placeholder)."""

    return DiscoveryService().list_repositories()
