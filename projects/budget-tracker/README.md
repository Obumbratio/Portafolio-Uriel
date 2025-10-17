# Budget Tracker

CLI expense logger that writes to CSV files and generates quick budget reports.
Ideal for students tracking spending across classes, commuting, and projects.

## Features
- Log expenses with consistent categories and notes.
- Generate month-to-date totals on demand.
- Summarize spending by category for budgeting conversations.
- Calculate date range totals for trips or events.

## Quickstart
```bash
cd projects/budget-tracker
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py --help
```

## `python src/main.py --help`
```
usage: main.py [-h] {add,report-month,report-category,report-range} ...

Track expenses with CSV reports.

positional arguments:
  {add,report-month,report-category,report-range}
    add                 Log a new expense entry
    report-month        Show the total spent in a year/month
    report-category     Totals per category
    report-range        Total spending between two dates

options:
  -h, --help            show this help message and exit
```

## CLI Usage Examples
```bash
python src/main.py add 2025-01-04 Food "Campus coffee" 4.50
python src/main.py report-month 2025 1
python src/main.py report-category
python src/main.py report-range 2025-01-01 2025-01-31
```

## Example CSV
```csv
date,category,description,amount
2025-01-04,Food,Campus coffee,4.50
2025-01-05,Transport,Bus pass,20.00
2025-01-10,Books,Data analytics workbook,35.00
```

## Report Samples
- `report-month 2025 1` → `2025-01: $59.50`
- `report-category` →
  ```
  Books: $35.00
  Food: $4.50
  Transport: $20.00
  ```
- `report-range 2025-01-01 2025-01-31` → `2025-01-01 to 2025-01-31: $59.50`

## Tests
```bash
pytest
```

## Troubleshooting
- Ensure dates follow `YYYY-MM-DD` or parsing will fail.
- CSV files are created automatically; delete them to reset history.
- Use `python src/main.py report-category` to verify categories before exporting.

## Data
Starter dataset: [`data/sample.csv`](data/sample.csv)

## Next Steps
- Add pandas-powered charts for weekly spending trends.
- Export reports as formatted Markdown summaries.
- Integrate SQLite for multi-device history.

## License
Released under the [MIT License](../../LICENSE).
