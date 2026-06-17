"""Business rule discovery endpoints."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException

from app.business_rules.service import BusinessRulesInputError, BusinessRulesService
from app.models.business_rules import BusinessRulesModel

router = APIRouter(tags=["business-rules"])


@router.post("/business-rules", response_model=BusinessRulesModel)
def build_business_rules_artifact() -> BusinessRulesModel:
    """Build business rule candidates from existing artifacts only.

    Reuses ``application.json`` + ``feature-inventory.json`` +
    ``domain-model.json`` + ``traceability.json`` and writes
    ``outputs/business-rules.json``. No repository is read or cloned.
    """

    try:
        return BusinessRulesService().build()
    except BusinessRulesInputError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/business-rules", response_model=BusinessRulesModel)
def get_business_rules() -> BusinessRulesModel:
    """Return the persisted ``business-rules.json`` artifact."""

    model = BusinessRulesService().load()
    if model is None:
        raise HTTPException(
            status_code=404,
            detail="No business rules found. Run POST /business-rules first.",
        )
    return model
