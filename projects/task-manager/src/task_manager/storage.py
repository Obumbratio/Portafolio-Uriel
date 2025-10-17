"""Persistence helpers for the Task Manager."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional

DEFAULT_DATA_PATH = Path(__file__).resolve().parents[2] / "data" / "tasks.json"


def _resolve_path(path: Optional[Path] = None) -> Path:
    return path or DEFAULT_DATA_PATH


def ensure_storage(path: Optional[Path] = None) -> Path:
    target = _resolve_path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        target.write_text("[]", encoding="utf-8")
    return target


def load_tasks(path: Optional[Path] = None) -> List[Dict[str, object]]:
    target = ensure_storage(path)
    raw = target.read_text(encoding="utf-8")
    try:
        data = json.loads(raw or "[]")
    except json.JSONDecodeError:
        data = []
    return data


def save_tasks(tasks: List[Dict[str, object]], path: Optional[Path] = None) -> None:
    target = ensure_storage(path)
    target.write_text(json.dumps(tasks, indent=2, sort_keys=True), encoding="utf-8")
