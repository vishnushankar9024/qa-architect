"""Tests for the governed business rule catalog layer."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.api import app
from app.business_rules.artifacts import save_business_rules
from app.config import get_settings
from app.models.business_rules import BusinessRule, BusinessRulesModel, DomainBusinessRules
from app.models.rule_catalog import CatalogRule, RuleOverridesModel
from app.rule_catalog.artifacts import save_overrides
from app.rule_catalog.service import build_rule_catalog, render_catalog_markdown

client = TestClient(app)


@pytest.fixture
def artifact_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    out = tmp_path / "outputs"
    monkeypatch.setattr(get_settings(), "output_dir", str(out))
    return out


def _business_rules() -> BusinessRulesModel:
    return BusinessRulesModel(
        domains=[
            DomainBusinessRules(
                domain="Workflow, Approval and RACI",
                rules=[
                    BusinessRule(
                        id="BR-001",
                        rule="Checklist items require an approval decision before completion.",
                        confidence=0.86,
                    ),
                    BusinessRule(
                        id="BR-002",
                        rule="Checklist records must be retrievable for authorized users.",
                        confidence=0.64,
                    ),
                ],
            )
        ]
    )


def _overrides() -> RuleOverridesModel:
    return RuleOverridesModel(
        rules=[
            CatalogRule(
                id="BR-001",
                domain="Workflow, Approval and RACI",
                feature="Checklist",
                title="Checklist completion required",
                description="All mandatory checklist items must be completed before review.",
                rule_type="Workflow",
                priority="High",
                source="Human",
                author="Vishnu Shankar",
                status="Approved",
                evidence=["SME workshop"],
                tags=["workflow", "checklist"],
            ),
            CatalogRule(
                id="BR-PMW-001",
                domain="Document, File and Template Management",
                feature="Documents",
                title="Document upload approval",
                description="Uploaded documents must be approved before publication.",
                rule_type="Workflow",
                priority="Medium",
                source="Human",
                author="Vishnu Shankar",
                status="Draft",
                evidence=[],
                tags=["document"],
            ),
        ]
    )


def test_build_rule_catalog_merges_generated_and_human_rules() -> None:
    catalog = build_rule_catalog(_business_rules(), _overrides())

    assert catalog.summary.total_generated_rules == 2
    assert catalog.summary.total_human_rules == 2
    assert catalog.summary.total_merged_rules == 3
    assert catalog.summary.rules_by_status == {"Draft": 1, "Approved": 1, "Generated": 1}

    overridden = next(rule for rule in catalog.rules if rule.id == "BR-001")
    assert overridden.source == "Human"
    assert overridden.status == "Approved"
    assert overridden.generated_rule_id == "BR-001"
    assert overridden.confidence == 0.86
    assert "Generated from business-rules.json rule BR-001" in overridden.evidence
    assert "SME workshop" in overridden.evidence

    human = next(rule for rule in catalog.rules if rule.id == "BR-PMW-001")
    assert human.source == "Human"
    assert human.status == "Draft"


def test_rule_catalog_markdown_groups_rules_by_domain() -> None:
    markdown = render_catalog_markdown(build_rule_catalog(_business_rules(), _overrides()))

    assert "# Workflow, Approval and RACI" in markdown
    assert "## BR-001" in markdown
    assert "Checklist completion required" in markdown
    assert "Priority: High" in markdown
    assert "Status: Approved" in markdown
    assert "Source: Human" in markdown
    assert "Tags: workflow, approval" in markdown or "Tags: workflow, checklist" in markdown


def test_rule_catalog_endpoint_roundtrip_without_repository_access(
    artifact_dir: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.discovery import cloner

    def fail_clone(*_args, **_kwargs):  # noqa: ANN002, ANN003
        raise AssertionError("rule catalog must not clone repositories")

    monkeypatch.setattr(cloner, "clone_repository", fail_clone)

    assert client.post("/rule-catalog/build").status_code == 404
    assert client.get("/rule-catalog").status_code == 404
    assert client.get("/rule-catalog/markdown").status_code == 404

    save_business_rules(_business_rules())
    save_overrides(_overrides())

    built = client.post("/rule-catalog/build")
    assert built.status_code == 200
    body = built.json()
    assert body["summary"]["total_generated_rules"] == 2
    assert body["summary"]["total_human_rules"] == 2
    assert body["summary"]["total_merged_rules"] == 3

    overrides = artifact_dir / "business-rule-overrides.json"
    catalog = artifact_dir / "business-rule-catalog.json"
    markdown = artifact_dir / "business-rule-catalog.md"
    assert overrides.is_file()
    assert catalog.is_file()
    assert markdown.is_file()
    assert json.loads(catalog.read_text()) == body

    fetched = client.get("/rule-catalog")
    assert fetched.status_code == 200
    assert fetched.json() == body

    fetched_markdown = client.get("/rule-catalog/markdown")
    assert fetched_markdown.status_code == 200
    assert "# Workflow, Approval and RACI" in fetched_markdown.text


def test_rule_catalog_creates_empty_overrides_when_absent(artifact_dir: Path) -> None:
    save_business_rules(_business_rules())

    response = client.post("/rule-catalog/build")

    assert response.status_code == 200
    assert json.loads((artifact_dir / "business-rule-overrides.json").read_text()) == {
        "rules": []
    }
    assert response.json()["summary"]["total_human_rules"] == 0
