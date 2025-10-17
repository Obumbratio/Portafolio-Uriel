"""CSV storage helpers for the budget tracker."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Dict, List, Optional

FIELDS = ["date", "category", "description", "amount"]
DEFAULT_CSV_PATH = Path(__file__).resolve().parents[2] / "data" / "expenses.csv"


def _resolve_path(path: Optional[Path] = None) -> Path:
    return path or DEFAULT_CSV_PATH


def ensure_storage(path: Optional[Path] = None) -> Path:
    target = _resolve_path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        with target.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=FIELDS)
            writer.writeheader()
    return target


def append_entry(entry: Dict[str, str], path: Optional[Path] = None) -> None:
    target = ensure_storage(path)
    with target.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writerow(entry)


def read_entries(path: Optional[Path] = None) -> List[Dict[str, str]]:
    target = ensure_storage(path)
    with target.open("r", newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return list(reader)
