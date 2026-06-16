"""Tests for the deterministic traceability engine."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.api import app
from app.config import get_settings
from app.discovery.artifacts import save_application
from app.domains.artifacts import save_domain_model
from app.features.artifacts import save_inventory
from app.models.discovery import AngularInsights, DiscoveryResult
from app.models.domain import Domain, DomainModel
from app.models.feature import Feature, FeatureInventory
from app.traceability.engine import build_traceability

client = TestClient(app)


@pytest.fixture
def artifact_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    out = tmp_path / "outputs"
    monkeypatch.setattr(get_settings(), "output_dir", str(out))
    return out


def _application() -> DiscoveryResult:
    return DiscoveryResult(
        application="demo",
        technology=["Angular", "NodeJS", "MongoDB"],
        services=["OpportunityHubService", "AuthService", "UserService"],
        collections=["Order"],
        angular=AngularInsights(
            component_hierarchy={
                "opportunity-hub": ["opportunity-list", "opportunity-detail"],
                "auth": ["login"],
            }
        ),
    )


def _inventory() -> FeatureInventory:
    return FeatureInventory(
        features=[
            Feature(
                name="Opportunityhub Management",
                routes=["opportunity", "opportunity-hub/:id/details"],
                apis=["GET /api/opportunities"],
                collections=["Order"],
            ),
            Feature(name="Authentication", routes=["login"], apis=["POST /login"]),
        ]
    )


def _domain_model() -> DomainModel:
    return DomainModel(
        domains=[
            Domain(name="Opportunity Management", features=["Opportunityhub Management"]),
            Domain(name="Identity and Access Management", features=["Authentication"]),
        ]
    )


def _feature(model, domain_name, feature_name):  # noqa: ANN001
    domain = next(d for d in model.domains if d.name == domain_name)
    return next(f for f in domain.features if f.name == feature_name)


def test_build_traceability_links_everything() -> None:
    model = build_traceability(_application(), _inventory(), _domain_model())

    opp = _feature(model, "Opportunity Management", "Opportunityhub Management")
    assert opp.routes == ["opportunity", "opportunity-hub/:id/details"]
    assert opp.components == ["opportunity-detail", "opportunity-list"]
    assert opp.services == ["OpportunityHubService"]
    assert opp.apis == ["GET /api/opportunities"]
    assert opp.collections == ["Order"]

    auth = _feature(model, "Identity and Access Management", "Authentication")
    assert auth.routes == ["login"]
    assert auth.components == ["login"]
    assert auth.services == ["AuthService"]


def test_traceability_is_deterministic() -> None:
    args = (_application(), _inventory(), _domain_model())
    assert build_traceability(*args).model_dump() == build_traceability(*args).model_dump()


def test_traceability_endpoint_roundtrip(artifact_dir: Path) -> None:
    # Artifact First Rule: without domain-model.json the build must 404.
    assert client.post("/traceability").status_code == 404
    assert client.get("/traceability").status_code == 404

    save_application(_application())
    save_inventory(_inventory())
    save_domain_model(_domain_model())

    built = client.post("/traceability")
    assert built.status_code == 200
    body = built.json()
    assert set(body.keys()) == {"domains"}
    feature_keys = {
        tuple(sorted(f.keys()))
        for d in body["domains"]
        for f in d["features"]
    }
    assert feature_keys == {("apis", "collections", "components", "name", "routes", "services")}

    artifact = artifact_dir / "traceability.json"
    assert artifact.is_file()
    assert json.loads(artifact.read_text()) == body

    fetched = client.get("/traceability")
    assert fetched.status_code == 200
    assert fetched.json() == body


def test_traceability_requires_all_upstream_artifacts(artifact_dir: Path) -> None:
    # Only domain-model present (upstream chain normally guarantees the others,
    # but the service defends against a deleted intermediate artifact).
    save_domain_model(_domain_model())
    response = client.post("/traceability")
    assert response.status_code == 404
    assert "application.json" in response.json()["detail"]