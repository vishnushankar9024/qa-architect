"""Models for the repository discovery module."""

from __future__ import annotations

from pydantic import BaseModel, Field


class DiscoverRequest(BaseModel):
    """Request body for the ``POST /discover`` endpoint."""

    repo_url: str = Field(
        ...,
        description="GitHub repository URL to clone and analyze.",
        examples=["https://github.com/octocat/Hello-World"],
    )
    branch: str | None = Field(
        None,
        description="Optional branch/ref to clone (defaults to the repo's default branch).",
    )


class AngularInsights(BaseModel):
    """Structural insights for Angular standalone applications.

    Standalone Angular apps have no ``*.module.ts`` files, so feature grouping
    must be inferred from folder structure and the routing graph instead.
    """

    feature_folders: list[str] = Field(
        default_factory=list,
        description="Feature folders under the app source root (standalone feature groupings).",
    )
    route_groups: list[str] = Field(
        default_factory=list,
        description="Route-group files (``*.routes.ts``) excluding the root app routes.",
    )
    lazy_feature_areas: list[str] = Field(
        default_factory=list,
        description="Feature areas loaded lazily via loadChildren/loadComponent imports.",
    )
    component_hierarchy: dict[str, list[str]] = Field(
        default_factory=dict,
        description="Mapping of feature folder -> component names within it.",
    )


class DiscoveryResult(BaseModel):
    """Deterministic discovery result for a repository.

    Field shape matches the QA Architect discovery contract.
    """

    application: str = Field("", description="Application/repository name.")
    technology: list[str] = Field(
        default_factory=list,
        description="Detected technologies (e.g. Angular, React, NodeJS, Python, MongoDB).",
    )
    modules: list[str] = Field(default_factory=list, description="Discovered modules.")
    routes: list[str] = Field(default_factory=list, description="Discovered frontend routes.")
    controllers: list[str] = Field(
        default_factory=list,
        description="Discovered controllers (Nest/Express/AngularJS).",
    )
    apis: list[str] = Field(default_factory=list, description="Discovered backend API endpoints.")
    services: list[str] = Field(default_factory=list, description="Discovered services.")
    collections: list[str] = Field(
        default_factory=list,
        description="Discovered MongoDB collections/models.",
    )
    roles: list[str] = Field(default_factory=list, description="Discovered roles.")
    config_files: list[str] = Field(
        default_factory=list,
        description="Discovered configuration files (relative paths).",
    )
    angular: AngularInsights | None = Field(
        None,
        description="Angular standalone structural insights (None if not applicable).",
    )


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
