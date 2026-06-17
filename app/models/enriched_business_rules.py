"""Models for QA-focused business rule enrichment."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

RuleClassification = Literal[
    "CRUD",
    "Authorization",
    "Workflow",
    "State Transition",
    "Validation",
    "Calculation",
    "Notification",
    "Integration",
    "Audit",
    "RACI",
    "Document Management",
    "Scheduling",
    "Configuration",
]
BusinessCriticality = Literal["Low", "Medium", "High", "Critical"]


class EnrichedBusinessRule(BaseModel):
    """A QA-focused business rule with preserved source traceability."""

    id: str = Field(..., description="Stable enriched rule identifier.")
    source_rule_ids: list[str] = Field(
        default_factory=list,
        description="Generated/catalog rule IDs that led to this enriched rule.",
    )
    classification: RuleClassification = Field(..., description="QA rule classification.")
    testing_value_score: int = Field(
        ...,
        ge=1,
        le=10,
        description="QA testing value from 1 (low) to 10 (highest).",
    )
    business_criticality: BusinessCriticality = Field(..., description="Business criticality.")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Deterministic confidence.")
    rule: str = Field(..., description="QA-focused business rule.")
    domain: str = Field("", description="Business domain.")
    feature: str = Field("", description="Business feature or concept.")
    evidence: list[str] = Field(default_factory=list, description="Traceability evidence.")
    tags: list[str] = Field(default_factory=list, description="Rule tags.")


class EnrichedBusinessRulesModel(BaseModel):
    """QA-focused enriched business rule repository."""

    rules: list[EnrichedBusinessRule] = Field(default_factory=list)


class QualityReport(BaseModel):
    """Rule quality metrics for the enrichment run."""

    total_rules: int = 0
    source_catalog_rules: int = 0
    source_crud_rules: int = 0
    crud_rules: int = 0
    workflow_rules: int = 0
    authorization_rules: int = 0
    validation_rules: int = 0
    raci_rules: int = 0
    consolidated_rules: int = 0
    average_testing_value_score: float = 0.0
    crud_reduction_percentage: float = 0.0
    top_100_highest_value_rules: list[EnrichedBusinessRule] = Field(default_factory=list)
