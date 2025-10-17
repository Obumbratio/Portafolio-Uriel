"""Command-line interface for managing tasks."""

from __future__ import annotations

import argparse
from typing import Iterable

from .core import add_task, delete_task, list_tasks, mark_done


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Lightweight CLI task manager with JSON persistence.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Short description of the task")
    add_parser.add_argument("--notes", help="Optional notes", default="")

    subparsers.add_parser("list", help="List existing tasks")

    done_parser = subparsers.add_parser("done", help="Mark a task as completed")
    done_parser.add_argument("task_id", type=int, help="Identifier of the task")

    delete_parser = subparsers.add_parser(
        "delete",
        help="Delete a task by its identifier",
    )
    delete_parser.add_argument("task_id", type=int)

    return parser


def _format_tasks(tasks: Iterable[dict]) -> str:
    lines = []
    for task in tasks:
        status = "✅" if task.get("status") == "done" else "⬜"
        line = (
            f"{status} #{task.get('id')}: {task.get('title')}"
            f" (notes: {task.get('notes', '')})"
        )
        lines.append(line)
    return "\n".join(lines) or "No tasks yet."


def handle_command(args: argparse.Namespace) -> str:
    if args.command == "add":
        task = add_task(args.title, notes=args.notes)
        return f"Created task #{task['id']}"
    if args.command == "list":
        return _format_tasks(list_tasks())
    if args.command == "done":
        task = mark_done(args.task_id)
        return "Task completed" if task else "Task not found"
    if args.command == "delete":
        return "Task deleted" if delete_task(args.task_id) else "Task not found"
    raise ValueError(f"Unsupported command: {args.command}")
