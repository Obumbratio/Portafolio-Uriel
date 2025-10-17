# Mini CSV Analyzer

Console utility that produces quick descriptive statistics from classroom-sized
CSV datasets. Built for fast iteration when learning Python data workflows.

## Features
- Numeric summaries: count, mean, median, min, and max.
- Categorical frequency tables using `collections.Counter`.
- Works on any comma-delimited file with headers.

## Quickstart
```bash
cd projects/mini-csv-analyzer
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py --help
```

## `python src/main.py --help`
```
usage: main.py [-h] {numeric,frequency} ...

Inspect CSV files with quick statistics.

positional arguments:
  {numeric,frequency}
    numeric             Numeric summary
    frequency           Categorical frequency table

options:
  -h, --help            show this help message and exit
```

## Sample Dataset
[`data/sample.csv`](data/sample.csv)
```csv
student_id,course,score
1001,Networking,88
1002,Programming,92
1003,Networking,75
1004,Databases,85
```

## Usage Examples
```bash
python src/main.py numeric data/sample.csv score
python src/main.py frequency data/sample.csv course
```

## Output Example
```
count: 4
mean: 85.0
median: 86.5
min: 75.0
max: 92.0
```

## Tests
```bash
pytest
```

## Extension Ideas
- Swap the manual parser for `pandas` to unlock groupby aggregations.
- Visualize distributions with `matplotlib` histograms.
- Package as a `pipx` command for instant usage on any workstation.

## License
Released under the [MIT License](../../LICENSE).
