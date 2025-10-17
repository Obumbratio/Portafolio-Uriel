"""Reporting helpers for expenses."""

from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from typing import Dict, Iterable, List

from .storage import read_entries

DATE_FMT = "%Y-%m-%d"


def _parse_amount(value: str) -> float:
    return float(value)


def _parse_date(value: str) -> datetime:
    return datetime.strptime(value, DATE_FMT)


def monthly_report(year: int, month: int) -> Dict[str, float]:
    entries = read_entries()
    total = 0.0
    for entry in entries:
        entry_date = _parse_date(entry["date"])
        if entry_date.year == year and entry_date.month == month:
            total += _parse_amount(entry["amount"])
    return {"year": year, "month": month, "total": round(total, 2)}


def category_report() -> Dict[str, float]:
    totals: Dict[str, float] = defaultdict(float)
    for entry in read_entries():
        totals[entry["category"]] += _parse_amount(entry["amount"])
    return {key: round(value, 2) for key, value in totals.items()}


def date_range_report(start: str, end: str) -> Dict[str, float]:
    start_date = _parse_date(start)
    end_date = _parse_date(end)
    total = 0.0
    for entry in read_entries():
        entry_date = _parse_date(entry["date"])
        if start_date <= entry_date <= end_date:
            total += _parse_amount(entry["amount"])
    return {
        "start": start,
        "end": end,
        "total": round(total, 2),
    }
