# 🚀 Password Manager

A small Tkinter password manager that generates passwords, saves them in a JSON
file and searches them by website. It is the day 30 assignment of Udemy's
"100 Days of Code: The Complete Python Pro Bootcamp", written for course
participants and for anyone who browses the repository for ideas.

## 📚 Table of Contents

- [Overview](#-overview)
- [Requirements](#-requirements)
- [Setup](#-setup)
- [Run](#-run)
- [Tests](#-tests)
- [License](#-license)
- [Links](#-links)
- [Appendix: Project documents](#-appendix-project-documents)

## 🧭 Overview

The program follows the three lectures of the assignment:

1. **JSON storage.** Each entry is saved as a nested record
   (`website → email, password`) in `data.json` with `json.dump`, and the
   existing data is loaded and updated before a new entry is added.
2. **Exception handling.** A missing, empty or damaged data file does not stop
   the program; the file is created or repaired on the next save.
3. **Search.** Type a website and press **Search** to see the saved e-mail and
   password, or a message when nothing is saved for it.

The assignment's function names are kept: `generate_password`, `save` and
`find_password`.

| Path | What it holds |
| --- | --- |
| `src/password_manager/` | The program: domain rules, use cases, JSON storage and the Tkinter window |
| `src/password_manager/constants.py` | Every constant (file name, labels, messages, password length bounds) |
| `tests/` | The pytest tests |
| `docs/` | Project documents, the Doxygen output folder and the wiki in `docs/wiki/` |
| `Doxyfile` | Doxygen configuration for the source comments |
| `pyproject.toml` | Project configuration (Python version, entry point, pytest) |

> **Security note.** The data file is plain JSON and the passwords are not
> encrypted. The program is a learning exercise; do not use it for real
> passwords.

## 📋 Requirements

- Python 3.13 or newer, with Tkinter (the standard Windows and macOS installers
  include it; on Debian or Ubuntu install `python3-tk`).
- `venv` and `pip`, both part of Python.
- No runtime dependencies. [pytest][pytest] is needed only to run the tests.
- Optional: [Doxygen][doxygen] to build the source documentation.

## 🛠️ Setup

Create and activate a local virtual environment, upgrade `pip`, then install
the project with its test dependency.

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

## ▶️ Run

With the virtual environment active:

```bash
python -m password_manager
```

or, after the install above, `password-manager`. The program creates `data.json`
in the folder you start it from. Build the source documentation with
`doxygen Doxyfile`; the HTML opens at `docs/doxygen/html/index.html`.

## 🧪 Tests

```bash
python -m pytest
```

## 📄 License

See [LICENSE][license].

## 🔗 Links

- [Repository][repository]
- [Documentation][documentation]
- [Issue tracker][issues]

## 📎 Appendix: Project documents

The documents a newcomer needs, in reading order.

| Document | What it tells you |
| --- | --- |
| [Business Case][BC-001] | Why the project exists, its scope and success criteria |
| [Stakeholder Analysis][SA-001] | Who is involved; the stakeholder IDs used for owners and reviewers |
| [Project Plan][PP-001] | The gateways and their schedule |
| [Milestones][milestones] | One document per gateway: Go/No-Go criteria and tasks |
| [Artifact registry][registry] | Where each artifact type lives, the next version, the PO language and domain |
| [Domain dictionary][DICT-001] | The PO terms and the IT terms |
| [Traceability matrix][TM-001] | How the artifacts link and when each was last reviewed |
| [Framework README][framework-readme] | The framework this project uses |
| [Framework changelog][framework-changelog] | What changed in each framework release |

---

[repository]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager
[documentation]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/wiki
[issues]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/issues
[license]: ./LICENSE
[pytest]: https://docs.pytest.org/
[doxygen]: https://www.doxygen.nl/
[BC-001]: ./docs/business-case.md
[SA-001]: ./docs/stakeholder-analysis.md
[PP-001]: ./docs/project-plan.md
[milestones]: ./docs/milestones/
[registry]: ./docs/artifact-registry.md
[DICT-001]: ./docs/dictionary.md
[TM-001]: ./docs/sqa/traceability-matrix.md
[framework-readme]: ./framework/README.md
[framework-changelog]: ./framework/CHANGELOG.md
