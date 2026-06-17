"""Feature discovery endpoints."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.features.service import FeatureInputError, FeatureService
from app.models.feature import FeatureInventory

router = APIRouter(tags=["features"])


@router.post("/features", response_model=FeatureInventory)
def build_features() -> FeatureInventory:
    """Build a feature inventory from ``application.json``.

    Reuses the existing discovery artifact only — no repository is read or
    cloned. The result is written to ``outputs/feature-inventory.json``.
    """

    try:
        return FeatureService().build()
    except FeatureInputError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/features", response_model=FeatureInventory)
def get_features() -> FeatureInventory:
    """Return the persisted ``feature-inventory.json`` artifact."""

    inventory = FeatureService().load()
    if inventory is None:
        raise HTTPException(
            status_code=404,
            detail="No feature inventory found. Run POST /features first.",
        )
    return inventory
