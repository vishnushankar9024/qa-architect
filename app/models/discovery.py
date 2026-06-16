"""Models for the repository discovery module."""

from __future__ import annotations

from pydantic import BaseModel, Field


class RepositoryFile(BaseModel):
    """A single file discovered within a repository."""

    path: str = Field(..., description="Path of the file relative to the repo root.")
    size: int = Field(0, ge=0, description="File size in bytes.")
    language: str | None = Field(None, description="Detected programming language.")


class Repository(BaseModel):
    """A source code repository known to QA Architect."""

    full_name: str = Field(..., description="Owner/name identifier, e.g. 'octocat/Hello-World'.")
    description: str | None = Field(None, description="Short repository description.")
    default_branch: str = Field("main", description="Default branch name.")
    private: bool = Field(False, description="Whether the repository is private.")
    files: list[RepositoryFile] = Field(
        default_factory=list,
        description="Files discovered during repository scanning.",
    )
