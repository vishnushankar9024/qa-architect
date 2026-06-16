"""Tests for the Artifact First Rule pipeline definition and enforcement."""

from __future__ import annotations

from pathlib import Path

import pytest

from app import pipeline
from app.config import get_settings


@pytest.fixture
def artifact_dir(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    out = tmp_path / "outputs"
    monkeypatch.setattr(get_settings(), "output_dir", str(out))
    return out


def test_pipeline_chain_order() -> None:
    stages = [stage for stage, _ in pipeline.PIPELINE]
    assert stages == [
        "discovery",
        "features",
        "domains",
        "traceability",
        "business-rules",
        "test-strategy",
        "test-scenarios",
    ]
    artifacts = [name for _, name in pipeline.PIPELINE]
    assert artifacts == [
        "application.json",
        "feature-inventory.json",
        "domain-model.json",
        "traceability.json",
        "business-rules.json",
        "test-strategy.json",
        "test-scenarios.json",
    ]


def test_only_discovery_scans_repositories() -> None:
    assert pipeline.REPOSITORY_SCANNING_STAGE == "discovery"


def test_previous_artifact_mapping() -> None:
    assert pipeline.previous_stage("discovery") is None
    assert pipeline.previous_artifact("discovery") is None
    assert pipeline.previous_artifact("features") == "application.json"
    assert pipeline.previous_artifact("domains") == "feature-inventory.json"
    assert pipeline.previous_artifact("traceability") == "domain-model.json"
    assert pipeline.previous_artifact("business-rules") == "traceability.json"
    assert pipeline.previous_artifact("test-strategy") == "business-rules.json"
    assert pipeline.previous_artifact("test-scenarios") == "test-strategy.json"


def test_require_previous_artifact_missing_then_present(artifact_dir: Path) -> None:
    # The 'features' stage requires application.json upstream.
    with pytest.raises(pipeline.MissingArtifactError):
        pipeline.require_previous_artifact("features")

    artifact_dir.mkdir(parents=True, exist_ok=True)
    (artifact_dir / "application.json").write_text("{}", encoding="utf-8")

    path = pipeline.require_previous_artifact("features")
    assert path == artifact_dir / "application.json"


def test_require_previous_artifact_first_stage_raises() -> None:
    with pytest.raises(ValueError):
        pipeline.require_previous_artifact("discovery")


def test_pipeline_status_progression(artifact_dir: Path) -> None:
    from fastapi.testclient import TestClient

    from app.api import app

    client = TestClient(app)

    # Nothing generated yet -> discovery is next, nothing completed.
    status = client.get("/pipeline-status").json()
    assert status["next_stage"] == "discovery"
    assert status["completed_stages"] == []
    assert {s["stage"] for s in status["stages"]} == {
        "discovery",
        "features",
        "domains",
        "traceability",
        "business-rules",
        "test-strategy",
        "test-scenarios",
    }
    # Implemented flags are reported.
    impl = {s["stage"]: s["implemented"] for s in status["stages"]}
    assert impl["discovery"] and impl["features"] and impl["domains"]
    assert impl["traceability"]
    assert not impl["business-rules"]

    # After the discovery artifact exists, features becomes the next stage.
    artifact_dir.mkdir(parents=True, exist_ok=True)
    (artifact_dir / "application.json").write_text("{}", encoding="utf-8")
    status = client.get("/pipeline-status").json()
    assert status["completed_stages"] == ["discovery"]
    assert status["next_stage"] == "features"

    # After features + domains artifacts exist, traceability is next.
    (artifact_dir / "feature-inventory.json").write_text("{}", encoding="utf-8")
    (artifact_dir / "domain-model.json").write_text("{}", encoding="utf-8")
    status = client.get("/pipeline-status").json()
    assert status["completed_stages"] == ["discovery", "features", "domains"]
    assert status["next_stage"] == "traceability"

    # Once traceability also exists, no implemented stage remains.
    (artifact_dir / "traceability.json").write_text("{}", encoding="utf-8")
    status = client.get("/pipeline-status").json()
    assert status["completed_stages"] == ["discovery", "features", "domains", "traceability"]
    assert status["next_stage"] is None
