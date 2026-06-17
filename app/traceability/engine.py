"""Deterministic traceability join.

Combines three upstream artifacts:

* ``application.json``     — provides component hierarchy (Angular) and services.
* ``feature-inventory.json`` — provides per-feature routes/apis/collections.
* ``domain-model.json``    — provides domain -> feature grouping.

into a Domain -> Feature -> (routes/components/services/apis/collections) graph.

Features are joined across artifacts on a normalized key (lowercased, the word
"management" dropped, non-alphanumerics removed) so that e.g. the inventory
feature "Opportunityhub Management", the Angular folder "opportunity-hub", and
the service "OpportunityHubService" all line up. No LLMs, no repo access.
"""

from __future__ import annotations

import re

from app.models.discovery import DiscoveryResult
from app.models.domain import DomainModel
from app.models.feature import Feature, FeatureInventory
from app.models.traceability import DomainTrace, FeatureTrace, TraceabilityModel


def _normalize(name: str) -> str:
    """Normalize a feature/folder/service name to a comparable key."""

    tokens = [t for t in re.split(r"[^a-z0-9]+", name.lower()) if t and t != "management"]
    return "".join(tokens)


def _service_key(service: str) -> str:
    """Normalize a service name, dropping a trailing 'Service' suffix."""

    base = service
    if base.endswith("Service"):
        base = base[: -len("Service")]
    return _normalize(base)


def _keys_match(a: str, b: str) -> bool:
    """Whether two normalized keys relate (equal or one is a prefix of the other).

    This bridges naming transformations across stages, e.g. the folder/service
    token "auth" and the canonical feature key "authentication".
    """

    if not a or not b:
        return False
    return a == b or a.startswith(b) or b.startswith(a)


def build_traceability(
    application: DiscoveryResult,
    inventory: FeatureInventory,
    domain_model: DomainModel,
) -> TraceabilityModel:
    """Build the deterministic traceability graph from the three artifacts."""

    # Feature inventory lookup by name (routes/apis/collections live here).
    features_by_name: dict[str, Feature] = {f.name: f for f in inventory.features}

    # Components: normalized Angular feature folder -> component names.
    components_by_key: dict[str, list[str]] = {}
    if application.angular:
        for folder, components in application.angular.component_hierarchy.items():
            components_by_key[_normalize(folder)] = list(components)

    # Services: precompute (service_name, normalized_key) pairs, sorted for
    # deterministic output.
    service_keys: list[tuple[str, str]] = sorted(
        ((svc, _service_key(svc)) for svc in application.services),
        key=lambda pair: pair[0].lower(),
    )

    domains: list[DomainTrace] = []
    for domain in domain_model.domains:
        feature_traces: list[FeatureTrace] = []
        for feature_name in domain.features:
            key = _normalize(feature_name)
            feature = features_by_name.get(feature_name)

            routes = list(feature.routes) if feature else []
            apis = list(feature.apis) if feature else []
            collections = list(feature.collections) if feature else []

            # Components from any Angular folder whose key relates to the feature.
            components: set[str] = set()
            for folder_key, folder_components in components_by_key.items():
                if _keys_match(folder_key, key):
                    components.update(folder_components)

            # Services whose normalized name relates to the feature key.
            services = [svc for svc, svc_key in service_keys if _keys_match(svc_key, key)]

            feature_traces.append(
                FeatureTrace(
                    name=feature_name,
                    routes=sorted(routes),
                    components=sorted(components),
                    services=sorted(services),
                    apis=sorted(apis),
                    collections=sorted(collections),
                )
            )
        domains.append(DomainTrace(name=domain.name, features=feature_traces))

    return TraceabilityModel(domains=domains)
