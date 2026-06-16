"""Models for the QA Architect module."""

from __future__ import annotations

from pydantic import BaseModel, Field


class TestCase(BaseModel):
    """A single test case definition."""

    id: str = Field(..., description="Stable identifier for the test case.")
    title: str = Field(..., description="Short, descriptive title.")
    steps: list[str] = Field(default_factory=list, description="Ordered test steps.")
    expected_result: str | None = Field(None, description="Expected outcome.")


class TestPlan(BaseModel):
    """A collection of test cases targeting a repository."""

    repository: str = Field(..., description="Target repository full name.")
    summary: str | None = Field(None, description="High-level summary of the plan.")
    test_cases: list[TestCase] = Field(
        default_factory=list,
        description="Test cases that make up the plan.",
    )
