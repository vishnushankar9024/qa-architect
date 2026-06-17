"""Tests for the deterministic feature discovery stage.

These tests build a ``DiscoveryResult`` directly (no clone / repo reads) and run
the grouping + artifact pipeline fully offline.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app.api import app
from app.config import get_settings
from app.discovery.artifacts import save_application
from app.features.grouping import build_feature_inventory
from app.models.discovery import DiscoveryResult

client = TestClient(app)


@pytest.fixture
def artifact_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    out = tmp_path / "outputs"
    monkeypatch.setattr(get_settings(), "output_dir", str(out))
    return out


def _sample_application() -> DiscoveryResult:
    return DiscoveryResult(
        application="demo-app",
        technology=["NodeJS", "MongoDB"],
        modules=["users", "orders", "app"],
        routes=["/users", "/orders/:id", "/login", "/"],
        apis=[
            "GET /api/users",
            "POST /api/users",
            "GET /api/orders/:id",
            "POST /login",
        ],
        services=["UsersService"],
        collections=["User", "Order"],
        roles=["admin"],
        config_files=["package.json"],
    )


def _feature(inventory, name):  # noqa: ANN001
    return next(f for f in inventory.features if f.name == name)


def test_grouping_creates_business_features() -> None:
    inventory = build_feature_inventory(_sample_application())
    names = {f.name for f in inventory.features}

    assert "User Management" in names
    assert "Order Management" in names
    assert "Authentication" in names

    users = _feature(inventory, "User Management")
    assert "users" in users.modules
    assert "/users" in users.routes
    assert "GET /api/users" in users.apis
    assert "POST /api/users" in users.apis
    assert "User" in users.collections

    orders = _feature(inventory, "Order Management")
    assert "orders" in orders.modules
    assert "/orders/:id" in orders.routes
    assert "GET /api/orders/:id" in orders.apis
    assert "Order" in orders.collections

    auth = _feature(inventory, "Authentication")
    assert "/login" in auth.routes
    assert "POST /login" in auth.apis


def test_grouping_is_deterministic() -> None:
    app_result = _sample_application()
    first = build_feature_inventory(app_result).model_dump()
    second = build_feature_inventory(app_result).model_dump()
    assert first == second


def test_general_bucket_collects_ungroupable() -> None:
    inventory = build_feature_inventory(_sample_application())
    # "app" module and "/" route have no business token -> General, listed last.
    general = _feature(inventory, "General")
    assert "app" in general.modules
    assert "/" in general.routes
    assert inventory.features[-1].name == "General"


def test_features_endpoint_roundtrip(artifact_dir: Path) -> None:
    # Without application.json the build must 404.
    assert client.post("/features").status_code == 404
    assert client.get("/features").status_code == 404

    save_application(_sample_application())

    built = client.post("/features")
    assert built.status_code == 200
    body = built.json()
    assert set(body.keys()) == {"features"}
    feature_keys = {tuple(sorted(f.keys())) for f in body["features"]}
    assert feature_keys == {("apis", "collections", "modules", "name", "routes")}

    # Artifact written and reusable via GET.
    artifact = artifact_dir / "feature-inventory.json"
    assert artifact.is_file()
    assert json.loads(artifact.read_text()) == body

    fetched = client.get("/features")
    assert fetched.status_code == 200
    assert fetched.json() == body
