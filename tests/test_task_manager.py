from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "projects" / "task-manager" / "src"))

from task_manager import build_parser, handle_command, storage


def run_cli(data_path: Path, command: list[str]) -> str:
    storage.DEFAULT_DATA_PATH = data_path
    parser = build_parser()
    args = parser.parse_args(command)
    return handle_command(args)


def test_add_and_list_tasks(tmp_path: Path) -> None:
    data_file = tmp_path / "tasks.json"
    message = run_cli(data_file, ["add", "Write unit tests"])
    assert "Created task" in message

    list_output = run_cli(data_file, ["list"])
    assert "Write unit tests" in list_output


def test_mark_done_updates_status(tmp_path: Path) -> None:
    data_file = tmp_path / "tasks.json"
    run_cli(data_file, ["add", "Plan sprint"])
    done_message = run_cli(data_file, ["done", "1"])
    assert done_message == "Task completed"

    list_output = run_cli(data_file, ["list"])
    assert "✅ #1" in list_output


def test_delete_task(tmp_path: Path) -> None:
    data_file = tmp_path / "tasks.json"
    run_cli(data_file, ["add", "Document API"])
    delete_message = run_cli(data_file, ["delete", "1"])
    assert delete_message == "Task deleted"

    list_output = run_cli(data_file, ["list"])
    assert list_output == "No tasks yet."
