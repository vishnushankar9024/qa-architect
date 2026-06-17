"""Tests for QA-focused business rule enrichment."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.api import app
from app.business_rule_enrichment.engine import build_enriched_business_rules
from app.config import get_settings
from app.discovery.artifacts import save_application
from app.domains.artifacts import save_domain_model
from app.features.artifacts import save_inventory
from app.models.discovery import DiscoveryResult
from app.models.domain import Domain, DomainModel
from app.models.feature import Feature, FeatureInventory
from app.models.rule_catalog import CatalogRule, RuleCatalogModel, RuleCatalogSummary
from app.models.traceability import DomainTrace, FeatureTrace, TraceabilityModel
from app.rule_catalog.artifacts import save_catalog
from app.traceability.artifacts import save_traceability

client = TestClient(app)


@pytest.fixture
def artifact_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    out = tmp_path / "outputs"
    monkeypatch.setattr(get_settings(), "output_dir", str(out))
    return out


def _application() -> DiscoveryResult:
    return DiscoveryResult(application="demo", technology=["NodeJS", "MongoDB"])


def _inventory() -> FeatureInventory:
    return FeatureInventory(
        features=[
            Feature(
                name="Checklist Management",
                apis=["POST /checklists", "GET /checklists"],
                collections=["Checklist"],
            ),
            Feature(
                name="Approval Management",
                apis=["POST /:id/approve"],
                collections=["Approval"],
            ),
            Feature(
                name="Notification Management",
                apis=["POST /notifications"],
                collections=["Notification"],
            ),
        ]
    )


def _domain_model() -> DomainModel:
    return DomainModel(
        domains=[
            Domain(
                name="Workflow, Approval and RACI",
                features=["Checklist Management", "Approval Management"],
            ),
            Domain(
                name="Collaboration and Communication",
                features=["Notification Management"],
            ),
        ]
    )


def _traceability() -> TraceabilityModel:
    return TraceabilityModel(
        domains=[
            DomainTrace(
                name="Workflow, Approval and RACI",
                features=[
                    FeatureTrace(
                        name="Checklist Management",
                        apis=["POST /checklists", "GET /checklists"],
                        collections=["Checklist"],
                    ),
                    FeatureTrace(
                        name="Approval Management",
                        apis=["POST /:id/approve"],
                        collections=["Approval"],
                    ),
                ],
            ),
            DomainTrace(
                name="Collaboration and Communication",
                features=[
                    FeatureTrace(
                        name="Notification Management",
                        apis=["POST /notifications"],
                        collections=["Notification"],
                    )
                ],
            ),
        ]
    )


def _catalog() -> RuleCatalogModel:
    rules = [
        CatalogRule(
            id="BR-001",
            domain="Workflow, Approval and RACI",
            feature="Checklist",
            title="Checklist records must be created through controlled API actions",
            description="Checklist records must be created through controlled API actions.",
            rule_type="Technical",
            priority="Low",
            source="Generated",
            status="Generated",
            evidence=["Generated"],
            tags=["crud"],
            confidence=0.72,
            generated_rule_id="BR-001",
        ),
        CatalogRule(
            id="BR-002",
            domain="Workflow, Approval and RACI",
            feature="Checklist",
            title="Checklist records must be retrievable for authorized users",
            description="Checklist records must be retrievable for authorized users.",
            rule_type="Authorization",
            priority="Low",
            source="Generated",
            status="Generated",
            evidence=["Generated"],
            tags=["crud"],
            confidence=0.64,
            generated_rule_id="BR-002",
        ),
        CatalogRule(
            id="BR-003",
            domain="Workflow, Approval and RACI",
            feature="Approval",
            title="Only accountable users should approve items in Approval",
            description="Only accountable users should approve items in Approval.",
            rule_type="Workflow",
            priority="High",
            source="Generated",
            status="Generated",
            evidence=["Generated"],
            tags=["approval", "raci"],
            confidence=0.88,
            generated_rule_id="BR-003",
        ),
        CatalogRule(
            id="BR-004",
            domain="Collaboration and Communication",
            feature="Notification",
            title="Notification records must be created through controlled API actions",
            description="Notification records must be created through controlled API actions.",
            rule_type="Technical",
            priority="Low",
            source="Generated",
            status="Generated",
            evidence=["Generated"],
            tags=["crud"],
            confidence=0.72,
            generated_rule_id="BR-004",
        ),
        CatalogRule(
            id="BR-005",
            domain="Workflow, Approval and RACI",
            feature="Checklist",
            title="Checklist item records must be created through controlled API actions",
            description="Checklist item records must be created through controlled API actions.",
            rule_type="Technical",
            priority="Low",
            source="Generated",
            status="Generated",
            evidence=["Generated"],
            tags=["crud"],
            confidence=0.72,
            generated_rule_id="BR-005",
        ),
        CatalogRule(
            id="BR-006",
            domain="Workflow, Approval and RACI",
            feature="Checklist",
            title="Checklist comment records must be created through controlled API actions",
            description="Checklist comment records must be created through controlled API actions.",
            rule_type="Technical",
            priority="Low",
            source="Generated",
            status="Generated",
            evidence=["Generated"],
            tags=["crud"],
            confidence=0.72,
            generated_rule_id="BR-006",
        ),
        CatalogRule(
            id="BR-007",
            domain="Workflow, Approval and RACI",
            feature="Checklist",
            title="Checklist item records must be retrievable for authorized users",
            description="Checklist item records must be retrievable for authorized users.",
            rule_type="Authorization",
            priority="Low",
            source="Generated",
            status="Generated",
            evidence=["Generated"],
            tags=["crud"],
            confidence=0.64,
            generated_rule_id="BR-007",
        ),
    ]
    return RuleCatalogModel(
        summary=RuleCatalogSummary(total_generated_rules=len(rules), total_merged_rules=len(rules)),
        rules=rules,
    )


def test_enrichment_consolidates_crud_and_adds_qa_rules() -> None:
    model, report = build_enriched_business_rules(
        _application(),
        _inventory(),
        _domain_model(),
        _traceability(),
        _catalog(),
    )

    rules = {rule.rule: rule for rule in model.rules}
    assert report.source_catalog_rules == 7
    assert report.source_crud_rules == 6
    assert report.crud_rules < report.source_crud_rules
    assert report.crud_reduction_percentage >= 50
    assert report.average_testing_value_score > 6

    checklist = rules["Mandatory checklist items must be completed before workflow progression."]
    assert checklist.classification == "Validation"
    assert checklist.testing_value_score == 9
    assert checklist.business_criticality == "Critical"
    assert checklist.source_rule_ids

    approval = rules["Only Accountable users may approve workflow items."]
    assert approval.classification == "RACI"
    assert approval.testing_value_score == 10

    notification = rules["Notifications must be generated on workflow state changes."]
    assert notification.classification == "Notification"
    assert notification.testing_value_score == 8


def test_enrichment_endpoint_roundtrip_without_repository_access(
    artifact_dir: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.discovery import cloner

    def fail_clone(*_args, **_kwargs):  # noqa: ANN002, ANN003
        raise AssertionError("enrichment must not clone repositories")

    monkeypatch.setattr(cloner, "clone_repository", fail_clone)

    assert client.post("/business-rules/enrich").status_code == 404
    assert client.get("/business-rules/enriched").status_code == 404
    assert client.get("/business-rules/enriched/markdown").status_code == 404
    assert client.get("/business-rules/quality-report").status_code == 404

    save_application(_application())
    save_inventory(_inventory())
    save_domain_model(_domain_model())
    save_traceability(_traceability())
    save_catalog(_catalog())

    built = client.post("/business-rules/enrich")
    assert built.status_code == 200
    body = built.json()
    assert body["rules"]

    enriched = artifact_dir / "enriched-business-rules.json"
    markdown = artifact_dir / "enriched-business-rules.md"
    quality = artifact_dir / "quality-report.json"
    assert enriched.is_file()
    assert markdown.is_file()
    assert quality.is_file()
    assert json.loads(enriched.read_text()) == body

    assert client.get("/business-rules/enriched").json() == body
    assert "Mandatory checklist" in client.get("/business-rules/enriched/markdown").text
    report = client.get("/business-rules/quality-report").json()
    assert report["average_testing_value_score"] > 6
