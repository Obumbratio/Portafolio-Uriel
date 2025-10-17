from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "projects" / "mini-csv-analyzer" / "src"),
)

from mini_csv_analyzer.analyzer import CSVAnalyzer


def test_numeric_summary(tmp_path: Path) -> None:
    csv_path = tmp_path / "scores.csv"
    csv_path.write_text(
        "student,score\n1,80\n2,90\n3,100\n",
        encoding="utf-8",
    )
    analyzer = CSVAnalyzer(csv_path)
    summary = analyzer.numeric_summary("score")
    assert summary["count"] == 3
    assert summary["min"] == 80
    assert summary["max"] == 100


def test_categorical_frequency(tmp_path: Path) -> None:
    csv_path = tmp_path / "courses.csv"
    csv_path.write_text(
        "student,course\n1,IT\n2,IT\n3,CS\n",
        encoding="utf-8",
    )
    analyzer = CSVAnalyzer(csv_path)
    frequencies = analyzer.categorical_frequency("course")
    assert frequencies == {"IT": 2, "CS": 1}
