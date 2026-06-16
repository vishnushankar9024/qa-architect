"""Common models used across the API."""

from __future__ import annotations

from pydantic import BaseModel, Field


class Message(BaseModel):
    """A generic message envelope."""

    detail: str = Field(..., description="Human-readable message.")


class HealthStatus(BaseModel):
    """Service health payload."""

    status: str = Field("ok", description="Overall service status.")
    app_name: str = Field(..., description="Configured application name.")
    version: str = Field(..., description="Application version.")
    environment: str = Field(..., description="Runtime environment name.")
