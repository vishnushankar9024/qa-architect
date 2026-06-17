"""Tests for the deterministic Flow Discovery Engine."""

import json
import os
import subprocess
import sys

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARTIFACT_DIR = os.path.join(REPO_ROOT, "artifacts")

sys.path.insert(0, REPO_ROOT)

from flow_discovery.engine import FlowDiscoveryEngine, discover_flows  # noqa: E402
from flow_discovery.patterns import (  # noqa: E402
    ALL_CATEGORIES,
    detect_verbs,
    resolve_category,
)
from flow_discovery.render import to_json, to_markdown  # noqa: E402


# Flows the specification's success criteria expect to emerge from the artifacts.
EXPECTED_SUCCESS_FLOWS = {
    "Project Creation Flow",
    "Template Creation Flow",
    "Project Assignment Flow",
    "RACI Assignment Flow",
    "Workstation Execution Flow",
    "Checklist Completion Flow",
    "Document Approval Flow",
    "Notification Flow",
    "Planner Synchronization Flow",
}


@pytest.fixture(scope="module")
def result():
    return discover_flows(ARTIFACT_DIR)


def _by_name(result):
    return {f.flow_name: f for f in result.flows}


# ---------------------------------------------------------------------------
# Pattern / vocabulary unit tests
# ---------------------------------------------------------------------------

def test_detect_verbs_whole_word():
    assert detect_verbs("Approve the document") == ["approve"]
    # camelCase identifiers should not match (no word boundary).
    assert detect_verbs("approveDocument") == []


def test_detect_verbs_are_order_sorted():
    verbs = detect_verbs("Close, then initiate and review the request")
    assert verbs == ["initiate", "review", "close"]


def test_resolve_category_uses_keywords_then_fallback():
    assert resolve_category("Planner Integrations", "Activity Flow") == "Integration Flow"
    assert resolve_category("totally unrelated text", "Activity Flow") == "Activity Flow"


def test_all_categories_count():
    # Specification requirement #4 lists exactly 12 flow categories.
    assert len(ALL_CATEGORIES) == 12


# ---------------------------------------------------------------------------
# Discovery behaviour
# ---------------------------------------------------------------------------

def test_success_criteria_flows_present(result):
    names = set(_by_name(result))
    missing = EXPECTED_SUCCESS_FLOWS - names
    assert not missing, f"missing expected flows: {sorted(missing)}"


def test_no_crud_style_flow_names(result):
    import re
    crud_tokens = ("get", "list", "fetch", "read", "update", "delete", "crud")
    for flow in result.flows:
        lowered = flow.flow_name.lower()
        for tok in crud_tokens:
            assert not re.search(r"\b" + tok + r"\b", lowered), flow.flow_name


def test_every_flow_has_valid_category(result):
    for flow in result.flows:
        assert flow.category in ALL_CATEGORIES


def test_steps_are_sequential_and_named(result):
    for flow in result.flows:
        assert flow.steps, flow.flow_name
        for idx, step in enumerate(flow.steps, start=1):
            assert step.sequence == idx
            assert step.name


def test_confidence_within_bounds(result):
    for flow in result.flows:
        assert 0.0 < flow.confidence <= 0.99


def test_qa_metadata_fields(result):
    for flow in result.flows:
        qa = flow.qa_metadata
        assert qa.complexity in {"Low", "Medium", "High"}
        assert qa.criticality in {"Low", "Medium", "High", "Critical"}
        assert qa.step_count == len(flow.steps)
        assert qa.integration_points >= 0
        assert qa.document_touchpoints >= 0
        assert qa.approval_touchpoints >= 0


def test_flow_ids_are_unique_and_sequential(result):
    ids = [f.flow_id for f in result.flows]
    assert ids == [f"FLOW-{i:03d}" for i in range(1, len(ids) + 1)]


def test_sources_only_reference_input_artifacts(result):
    allowed = {
        "application.json", "feature-inventory.json", "domain-model.json",
        "traceability.json", "business-rule-catalog.json",
    }
    for flow in result.flows:
        for source in flow.sources:
            assert source["artifact"] in allowed


def test_planner_flow_is_integration(result):
    planner = _by_name(result)["Planner Synchronization Flow"]
    assert planner.category == "Integration Flow"
    assert planner.qa_metadata.integration_points > 0
    assert "Primavera P6" in planner.dependencies


def test_document_flow_is_approval_critical(result):
    doc = _by_name(result)["Document Approval Flow"]
    assert doc.qa_metadata.criticality == "Critical"
    assert doc.qa_metadata.approval_touchpoints > 0


# ---------------------------------------------------------------------------
# Validation summary
# ---------------------------------------------------------------------------

def test_summary_consistency(result):
    s = result.summary
    assert s["total_flows"] == len(result.flows)
    assert sum(s["flows_per_domain"].values()) == len(result.flows)
    assert sum(s["flows_per_category"].values()) == len(result.flows)
    assert s["average_steps_per_flow"] > 0


# ---------------------------------------------------------------------------
# Determinism
# ---------------------------------------------------------------------------

def test_discovery_is_deterministic():
    a = to_json(discover_flows(ARTIFACT_DIR))
    b = to_json(discover_flows(ARTIFACT_DIR))
    assert a == b


def test_markdown_is_deterministic():
    a = to_markdown(discover_flows(ARTIFACT_DIR))
    b = to_markdown(discover_flows(ARTIFACT_DIR))
    assert a == b


def test_markdown_contains_required_sections(result):
    md = to_markdown(result)
    assert "# Business Flows" in md
    assert "## Validation Summary" in md
    assert "**Purpose**" in md
    assert "**Complexity:**" in md
    assert "**Criticality:**" in md
    assert "**Dependencies**" in md


# ---------------------------------------------------------------------------
# CLI end-to-end
# ---------------------------------------------------------------------------

def test_cli_generates_outputs(tmp_path):
    out_dir = tmp_path / "out"
    proc = subprocess.run(
        [sys.executable, "-m", "flow_discovery", "-a", ARTIFACT_DIR,
         "-o", str(out_dir), "-q"],
        cwd=REPO_ROOT, capture_output=True, text=True,
    )
    assert proc.returncode == 0, proc.stderr
    json_path = out_dir / "business-flows.json"
    md_path = out_dir / "business-flows.md"
    assert json_path.exists() and md_path.exists()
    data = json.loads(json_path.read_text())
    assert data["flows"]
    assert data["summary"]["total_flows"] == len(data["flows"])
