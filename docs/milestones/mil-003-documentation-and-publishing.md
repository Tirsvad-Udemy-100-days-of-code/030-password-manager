# Documentation and Publishing

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

# Documentation and Publishing

## Purpose

Decide whether the project can be handed to course participants (S02) and repository visitors (S03): screenshots, README and a wiki in three languages.

## Deliverable

Screenshots of the running window under `docs/images/`, a README that shows them, a wiki under `docs/wiki/` in English, Danish (`-da`) and Bahasa Malaysia (`-ms`) with the same pages, a publish-wiki workflow and a passing framework check.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `docs/images/` holds at least 2 screenshots of the real window | 2 or more PNG files | Fewer |
| 2 | README embeds a screenshot and still passes `check-readme.sh` | Both true | Either false |
| 3 | Every wiki page exists in `en`, `da` and `ms` with the same page set | Page sets equal | Any page missing |
| 4 | Every wiki page starts with the language switch line | All pages | Any page without |
| 5 | `bash framework/scripts/check-languages.sh` exits 0 | Exit 0 | Any finding |
| 6 | `python -m pytest` still passes | 0 failures | Any failure |

## Dependencies

| Depends on | Reason |
| --- | --- |
| MIL-002 | A finished, running program is needed to take screenshots |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| BC-001 O4; Success criteria 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in, autonomous mode) |

## Target Date

2026-10-19 — follows MIL-002 by two days, within the Business Case constraints.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Capture screenshots of the application | Run the window with sample data, capture the main window, a successful search and a not-found message into `docs/images/` and record the capture steps so they can be repeated. | No | |
| 2 | Add the screenshots to the README | Embed the main-window screenshot in `README.md` with alternative text so S02 and S03 see the result before they run it. | No | |
| 3 | Write the English wiki | Write Home, Installation, Usage and Development pages in `docs/wiki/` with `_Sidebar.md` and `_Footer.md`; English is the authoritative text. | No | |
| 4 | Write the Danish wiki | Translate every English page to Danish as `<Page>-da.md`, keeping code blocks, commands and file names in English. | No | |
| 5 | Write the Bahasa Malaysia wiki | Translate every English page to Bahasa Malaysia as `<Page>-ms.md`, keeping code blocks, commands and file names in English. | No | |
| 6 | Add the publish-wiki workflow | Copy `framework/templates/ci/publish-wiki.yml` to the host's workflow folder so the wiki reaches the host's wiki after the merge. | No | |
| 7 | Run the framework and final checks | Run `check-readme.sh`, `check-languages.sh`, the test suite and record the final review so the milestone has its evidence. | No | |

---

[BC-001]: ../business-case.md
