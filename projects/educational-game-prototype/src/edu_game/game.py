"""Simple text-based educational game prototype."""

from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import List, Tuple

GRID_SIZE = 5
TOKENS = {(1, 3): "math", (3, 1): "science", (4, 4): "history"}
OBSTACLES = {(2, 2), (0, 4)}


@dataclass
class Player:
    position: Tuple[int, int] = (0, 0)
    score: int = 0
    inventory: List[str] = field(default_factory=list)


@dataclass
class GameSession:
    player: Player = field(default_factory=Player)
    turns: int = 10

    def move(self, direction: str) -> None:
        x, y = self.player.position
        if direction == "up" and y > 0:
            y -= 1
        elif direction == "down" and y < GRID_SIZE - 1:
            y += 1
        elif direction == "left" and x > 0:
            x -= 1
        elif direction == "right" and x < GRID_SIZE - 1:
            x += 1
        self.player.position = (x, y)

    def collect_token(self) -> None:
        pos = self.player.position
        if pos in TOKENS:
            topic = TOKENS[pos]
            if topic not in self.player.inventory:
                self.player.inventory.append(topic)
                self.player.score += 10

    def apply_penalty(self) -> None:
        if self.player.position in OBSTACLES:
            self.player.score = max(0, self.player.score - 5)

    def step(self, direction: str) -> str:
        if self.turns <= 0:
            return "Game over"
        self.move(direction)
        self.collect_token()
        self.apply_penalty()
        self.turns -= 1
        return self.describe_state()

    def describe_state(self) -> str:
        x, y = self.player.position
        inventory = ", ".join(self.player.inventory) or "None"
        return (
            f"Pos: ({x},{y}) | Score: {self.player.score}"
            f" | Inventory: {inventory} | Turns left: {self.turns}"
        )

    def auto_play(self) -> List[str]:
        transcript = []
        for _ in range(self.turns):
            direction = random.choice(["up", "down", "left", "right"])
            transcript.append(self.step(direction))
            if self.turns == 0:
                break
        return transcript
