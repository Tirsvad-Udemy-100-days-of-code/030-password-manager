# Password Manager Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [53f56ee] |

---

# Password Manager Business Case

## Executive Summary

A desktop password manager written in Python 3.13 and Tkinter, built as the
assignment of days 29 and 30 of Udemy's "100 Days of Code: The Complete Python
Pro Bootcamp". The application generates passwords, saves them with a website
and an e-mail address in a JSON file, handles a missing or empty data file
without crashing, and searches the saved data for a website. The repository is
meant to be read, run and compared by other course participants, so it keeps
the assignment's function names, has no runtime dependencies and ships a README
and a wiki in English, Danish and Bahasa Malaysia.

## Methodological and Standards Foundation

- Larman, *Applying UML and Patterns*: planning-first, small iterations, the
  artifact chain of the framework mounted at `framework/`.
- ISO/IEC 25010:2023 characteristics tag every quality criterion.
- Clean Architecture layering and MVVM for the user interface
  (`clean-architecture` skill).
- Python conventions of the `coding-conventions` skill; Doxygen comments in
  the source.

## Problem Statement

The course's earlier version of the program stores passwords in a plain text
file. A text file cannot be searched by website, is hard to update without
rewriting the whole file and breaks the program when it is missing. A course
participant who wants to compare solutions also has no reference repository
that shows the finished assignment together with tests and set-up
instructions.

## Business Opportunity

A small, tested, documented reference solution lets other participants verify
their own work, and shows the author's engineering practice to anyone who
browses the repository.

## Objectives

1. O1: Store each saved entry as a nested key-value record (website, e-mail,
   password) in a JSON file.
2. O2: Keep the program running when the data file is missing, empty or invalid
   by creating or repairing it.
3. O3: Let the user search the saved data by website and see the e-mail and
   password, or a clear message when nothing is found.
4. O4: Publish the work as a runnable, tested and documented repository with a
   description, topics, a README and a three-language wiki with screenshots.

## Scope

### In Scope

- Password generation, saving to JSON, searching by website.
- Exception handling for a missing, empty or invalid data file.
- A Tkinter window with the assignment's fields and buttons.
- `pyproject.toml`, pytest tests, `constants.py`, a Python `.gitignore`, a
  Doxyfile and Doxygen comments.
- README, a wiki in English, Danish and Bahasa Malaysia, and screenshots.
- Repository description and topics on the git host.
- Instructions for a local `.venv` and `python -m pip install --upgrade pip`.

### Out of Scope

- Encryption of the stored passwords; the file is plain JSON as in the course.
- Editing or deleting saved entries.
- Packaging for PyPI or an installer.
- Any runtime dependency beyond the Python standard library.

## Expected Benefits

### Tangible Benefits

- A runnable program with an automated test suite.
- A README and a three-language wiki a newcomer can follow without help.
- A repository with a description and topics that can be found and understood.

### Intangible Benefits

- Practice of exception handling and JSON in a worked example.
- A worked example of the planning-first framework for a small project.

## Strategic Alignment

The project supports the author's course goal of finishing the 100 Days of Code
bootcamp with reviewable, documented solutions, and the goal of keeping each
day's project as a self-contained repository.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Entries are stored as nested JSON | 100 % of saves produce valid JSON that `json.load` reads back | pytest test of the storage module |
| 2 | A missing, empty or invalid data file does not crash the program | 3 of 3 cases handled, each covered by a test | pytest tests |
| 3 | A search for a saved website returns its e-mail and password; an unknown website gives a message | 2 of 2 cases covered by tests | pytest tests |
| 4 | The test suite passes on Python 3.13 | 0 failures | `python -m pytest` |
| 5 | The project has no runtime dependencies | 0 entries in `dependencies` of `pyproject.toml` | file inspection |
| 6 | The wiki exists in three languages with the same page set | 3 languages, same pages, every page has a screenshot or a reason it has none | `check-languages.sh` and file listing |
| 7 | The repository has a description and at least 5 topics | description set, topics >= 5 | git host API read |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Plain-text storage of passwords is mistaken for a secure design | Readers copy an insecure pattern | README and wiki state in a Security note that the file is unencrypted and for learning only |
| The author's token in `.env` is committed or printed | Credential leak | `.env` is in `.gitignore`, is never imported by the program and is never echoed |
| Tkinter is missing on a reader's Python | The window does not start | README lists Tkinter as a requirement and the logic is testable without the window |
| Danish or Bahasa Malaysia translation errors | Misleading instructions | Code blocks and commands stay English; English is the authoritative text |
| Screenshots become outdated | Docs disagree with the program | Screenshots are produced by a documented step in the last milestone |

## Assumptions

- Python 3.13 or newer is installed on the reader's machine.
- Tkinter ships with the reader's Python.
- The git host `git.tirsystem.com` is reachable and the token in `.env` can edit
  repository metadata and open pull requests.
- S01 can act as reviewer of every artifact, as stand-in in autonomous mode.

## Constraints

- Python 3.13 or newer; `venv` for the environment; pytest for tests.
- Folder structure `src/`, `tests/`, `docs/`.
- Constants live in `constants.py`.
- No runtime dependencies unless needed.
- Work is done on branches and pull requests, one per milestone.
- Tokens are read from `.env`, which is neither tested nor imported.

## Cost–Benefit Assessment

The assessment is qualitative: the project is an unpaid learning exercise with
no revenue, and the cost is the author's time.

| Costs | Benefits |
| --- | --- |
| About three working sessions of the author's time | A complete, reviewed reference solution |
| Effort to keep three wiki languages in step | Readable by English, Danish and Malay speaking participants |
| Effort to maintain tests and documentation | A reliable program and a repeatable set-up |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Finish the assignment, own the result and review it |
| S02 | Readable, runnable code with the assignment's function names and run instructions |
| S03 | A clear description, topics and README, and no runtime dependencies |

## Recommendation

Proceed — the scope is small, every objective is verifiable by a test or a file
check, and the risks have mitigations.

---

[SA-001]: ./stakeholder-analysis.md
[53f56ee]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/commit/53f56eeb143d810b91da23f743a53a32207f81bb
