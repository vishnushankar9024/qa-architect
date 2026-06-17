"""QA Architect service (placeholder)."""

from __future__ import annotations

from app.models.qa import TestPlan


class QAArchitectService:
    """Produces QA artifacts such as test plans.

    This is a scaffold. AI-assisted generation will be implemented later.
    """

    def build_test_plan(self, repository: str) -> TestPlan:
        """Return an empty test plan for the given repository (placeholder)."""

        return TestPlan(
            repository=repository,
            summary="Placeholder plan; QA generation not implemented yet.",
            test_cases=[],
        )
