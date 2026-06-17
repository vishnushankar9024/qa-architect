"""Governed business rule catalog endpoints."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse

from app.models.rule_catalog import RuleCatalogModel
from app.rule_catalog.service import RuleCatalogInputError, RuleCatalogService

router = APIRouter(tags=["rule-catalog"])


@router.post("/rule-catalog/build", response_model=RuleCatalogModel)
def build_rule_catalog() -> RuleCatalogModel:
    """Build the governed rule catalog from artifacts only."""

    try:
        return RuleCatalogService().build()
    except RuleCatalogInputError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/rule-catalog", response_model=RuleCatalogModel)
def get_rule_catalog() -> RuleCatalogModel:
    """Return the persisted ``business-rule-catalog.json`` artifact."""

    catalog = RuleCatalogService().load()
    if catalog is None:
        raise HTTPException(
            status_code=404,
            detail="No rule catalog found. Run POST /rule-catalog/build first.",
        )
    return catalog


@router.get("/rule-catalog/markdown", response_class=PlainTextResponse)
def get_rule_catalog_markdown() -> str:
    """Return the persisted ``business-rule-catalog.md`` artifact."""

    markdown = RuleCatalogService().load_markdown()
    if markdown is None:
        raise HTTPException(
            status_code=404,
            detail="No Markdown rule catalog found. Run POST /rule-catalog/build first.",
        )
    return markdown
