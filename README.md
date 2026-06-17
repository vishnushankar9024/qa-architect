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
| GET | `/pipeline-status` | Validate pipeline state: which stage artifacts exist and what can run next. |
| GET | `/discovery/repositories` | List known repositories. |
| POST | `/discover` | Clone a GitHub repo and return a deterministic discovery result (also writes `outputs/application.json`). |
| GET | `/application` | Return the saved `outputs/application.json` discovery artifact. |
| POST | `/features` | Group `application.json` into business features (writes `outputs/feature-inventory.json`). |
| GET | `/features` | Return the saved `outputs/feature-inventory.json` feature inventory. |
| POST | `/domains` | Group `feature-inventory.json` into business domains (writes `outputs/domain-model.json`). |
| GET | `/domains` | Return the saved `outputs/domain-model.json` domain model. |
| POST | `/traceability` | Join discovery/feature/domain artifacts into a domain→feature→relationships graph (writes `outputs/traceability.json`). |
| GET | `/traceability` | Return the saved `outputs/traceability.json` graph. |
| POST | `/business-rules` | Infer deterministic business rule candidates from existing artifacts (writes `outputs/business-rules.json`). |
| GET | `/business-rules` | Return the saved `outputs/business-rules.json` artifact. |
| POST | `/rule-catalog/build` | Merge generated rules with human overrides (writes catalog JSON and Markdown artifacts). |
| GET | `/rule-catalog` | Return the saved `outputs/business-rule-catalog.json` artifact. |
| GET | `/rule-catalog/markdown` | Return the saved `outputs/business-rule-catalog.md` artifact. |
| POST | `/business-rules/enrich` | Transform the catalog into QA-focused enriched business rules and quality metrics. |
| GET | `/business-rules/enriched` | Return the saved `outputs/enriched-business-rules.json` artifact. |
| GET | `/business-rules/enriched/markdown` | Return the saved `outputs/enriched-business-rules.md` artifact. |
| GET | `/business-rules/quality-report` | Return the saved `outputs/quality-report.json` artifact. |
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
- **angular** — standalone Angular insights (or `null`): `feature_folders`, `route_groups`, `lazy_feature_areas`, and `component_hierarchy` (feature → components). Standalone apps have no `*.module.ts`, so feature folders are inferred from structure/routing and also surfaced in `modules`.

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

## Feature Discovery (`POST /features`)

The second stage. It **consumes `outputs/application.json` only** — it never
reads or clones the repository and makes no LLM calls. It deterministically
groups `modules`, `routes`, `apis`, and `collections` into business features by
reducing each artifact to a canonical feature key (first meaningful path/name
segment, singularized, with auth/role synonyms collapsed).

```bash
curl -X POST http://localhost:8000/features    # builds outputs/feature-inventory.json
curl http://localhost:8000/features            # returns the saved inventory
```

Output shape (`outputs/feature-inventory.json`):

```json
{
  "features": [
    {
      "name": "User Management",
      "modules": [],
      "routes": [],
      "apis": [],
      "collections": []
    }
  ]
}
```

Artifacts that carry no business token (e.g. `/`, `:id`) are collected under a
`General` feature, listed last. Run `POST /discover` first so `application.json`
exists.

## Domain Discovery (`POST /domains`)

The third stage. It **consumes `outputs/feature-inventory.json` only** (no repo
reads/clones, no LLM) and deterministically groups features into business
domains using a fixed keyword taxonomy. Each feature name is tokenized and
matched to the best-scoring domain; unmatched features fall under `General`.

```bash
curl -X POST http://localhost:8000/domains   # builds outputs/domain-model.json
curl http://localhost:8000/domains           # returns the saved domain model
```

Output shape (`outputs/domain-model.json`):

```json
{
  "domains": [
    {
      "name": "Identity and Access Management",
      "features": ["Authentication", "Roles & Permissions", "User Management"]
    }
  ]
}
```

Run `POST /features` first so `feature-inventory.json` exists (enforced by the
Artifact First Rule).

## Traceability Engine (`POST /traceability`)

The fourth stage. It **consumes `application.json` + `feature-inventory.json` +
`domain-model.json` only** (no repo reads/clones, no LLM) and builds a nested
graph:

```
Domain -> Feature -> { routes, components, services, apis, collections }
```

