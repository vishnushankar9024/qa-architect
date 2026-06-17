"""Feature discovery stage.

Groups deterministic discovery artifacts (``application.json``) into business
features (``feature-inventory.json``). No repositories are read or cloned and no
LLM calls are made — grouping is purely rule based.
"""

from app.features.grouping import build_feature_inventory
from app.features.router import router
from app.features.service import FeatureInputError, FeatureService

__all__ = [
    "build_feature_inventory",
    "router",
    "FeatureService",
    "FeatureInputError",
]
