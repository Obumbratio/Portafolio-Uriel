# Task Manager

Command-line task tracker that stores todos in JSON and keeps the workflow in the
terminal. Built with modular Python functions and robust argparse commands.

## Features
- Add, list, complete, and delete tasks from the CLI.
- Persist tasks in a JSON document for offline use.
- Track creation and completion timestamps in UTC.
- Export-friendly schema for future dashboards.

## Quickstart
```bash
cd projects/task-manager
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/main.py --help
```

## `python src/main.py --help`
```
usage: main.py [-h] {add,list,done,delete} ...

Lightweight CLI task manager with JSON persistence.

positional arguments:
  {add,list,done,delete}
    add                 Add a new task
    list                List existing tasks
    done                Mark a task as completed
    delete              Delete a task by its identifier

options:
  -h, --help            show this help message and exit
```

## Example Commands
```bash
python src/main.py add "Draft internship report" --notes "Include analytics wins"
python src/main.py list
python src/main.py done 1
python src/main.py delete 1
```

## JSON Schema
```json
{
  "id": 1,
  "title": "Draft resume bullet points",
  "notes": "Focus on quantifiable results",
  "status": "todo" | "done",
  "created_at": "2025-01-12T10:00:00",
  "completed_at": "2025-01-13T09:30:00" | null
}
```

## Code Snippet
```python
from task_manager import build_parser, handle_command

parser = build_parser()
args = parser.parse_args(["add", "Stand-up agenda"])
print(handle_command(args))
```

## Data Sample
See [`data/sample_tasks.json`](data/sample_tasks.json) for a starter file.

## Tests
Run the unit tests to verify core flows:
```bash
pytest
```

## Future Roadmap
- Sync with a lightweight FastAPI backend for shared task boards.
- Add tagging and filtering for focus areas.
- Publish as a `pipx` package with shell completions.

## License
Released under the [MIT License](../../LICENSE).
