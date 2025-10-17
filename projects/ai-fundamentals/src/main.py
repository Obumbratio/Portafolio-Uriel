"""Run AI fundamentals simulations."""

from __future__ import annotations

from ai_fundamentals.simulations import decide_route, detect_pattern, simulate_planning


def main() -> None:
    insight = detect_pattern([
        "Sensors detected pattern X",
        "Pattern X repeated during peak hours",
    ], "pattern x")
    decision = decide_route("Clear", "Heavy")
    plan = simulate_planning([
        "If sensors trip twice, notify support",
        "Document observed outcomes",
        "Follow-up question?",
    ])

    print(f"Pattern '{insight.pattern}' occurrences: {insight.occurrences}")
    print(f"Recommended route: {decision.destination} ({decision.rationale})")
    print("Planning queue:")
    for step in plan:
        print(f"- {step}")


if __name__ == "__main__":
    main()
