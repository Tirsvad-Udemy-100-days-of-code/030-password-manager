# Project Foundation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [53f56ee] |

---

# Project Foundation

## Purpose

Decide whether the repository has the configuration, conventions and entry documentation every later phase builds on, so that feature work starts on a runnable, testable skeleton.

## Deliverable

A repository with `pyproject.toml` (Python 3.13 or newer, pytest as a development dependency, no runtime dependency), a Python `.gitignore` that excludes `.env` and `.venv`, `src/password_manager/constants.py`, a smoke test under `tests/`, a `Doxyfile`, a `README.md` built from the framework template with `.venv` instructions, and a repository description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` passes in a fresh `.venv` | 0 failures | Any failure |
| 2 | `pyproject.toml` has `requires-python >= 3.13` and an empty runtime `dependencies` list | Both present | Missing or non-empty |
| 3 | `.gitignore` contains `.env` and `.venv` | Both present | Either missing |
| 4 | `bash framework/scripts/check-readme.sh` exits 0 | Exit 0 | Any finding |
| 5 | The git host shows a description and at least 5 topics for the repository | Both set | Either missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| (none) | The baseline documents are in the repository |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| BC-001 O4; Success criteria 4, 5 and 7 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in, autonomous mode) |

## Target Date

2026-10-15 — the Business Case sets no deadline; the plan's first phase is one to two days.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create pyproject.toml and the package skeleton | Add `pyproject.toml` with Python 3.13 or newer, the setuptools build backend, a `src/password_manager` package, pytest as an optional `dev` dependency and pytest paths. Needed so the project installs with `python -m pip install -e .[dev]` and tests find the package. | No | |
| 2 | Add the Python .gitignore | Add a Python `.gitignore` that also excludes `.env`, `.venv` and Doxygen output, so a token or an environment is never committed. | No | |
| 3 | Add constants.py | Create `src/password_manager/constants.py` holding the data file name, window title, padding, default e-mail and password-length values, because the requirement is that constants live in one module. | No | |
| 4 | Add the Doxyfile | Add a `Doxyfile` that documents `src/` into `docs/doxygen/` so the Doxygen comments in the source can be built into HTML. | No | |
| 5 | Write the README from the framework template | Create `README.md` from the framework template with requirements, the `.venv` creation and `python -m pip install --upgrade pip` commands, run and test instructions and a Security note. | No | |
| 6 | Set the repository description and topics | Use the git host API with the token from `.env` (never printed, never imported by the project) to set a description and topics for the repository so viewers (S03) can find it. | No | |
| 7 | Add the smoke test | Add a first pytest test that imports the package and its constants so the test command is proven from the first milestone. | No | |

---

[BC-001]: ../business-case.md
[53f56ee]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/commit/53f56eeb143d810b91da23f743a53a32207f81bb
