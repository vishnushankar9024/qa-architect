"""Knowledge module endpoints."""

from __future__ import annotations

from fastapi import APIRouter

from app.knowledge.service import KnowledgeService
from app.models.knowledge import KnowledgeEntry

router = APIRouter(prefix="/knowledge", tags=["knowledge"])


@router.get("/entries", response_model=list[KnowledgeEntry])
def list_entries() -> list[KnowledgeEntry]:
    """List stored knowledge entries (placeholder)."""

    return KnowledgeService().list_entries()
