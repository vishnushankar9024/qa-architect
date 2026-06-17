"""Models for the business rule discovery stage."""

from __future__ import annotations

from pydantic import BaseModel, Field


class BusinessRule(BaseModel):
    """A deterministic business rule candidate."""

    id: str = Field(..., description="Stable business rule identifier.")
    rule: str = Field(..., description="Business-facing rule candidate.")
    confidence: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Deterministic confidence score between 0 and 1.",
    )


class DomainBusinessRules(BaseModel):
    """Rule candidates grouped by business domain."""

    domain: str = Field(..., description="Business domain name.")
    rules: list[BusinessRule] = Field(
        default_factory=list,
        description="Business rule candidates inferred for this domain.",
    )


class BusinessRulesModel(BaseModel):
    """Business rule candidates grouped by domain."""

    domains: list[DomainBusinessRules] = Field(
        default_factory=list,
        description="Domain-level business rule candidates.",
    )
