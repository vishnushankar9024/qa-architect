"""Models for the traceability stage."""

from __future__ import annotations

from pydantic import BaseModel, Field


class FeatureTrace(BaseModel):
    """A feature with its traced relationships."""

    name: str = Field(..., description="Feature name.")
    routes: list[str] = Field(default_factory=list, description="Routes for this feature.")
    components: list[str] = Field(
        default_factory=list,
        description="Components for this feature (from Angular component hierarchy).",
    )
    services: list[str] = Field(default_factory=list, description="Services for this feature.")
    apis: list[str] = Field(default_factory=list, description="API endpoints for this feature.")
    collections: list[str] = Field(
        default_factory=list,
        description="MongoDB collections for this feature.",
    )


class DomainTrace(BaseModel):
    """A domain with its features and their traced relationships."""

    name: str = Field(..., description="Business domain name.")
    features: list[FeatureTrace] = Field(
        default_factory=list,
        description="Features within this domain.",
    )


class TraceabilityModel(BaseModel):
    """Domain -> Feature -> (routes/components/services/apis/collections) graph."""

    domains: list[DomainTrace] = Field(
        default_factory=list,
        description="Traceability graph rooted at business domains.",
    )
