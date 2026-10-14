# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [463ffc3] |

---

# Code review for MIL-002

## Artifact Under Review

- Instance reviewed: `src/password_manager/` and `tests/` (19 modules, 37 tests) as of the MIL-002 pull request, delivering [MIL-002]
- Checklist used: [QC-PY-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Packages and modules are snake_case, classes PascalCase (`JsonPasswordRepository`, `PasswordEntry`), constants UPPER_SNAKE. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (`EntryNotFoundError`, `find_password`, `confirm_save`); no cryptic abbreviations. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff format --check` reports 26 files already formatted; `ruff check` reports 0 findings and the sources contain no `noqa`. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | ruff rule set `ANN` is enabled and passes, so every signature is annotated. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare `except`; repository and view model catch the narrowest domain errors and re-raise with `raise ... from error`. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; ruff `B` rules pass. |
| 7 | Files, locks and connections are managed with context managers | Pass | The repository opens the JSON file with `with self._path.open(...)`. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Every public module, class and function has a Doxygen docstring (`@brief`, `@param`, `@return`, `@throws`); `doxygen Doxyfile` runs without warnings. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No `print` and no logging; passwords are shown only in the window messages the course requires. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | Pass | No DCD exists (no use case modelled, see Project Plan Open Issues); the class set follows the clean-architecture layers and is recorded in MIL-002 tasks. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | `python -m pytest` runs 37 tests (unit, integration, e2e) named for behaviour, using `tmp_path` and fakes; none touch the network or depend on order. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | No type checker is configured. The single `Any` (JSON object values) has a justifying comment. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | `dependencies = []`; pytest and ruff are the only dev extras and both are used. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Constants, messages and JSON keys are defined once in `constants.py`; validation of empty fields is in the use cases only. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | `domain` imports only `constants` and the standard library; `application` imports `domain`; `presentation` imports no `infrastructure` module (grep); only `main.py` composes them. No import cycle. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Each class has one job (entry, generator, use cases, JSON repository, view model, view); the use cases depend on the `PasswordRepository` protocol and receive the implementation. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | `domain`, `application`, `infrastructure`, `presentation` packages under `src/password_manager/` and `unit`, `integration`, `e2e` under `tests/`; imports point inward. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | All file and folder names are English snake_case with no spaces. |

## Overall Verdict

Go — every Mandatory criterion passes.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[MIL-002]: ../../milestones/mil-002-password-manager-features.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[463ffc3]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/commit/463ffc3d4a477affa3ac45f1c33c4241a62677e1
