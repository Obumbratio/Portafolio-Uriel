"""Simple simulations to illustrate foundational AI concepts."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List


@dataclass
class PatternInsight:
    pattern: str
    occurrences: int


def detect_pattern(sequence: Iterable[str], motif: str) -> PatternInsight:
    """Count motif occurrences to mimic pattern recognition."""
    joined = " ".join(sequence).lower()
    count = joined.count(motif.lower())
    return PatternInsight(pattern=motif, occurrences=count)


@dataclass
class RouteDecision:
    destination: str
    rationale: str


def decide_route(weather: str, traffic: str) -> RouteDecision:
    """Simple rule engine that recommends walking, biking, or driving."""
    weather = weather.lower()
    traffic = traffic.lower()
    if weather in {"clear", "mild"} and traffic == "heavy":
        return RouteDecision("bike", "Avoid traffic with a reliable bike route")
    if weather in {"rain", "storm"}:
        return RouteDecision("drive", "Stay sheltered from wet conditions")
    return RouteDecision("walk", "Enjoy the weather and save energy")


def simulate_planning(notes: List[str]) -> List[str]:
    """Generate next steps by prioritizing actionable statements."""
    actions = []
    for note in notes:
        if note.lower().startswith("if"):
            actions.append("Analyze conditional: " + note)
        elif note.endswith("?"):
            actions.append("Research answer: " + note)
        else:
            actions.append("Schedule: " + note)
    return actions
