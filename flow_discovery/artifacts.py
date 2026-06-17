"""Artifact loading and normalization.

The engine is *artifact-first*: it only reads the JSON artifacts produced by
earlier QA Architect stages and never touches a repository. This module loads
those artifacts and flattens them into a uniform list of :class:`Signal`
objects.

Input artifact schemas can vary, so loading is intentionally tolerant: each
loader looks for a handful of likely key names and degrades gracefully when a
field is missing.
"""

from __future__ import annotations

import json
import os
from typing import Any, Dict, Iterable, List, Optional

from .models import Signal
from .patterns import detect_verbs

# Canonical artifact file names consumed by the engine.
ARTIFACT_FILES = {
    "application": "application.json",
    "features": "feature-inventory.json",
    "domain": "domain-model.json",
    "traceability": "traceability.json",
    "rules": "business-rule-catalog.json",
}


def _read_json(path: str) -> Any:
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _as_list(value: Any) -> List[Any]:
    """Coerce ``value`` into a list (objects/dicts become a single-item list)."""

    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, dict):
        return [value]
    return [value]


def _first(mapping: Dict[str, Any], *keys: str, default: Any = "") -> Any:
    for key in keys:
        if key in mapping and mapping[key] not in (None, ""):
            return mapping[key]
    return default


def _collection(data: Any, *keys: str) -> List[Any]:
    """Return the first present list-valued key from ``data``.

    ``data`` may itself be a list (already the collection) or a dict that wraps
    the collection under one of ``keys``.
    """

    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in keys:
            if key in data:
                return _as_list(data[key])
    return []


def _text_of(mapping: Dict[str, Any], *extra: str) -> str:
    """Build a searchable text blob from common descriptive fields."""

    parts: List[str] = []
    for key in ("name", "title", "operation", "operationId", "summary",
                "description", "desc", "path", "route", "url", "method", "action"):
        val = mapping.get(key)
        if isinstance(val, str):
            parts.append(val)
    parts.extend(e for e in extra if e)
    return " ".join(parts).strip()


class ArtifactBundle:
    """In-memory representation of the loaded artifacts plus derived signals."""

    def __init__(self) -> None:
        self.application: Dict[str, Any] = {}
        self.signals: List[Signal] = []
        self.entities: List[Dict[str, str]] = []  # {name, domain, criticality}
        self.domains: List[str] = []
        self.loaded_files: List[str] = []
        self.traceability: List[Dict[str, Any]] = []

    # -- entity helpers ----------------------------------------------------
    def entity_names(self) -> List[str]:
        return [e["name"] for e in self.entities]


def load_bundle(artifact_dir: str) -> ArtifactBundle:
    """Load every available artifact in ``artifact_dir`` into an ArtifactBundle."""

    bundle = ArtifactBundle()

    paths = {key: os.path.join(artifact_dir, name)
             for key, name in ARTIFACT_FILES.items()}

    # application.json -----------------------------------------------------
    if os.path.exists(paths["application"]):
        bundle.application = _read_json(paths["application"]) or {}
        bundle.loaded_files.append(ARTIFACT_FILES["application"])

    # domain-model.json ----------------------------------------------------
    if os.path.exists(paths["domain"]):
        domain_data = _read_json(paths["domain"])
        bundle.loaded_files.append(ARTIFACT_FILES["domain"])
        _ingest_domain_model(domain_data, bundle)

    # feature-inventory.json ----------------------------------------------
    if os.path.exists(paths["features"]):
        feat_data = _read_json(paths["features"])
        bundle.loaded_files.append(ARTIFACT_FILES["features"])
        _ingest_feature_inventory(feat_data, bundle)

    # business-rule-catalog.json ------------------------------------------
    if os.path.exists(paths["rules"]):
        rule_data = _read_json(paths["rules"])
        bundle.loaded_files.append(ARTIFACT_FILES["rules"])
        _ingest_rules(rule_data, bundle)

    # traceability.json ----------------------------------------------------
    if os.path.exists(paths["traceability"]):
        trace_data = _read_json(paths["traceability"])
        bundle.loaded_files.append(ARTIFACT_FILES["traceability"])
        _ingest_traceability(trace_data, bundle)

    return bundle


