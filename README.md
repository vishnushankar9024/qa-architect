# QA Architect

QA Architect is a Python service (FastAPI + Pydantic) that helps generate and
manage QA artifacts from source repositories. This repository currently contains
a **scaffold only** — the module structure and placeholder endpoints are in
place, but AI features are intentionally not implemented yet.

## Tech stack

- Python 3.12
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://docs.pydantic.dev/) (+ `pydantic-settings`)
- GitHub integration (via PyGithub / httpx)

## Project structure

```
qa-architect/
├── app/
│   ├── discovery/   # Repository discovery module
│   ├── knowledge/   # Knowledge module
│   ├── qa/          # QA Architect module
│   ├── github/      # GitHub integration
│   └── models/      # Shared Pydantic models
├── tests/           # Automated tests
├── docs/            # Documentation
├── prompts/         # Prompt templates (future AI features)
├── outputs/         # Generated artifacts (git-ignored)
├── requirements.txt
├── main.py          # Entrypoint (uvicorn main:app)
└── README.md
```

## Getting started

```bash
# 1. Create and activate a virtual environment (Python 3.12)
python3.12 -m venv .venv
source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the development server
uvicorn main:app --reload
# or: python main.py
```

The API is then available at http://localhost:8000 and interactive docs at
http://localhost:8000/docs.

## Configuration

Settings are read from environment variables (prefix `QA_ARCHITECT_`) and an
optional `.env` file. See `.env.example` for available options. All settings are
optional for the scaffold.

## Endpoints (placeholders)

| Method | Path | Description |
| --- | --- | --- |
| GET | `/` | Service health. |
| GET | `/health` | Liveness/readiness probe. |
| GET | `/discovery/repositories` | List known repositories. |
| GET | `/knowledge/entries` | List knowledge entries. |
| GET | `/qa/test-plan?repository=<full_name>` | Build a placeholder test plan. |
| GET | `/github/status` | Report GitHub integration status. |

## Testing

```bash
pytest
```
