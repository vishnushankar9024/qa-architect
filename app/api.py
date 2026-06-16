"""FastAPI application factory."""

from __future__ import annotations

from fastapi import FastAPI

from app import __version__
from app.config import get_settings
from app.discovery import router as discovery_router
from app.github import router as github_router
from app.knowledge import router as knowledge_router
from app.models.common import HealthStatus
from app.qa import router as qa_router


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

    app.include_router(discovery_router)
    app.include_router(knowledge_router)
    app.include_router(qa_router)
    app.include_router(github_router)

    return app


app = create_app()
