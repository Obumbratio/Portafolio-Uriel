from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "projects" / "ai-fundamentals" / "src"),
)

from ai_fundamentals.simulations import decide_route, detect_pattern, simulate_planning


def test_detect_pattern_counts_occurrences() -> None:
    insight = detect_pattern(["pattern a", "PATTERN A appears"], "pattern a")
    assert insight.occurrences == 2


def test_decide_route_handles_weather() -> None:
    decision = decide_route("Rain", "Light")
    assert decision.destination == "drive"


def test_simulate_planning_orders_notes() -> None:
    plan = simulate_planning(["If sensors trip", "Schedule meeting", "Check logs?"])
    assert plan[0].startswith("Analyze conditional")
    assert plan[-1].startswith("Research answer")
