**English** · [Dansk](Development-da) · [Bahasa Malaysia](Development-ms)

# Development

## Layout

| Folder | Holds |
| --- | --- |
| `src/password_manager/domain` | Entry, password generator and errors; no input or output |
| `src/password_manager/application` | Use cases and the repository port |
| `src/password_manager/infrastructure` | The JSON repository |
| `src/password_manager/presentation` | The MVVM view and view model |
| `src/password_manager/constants.py` | Every constant and message |
| `tests/` | `unit`, `integration` and `e2e` tests |
| `tools/` | `capture_screenshots.py` |

Imports point inward; only `main.py` connects the layers.

## Tests and lint

```bash
python -m pytest
python -m ruff format src tests tools
python -m ruff check src tests tools
```

## Source documentation

Comments are Doxygen style. Build the HTML with `doxygen Doxyfile`; it opens at
`docs/doxygen/html/index.html`.

## Screenshots

On Windows, with the virtual environment active:

```bash
python tools/capture_screenshots.py
```

The images are written to `docs/images/` from the real window and a temporary
data file.

## Project documents

The project follows a planning-first workflow: Business Case, Stakeholder
Analysis, Project Plan and milestones are in `docs/`. Work is done on one branch
and one pull request per milestone.
