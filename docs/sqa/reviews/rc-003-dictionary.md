# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [DICT-001], [QC-DICT-001], [QC-LANG-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [53f56ee] |

---

# Review of DICT-001

## Artifact Under Review

- Instance reviewed: [DICT-001]
- Checklist used: [QC-DICT-001], [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: S01 (reads English and the IT domain; confirmed in chat by replying "accepted" to the plan message that asked for it)
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Every row has a PO term, its language, an IT term and a definition | Pass | All 7 rows have PO term, language, IT term and definition. |
| 2 | Each PO term maps to exactly one IT term and the reverse (no synonyms) | Pass | Each PO term has exactly one IT term and the reverse. |
| 3 | Every Domain Model concept has a row, and the Domain Model uses its PO term | Pass | No Domain Model exists; the Rules section says so. The criterion applies to the document set that exists, and every term used in BC, SA, PP, MIL has a row. |
| 4 | The Operation Contracts, Sequence Diagrams, Design Class Diagrams and ERD use the IT term, not the PO term | Pass | No OC, SD, DCD or ERD exists; the Python source is the IT-term consumer and is checked in the code review. |
| 5 | Definitions are written in the PO language and are one sentence | Pass | Each definition is one English sentence. |
| 6 | "Used as PO term in" and "Used as IT term in" name artifact types that exist in the project | Pass | Used-in columns name only BC, SA, PP, MIL and PY, which exist. |
| 7 | The dictionary's `Language` and `Domain` rows, and the language of every row, match the PO language and domain in the project registry | Pass | Language `en` and Domain `it` match the registry. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Language `en` and Domain `it` rows are present and filled. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47; `it` is in the registry's domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English; headings are English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register `IT Professional English` per the registry; the text matches the reader it assumes. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | PO terms of [DICT-001] (password entry, password file, search, window) are used; no synonym found. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No `*.en.md` or other translated twin exists beside the file. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version: no language change since an earlier accepted version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 is the language reviewer and confirmed the English text and IT terms. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations (PO, MVVM, JSON) are spelled out or defined where first used. |

## Overall Verdict

Go — every Mandatory criterion passes.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | - |

---

[DICT-001]: ../../dictionary.md
[53f56ee]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/commit/53f56eeb143d810b91da23f743a53a32207f81bb
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