def _ingest_domain_model(data: Any, bundle: ArtifactBundle) -> None:
    domains = _collection(data, "domains", "domain", "items")
    seen_domains: List[str] = []
    for dom in domains:
        if not isinstance(dom, dict):
            continue
        domain_name = str(_first(dom, "domain", "name", "title"))
        if domain_name and domain_name not in seen_domains:
            seen_domains.append(domain_name)
        for ent in _collection(dom, "entities", "models", "objects"):
            if isinstance(ent, dict):
                name = str(_first(ent, "name", "entity", "title"))
                crit = str(_first(ent, "criticality", "importance", default="")).title()
            else:
                name, crit = str(ent), ""
            if not name:
                continue
            bundle.entities.append({
                "name": name,
                "domain": domain_name,
                "criticality": crit,
            })
    # Some schemas list entities at the top level.
    for ent in _collection(data, "entities"):
        if isinstance(ent, dict):
            name = str(_first(ent, "name", "entity", "title"))
            if not name:
                continue
            bundle.entities.append({
                "name": name,
                "domain": str(_first(ent, "domain", default="")),
                "criticality": str(_first(ent, "criticality", default="")).title(),
            })
    bundle.domains = seen_domains


def _ingest_feature_inventory(data: Any, bundle: ArtifactBundle) -> None:
    for feat in _collection(data, "features", "items", "inventory"):
        if not isinstance(feat, dict):
            continue
        _add_signal(bundle, "feature-inventory.json", "feature", feat,
                    id_keys=("id", "feature_id", "featureId", "key"))

    for api in _collection(data, "apis", "endpoints", "operations"):
        if not isinstance(api, dict):
            continue
        method = str(_first(api, "method", "verb", default="")).upper()
        path = str(_first(api, "path", "route", "url", "endpoint"))
        _add_signal(bundle, "feature-inventory.json", "api", api,
                    id_keys=("id", "api_id", "operationId", "operation"),
                    extra_text=f"{method} {path}")

    for route in _collection(data, "routes", "pages", "screens"):
        if not isinstance(route, dict):
            continue
        _add_signal(bundle, "feature-inventory.json", "route", route,
                    id_keys=("id", "route_id", "path", "name"))

    for coll in _collection(data, "collections", "postman", "requests"):
        if isinstance(coll, dict):
            coll_name = str(_first(coll, "name", "title"))
            requests = _collection(coll, "requests", "items", "endpoints")
            if requests:
                for req in requests:
                    if isinstance(req, dict):
                        _add_signal(bundle, "feature-inventory.json", "collection", req,
                                    id_keys=("id", "name"),
                                    extra_text=coll_name)
            else:
                _add_signal(bundle, "feature-inventory.json", "collection", coll,
                            id_keys=("id", "name"))


def _ingest_rules(data: Any, bundle: ArtifactBundle) -> None:
    for rule in _collection(data, "rules", "business_rules", "businessRules", "catalog", "items"):
        if not isinstance(rule, dict):
            continue
        _add_signal(bundle, "business-rule-catalog.json", "rule", rule,
                    id_keys=("id", "rule_id", "ruleId", "key"))


def _ingest_traceability(data: Any, bundle: ArtifactBundle) -> None:
    links = _collection(data, "links", "traceability", "relationships", "mappings", "items")
    for link in links:
        if isinstance(link, dict):
            bundle.traceability.append(link)


def _add_signal(bundle: ArtifactBundle, artifact: str, kind: str,
                mapping: Dict[str, Any], id_keys: Iterable[str],
                extra_text: str = "") -> None:
    ref_id = str(_first(mapping, *id_keys, default=""))
    name = str(_first(mapping, "name", "title", "operation", "summary", "path", default=ref_id))
    text = _text_of(mapping, extra_text)
    domain = str(_first(mapping, "domain", "module", "area", default=""))
    entity = str(_first(mapping, "entity", "object", "model", "resource", default=""))
    signal = Signal(
        artifact=artifact,
        kind=kind,
        ref_id=ref_id or name,
        name=name or ref_id,
        text=text,
        domain=domain,
        entity=entity,
        verbs=detect_verbs(text),
        name_verbs=detect_verbs(name),
    )
    bundle.signals.append(signal)
