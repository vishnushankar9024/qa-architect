"""Domain discovery endpoints."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.domains.service import DomainInputError, DomainService
from app.models.domain import DomainModel

router = APIRouter(tags=["domains"])


@router.post("/domains", response_model=DomainModel)
def build_domains() -> DomainModel:
    """Group ``feature-inventory.json`` into business domains.

    Reuses the existing feature artifact only — no repository is read or cloned.
    The result is written to ``outputs/domain-model.json``.
    """

    try:
        return DomainService().build()
    except DomainInputError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/domains", response_model=DomainModel)
def get_domains() -> DomainModel:
    """Return the persisted ``domain-model.json`` artifact."""

    model = DomainService().load()
    if model is None:
        raise HTTPException(
            status_code=404,
            detail="No domain model found. Run POST /domains first.",
        )
    return model
