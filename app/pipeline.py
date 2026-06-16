"""The QA Architect artifact pipeline — the "Artifact First Rule".

Every stage consumes the output artifact of the **previous** stage and writes
its own artifact. Repositories are scanned **only** in the Discovery stage; once
an artifact exists, downstream stages must read the artifact instead of
re-reading or re-cloning the repository.

Allowed chain (each arrow = "consumes"):

    application.json
    -> feature-inventory.json
    -> domain-model.json
    -> business-rules.json
    -> test-strategy.json
    -> test-scenarios.json

This module is the single source of truth for that ordering and for artifact
file names, plus generic save/load helpers and enforcement of the rule via
:func:`require_previous_artifact`.
"""

from __future__ import annotations

from pathlib import Path
from typing import TypeVar

from pydantic import BaseModel

from app.config import Settings, get_settings

# Ordered (stage, artifact-filename) pairs. Order defines the pipeline.
PIPELINE: tuple[tuple[str, str], ...] = (
    ("discovery", "application.json"),
    ("features", "feature-inventory.json"),
    ("domains", "domain-model.json"),
    ("business-rules", "business-rules.json"),
    ("test-strategy", "test-strategy.json"),
    ("test-scenarios", "test-scenarios.json"),
)

# Only this stage is permitted to scan/clone repositories.
REPOSITORY_SCANNING_STAGE = "discovery"

# Stages that currently have a runnable implementation (the rest are reserved
# placeholders in the chain).
IMPLEMENTED_STAGES: tuple[str, ...] = ("discovery", "features", "domains")

_ARTIFACT_BY_STAGE: dict[str, str] = {stage: name for stage, name in PIPELINE}
_STAGE_ORDER: list[str] = [stage for stage, _ in PIPELINE]

T = TypeVar("T", bound=BaseModel)


class MissingArtifactError(RuntimeError):
    """Raised when a required upstream artifact does not exist."""


def output_dir(settings: Settings | None = None) -> Path:
    """Return the configured artifact output directory."""

    settings = settings or get_settings()
    return Path(settings.output_dir)


def artifact_path(filename: str, settings: Settings | None = None) -> Path:
    """Return the absolute path for an artifact ``filename``."""

    return output_dir(settings) / filename


def stage_artifact(stage: str) -> str:
    """Return the artifact filename produced by ``stage``."""

    try:
        return _ARTIFACT_BY_STAGE[stage]
    except KeyError as exc:
        raise KeyError(f"Unknown pipeline stage: {stage!r}") from exc


def previous_stage(stage: str) -> str | None:
    """Return the stage that comes before ``stage`` (or ``None`` for the first)."""

    index = _STAGE_ORDER.index(stage)
    return _STAGE_ORDER[index - 1] if index > 0 else None


def previous_artifact(stage: str) -> str | None:
    """Return the artifact filename ``stage`` must consume, or ``None``."""

    prev = previous_stage(stage)
    return stage_artifact(prev) if prev else None


def save_model(filename: str, model: BaseModel, settings: Settings | None = None) -> Path:
    """Persist a pydantic ``model`` as JSON under the output directory."""

    path = artifact_path(filename, settings)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(model.model_dump_json(indent=2) + "\n", encoding="utf-8")
    return path


def load_model(
    filename: str,
    model_cls: type[T],
    settings: Settings | None = None,
) -> T | None:
    """Load an artifact into ``model_cls``, or return ``None`` if it is absent."""

    path = artifact_path(filename, settings)
    if not path.is_file():
        return None
    return model_cls.model_validate_json(path.read_text(encoding="utf-8"))


def require_previous_artifact(stage: str, settings: Settings | None = None) -> Path:
    """Enforce the Artifact First Rule for ``stage``.

    Returns the path to the previous stage's artifact, raising
    :class:`MissingArtifactError` if it has not been produced yet. The first
    stage (Discovery) has no upstream artifact and raises ``ValueError``.
    """

    prev_artifact = previous_artifact(stage)
    if prev_artifact is None:
        raise ValueError(f"Stage {stage!r} is the first stage and has no upstream artifact.")

    path = artifact_path(prev_artifact, settings)
    if not path.is_file():
        prev = previous_stage(stage)
        raise MissingArtifactError(
            f"{prev_artifact} not found. Run the '{prev}' stage before '{stage}'."
        )
    return path


def pipeline_status(settings: Settings | None = None):
    """Return a validation snapshot of the artifact pipeline.

    Reports, per stage, whether its artifact exists and whether the stage is
    implemented, plus the next implemented stage that can run (its upstream
    artifact is present). Imported lazily to avoid a model import at module load.
    """

    from app.models.pipeline import PipelineStatus, StageStatus

    stages: list[StageStatus] = []
    completed: list[str] = []
    for stage, artifact in PIPELINE:
        exists = artifact_path(artifact, settings).is_file()
        stages.append(
            StageStatus(
                stage=stage,
                artifact=artifact,
                artifact_exists=exists,
                implemented=stage in IMPLEMENTED_STAGES,
            )
        )
        if exists:
            completed.append(stage)

    next_stage: str | None = None
    for stage, artifact in PIPELINE:
        if stage not in IMPLEMENTED_STAGES:
            continue
        if artifact_path(artifact, settings).is_file():
            continue
        prev = previous_artifact(stage)
        if prev is None or artifact_path(prev, settings).is_file():
            next_stage = stage
            break

    return PipelineStatus(
        output_dir=str(output_dir(settings)),
        stages=stages,
        completed_stages=completed,
        next_stage=next_stage,
    )
