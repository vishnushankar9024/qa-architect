"""FastAPI application factory."""

from __future__ import annotations

from fastapi import FastAPI

from app import __version__, pipeline
from app.config import get_settings
from app.discovery import discover_router
from app.discovery import router as discovery_router
from app.domains import router as domains_router
from app.features import router as features_router
from app.github import router as github_router
from app.knowledge import router as knowledge_router
from app.models.common import HealthStatus
from app.models.pipeline import PipelineStatus
from app.qa import router as qa_router
from app.traceability import router as traceability_router


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""

    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=__version__,
        debug=settings.debug,
    )

    @app.get("/", response_model=HealthStatus, tags=["health"])
    def root() -> HealthStatus:
        """Root health endpoint."""

        return HealthStatus(
            status="ok",
            app_name=settings.app_name,
            version=__version__,
            environment=settings.environment,
        )

    @app.get("/health", response_model=HealthStatus, tags=["health"])
    def health() -> HealthStatus:
        """Liveness/readiness probe."""

        return HealthStatus(
            status="ok",
            app_name=settings.app_name,
            version=__version__,
            environment=settings.environment,
        )

    @app.get("/pipeline-status", response_model=PipelineStatus, tags=["pipeline"])
    def pipeline_status() -> PipelineStatus:
        """Validate the Artifact First pipeline state.

        Reports which stage artifacts exist under the output directory and the
        next implemented stage that can run (its upstream artifact is present).
        """

        return pipeline.pipeline_status()

    app.include_router(discovery_router)
    app.include_router(discover_router)
    app.include_router(features_router)
    app.include_router(domains_router)
    app.include_router(traceability_router)
    app.include_router(knowledge_router)
    app.include_router(qa_router)
    app.include_router(github_router)

    return app


app = create_app()
