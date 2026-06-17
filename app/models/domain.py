"""Models for the domain discovery stage."""

from __future__ import annotations

from pydantic import BaseModel, Field


class Domain(BaseModel):
    """A business domain grouping one or more features."""

    name: str = Field(..., description="Human-friendly business domain name.")
    features: list[str] = Field(
        default_factory=list,
        description="Feature names (from feature-inventory.json) in this domain.",
    )


class DomainModel(BaseModel):
    """A deterministic grouping of features into business domains."""

    domains: list[Domain] = Field(
        default_factory=list,
        description="Discovered business domains.",
    )
