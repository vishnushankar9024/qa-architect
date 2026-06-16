# AGENTS.md

## Implementation preferences

Standing guidance for implementation/coding tasks in this repo:

- **Models**: do NOT use Opus unless explicitly requested; prefer GPT-5 (use the
  latest GPT-5 family) for implementation tasks and any subagents spawned for
  coding/analysis.
- **Deterministic parsing**: implement stages with deterministic parsing/rules;
  no LLM calls in the pipeline.
- **Avoid repository re-scans**: only the Discovery stage may scan/clone a repo.
- **Reuse artifacts**: downstream stages consume the previous stage's artifact
  (see the Artifact First Rule below); never re-read a repo when its artifact
  already exists.

## Cursor Cloud specific instructions

QA Architect is a Python 3.12 + FastAPI + Pydantic service. Discovery (`POST
/discover`), Feature Discovery (`POST /features`), Domain Discovery (`POST
/domains`), and the Traceability Engine (`POST /traceability`) are implemented
with deterministic parsing; `knowledge`/`qa`/`github` remain placeholders.
AI/LLM features are intentionally not implemented yet.

### Services

There is a single service: the FastAPI API.

- Run (dev): `.venv/bin/uvicorn main:app --reload` (serves on port 8000; docs at `/docs`). `python main.py` works too.
- Test: `.venv/bin/pytest`
- The app boots without any configuration. Settings use the `QA_ARCHITECT_` env prefix (see `.env.example`); `QA_ARCHITECT_GITHUB_TOKEN` is optional.

### Non-obvious notes

- Use the project virtualenv at `.venv` (created during setup). The system has no `pip` outside it, and `python3.12 -m venv` requires the `python3.12-venv` apt package (already installed).
- The FastAPI app is built in `app/api.py` via `create_app()`; `main:app` is the ASGI target.
- `outputs/` is git-ignored except for `.gitkeep`.
- **Artifact First Rule**: QA Architect is a staged artifact pipeline
  (`application.json` → `feature-inventory.json` → `domain-model.json` →
  `traceability.json` → `business-rules.json` → `test-strategy.json` →
  `test-scenarios.json`). Each stage must consume the
  previous stage's artifact; **only the Discovery stage may scan/clone a
  repository**. Never re-read/re-clone a repo when its artifact already exists.
  The chain, artifact names, and enforcement helpers live in `app/pipeline.py`
  (single source of truth); new stages should call
  `pipeline.require_previous_artifact("<stage>")`. See `docs/architecture.md`.
