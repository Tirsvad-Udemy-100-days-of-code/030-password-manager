# Password Manager Features

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

# Password Manager Features

## Purpose

Decide whether the program does what the three lectures describe: JSON storage, exception handling and search, behind the Tkinter window.

## Deliverable

The `password_manager` package with a JSON storage module, `generate_password`, `save` and `find_password` functions under the assignment's names, a Tkinter view with an MVVM view model, and pytest tests for every behaviour, all with Doxygen comments and reviewed against the Python checklist.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m pytest` passes | 0 failures | Any failure |
| 2 | Saving an entry writes nested JSON that `json.load` reads back | Test passes | Test fails or missing |
| 3 | A missing, empty and invalid data file are each handled without an exception reaching the user | 3 of 3 tests pass | Any case unhandled |
| 4 | Searching a saved website returns its e-mail and password; an unknown website returns a not-found message | 2 of 2 tests pass | Either fails |
| 5 | The code review record against `qc-programming-python` is `Go` | Go | No-Go or Go-with-conditions |
| 6 | No third-party import exists in `src/` | None found | Any found |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-001 | The skeleton, constants and configuration must exist first |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| BC-001 O1, O2, O3; Success criteria 1 to 5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in, autonomous mode) |

## Target Date

2026-10-17 — follows MIL-001 by two days, within the Business Case constraints.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement JSON storage | Create the storage module that writes entries with `json.dump(indent=4)`, reads with `json.load` and updates by loading the existing data first, as the first lecture explains, so the file stays one valid nested dictionary. | No | |
| 2 | Handle a missing, empty or invalid data file | Catch `FileNotFoundError` and `json.JSONDecodeError` with try, except, else and finally so a first save creates the file and the entry fields are cleared in every case (challenge 1). | No | |
| 3 | Implement find_password | Add the search that loads the data, looks the website up and returns the e-mail and password, or a clear not-found message, including the case where the file does not exist (challenge 2). | No | |
| 4 | Implement generate_password | Generate a random password of letters, digits and symbols with `random`/`secrets` from the standard library, using the length bounds from `constants.py`. | No | |
| 5 | Build the Tkinter window | Create the view and view model (MVVM): logo canvas, Website with Search, Email/Username, Password with Generate Password, and the Add button; copy the generated password with the Tkinter clipboard so no dependency is added. | No | |
| 6 | Write the pytest tests | Cover storage, the three file conditions, search found and not found, the generator and the view model with temporary files, because the tests are the evidence of the Business Case success criteria. | No | |
| 7 | Review the code against qc-programming-python | Review `src/` and `tests/` against the Python checklist and record an RC with the verdict before the pull request. | No | |

---

[BC-001]: ../business-case.md
