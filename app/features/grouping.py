"""Deterministic grouping of discovery artifacts into business features.

The input is a :class:`~app.models.discovery.DiscoveryResult` (loaded from
``application.json``). Each module/route/api/collection is reduced to a
canonical *feature key* derived from its most meaningful name segment, and
artifacts that share a key are grouped into a single feature.

No LLMs, no repository access — this is pure string/rule processing.
"""

from __future__ import annotations

import re

from app.models.discovery import DiscoveryResult
from app.models.feature import Feature, FeatureInventory

# Path/name segments that carry no business meaning on their own.
_GENERIC_SEGMENTS = {
    "api",
    "apis",
    "v1",
    "v2",
    "v3",
    "rest",
    "graphql",
    "public",
    "static",
    "assets",
    "health",
    "healthz",
    "ping",
    "status",
    "www",
}

# Tokens that are too generic to identify a feature on their own.
_STOPWORD_TOKENS = {
    "app",
    "index",
    "home",
    "main",
    "core",
    "common",
    "shared",
    "base",
    "default",
}

# Map synonymous tokens onto a single canonical feature key.
_SYNONYMS = {
    "login": "auth",
    "logout": "auth",
    "register": "auth",
    "signup": "auth",
    "signin": "auth",
    "authentication": "auth",
    "authorize": "auth",
    "session": "auth",
    "oauth": "auth",
    "jwt": "auth",
    "credential": "auth",
    "permission": "role",
    "rbac": "role",
}

# Explicit display names for canonical keys (default is "<Title> Management").
_FEATURE_NAMES = {
    "auth": "Authentication",
    "role": "Roles & Permissions",
}

_GENERAL_KEY = "__general__"
_GENERAL_NAME = "General"


def _singularize(word: str) -> str:
    w = word.lower()
    if len(w) <= 3:
        return w
    if w.endswith("ies"):
        return w[:-3] + "y"
    for suffix in ("ches", "shes", "sses", "xes", "zes"):
        if w.endswith(suffix):
            return w[:-2]
    if w.endswith("ss"):
        return w
    if w.endswith("s"):
        return w[:-1]
    return w


def _canonical(token: str | None) -> str | None:
    """Reduce a raw token to a canonical feature key, or ``None`` if generic."""

    if not token:
        return None
    cleaned = re.sub(r"[^a-z0-9]", "", token.lower())
    if not cleaned:
        return None
    singular = _singularize(cleaned)
    if not singular or singular in _STOPWORD_TOKENS:
        return None
    return _SYNONYMS.get(singular, singular)


def _path_token(path: str) -> str | None:
    """Return the first business-meaningful segment of a URL path."""

    for raw in path.split("/"):
        seg = raw.strip()
        if not seg:
            continue
        # Skip path parameters: ":id", "{id}", "<id>", "*splat".
        if seg[0] in ":{<*" or seg.endswith("}"):
            continue
        seg = re.sub(r"[{}<>:*]", "", seg)
        seg = seg.split(".")[0]  # drop file extension, e.g. client.js -> client
        if not seg or seg.lower() in _GENERIC_SEGMENTS:
            continue
        return seg
    return None


def _api_path(api: str) -> str:
    """Extract the path part of an ``"METHOD /path"`` API entry."""

    parts = api.split(None, 1)
    return parts[1] if len(parts) == 2 else api


def _feature_name(key: str) -> str:
    if key in _FEATURE_NAMES:
        return _FEATURE_NAMES[key]
    pretty = re.sub(r"[-_]+", " ", key).strip()
    return f"{pretty.title()} Management"


def build_feature_inventory(result: DiscoveryResult) -> FeatureInventory:
    """Group ``result`` artifacts into a deterministic feature inventory."""

    buckets: dict[str, dict[str, set[str]]] = {}

    def add(key: str | None, kind: str, value: str) -> None:
        feature = buckets.setdefault(
            key or _GENERAL_KEY,
            {"modules": set(), "routes": set(), "apis": set(), "collections": set()},
        )
        feature[kind].add(value)

    for module in result.modules:
        add(_canonical(module), "modules", module)
    for route in result.routes:
        add(_canonical(_path_token(route)), "routes", route)
    for api in result.apis:
        add(_canonical(_path_token(_api_path(api))), "apis", api)
    for collection in result.collections:
        add(_canonical(collection), "collections", collection)

    features: list[Feature] = []
    for key, contents in buckets.items():
        name = _GENERAL_NAME if key == _GENERAL_KEY else _feature_name(key)
        features.append(
            Feature(
                name=name,
                modules=sorted(contents["modules"]),
                routes=sorted(contents["routes"]),
                apis=sorted(contents["apis"]),
                collections=sorted(contents["collections"]),
            )
        )

    # Deterministic ordering: named features alphabetically, "General" last.
    features.sort(key=lambda f: (f.name == _GENERAL_NAME, f.name.lower()))
    return FeatureInventory(features=features)
