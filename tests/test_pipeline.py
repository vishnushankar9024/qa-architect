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
        "business-rules",
        "test-strategy",
        "test-scenarios",
    ]
    artifacts = [name for _, name in pipeline.PIPELINE]
    assert artifacts == [
        "application.json",
        "feature-inventory.json",
        "domain-model.json",
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
    assert pipeline.previous_artifact("business-rules") == "domain-model.json"
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
