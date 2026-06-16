"""Repository discovery endpoints."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.discovery.cloner import CloneError
from app.discovery.service import DiscoveryService
from app.models.discovery import DiscoverRequest, DiscoveryResult, Repository

router = APIRouter(prefix="/discovery", tags=["discovery"])

# The discovery capability is exposed at the top-level ``POST /discover`` path.
discover_router = APIRouter(tags=["discovery"])


@router.get("/repositories", response_model=list[Repository])
def list_repositories() -> list[Repository]:
    """List repositories known to QA Architect (placeholder)."""

    return DiscoveryService().list_repositories()


@discover_router.post("/discover", response_model=DiscoveryResult)
def discover(request: DiscoverRequest) -> DiscoveryResult:
    """Clone a GitHub repository and return a deterministic discovery result."""

    try:
        return DiscoveryService().discover(request.repo_url, branch=request.branch)
    except CloneError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
