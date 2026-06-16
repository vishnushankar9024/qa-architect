# QA Architect — Architecture (Scaffold)

This document is a placeholder describing the intended structure of QA Architect.
AI features are intentionally **not** implemented yet.

## Modules

| Module | Package | Responsibility |
| --- | --- | --- |
| Discovery | `app/discovery` | Locate and scan repositories. |
| Features | `app/features` | Group discovery artifacts into business features. |
| Domains | `app/domains` | Group features into business domains. |
| Traceability | `app/traceability` | Join artifacts into a domain→feature→relationships graph. |
| Knowledge | `app/knowledge` | Store and retrieve project knowledge. |
| QA | `app/qa` | Build test plans and test cases. |
| GitHub | `app/github` | GitHub integration / API access. |
| Models | `app/models` | Shared Pydantic data models. |

## Artifact First Rule

QA Architect is a staged pipeline. **Every stage consumes the output artifact of
the previous stage**, and stages write their own artifact under `outputs/`:

```
application.json        (Discovery)
  -> feature-inventory.json   (Feature Discovery)
  -> domain-model.json        (Domain Discovery)
  -> traceability.json        (Traceability Engine)
  -> business-rules.json      (Business Rules — not implemented yet)
  -> test-strategy.json       (Test Strategy — not implemented yet)
  -> test-scenarios.json      (Test Scenarios — not implemented yet)
```

Rules:

- **Repository scanning/cloning is allowed ONLY in the Discovery stage.** Every
  later stage must read the upstream artifact, never the repository.
- Do **not** re-read or re-clone a repository when an artifact already exists.

The chain, artifact filenames, generic JSON save/load, and rule enforcement live
in `app/pipeline.py` (the single source of truth). Downstream stages call
`pipeline.require_previous_artifact("<stage>")` to fail fast (HTTP 404) when the
upstream artifact is missing — see `app/features/service.py` for the reference
implementation.

## API

The FastAPI application is assembled in `app/api.py` via `create_app()` and is
served through `main.py` (`uvicorn main:app`).

Current endpoints (all placeholders):

- `GET /` and `GET /health` — service health.
- `GET /pipeline-status` — validation snapshot of the Artifact First pipeline:
  per-stage artifact existence + `implemented` flag, completed stages, and the
  next implemented stage that can run. Backed by `pipeline.pipeline_status()`.
- `POST /discover` — clone a GitHub repo and return a deterministic discovery
  result (`technology`, `modules`, `routes`, `controllers`, `apis`, `services`,
  `collections`, `roles`, `config_files`, `angular`). Implemented in
  `app/discovery/` (`cloner.py` + `analyzer.py`). The result is persisted to
  `outputs/application.json` via `app/discovery/artifacts.py`. For standalone
  Angular apps (no `*.module.ts`), feature folders are inferred from folder
  structure and the routing graph (`loadChildren`/`loadComponent`) and surfaced
  both in `modules` and the structured `angular` insights
  (`feature_folders`, `route_groups`, `lazy_feature_areas`, `component_hierarchy`).
- `GET /application` — return the saved `outputs/application.json` artifact so
  later stages consume it instead of re-reading the repository.
- `POST /features` — feature discovery stage. Consumes `application.json` only
  (no repo reads/clones, no LLM) and deterministically groups modules/routes/
  apis/collections into business features, written to
  `outputs/feature-inventory.json`. Implemented in `app/features/`
  (`grouping.py` + `service.py` + `artifacts.py`).
- `GET /features` — return the saved `outputs/feature-inventory.json` artifact.
- `POST /domains` — domain discovery stage. Consumes `feature-inventory.json`
  only (no repo reads/clones, no LLM) and deterministically groups features into
  business domains via a keyword taxonomy, written to `outputs/domain-model.json`.
  Implemented in `app/domains/` (`grouping.py` + `service.py` + `artifacts.py`).
- `GET /domains` — return the saved `outputs/domain-model.json` artifact.
- `POST /traceability` — traceability stage. Consumes `application.json` +
  `feature-inventory.json` + `domain-model.json` only (no repo reads/clones, no
  LLM) and joins them into a `Domain -> Feature -> {routes, components, services,
  apis, collections}` graph, written to `outputs/traceability.json`. Implemented
  in `app/traceability/` (`engine.py` + `service.py` + `artifacts.py`).
- `GET /traceability` — return the saved `outputs/traceability.json` artifact.
- `GET /discovery/repositories` — list known repositories.
- `GET /knowledge/entries` — list knowledge entries.
- `GET /qa/test-plan?repository=<full_name>` — build a placeholder test plan.
- `GET /github/status` — report GitHub integration status.

## Other directories

- `prompts/` — prompt templates (for future AI features).
- `outputs/` — generated artifacts (git-ignored).
- `tests/` — automated tests.
