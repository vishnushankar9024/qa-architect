"""Models for the governed business rule catalog."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, Field

RuleStatus = Literal["Generated", "Draft", "Reviewed", "Approved", "Deprecated"]
RuleSource = Literal["Generated", "Human"]
RuleType = Literal["Business", "Workflow", "Authorization", "Data", "Technical"]
RulePriority = Literal["Low", "Medium", "High", "Critical"]


class CatalogRule(BaseModel):
    """A governed business rule ready for human review and downstream reuse."""

    id: str = Field(..., description="Stable catalog rule identifier.")
    domain: str = Field(..., description="Business domain.")
    feature: str = Field("", description="Business feature or capability.")
    title: str = Field(..., description="Short business-facing rule title.")
    description: str = Field(..., description="Full rule description.")
    rule_type: RuleType = Field("Business", description="Rule classification.")
    priority: RulePriority = Field("Medium", description="Business priority.")
    source: RuleSource = Field(..., description="Generated or Human.")
    author: str | None = Field(None, description="Human author, reviewer, or source owner.")
    status: RuleStatus = Field(..., description="Governed lifecycle status.")
    evidence: list[str] = Field(default_factory=list, description="Traceability evidence.")
    tags: list[str] = Field(default_factory=list, description="Search and grouping tags.")
    confidence: float | None = Field(
        None,
        ge=0.0,
        le=1.0,
        description="Generated confidence score, when available.",
    )
    generated_rule_id: str | None = Field(
        None,
        description="Original generated rule identifier retained for traceability.",
    )


class RuleOverridesModel(BaseModel):
    """Human-authored or human-curated rule overrides."""

    rules: list[CatalogRule] = Field(
        default_factory=list,
        description="Rules maintained by SMEs, architects, BAs, testers, or QA agents.",
    )


class RuleCatalogSummary(BaseModel):
    """Validation summary for a built rule catalog."""

    total_generated_rules: int = 0
    total_human_rules: int = 0
    total_merged_rules: int = 0
    rules_by_status: dict[str, int] = Field(default_factory=dict)
    rules_by_domain: dict[str, int] = Field(default_factory=dict)


class RuleCatalogModel(BaseModel):
    """Merged generated and human-governed business rule catalog."""

    summary: RuleCatalogSummary = Field(default_factory=RuleCatalogSummary)
    rules: list[CatalogRule] = Field(default_factory=list)
