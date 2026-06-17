"""QA-focused business rule enrichment endpoints."""

from __future__ import annotations

from fastapi import APIRouter, HTTPException
from fastapi.responses import PlainTextResponse

from app.business_rule_enrichment.service import (
    BusinessRuleEnrichmentInputError,
    BusinessRuleEnrichmentService,
)
from app.models.enriched_business_rules import EnrichedBusinessRulesModel, QualityReport

router = APIRouter(tags=["business-rule-enrichment"])


@router.post("/business-rules/enrich", response_model=EnrichedBusinessRulesModel)
def build_enriched_business_rules() -> EnrichedBusinessRulesModel:
    """Build QA-focused enriched rules from existing artifacts only."""

    try:
        return BusinessRuleEnrichmentService().build()
    except BusinessRuleEnrichmentInputError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc


@router.get("/business-rules/enriched", response_model=EnrichedBusinessRulesModel)
def get_enriched_business_rules() -> EnrichedBusinessRulesModel:
    """Return the persisted ``enriched-business-rules.json`` artifact."""

    model = BusinessRuleEnrichmentService().load()
    if model is None:
        raise HTTPException(
            status_code=404,
            detail="No enriched business rules found. Run POST /business-rules/enrich first.",
        )
    return model


@router.get("/business-rules/enriched/markdown", response_class=PlainTextResponse)
def get_enriched_business_rules_markdown() -> str:
    """Return the persisted ``enriched-business-rules.md`` artifact."""

    markdown = BusinessRuleEnrichmentService().load_markdown()
    if markdown is None:
        raise HTTPException(
            status_code=404,
            detail="No enriched business rules Markdown found. Run POST /business-rules/enrich first.",
        )
    return markdown


@router.get("/business-rules/quality-report", response_model=QualityReport)
def get_quality_report() -> QualityReport:
    """Return the persisted ``quality-report.json`` artifact."""

    report = BusinessRuleEnrichmentService().load_quality_report()
    if report is None:
        raise HTTPException(
            status_code=404,
            detail="No quality report found. Run POST /business-rules/enrich first.",
        )
    return report
