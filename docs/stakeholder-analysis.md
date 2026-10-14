# Password Manager Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [53f56ee] |

---

## Purpose

Identify who is affected by the password manager project and what each person
or group needs, so that owners, reviewers and readers can be named by a stable
ID in every other document. The analysis follows the Power/Interest grid
(Mendelow) and maps concerns to FURPS+.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | Finish the assignment correctly and publish a result worth keeping |
| S02 | Udemy coursists | Course participants who share and compare solutions | Udemy 100 Days of Code community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names and instructions to run it |
| S03 | GitHub viewers | Visitors who browse the repository for ideas | Public | LOW | LOW | Monitor | A clear repository description, topics and README, and no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, accepts every artifact and merges
  the work. High power and high interest.
- **Keep Informed (S02):** cannot change the project but cares about the
  result; they are served by the README and the wiki.
- **Monitor (S03):** casual visitors; they are served by the repository
  description, topics and README and need no direct communication.

## Primary Concerns and FURPS+ Mapping

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | The program behaves as the assignment describes | Functionality |
| S01 | The work is planned, reviewed and traceable | Supportability |
| S02 | Function names match the assignment | Functionality |
| S02 | The program runs after following the README | Usability |
| S02 | The code is readable | Supportability |
| S03 | The repository explains itself at first glance | Usability |
| S03 | Nothing extra has to be installed | Performance (installation effort) |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Chat session and pull request review | Once per milestone | Pull request and run summary | MIL-001, MIL-002, MIL-003 |
| S02 | README and wiki | Once, at publication | Run instructions and usage pages in three languages | MIL-003 |
| S03 | Repository description, topics and README | Once, at publication | Description, topics and README | MIL-001, MIL-003 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S02 wants the code to stay close to the course; S01 wants tests and layering | S01, S02 | Keep the assignment's function names in the public module and put structure behind them |
| S03 wants no dependencies; a convenient clipboard copy would need one | S01, S03 | Use Tkinter's own clipboard methods; add no runtime dependency |
| Plain-text storage suits the course but is unsafe for real use | S01, S02, S03 | State the limitation in README and wiki |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Correct behaviour | [BC-001] O1, O2, O3 |
| S01 | Planned and reviewed work | [BC-001] O4 |
| S02 | Function names, run instructions | [BC-001] O3, O4 |
| S03 | Description, topics, README, no dependencies | [BC-001] O4 |

## Sign-Off

Reviewed and signed off by S01 (autonomous mode: AI as stand-in for S01).

---

[BC-001]: ./business-case.md
[53f56ee]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/commit/53f56eeb143d810b91da23f743a53a32207f81bb
