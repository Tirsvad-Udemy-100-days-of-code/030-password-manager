# Password Manager Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [53f56ee] |

---

## Purpose

Tracks backward and forward links between artifact instances so that the
Business Case's traceability can be checked. A row is added or updated whenever
an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001], [DICT-001] | [RC-001] |
| [SA-001] | SA | en | it | [BC-001] | [PP-001], [DICT-001] | [RC-002] |
| [DICT-001] | DICT | en | it | [BC-001], [SA-001] | - | [RC-003] |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003] | - |
| [MIL-001] | MIL | en | it | [BC-001], [PP-001] | [MIL-002] | [RC-004] |
| [MIL-002] | MIL | en | it | [BC-001], [MIL-001] | [MIL-003] | [RC-005] |
| [MIL-003] | MIL | en | it | [BC-001], [MIL-002] | - | [RC-006] |

## Coverage Notes

- `-` in Upstream means foundational; in Downstream it means nothing is built
  on it yet; in Last Reviewed it means no `RC-*` exists. The Project Plan has
  no QC checklist; the Product Owner accepted it in chat.
- No KPI, use case, user story or design artifact exists: the project models
  its tasks as plain technical tasks (see the Project Plan's Open Issues).
- Code reviews (`PY`) are added by the milestones that produce code.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[DICT-001]: ../dictionary.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-foundation.md
[MIL-002]: ../milestones/mil-002-password-manager-features.md
[MIL-003]: ../milestones/mil-003-documentation-and-publishing.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-dictionary.md
[RC-004]: ./reviews/rc-004-mil-001.md
[RC-005]: ./reviews/rc-005-mil-002.md
[RC-006]: ./reviews/rc-006-mil-003.md
[53f56ee]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/commit/53f56eeb143d810b91da23f743a53a32207f81bb
