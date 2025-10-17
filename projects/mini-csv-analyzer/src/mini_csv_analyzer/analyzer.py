"""Utility functions to compute statistics from CSV data."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path
from statistics import mean, median
from typing import Dict, Iterable, List


class CSVAnalyzer:
    """Compute numeric and categorical summaries."""

    def __init__(self, path: Path) -> None:
        self.path = path
        self.rows = self._load_rows()

    def _load_rows(self) -> List[Dict[str, str]]:
        with self.path.open("r", newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            return list(reader)

    def numeric_summary(self, column: str) -> Dict[str, float]:
        values = [float(row[column]) for row in self.rows if row.get(column)]
        if not values:
            raise ValueError(f"No numeric data found in column '{column}'")
        return {
            "count": len(values),
            "mean": round(mean(values), 2),
            "median": round(median(values), 2),
            "min": round(min(values), 2),
            "max": round(max(values), 2),
        }

    def categorical_frequency(self, column: str) -> Dict[str, int]:
        values = [row[column] for row in self.rows if row.get(column)]
        if not values:
            raise ValueError(f"No categorical data found in column '{column}'")
        counts = Counter(values)
        return dict(counts)
