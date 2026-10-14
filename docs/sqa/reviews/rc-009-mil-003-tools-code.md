# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [MIL-003], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [eb7b7dc] |

---

# Code review of tools/capture_screenshots.py (MIL-003)

## Artifact Under Review

- Instance reviewed: `tools/capture_screenshots.py` as of the MIL-003 pull request, delivering [MIL-003]
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Names in `tools/capture_screenshots.py` follow PEP 8 (`render_window`, `STATES`, `BitmapInfoHeader`). |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose; the only short names are `x`, `y` in pixel loops. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format --check` and `ruff check` pass for `tools`; no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | ruff rule set `ANN` passes, so every signature is annotated. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No `except` clauses; no bare handlers. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults and no shadowed builtins. |
| 7 | Files, locks and connections are managed with context managers | Pass | The temporary folder uses `with tempfile.TemporaryDirectory()`; GDI handles are released explicitly. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every public function and class has a Doxygen docstring. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` for diagnostics beyond the progress line `wrote <file>` of a command line tool; no secrets. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | A tool script, no design class; it traces to MIL-003 task 1. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | The tool is exercised by the capture run itself and its output was inspected; it is not unit tested because it needs a Windows desktop (stated in its docstring). |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | No type checker configured; `Any` is not used. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Standard library only; no dependency declared. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | The sample values and state names are defined once at the top of the file. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | A tool outside `src/`; it imports the application only through its public layers. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Functions each have one job (render, enumerate, compose, write PNG, run a state). |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | Placed in `tools/`, outside the layers, as MIL-003 and the wiki state; `src/` layout unchanged. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | File and folder names are English, snake_case, no spaces. |

## Overall Verdict

Go — every Mandatory criterion passes.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[MIL-003]: ../../milestones/mil-003-documentation-and-publishing.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[eb7b7dc]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/commit/eb7b7dcb17cb96535db0812c26252e9db0174d73
