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
    """Clone a GitHub repository and return a deterministic discovery result.

    The result is also written to ``outputs/application.json`` for reuse by later
    QA Architect stages.
    """

    try:
        return DiscoveryService().discover(request.repo_url, branch=request.branch)
    except CloneError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@discover_router.get("/application", response_model=DiscoveryResult)
def get_application() -> DiscoveryResult:
    """Return the persisted ``application.json`` discovery artifact.

    Later stages should consume this instead of re-reading the repository.
    """

    result = DiscoveryService().load_artifact()
    if result is None:
        raise HTTPException(
            status_code=404,
            detail="No discovery artifact found. Run POST /discover first.",
        )
    return result
