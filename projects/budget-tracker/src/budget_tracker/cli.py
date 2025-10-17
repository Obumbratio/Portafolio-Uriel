"""Command-line interface for the budget tracker."""

from __future__ import annotations

import argparse
from datetime import datetime

from .reports import category_report, date_range_report, monthly_report
from .storage import append_entry

DATE_FMT = "%Y-%m-%d"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Track expenses with CSV reports.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    add_parser = subparsers.add_parser("add", help="Log a new expense entry")
    add_parser.add_argument("date", help="Transaction date in YYYY-MM-DD")
    add_parser.add_argument("category", help="Expense category tag")
    add_parser.add_argument("description", help="Short description")
    add_parser.add_argument("amount", type=float, help="Amount spent")

    month_parser = subparsers.add_parser(
        "report-month", help="Show the total spent in a year/month"
    )
    month_parser.add_argument("year", type=int)
    month_parser.add_argument("month", type=int)

    subparsers.add_parser("report-category", help="Totals per category")

    range_parser = subparsers.add_parser(
        "report-range",
        help="Total spending between two dates",
    )
    range_parser.add_argument("start", help="Start date YYYY-MM-DD")
    range_parser.add_argument("end", help="End date YYYY-MM-DD")

    return parser


def handle_command(args: argparse.Namespace) -> str:
    if args.command == "add":
        entry = {
            "date": args.date,
            "category": args.category,
            "description": args.description,
            "amount": f"{args.amount:.2f}",
        }
        datetime.strptime(entry["date"], DATE_FMT)
        append_entry(entry)
        return "Expense logged"
    if args.command == "report-month":
        data = monthly_report(args.year, args.month)
        return f"{data['year']}-{data['month']:02d}: ${data['total']:.2f}"
    if args.command == "report-category":
        totals = category_report()
        return "\n".join(
            f"{category}: ${amount:.2f}" for category, amount in sorted(totals.items())
        ) or "No data"
    if args.command == "report-range":
        data = date_range_report(args.start, args.end)
        return (
            f"{data['start']} to {data['end']}: ${data['total']:.2f}"
        )
    raise ValueError(f"Unknown command: {args.command}")
