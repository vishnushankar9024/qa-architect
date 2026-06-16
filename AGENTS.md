# AGENTS.md

## Cursor Cloud specific instructions

QA Architect is a Python 3.12 + FastAPI + Pydantic service. It is a **scaffold**:
modules (`discovery`, `knowledge`, `qa`, `github`, `models`) expose placeholder
endpoints only — AI features are intentionally not implemented.

### Services

There is a single service: the FastAPI API.

- Run (dev): `.venv/bin/uvicorn main:app --reload` (serves on port 8000; docs at `/docs`). `python main.py` works too.
- Test: `.venv/bin/pytest`
- The app boots without any configuration. Settings use the `QA_ARCHITECT_` env prefix (see `.env.example`); `QA_ARCHITECT_GITHUB_TOKEN` is optional.

### Non-obvious notes

- Use the project virtualenv at `.venv` (created during setup). The system has no `pip` outside it, and `python3.12 -m venv` requires the `python3.12-venv` apt package (already installed).
- The FastAPI app is built in `app/api.py` via `create_app()`; `main:app` is the ASGI target.
- `outputs/` is git-ignored except for `.gitkeep`.
