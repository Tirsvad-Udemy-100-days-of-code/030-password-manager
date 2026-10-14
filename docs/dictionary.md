# Password Manager Domain Dictionary

## Metadata
| Key | Value |
| --- | --- |
| ID | DICT-001 |
| CrossReference | [BC-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [53f56ee] |

---

## Purpose and Scope

Maps each Product Owner (PO) term of the password manager to its professional
IT term. PO language: English (`en`); domain: `it`. The dictionary covers the
words used in the Business Case, the Stakeholder Analysis, the Project Plan and
the milestones, and the names used in the Python source.

## Dictionary

| PO term | Language | IT term | Definition | Used as PO term in | Used as IT term in |
| --- | --- | --- | --- | --- | --- |
| Password entry | en | Credential record | One saved website with its e-mail address and password. | BC, SA, PP, MIL | PY |
| Password file | en | JSON data file | The file on disk that holds every password entry as nested key-value data. | BC, SA, PP, MIL | PY |
| Search | en | Lookup | Finding the password entry of a website by its name. | BC, SA, PP, MIL | PY |
| Password generator | en | Random string generator | The function that creates a random password of letters, digits and symbols. | BC, PP, MIL | PY |
| Window | en | Tkinter view | The graphical form where the user types, searches and saves. | BC, SA, PP, MIL | PY |
| Missing file | en | FileNotFoundError | The condition where the password file does not exist yet. | BC, PP, MIL | PY |
| Empty or damaged file | en | JSONDecodeError | The condition where the password file exists but holds no valid JSON. | BC, PP, MIL | PY |

## Rules

- The Business Case, Stakeholder Analysis, Project Plan and milestones use the
  PO term; the Python source, its docstrings and its tests use the IT term.
- One IT term per PO term and one PO term per IT term; no synonyms.
- The Domain Model does not exist in this project (no use case is modelled), so
  the dictionary holds the terms of the documents that exist.

---

[BC-001]: ./business-case.md
[SA-001]: ./stakeholder-analysis.md
[53f56ee]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/commit/53f56eeb143d810b91da23f743a53a32207f81bb
