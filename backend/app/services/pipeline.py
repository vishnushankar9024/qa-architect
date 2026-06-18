from __future__ import annotations

from dataclasses import dataclass

from app.schemas import ReviewableItem, TraceabilityItem, generate_id


PIPELINE_STAGES = (
    "Discovery",
    "Features",
    "Domains",
    "Traceability",
    "Business Rules",
    "Flow Discovery",
)


@dataclass
class PipelineOutput:
    features: list[ReviewableItem]
    domains: list[ReviewableItem]
    flows: list[ReviewableItem]
    business_rules: list[ReviewableItem]
    traceability: list[TraceabilityItem]


def _item(name: str, description: str) -> ReviewableItem:
    return ReviewableItem(id=generate_id("item"), name=name, description=description)


def _trace(source: str, target: str) -> TraceabilityItem:
    return TraceabilityItem(id=generate_id("trace"), source=source, target=target)


def discovery(project_name: str, source_descriptors: list[str]) -> list[str]:
    if not source_descriptors:
        source_descriptors = ["baseline application context"]
    return [f"{project_name} from {descriptor}" for descriptor in source_descriptors]


def features(discovery_items: list[str]) -> list[ReviewableItem]:
    return [
        _item(
            name=f"Feature {index + 1}",
            description=f"Derived user capability from {item}.",
        )
        for index, item in enumerate(discovery_items)
    ]


def domains(feature_items: list[ReviewableItem]) -> list[ReviewableItem]:
    return [
        _item(
            name=f"Domain {index + 1}",
            description=f"Domain model area linked to {feature.name.lower()}.",
        )
        for index, feature in enumerate(feature_items)
    ]


def traceability(
    feature_items: list[ReviewableItem], domain_items: list[ReviewableItem]
) -> list[TraceabilityItem]:
    return [
        _trace(source=feature.name, target=domain.name)
        for feature, domain in zip(feature_items, domain_items, strict=False)
    ]


def business_rules(feature_items: list[ReviewableItem]) -> list[ReviewableItem]:
    return [
        _item(
            name=f"Rule {index + 1}",
            description=f"Business constraint for {feature.name.lower()}.",
        )
        for index, feature in enumerate(feature_items)
    ]


def flow_discovery(
    domain_items: list[ReviewableItem], rule_items: list[ReviewableItem]
) -> list[ReviewableItem]:
    flows: list[ReviewableItem] = []
    for index, (domain, rule) in enumerate(zip(domain_items, rule_items, strict=False)):
        flows.append(
            _item(
                name=f"Flow {index + 1}",
                description=f"Process flow in {domain.name.lower()} enforcing {rule.name.lower()}.",
            )
        )
    return flows


def run_pipeline(project_name: str, source_descriptors: list[str]) -> PipelineOutput:
    discovery_items = discovery(project_name, source_descriptors)
    feature_items = features(discovery_items)
    domain_items = domains(feature_items)
    trace_items = traceability(feature_items, domain_items)
    rule_items = business_rules(feature_items)
    flow_items = flow_discovery(domain_items, rule_items)
    return PipelineOutput(
        features=feature_items,
        domains=domain_items,
        flows=flow_items,
        business_rules=rule_items,
        traceability=trace_items,
    )
