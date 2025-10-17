"""Run the educational game prototype."""

from __future__ import annotations

from edu_game.game import GameSession


def main() -> None:
    game = GameSession()
    print("Welcome to the learning quest! Use arrow words to move.")
    for command in ["right", "right", "down", "down", "down", "left"]:
        print(f"Action: {command}")
        print(game.step(command))
    print("Session complete. Final status:")
    print(game.describe_state())


if __name__ == "__main__":
    main()
