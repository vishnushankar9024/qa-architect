"""Models for the feature discovery stage."""

from __future__ import annotations

from pydantic import BaseModel, Field


class Feature(BaseModel):
    """A business feature grouping discovery artifacts."""

    name: str = Field(..., description="Human-friendly feature name.")
    modules: list[str] = Field(default_factory=list, description="Modules in this feature.")
    routes: list[str] = Field(default_factory=list, description="Routes in this feature.")
    apis: list[str] = Field(default_factory=list, description="API endpoints in this feature.")
    collections: list[str] = Field(
        default_factory=list,
        description="MongoDB collections in this feature.",
    )


class FeatureInventory(BaseModel):
    """A deterministic inventory of business features."""

    features: list[Feature] = Field(
        default_factory=list,
        description="Discovered business features.",
    )
