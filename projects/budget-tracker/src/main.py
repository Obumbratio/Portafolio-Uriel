"""Entry point for the Budget Tracker CLI."""

from __future__ import annotations

from budget_tracker import build_parser, handle_command


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    print(handle_command(args))


if __name__ == "__main__":
    main()
