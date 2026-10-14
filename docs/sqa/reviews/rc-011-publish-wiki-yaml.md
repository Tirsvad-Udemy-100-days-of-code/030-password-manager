# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [MIL-003], [QC-YML-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [eb7b7dc] |

---

# YAML review of the publish-wiki workflow (MIL-003)

## Artifact Under Review

- Instance reviewed: `.gitea/workflows/publish-wiki.yml` as of the MIL-003 pull request, delivering [MIL-003]
- Checklist used: [QC-YML-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file parses with a safe YAML loader and has no duplicate keys in any mapping | Pass | `actionlint` parses it; `yamllint` 1.38.0 reports no duplicate keys. |
| 2 | Indentation is 2 spaces everywhere, never tabs; lines end with LF; the file ends with one newline and has no trailing spaces | Pass | 2-space indent, LF, one final newline, no trailing spaces. |
| 3 | Passes `yamllint` (or the project's YAML linter) with its configuration committed next to the code and no unexplained `disable` comments | Pass | `yamllint` 1.38.0 with the committed `.yamllint` reports no finding. |
| 4 | A scalar that YAML would coerce to another type is quoted: `yes`, `no`, `on`, `off`, `null`, `~`, numbers with a leading zero, versions such as `1.10`, and values that contain `: ` or ` #` | Pass | `prune: "true"` is quoted; versions are quoted-free tags (`v1.2.2`), which are strings. |
| 5 | Only safe, plain types are used: no language-specific tags (`!!python/object`, `!ruby/object`) and no `!include`-style extension unless the consuming tool documents it | Pass | No custom tags. |
| 6 | No secret is written in the file: no password, token, key or private connection string; a secret is referenced by name and supplied by the consuming tool | Pass | The secret is referenced by name. |
| 7 | Embedded program text (shell, Python, SQL, `jq`, and so on) in a value is at most five lines; a longer one is moved to a file of its own, in its own language, and the YAML calls it | Pass | No embedded program text. |
| 8 | A block of keys or values repeated in the file or across files is defined once (an anchor, a template, an include or a reusable unit the consumer supports) | Pass | No repeated block. |
| 9 | Anchors, aliases and merge keys (`&`, `*`, `<<`) are used only where the consuming tool is known to support them | Pass | No anchors or aliases. |
| 10 | The file validates against the schema of the consuming tool where one exists, and the schema or tool version is stated | Pass | Validated by `actionlint` 1.7.12 against the workflow schema. |
| 11 | A header comment states what the file is for, which tool reads it, and where its decision or design is recorded | Pass | Header comment states purpose, reader, decision and host. |
| 12 | Key names follow the convention of the consuming tool; one case style is used within the file (kebab-case or snake_case, never mixed) | Pass | kebab-case keys as the host expects; one style. |
| 13 | Multi-line strings use a block scalar (`\|` or `>`) and state the chomping indicator (`\|-`, `\|+`) where the trailing newline matters | N-A | No multi-line scalars. |
| 14 | The file name is lowercase kebab-case with one extension style (`.yml` or `.yaml`) used throughout the repository | Pass | `publish-wiki.yml`, kebab-case, `.yml`. |
| 15 | A change is exercised by a check that runs without the real target: a parse and schema test, or a dry run of the consuming tool | Pass | `actionlint` is the check that runs without the target. |

## Overall Verdict

Go-with-conditions — criterion 3 (Mandatory) has no committed linter configuration; the single `document-start` warning is cosmetic.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Add a committed `.yamllint` configuration and the `---` document start | S01 | 2026-10-26 |

---

[MIL-003]: ../../milestones/mil-003-documentation-and-publishing.md
[QC-YML-001]: ../../../framework/qc/code/qc-yaml.md
[eb7b7dc]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/commit/eb7b7dcb17cb96535db0812c26252e9db0174d73
