from __future__ import annotations

import csv
import io
import json
from typing import Any


def approved_knowledge_pack(knowledge_base: dict[str, Any]) -> dict[str, Any]:
    pack: dict[str, Any] = {}
    for key in ("features", "domains", "business_rules", "flows", "traceability"):
        approved_items = [
            item
            for item in knowledge_base.get(key, [])
            if item.get("status") == "Approved"
        ]
        pack[key] = approved_items
    return pack


def to_json(pack: dict[str, Any]) -> str:
    return json.dumps(pack, indent=2)


def to_markdown(pack: dict[str, Any]) -> str:
    lines = ["# Knowledge Pack", ""]
    for section, items in pack.items():
        lines.append(f"## {section.replace('_', ' ').title()}")
        if not items:
            lines.append("- No approved items")
        for item in items:
            if "name" in item:
                lines.append(f"- **{item['name']}**: {item.get('description', '')}")
            else:
                lines.append(f"- {item.get('source', '')} -> {item.get('target', '')}")
        lines.append("")
    return "\n".join(lines).strip() + "\n"


def to_csv(pack: dict[str, Any]) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["type", "id", "name_or_source", "description_or_target", "status"])
    for section, items in pack.items():
        for item in items:
            if "name" in item:
                writer.writerow(
                    [
                        section,
                        item.get("id"),
                        item.get("name"),
                        item.get("description"),
                        item.get("status"),
                    ]
                )
            else:
                writer.writerow(
                    [
                        section,
                        item.get("id"),
                        item.get("source"),
                        item.get("target"),
                        item.get("status"),
                    ]
                )
    return buffer.getvalue()
