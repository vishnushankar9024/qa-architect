"""QA Architect module endpoints."""

from __future__ import annotations

from fastapi import APIRouter

from app.models.qa import TestPlan
from app.qa.service import QAArchitectService

router = APIRouter(prefix="/qa", tags=["qa"])


@router.get("/test-plan", response_model=TestPlan)
def build_test_plan(repository: str) -> TestPlan:
    """Build a placeholder test plan for a repository."""

    return QAArchitectService().build_test_plan(repository)
