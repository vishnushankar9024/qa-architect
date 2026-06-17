"""Models for pipeline status reporting."""

from __future__ import annotations

from pydantic import BaseModel, Field


class StageStatus(BaseModel):
    """Status of a single pipeline stage."""

    stage: str = Field(..., description="Pipeline stage name.")
    artifact: str = Field(..., description="Artifact filename produced by the stage.")
    artifact_exists: bool = Field(..., description="Whether the artifact has been generated.")
    implemented: bool = Field(..., description="Whether the stage is implemented yet.")


class PipelineStatus(BaseModel):
    """Validation snapshot of the Artifact First pipeline."""

    output_dir: str = Field(..., description="Directory where artifacts are stored.")
    stages: list[StageStatus] = Field(
        default_factory=list,
        description="Per-stage status in pipeline order.",
    )
    completed_stages: list[str] = Field(
        default_factory=list,
        description="Stages whose artifact already exists.",
    )
    next_stage: str | None = Field(
        None,
        description="Next implemented stage that can run (upstream satisfied), or None.",
    )
