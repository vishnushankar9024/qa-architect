"""Tests for the deterministic domain discovery stage."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.api import app
from app.config import get_settings
from app.domains.grouping import build_domain_model
from app.features.artifacts import save_inventory
from app.models.feature import Feature, FeatureInventory

client = TestClient(app)


@pytest.fixture
def artifact_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    out = tmp_path / "outputs"
    monkeypatch.setattr(get_settings(), "output_dir", str(out))
    return out


def _sample_inventory() -> FeatureInventory:
    names = [
        "Authentication",
        "Roles & Permissions",
        "User Management",
        "Opportunity Management",
        "Award Management",
        "Enquiry Management",
        "Activitychecklist Management",
        "Accountableinput Management",
        "Activityfile Management",
        "Alldelegationlog Management",
        "Allocation Management",
        "Document Management",
        "Notification Management",
        "Widget Management",  # no taxonomy match -> General
    ]
    return FeatureInventory(features=[Feature(name=n) for n in names])


def _domain(model, name):  # noqa: ANN001
    return next(d for d in model.domains if d.name == name)


def test_grouping_into_business_domains() -> None:
    model = build_domain_model(_sample_inventory())
    names = {d.name for d in model.domains}

    assert "Identity and Access Management" in names
    assert "Opportunity and Procurement Lifecycle" in names
    assert "Project and Activity Management" in names
    assert "Workflow, Approval and RACI" in names
    assert "Document, File and Template Management" in names
    assert "Reporting, Audit and Logs" in names
    assert "Location and Asset Management" in names

    iam = _domain(model, "Identity and Access Management")
    assert set(iam.features) == {"Authentication", "Roles & Permissions", "User Management"}

    opp = _domain(model, "Opportunity and Procurement Lifecycle")
    assert {"Opportunity Management", "Award Management", "Enquiry Management"}.issubset(
        set(opp.features)
    )

    assert "Activitychecklist Management" in _domain(
        model, "Project and Activity Management"
    ).features
    assert "Accountableinput Management" in _domain(model, "Workflow, Approval and RACI").features
    assert "Activityfile Management" in _domain(
        model, "Document, File and Template Management"
    ).features
    assert "Alldelegationlog Management" in _domain(model, "Reporting, Audit and Logs").features
    assert "Allocation Management" in _domain(model, "Location and Asset Management").features


def test_unmatched_feature_goes_to_general() -> None:
    model = build_domain_model(_sample_inventory())
    general = _domain(model, "General")
    assert "Widget Management" in general.features
    assert model.domains[-1].name == "General"  # General listed last


def test_grouping_is_deterministic() -> None:
    inv = _sample_inventory()
    first = build_domain_model(inv).model_dump()
    second = build_domain_model(inv).model_dump()
    assert first == second


def test_domains_endpoint_roundtrip(artifact_dir: Path) -> None:
    # Artifact First Rule: without feature-inventory.json the build must 404.
    assert client.post("/domains").status_code == 404
    assert client.get("/domains").status_code == 404

    save_inventory(_sample_inventory())

    built = client.post("/domains")
    assert built.status_code == 200
    body = built.json()
    assert set(body.keys()) == {"domains"}
    domain_keys = {tuple(sorted(d.keys())) for d in body["domains"]}
    assert domain_keys == {("features", "name")}

    artifact = artifact_dir / "domain-model.json"
    assert artifact.is_file()
    assert json.loads(artifact.read_text()) == body

    fetched = client.get("/domains")
    assert fetched.status_code == 200
    assert fetched.json() == body
