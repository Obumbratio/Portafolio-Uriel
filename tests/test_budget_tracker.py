from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "projects" / "budget-tracker" / "src"),
)

from budget_tracker import build_parser, handle_command, storage


def run_cli(csv_path: Path, command: list[str]) -> str:
    storage.DEFAULT_CSV_PATH = csv_path
    parser = build_parser()
    args = parser.parse_args(command)
    return handle_command(args)


def test_add_and_month_report(tmp_path: Path) -> None:
    csv_file = tmp_path / "expenses.csv"
    run_cli(csv_file, ["add", "2025-01-04", "Food", "Coffee", "4.50"])
    run_cli(csv_file, ["add", "2025-01-05", "Transport", "Bus", "20.00"])

    report = run_cli(csv_file, ["report-month", "2025", "1"])
    assert "2025-01" in report
    assert "$24.50" in report


def test_category_report(tmp_path: Path) -> None:
    csv_file = tmp_path / "expenses.csv"
    run_cli(csv_file, ["add", "2025-02-01", "Books", "Workbook", "35.00"])
    run_cli(csv_file, ["add", "2025-02-02", "Books", "Notebook", "5.00"])

    report = run_cli(csv_file, ["report-category"])
    assert "Books: $40.00" in report


def test_range_report(tmp_path: Path) -> None:
    csv_file = tmp_path / "expenses.csv"
    run_cli(csv_file, ["add", "2025-03-01", "Food", "Lunch", "12.00"])
    run_cli(csv_file, ["add", "2025-03-10", "Food", "Groceries", "45.00"])

    report = run_cli(csv_file, ["report-range", "2025-03-01", "2025-03-31"])
    assert "$57.00" in report
