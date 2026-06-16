"""Smoke tests for the QA Architect API."""

from __future__ import annotations

from fastapi.testclient import TestClient

from app.api import app

client = TestClient(app)


def test_root_health() -> None:
    response = client.get("/")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["app_name"] == "QA Architect"


def test_health_endpoint() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_discovery_repositories_empty() -> None:
    response = client.get("/discovery/repositories")
    assert response.status_code == 200
    assert response.json() == []


def test_knowledge_entries_empty() -> None:
    response = client.get("/knowledge/entries")
    assert response.status_code == 200
    assert response.json() == []


def test_qa_test_plan_placeholder() -> None:
    response = client.get("/qa/test-plan", params={"repository": "octocat/Hello-World"})
    assert response.status_code == 200
    body = response.json()
    assert body["repository"] == "octocat/Hello-World"
    assert body["test_cases"] == []


def test_github_status() -> None:
    response = client.get("/github/status")
    assert response.status_code == 200
    assert "GitHub integration" in response.json()["detail"]
