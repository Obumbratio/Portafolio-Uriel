# Educational Game Prototype

Text-based prototype that reinforces classroom topics through lightweight game
mechanics. Players move across a grid to collect knowledge tokens before turns
run out.

## Features
- 5x5 grid with three themed knowledge tokens.
- Score system rewards exploration and penalizes obstacles.
- Deterministic loop ideal for experimentation with new mechanics.

## Controls
- `up`, `down`, `left`, `right` — move the learner avatar.
- Each turn moves once, collects tokens automatically, and reduces turns.

## Architecture Overview
- `GameSession` holds the grid, player state, and turn counter.
- `Player` tracks position, score, and collected topics.
- `step()` orchestrates move → collect → penalty → status updates.
- `auto_play()` simulates random moves for quick demos.

## Quickstart
```bash
cd projects/educational-game-prototype
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

## Example Output
```
Welcome to the learning quest! Use arrow words to move.
Action: right
Pos: (1,0) | Score: 0 | Inventory: None | Turns left: 9
...
```

## Tests
```bash
pytest
```

## Future Improvements
- Add ASCII sprites and colors for better accessibility.
- Introduce quiz prompts before collecting advanced tokens.
- Export session summaries to CSV for classroom analytics.

## License
Released under the [MIT License](../../LICENSE).
