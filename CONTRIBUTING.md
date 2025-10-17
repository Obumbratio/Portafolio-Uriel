# Contributing Guidelines

Thank you for investing time in contributing to Uriel Castaneda Valencia's
portfolio projects. Please follow the steps below to keep the workflow smooth
and collaborative.

## Getting Started
1. Fork the repository on GitHub.
2. Clone your fork and set the original repo as an `upstream` remote.
3. Create a Python 3.11 virtual environment and install the development tools:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

## Branch Naming
Use descriptive branch names following this convention:
```
feature/short-description
fix/short-description
chore/short-description
```

## Commit Style
Write commits in the imperative mood and keep them concise:
```
feat: add monthly summary report
fix: handle empty csv gracefully
chore: update ci workflow
```

## Pull Request Checklist
Before opening a PR, confirm the following:
- [ ] Tests pass locally with `pytest`.
- [ ] Linting passes with `flake8`.
- [ ] Documentation is updated when behavior changes.
- [ ] Screenshots or logs are attached when relevant.
- [ ] The PR description includes context and testing notes.

## Running Tests and Linters
From the project root run:
```bash
pytest
flake8
```
If a subproject includes additional instructions, follow its README.

## Code Review
Be responsive to feedback. Update your PR with fixes and clarifications as
needed. Maintainers will merge once the checklist is satisfied.
