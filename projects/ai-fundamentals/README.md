# AI Fundamentals Prototype

Lightweight Python prototypes that demonstrate foundational AI concepts for
pattern recognition and simple decision logic. Designed as a learning sandbox
while progressing toward advanced coursework.

## Learning Goals
- Practice translating real-world observations into structured data signals.
- Understand how rule-based systems provide transparent decisions.
- Explore how planning heuristics prioritize tasks.

## What's Included
- `detect_pattern` tallies repeated motifs to mimic recognition tasks.
- `decide_route` applies deterministic rules to recommend an action.
- `simulate_planning` transforms notes into actionable follow-ups.

## Quickstart
```bash
cd projects/ai-fundamentals
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

## Tiny Examples
```python
from ai_fundamentals.simulations import detect_pattern, decide_route

detect_pattern(["Alert: spike", "Spike detected twice"], "spike")
# -> PatternInsight(pattern='spike', occurrences=2)

decide_route("Clear", "Heavy")
# -> RouteDecision(destination='bike', rationale='Avoid traffic with a reliable bike route')
```

## Limitations & Warnings
- These are deterministic demonstrations, not production AI systems.
- No model training is performed; examples assume clean, curated inputs.
- For critical decisions, replace with validated ML models and guardrails.

## Tests
```bash
pytest
```

## Next Steps
- Add a perceptron example to visualize classification boundaries.
- Experiment with reinforcement learning style reward tracking.
- Package modules into Jupyter notebooks for instructional workshops.

## License
Released under the [MIT License](../../LICENSE).
