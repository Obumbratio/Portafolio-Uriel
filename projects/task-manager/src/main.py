"""Entry point for the Task Manager CLI."""

from __future__ import annotations

from task_manager import build_parser, handle_command


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    message = handle_command(args)
    print(message)


if __name__ == "__main__":
    main()
