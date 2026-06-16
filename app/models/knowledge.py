"""Models for the knowledge module."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class KnowledgeEntry(BaseModel):
    """A single piece of stored project knowledge."""

    id: str = Field(..., description="Stable identifier for the entry.")
    title: str = Field(..., description="Short title for the entry.")
    content: str = Field(..., description="Body of the knowledge entry.")
    tags: list[str] = Field(default_factory=list, description="Free-form tags.")
    created_at: datetime = Field(
        default_factory=datetime.utcnow,
        description="When the entry was created (UTC).",
    )
