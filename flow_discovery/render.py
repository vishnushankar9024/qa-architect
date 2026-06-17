"""Serialization of discovery results to JSON and Markdown."""

from __future__ import annotations

import json
from typing import Dict, List

from .models import BusinessFlow, DiscoveryResult


def to_json(result: DiscoveryResult) -> str:
    return json.dumps(result.to_dict(), indent=2, ensure_ascii=False) + "\n"


def to_markdown(result: DiscoveryResult) -> str:
    lines: List[str] = []
    lines.append("# Business Flows")
    lines.append("")
    lines.append(
        "Discovered deterministically from existing QA Architect artifacts "
        "(artifact-first, no repository scanning, no LLM)."
    )
    lines.append("")

    _render_validation(result, lines)

    # Group flows by domain, preserving the deterministic sort already applied.
    by_domain: Dict[str, List[BusinessFlow]] = {}
    for flow in result.flows:
        by_domain.setdefault(flow.domain, []).append(flow)

    for domain in sorted(by_domain):
        lines.append(f"# {domain}")
        lines.append("")
        for flow in by_domain[domain]:
            _render_flow(flow, lines)

    return "\n".join(lines).rstrip() + "\n"


def _render_validation(result: DiscoveryResult, lines: List[str]) -> None:
    s = result.summary
    lines.append("## Validation Summary")
    lines.append("")
    lines.append(f"- **Total flows discovered:** {s['total_flows']}")
    lines.append(f"- **Average steps per flow:** {s['average_steps_per_flow']}")
    lines.append("")
    lines.append("**Flows per domain**")
    lines.append("")
    for domain, count in s["flows_per_domain"].items():
        lines.append(f"- {domain}: {count}")
    lines.append("")
    lines.append("**Flows per category**")
    lines.append("")
    for category, count in s["flows_per_category"].items():
        lines.append(f"- {category}: {count}")
    lines.append("")
    lines.append("**Highest complexity flows**")
    lines.append("")
    if s["highest_complexity_flows"]:
        for name in s["highest_complexity_flows"]:
            lines.append(f"- {name}")
    else:
        lines.append("- _none_")
    lines.append("")
    lines.append("**Highest criticality flows**")
    lines.append("")
    if s["highest_criticality_flows"]:
        for name in s["highest_criticality_flows"]:
            lines.append(f"- {name}")
    else:
        lines.append("- _none_")
    lines.append("")


def _render_flow(flow: BusinessFlow, lines: List[str]) -> None:
    lines.append(f"## {flow.flow_name}")
    lines.append("")
    lines.append(f"_{flow.flow_id} · {flow.category} · confidence {flow.confidence}_")
    lines.append("")
    lines.append("**Purpose**")
    lines.append("")
    lines.append(flow.purpose)
    lines.append("")
    lines.append("**Steps**")
    lines.append("")
    for step in flow.steps:
        mark = "" if step.evidenced else " _(inferred)_"
        lines.append(f"{step.sequence}. {step.name}{mark}")
    lines.append("")
    qa = flow.qa_metadata
    lines.append(f"**Complexity:** {qa.complexity}")
    lines.append("")
    lines.append(f"**Criticality:** {qa.criticality}")
    lines.append("")
    lines.append("**Dependencies**")
    lines.append("")
    if flow.dependencies:
        for dep in flow.dependencies:
            lines.append(f"- {dep}")
    else:
        lines.append("- _none_")
    lines.append("")
    lines.append(
        "**QA metadata:** "
        f"steps={qa.step_count}, "
        f"integration_points={qa.integration_points}, "
        f"document_touchpoints={qa.document_touchpoints}, "
        f"approval_touchpoints={qa.approval_touchpoints}"
    )
    lines.append("")
