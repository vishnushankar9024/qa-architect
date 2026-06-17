"""Command line interface for the Flow Discovery Engine.

Usage::

    python -m flow_discovery --artifacts ./artifacts --out ./output

Reads the five input artifacts from ``--artifacts`` and writes
``business-flows.json`` and ``business-flows.md`` to ``--out``.
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import List, Optional

from .engine import FlowDiscoveryEngine
from .render import to_json, to_markdown


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="flow_discovery",
        description="Discover end-to-end business flows from QA Architect artifacts "
                    "(deterministic, artifact-first).",
    )
    parser.add_argument(
        "--artifacts", "-a", default="artifacts",
        help="Directory containing the input artifacts (default: ./artifacts)",
    )
    parser.add_argument(
        "--out", "-o", default="output",
        help="Directory to write business-flows.json/.md (default: ./output)",
    )
    parser.add_argument(
        "--quiet", "-q", action="store_true",
        help="Suppress the validation summary printed to stdout.",
    )
    return parser


def _print_summary(summary: dict) -> None:
    print("Flow Discovery - Validation Summary")
    print("=" * 38)
    print(f"Total flows discovered : {summary['total_flows']}")
    print(f"Average steps per flow : {summary['average_steps_per_flow']}")
    print("Flows per domain:")
    for domain, count in summary["flows_per_domain"].items():
        print(f"  - {domain}: {count}")
    print("Highest complexity flows:")
    for name in summary["highest_complexity_flows"] or ["(none)"]:
        print(f"  - {name}")
    print("Highest criticality flows:")
    for name in summary["highest_criticality_flows"] or ["(none)"]:
        print(f"  - {name}")


def main(argv: Optional[List[str]] = None) -> int:
    args = _build_parser().parse_args(argv)

    if not os.path.isdir(args.artifacts):
        print(f"error: artifacts directory not found: {args.artifacts}", file=sys.stderr)
        return 2

    engine = FlowDiscoveryEngine.from_directory(args.artifacts)
    if not engine.bundle.loaded_files:
        print(f"error: no input artifacts found in {args.artifacts}", file=sys.stderr)
        return 2

    result = engine.discover()

    os.makedirs(args.out, exist_ok=True)
    json_path = os.path.join(args.out, "business-flows.json")
    md_path = os.path.join(args.out, "business-flows.md")
    with open(json_path, "w", encoding="utf-8") as handle:
        handle.write(to_json(result))
    with open(md_path, "w", encoding="utf-8") as handle:
        handle.write(to_markdown(result))

    if not args.quiet:
        _print_summary(result.summary)
        print()
        print(f"Wrote {json_path}")
        print(f"Wrote {md_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
