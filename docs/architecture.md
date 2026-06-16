# QA Architect — Architecture (Scaffold)

This document is a placeholder describing the intended structure of QA Architect.
AI features are intentionally **not** implemented yet.

## Modules

| Module | Package | Responsibility |
| --- | --- | --- |
| Discovery | `app/discovery` | Locate and scan repositories. |
| Features | `app/features` | Group discovery artifacts into business features. |
| Knowledge | `app/knowledge` | Store and retrieve project knowledge. |
| QA | `app/qa` | Build test plans and test cases. |
| GitHub | `app/github` | GitHub integration / API access. |
| Models | `app/models` | Shared Pydantic data models. |

## API

The FastAPI application is assembled in `app/api.py` via `create_app()` and is
served through `main.py` (`uvicorn main:app`).

Current endpoints (all placeholders):

- `GET /` and `GET /health` — service health.
- `POST /discover` — clone a GitHub repo and return a deterministic discovery
  result (`technology`, `modules`, `routes`, `controllers`, `apis`, `services`,
  `collections`, `roles`, `config_files`). Implemented in `app/discovery/`
  (`cloner.py` + `analyzer.py`). The result is persisted to
  `outputs/application.json` via `app/discovery/artifacts.py`.
- `GET /application` — return the saved `outputs/application.json` artifact so
  later stages consume it instead of re-reading the repository.
- `POST /features` — feature discovery stage. Consumes `application.json` only
  (no repo reads/clones, no LLM) and deterministically groups modules/routes/
  apis/collections into business features, written to
  `outputs/feature-inventory.json`. Implemented in `app/features/`
  (`grouping.py` + `service.py` + `artifacts.py`).
- `GET /features` — return the saved `outputs/feature-inventory.json` artifact.
- `GET /discovery/repositories` — list known repositories.
- `GET /knowledge/entries` — list knowledge entries.
- `GET /qa/test-plan?repository=<full_name>` — build a placeholder test plan.
- `GET /github/status` — report GitHub integration status.

## Other directories

- `prompts/` — prompt templates (for future AI features).
- `outputs/` — generated artifacts (git-ignored).
- `tests/` — automated tests.
