"""Command-line interface for CSV analysis."""

from __future__ import annotations

import argparse
from pathlib import Path

from .analyzer import CSVAnalyzer


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Inspect CSV files with quick statistics.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    numeric_parser = subparsers.add_parser("numeric", help="Numeric summary")
    numeric_parser.add_argument("path", help="Path to CSV file")
    numeric_parser.add_argument("column", help="Numeric column name")

    freq_parser = subparsers.add_parser(
        "frequency", help="Categorical frequency table"
    )
    freq_parser.add_argument("path", help="Path to CSV file")
    freq_parser.add_argument("column", help="Categorical column name")

    return parser


def handle_command(args: argparse.Namespace) -> str:
    analyzer = CSVAnalyzer(Path(args.path))
    if args.command == "numeric":
        summary = analyzer.numeric_summary(args.column)
        return "\n".join(f"{key}: {value}" for key, value in summary.items())
    if args.command == "frequency":
        counts = analyzer.categorical_frequency(args.column)
        return "\n".join(f"{key}: {value}" for key, value in counts.items())
    raise ValueError(f"Unknown command: {args.command}")
