"""Entry point for the mini CSV analyzer CLI."""

from __future__ import annotations

from mini_csv_analyzer import build_parser, handle_command


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    print(handle_command(args))


if __name__ == "__main__":
    main()