Routes/apis/collections come from the feature inventory; components come from the
Angular component hierarchy in `application.json`; services come from
`application.json`. Cross-artifact joins use a normalized feature key (lowercased,
"management" dropped, non-alphanumerics removed) with prefix matching so naming
differences across stages (e.g. `auth` ↔ `Authentication`) still line up. The
join is intentionally inclusive.

```bash
curl -X POST http://localhost:8000/traceability   # builds outputs/traceability.json
curl http://localhost:8000/traceability           # returns the saved graph
```

Output shape (`outputs/traceability.json`):

```json
{
  "domains": [
    {
      "name": "Opportunity Management",
      "features": [
        {
          "name": "Opportunityhub Management",
          "routes": ["opportunity", "opportunity-hub/:id/details"],
          "components": [],
          "services": [],
          "apis": [],
          "collections": []
        }
      ]
    }
  ]
}
```

Run `POST /domains` (and its upstream stages) first; enforced by the Artifact
First Rule.

## Business Rule Discovery (`POST /business-rules`)

The fifth stage. It **consumes `application.json` + `feature-inventory.json` +
`domain-model.json` + `traceability.json` only** (no repo reads/clones, no LLM)
and deterministically infers business rule candidates from routes, APIs,
collections, naming conventions, and workflow patterns.

```bash
curl -X POST http://localhost:8000/business-rules   # builds outputs/business-rules.json
curl http://localhost:8000/business-rules           # returns the saved artifact
```

Output shape (`outputs/business-rules.json`):

```json
{
  "domains": [
    {
      "domain": "RACI Management",
      "rules": [
        {
          "id": "BR-001",
          "rule": "Only accountable users should approve items in RACI Approval.",
          "confidence": 0.88
        }
      ]
    }
  ]
}
```

Run `POST /traceability` (and its upstream stages) first; enforced by the
Artifact First Rule.

## Business Rule Catalog (`POST /rule-catalog/build`)

The governed catalog layer. It **consumes `outputs/business-rules.json` only**
plus optional human overrides from `outputs/business-rule-overrides.json`. It
never reads or clones repositories and makes no LLM calls.

```bash
curl -X POST http://localhost:8000/rule-catalog/build
curl http://localhost:8000/rule-catalog
curl http://localhost:8000/rule-catalog/markdown
```

Artifacts:

- `outputs/business-rule-overrides.json` — human-authored rules and overrides.
- `outputs/business-rule-catalog.json` — merged generated + human catalog.
- `outputs/business-rule-catalog.md` — human-readable catalog.

Rule shape:

```json
{
  "id": "BR-PMW-001",
  "domain": "Workflow, Approval and RACI",
  "feature": "Checklist",
  "title": "Checklist completion required",
  "description": "All mandatory checklist items must be completed before review.",
  "rule_type": "Workflow",
  "priority": "High",
  "source": "Human",
  "author": "Vishnu Shankar",
  "status": "Approved",
  "evidence": [],
  "tags": ["workflow", "checklist"]
}
```

Supported statuses are `Generated`, `Draft`, `Reviewed`, `Approved`, and
`Deprecated`. Human overrides use the same `id` to take precedence over a
generated rule, while retaining generated traceability in the catalog.

## Business Rule Enrichment (`POST /business-rules/enrich`)

The QA-focused enrichment layer. It **consumes existing artifacts only**:
`application.json`, `feature-inventory.json`, `domain-model.json`,
`traceability.json`, and `business-rule-catalog.json`. It does not scan or clone
repositories and makes no LLM calls.

Outputs:

- `outputs/enriched-business-rules.json`
- `outputs/enriched-business-rules.md`
- `outputs/quality-report.json`

Each enriched rule keeps traceability to source catalog/generated rule IDs:

```json
{
  "id": "EBR-0001",
  "source_rule_ids": ["BR-001"],
  "classification": "Workflow",
  "testing_value_score": 10,
  "business_criticality": "Critical",
  "confidence": 0.9,
  "rule": "Only Accountable users may approve workflow items."
}
```

The quality report includes total rules, CRUD counts, Workflow/Authorization/
Validation/RACI counts, consolidated rule count, average testing value score,
CRUD reduction percentage, and the top 100 highest-value QA rules.

## Testing

```bash
pytest
```
