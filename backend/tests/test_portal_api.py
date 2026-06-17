from fastapi.testclient import TestClient

from app.main import app
from app.store import store

client = TestClient(app)


def setup_function() -> None:
    store.projects.clear()
    store.sources.clear()
    store.knowledge_bases.clear()
    store.review_log.clear()


def test_end_to_end_portal_flow() -> None:
    create_project = client.post(
        "/projects",
        json={
            "name": "Payments Platform",
            "description": "Project for checkout modernization",
            "createdBy": "qa.architect",
        },
    )
    assert create_project.status_code == 200
    project = create_project.json()
    project_id = project["id"]
    assert project["status"] == "Draft"

    repo_source = client.post(
        f"/projects/{project_id}/sources/repository",
        json={
            "sourceType": "GitHub URL",
            "url": "https://github.com/example/payments",
            "createdBy": "qa.architect",
        },
    )
    assert repo_source.status_code == 200
    assert repo_source.json()["status"] == "Uploaded"

    doc_source = client.post(
        f"/projects/{project_id}/sources/document",
        json={
            "sourceType": "Markdown",
            "fileName": "requirements.md",
            "fileSizeBytes": 2048,
            "createdBy": "qa.architect",
        },
    )
    assert doc_source.status_code == 200
    assert doc_source.json()["metadata"]["fileName"] == "requirements.md"

    generate = client.post(f"/knowledge-base/{project_id}")
    assert generate.status_code == 200
    knowledge = generate.json()
    assert len(knowledge["features"]) > 0
    assert len(knowledge["domains"]) > 0
    assert len(knowledge["business_rules"]) > 0
    assert len(knowledge["flows"]) > 0
    assert len(knowledge["traceability"]) > 0

    feature_to_approve = knowledge["features"][0]["id"]
    review = client.post(
        "/review",
        json={
            "projectId": project_id,
            "artifactType": "features",
            "itemId": feature_to_approve,
            "action": "approve",
            "reviewer": "lead.reviewer",
        },
    )
    assert review.status_code == 200
    assert review.json()["status"] == "Approved"

    dashboard = client.get(f"/knowledge-base/{project_id}/dashboard")
    assert dashboard.status_code == 200
    metrics = dashboard.json()
    assert metrics["featureCount"] >= 1
    assert metrics["approvalPercentage"] >= 0

    export_json = client.get(f"/export/{project_id}?format=json")
    assert export_json.status_code == 200
    assert export_json.headers["content-type"].startswith("application/json")

    export_md = client.get(f"/export/{project_id}?format=markdown")
    assert export_md.status_code == 200
    assert export_md.text.startswith("# Knowledge Pack")

    export_csv = client.get(f"/export/{project_id}?format=csv")
    assert export_csv.status_code == 200
    assert "type,id,name_or_source" in export_csv.text
