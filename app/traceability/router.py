"""Traceability endpoints."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.models.traceability import TraceabilityModel
from app.traceability.service import TraceabilityInputError, TraceabilityService

router = APIRouter(tags=["traceability"])


@router.post("/traceability", response_model=TraceabilityModel)
def build_traceability_graph() -> TraceabilityModel:
    """Build the Domain -> Feature -> relationships graph from existing artifacts.

    Reuses ``application.json`` + ``feature-inventory.json`` + ``domain-model.json``
    only — no repository is read or cloned. Result is written to
    ``outputs/traceability.json``.
    """

    try:
        return TraceabilityService().build()
    except TraceabilityInputError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/traceability", response_model=TraceabilityModel)
def get_traceability() -> TraceabilityModel:
    """Return the persisted ``traceability.json`` artifact."""

    model = TraceabilityService().load()
    if model is None:
        raise HTTPException(
            status_code=404,
            detail="No traceability graph found. Run POST /traceability first.",
        )
    return model
