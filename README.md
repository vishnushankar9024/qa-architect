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
| POST | `/discover` | Clone a GitHub repo and return a deterministic discovery result (also writes `outputs/application.json`). |
| GET | `/application` | Return the saved `outputs/application.json` discovery artifact. |
| GET | `/knowledge/entries` | List knowledge entries. |
| GET | `/qa/test-plan?repository=<full_name>` | Build a placeholder test plan. |
| GET | `/github/status` | Report GitHub integration status. |

## Repository Discovery (`POST /discover`)

The first capability. Given a GitHub repository URL, QA Architect shallow-clones
the repo and runs **deterministic** (no-AI) analysis to detect the technology
stack and structure.

Request:

```bash
curl -X POST http://localhost:8000/discover \
  -H 'Content-Type: application/json' \
  -d '{"repo_url": "https://github.com/mongodb-developer/mongodb-with-fastapi"}'
```

Response shape:

```json
{
  "application": "",
  "technology": [],
  "modules": [],
  "routes": [],
  "controllers": [],
  "apis": [],
  "services": [],
  "collections": [],
  "roles": [],
  "config_files": []
}
```

- **technology** — any of `Angular`, `React`, `NodeJS`, `Python`, `MongoDB`.
- **modules** — Angular/Nest `*.module.ts` and Python packages.
- **routes** — frontend routes (Angular Router / React Router).
- **controllers** — Nest/Express `*.controller.ts`, `*Controller` classes, AngularJS controllers.
- **apis** — backend endpoints (Express / FastAPI / Flask), as `METHOD path`.
- **services** — Angular/Nest `*.service.ts` and `*Service` classes.
- **collections** — MongoDB collections/models (Mongoose / mongoengine / PyMongo).
- **roles** — best-effort role identifiers.
- **config_files** — configuration files (`package.json`, `angular.json`, `tsconfig*`, `requirements*`, `.env*`, `Dockerfile`, etc.) as relative paths.

`controllers`, `services`, `roles`, and `config_files` are included in addition
to the keys shown in the spec example so all discovery targets (requirement #4)
are surfaced. Optional `branch` may be supplied in the request body. A configured
`QA_ARCHITECT_GITHUB_TOKEN` is used for private `github.com` repositories.

### Reusable artifact

Each successful `POST /discover` writes the result to **`outputs/application.json`**
(configurable via `QA_ARCHITECT_OUTPUT_DIR`). Later QA Architect stages should
consume this artifact instead of re-reading the repository:

```bash
curl http://localhost:8000/application   # returns the saved application.json
```

## Testing

```bash
pytest
```
