from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(
    0,
    str(
        Path(__file__).resolve().parents[1]
        / "projects"
        / "educational-game-prototype"
        / "src"
    ),
)

from edu_game.game import GameSession


def test_collecting_tokens_increases_score() -> None:
    game = GameSession()
    game.step("right")
    game.step("right")
    game.step("right")
    game.step("down")
    game.step("down")
    game.step("down")
    assert "math" in game.player.inventory or "science" in game.player.inventory
    assert game.player.score >= 10


def test_penalty_does_not_go_negative() -> None:
    game = GameSession()
    game.player.position = (2, 1)
    game.step("down")  # moves into obstacle (2,2)
    assert game.player.score >= 0
