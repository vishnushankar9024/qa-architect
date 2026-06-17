"""Tests for deterministic business rule discovery."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.api import app
from app.business_rules.engine import build_business_rules
from app.discovery.artifacts import save_application
from app.domains.artifacts import save_domain_model
from app.features.artifacts import save_inventory
from app.models.discovery import DiscoveryResult
from app.models.domain import Domain, DomainModel
from app.models.feature import Feature, FeatureInventory
from app.models.traceability import DomainTrace, FeatureTrace, TraceabilityModel
from app.config import get_settings
from app.traceability.artifacts import save_traceability

client = TestClient(app)


@pytest.fixture
def artifact_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    out = tmp_path / "outputs"
    monkeypatch.setattr(get_settings(), "output_dir", str(out))
    return out


def _application() -> DiscoveryResult:
    return DiscoveryResult(
        application="demo",
        technology=["NodeJS", "MongoDB"],
        roles=["Accountable", "Responsible"],
    )


def _inventory() -> FeatureInventory:
    return FeatureInventory(
        features=[
            Feature(
                name="RACI Approval Management",
                routes=["raci/:id/approve"],
                apis=["GET /api/raci/:id", "POST /api/raci/:id/approve"],
                collections=["RaciAssignment"],
            ),
            Feature(
                name="Document Management",
                apis=["POST /api/documents", "DELETE /api/documents/:id"],
                collections=["Document"],
            ),
        ]
    )


def _domain_model() -> DomainModel:
    return DomainModel(
        domains=[
            Domain(name="RACI Management", features=["RACI Approval Management"]),
            Domain(name="Document and Template Management", features=["Document Management"]),
        ]
    )


def _traceability() -> TraceabilityModel:
    return TraceabilityModel(
        domains=[
            DomainTrace(
                name="RACI Management",
                features=[
                    FeatureTrace(
                        name="RACI Approval Management",
                        routes=["raci/:id/approve"],
                        apis=["GET /api/raci/:id", "POST /api/raci/:id/approve"],
                        collections=["RaciAssignment"],
                    )
                ],
            ),
            DomainTrace(
                name="Document and Template Management",
                features=[
                    FeatureTrace(
                        name="Document Management",
                        apis=["POST /api/documents", "DELETE /api/documents/:id"],
                        collections=["Document"],
                    )
                ],
            ),
        ]
    )


def test_build_business_rules_infers_deterministic_candidates() -> None:
    model = build_business_rules(_application(), _inventory(), _domain_model(), _traceability())

    assert build_business_rules(
        _application(), _inventory(), _domain_model(), _traceability()
    ).model_dump() == model.model_dump()
    raci = next(domain for domain in model.domains if domain.domain == "RACI Management")
    rules = {rule.rule: rule.confidence for rule in raci.rules}

    assert "Only accountable users should approve items in RACI Approval." in rules
    assert rules["Only accountable users should approve items in RACI Approval."] == 0.88
    assert all(rule.id.startswith("BR-") for domain in model.domains for rule in domain.rules)
    assert all(0 <= rule.confidence <= 1 for domain in model.domains for rule in domain.rules)


def test_business_rules_endpoint_roundtrip_without_repository_access(
    artifact_dir: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    from app.discovery import cloner

    def fail_clone(*_args, **_kwargs):  # noqa: ANN002, ANN003
        raise AssertionError("business rules must not clone repositories")

    monkeypatch.setattr(cloner, "clone_repository", fail_clone)

    assert client.post("/business-rules").status_code == 404
    assert client.get("/business-rules").status_code == 404

    save_application(_application())
    save_inventory(_inventory())
    save_domain_model(_domain_model())
    save_traceability(_traceability())

    built = client.post("/business-rules")
    assert built.status_code == 200
    body = built.json()
    assert set(body.keys()) == {"domains"}
    assert {
        tuple(sorted(rule.keys()))
        for domain in body["domains"]
        for rule in domain["rules"]
    } == {("confidence", "id", "rule")}

    artifact = artifact_dir / "business-rules.json"
    assert artifact.is_file()
    assert json.loads(artifact.read_text()) == body

    fetched = client.get("/business-rules")
    assert fetched.status_code == 200
    assert fetched.json() == body


def test_business_rules_requires_all_upstream_artifacts(artifact_dir: Path) -> None:
    save_traceability(_traceability())

    response = client.post("/business-rules")

    assert response.status_code == 404
    assert "application.json" in response.json()["detail"]
