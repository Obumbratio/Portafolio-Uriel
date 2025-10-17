"""Business logic for task manipulation."""

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional

from .storage import load_tasks, save_tasks

ISO_FORMAT = "%Y-%m-%dT%H:%M:%S"


def _now() -> str:
    return datetime.utcnow().strftime(ISO_FORMAT)


def list_tasks() -> List[Dict[str, object]]:
    return load_tasks()


def add_task(title: str, notes: Optional[str] = None) -> Dict[str, object]:
    tasks = load_tasks()
    task_id = max((task.get("id", 0) for task in tasks), default=0) + 1
    task = {
        "id": task_id,
        "title": title,
        "notes": notes or "",
        "status": "todo",
        "created_at": _now(),
        "completed_at": None,
    }
    tasks.append(task)
    save_tasks(tasks)
    return task


def mark_done(task_id: int) -> Optional[Dict[str, object]]:
    tasks = load_tasks()
    for task in tasks:
        if task.get("id") == task_id:
            task["status"] = "done"
            task["completed_at"] = _now()
            save_tasks(tasks)
            return task
    return None


def delete_task(task_id: int) -> bool:
    tasks = load_tasks()
    remaining = [task for task in tasks if task.get("id") != task_id]
    if len(remaining) == len(tasks):
        return False
    save_tasks(remaining)
    return True
