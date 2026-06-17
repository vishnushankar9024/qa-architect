# QA Architect — Flow Discovery Engine

A **deterministic, artifact-first** engine that discovers end-to-end **business
flows** (workflows) from artifacts produced by earlier QA Architect stages.

Business Rule Discovery tends to emit isolated, CRUD-style and authorization
rules. For QA, *business flows* — the journeys a record takes through the
system — provide far more value. This engine reconstructs those journeys so
they can later drive Scenario Generation, Test Strategy, Test Cases and
Automation Suites.

## Guarantees

- **Artifact-first:** consumes existing artifacts only. It never clones or
  re-scans repositories and never re-parses source code.
- **Deterministic:** identical inputs always yield byte-identical outputs. No
  randomness, no timestamps.
- **No LLM:** pure rule/pattern logic, standard library only.

## Inputs

Placed in an artifacts directory (defaults shown):

| File | Used for |
| --- | --- |
| `application.json` | app metadata, domains, external integrations |
| `feature-inventory.json` | features, APIs, routes, Postman collections |
| `domain-model.json` | entities + per-entity business criticality |
| `traceability.json` | feature ↔ api ↔ route ↔ rule relationships |
| `business-rule-catalog.json` | existing business rules (reinforce flows) |

All files are optional; the engine degrades gracefully and tolerates several
common key-name variations per artifact.

## Outputs

Written to the output directory:

- `business-flows.json` — machine-readable flows + validation summary.
- `business-flows.md` — human-readable report grouped by domain.

## Usage

```bash
python -m flow_discovery --artifacts ./artifacts --out ./output
# or, after `pip install -e .`
flow-discovery -a ./artifacts -o ./output
```

## How it works

1. **Load & normalize** — every feature, API, route, collection request and
   business rule is flattened into a uniform `Signal` carrying the PMWebX
   workflow verbs detected in its text (`flow_discovery/artifacts.py`,
   `flow_discovery/patterns.py`).
2. **Group by entity** — signals are attached to domain-model entities
   (declared entity wins; otherwise whole-word text matching).
3. **Activate journey archetypes** — for each entity, a journey
   [`Archetype`](flow_discovery/patterns.py) (Creation, Approval, Assignment,
   Execution, Completion, Synchronization, Publishing, Notification) activates
   when its **primary action verb** is present. Primary verbs come from signal
   *names* (not prose) and business rules never start a journey — this keeps
   incidental verbs from spawning noise.
4. **Build the flow** — ordered steps (entry → intermediate → exit / state
   transitions), category classification (one of 12), QA metadata
   (complexity, criticality, step / integration / document / approval
   touchpoints), confidence, sources and dependencies.
5. **Finalize** — deduplicate, sort deterministically, assign `FLOW-NNN` ids
   and compute the validation summary.

### PMWebX patterns

The engine recognises the workflow concepts `initiate, create, submit, upload,
map, assign, delegate, review, approve, reject, resend, activate, execute,
complete, sync, publish, notify, download, close` and uses them to assemble
likely business journeys.

### Flow schema

```json
{
  "flow_id": "FLOW-001",
  "domain": "Document Management",
  "flow_name": "Document Approval Flow",
  "category": "Document Flow",
  "confidence": 0.94,
  "purpose": "Route a Document through review and approval to a final decision.",
  "qa_metadata": {
    "complexity": "High",
    "criticality": "Critical",
    "step_count": 5,
    "integration_points": 0,
    "document_touchpoints": 3,
    "approval_touchpoints": 3
  },
  "steps": [{ "sequence": 1, "name": "Initiate" }],
  "dependencies": [],
  "sources": []
}
```

## Sample artifacts

A complete PMWebX-style sample artifact set lives in [`artifacts/`](artifacts/)
and the generated deliverables in [`output/`](output/). The sample produces the
flows called out in the success criteria (Project Creation, Template Creation,
Project Assignment, RACI Assignment, Workstation Execution, Checklist
Completion, Document Approval, Notification, Planner Synchronization) rather
than CRUD operations.

## Tests

```bash
pip install -e ".[dev]"
pytest
```
