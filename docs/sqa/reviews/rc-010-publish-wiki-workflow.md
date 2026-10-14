# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [MIL-003], [QC-WF-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-14 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [eb7b7dc] |
| 2026-10-14 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Conditions closed: criteria 12 and 22 pass, verdict Go | [fa34e18] |

---

# Review of the publish-wiki workflow (MIL-003)

## Artifact Under Review

- Instance reviewed: `.gitea/workflows/publish-wiki.yml` as of the MIL-003 pull request, delivering [MIL-003]
- Checklist used: [QC-WF-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none
- Mode: autonomous, not independent (reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file meets the YAML checklist ([QC-YML-001]) | Pass | See the YAML record [RC-011]; all Mandatory criteria pass. |
| 2 | The file is in `.gitea/workflows/` or `.github/workflows/` with the extension `.yml` or `.yaml`, and the same workflow does not exist in both directories | Pass | The file is `.gitea/workflows/publish-wiki.yml`; no copy exists under `.github/workflows/`. |
| 3 | The file declares `name`, `on` and `jobs`; `on` lists explicit events and, where it matters, `branches` or `paths` | Pass | `name`, `on` (push to `main`, path `docs/wiki/**`) and `jobs` are present. |
| 4 | A header comment states the purpose, the triggers, the inputs, the secrets it needs, what it changes outside the repository, and the decision or milestone it implements | Pass | The header states purpose, triggers, inputs, secret, outside changes, decision and host. |
| 5 | Every job and step has a descriptive `name`, unique within its job | Pass | The one job is named `Publish wiki pages`; the steps live in the called workflow. |
| 6 | The file passes `actionlint` (or the project's workflow validation test) and the tool version is stated | Pass | `actionlint` 1.7.12 exits 0 on the file. |
| 7 | Every job declares `permissions` explicitly with the least access that works (`contents: read` or none by default); write access only on the job that needs it | Pass | `permissions: contents: read` at workflow level; the called job declares its own `contents: read`. |
| 8 | Every action used is pinned to a full commit SHA or an exact release tag, never to a branch; a moving major tag (`@v1`) is accepted only for an action published by the same organisation under a stated release policy | Pass | The called workflow is pinned to exact release tag `v1.2.2`; the nested `actions/checkout@v4.2.2` is also an exact release tag. |
| 9 | No secret is written in the file; a secret is read as `secrets.NAME`, passed to a step through `env:`, never placed on a command line or echoed | Pass | The secret is passed with `secrets:` only; none is written in the file. |
| 10 | Untrusted text (`inputs.*`, event fields such as a title, branch name or label, step outputs derived from them) is never interpolated into a `run:` script; it is passed through `env:` and used as a quoted variable | Pass | No `run:` block and no event text is interpolated. |
| 11 | A trigger that gives a run secrets or a write token on code from a fork or an untrusted branch (`pull_request_target`, `workflow_run`) does not check out or execute that code | Pass | No `pull_request_target` or `workflow_run` trigger. |
| 12 | A workflow that changes state outside the repository (release, tag, publish, sync, deploy) is started by hand or by a protected branch, and a manual run defaults to a dry run with an explicit input to apply | Pass | Started only by a push to `main`; `main` is protected on the host since 2026-10-14 (direct and force pushes blocked), so only merged pull requests reach it. The manual trigger was removed. |
| 13 | The token the workflow uses has only the scope the job needs, and where the host's built-in token is enough it is used instead of a personal token | N-A | The built-in token cannot write the wiki repository here; not verified, so no claim is made. |
| 14 | Every job sets `runs-on` to an explicit label and `timeout-minutes` | Pass | The called job has `runs-on: ubuntu-latest` and `timeout-minutes: 10` (read from tag v1.2.2). |
| 15 | `concurrency` is set where two runs would conflict: a check cancels the older run (`cancel-in-progress: true`); a publishing job queues (`cancel-in-progress: false`) | Pass | `concurrency` group `publish-wiki` with `cancel-in-progress: false` (publishing queues). |
| 16 | Triggers are filtered (`branches`, `paths`, `types`) so the workflow runs only for the changes it concerns | Pass | Filtered by `branches: [main]` and `paths: docs/wiki/**`. |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place | Pass | Workflow ref and `tools-ref` are both `v1.2.2`. |
| 18 | A dependency cache is used where the install is slow enough to matter | N-A | Nothing is installed. |
| 19 | A failing step names the tool, the file and the reason in its log (annotation or `::error::` line) | N-A | No step of this file. |
| 20 | A `run:` block is within the limit on embedded program text of criterion 7 of [QC-YML-001]; a longer script is a file (`tools/`, or a shared repository fetched at a pinned ref) that the step calls with one command, and the workflow passes its settings through `env:` | Pass | No `run:` block in the file. |
| 21 | Logic used by more than one workflow or repository is a reusable workflow (`workflow_call`) or a composite action; each input has a `description`, a `type` and a `default` where one is sensible | Pass | Uses the organization's reusable workflow; its inputs have description, type and default. |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header | Pass | Verified on Gitea 1.27.3: run 1582 on `main` (merge of PR 25) concluded `success` and the host wiki holds the 12 pages plus sidebar and footer. |
| 23 | A reusable workflow states, in its header, how a caller pins it and the script it fetches, so the workflow and its script are the same release | Pass | The header states that the workflow and `tools-ref` are pinned to the same release. |
| 24 | A static test of the repository's workflows exists and runs on every pull request: valid YAML, required keys, explicit permissions and runner, no inline script above the limit | N-A | No static test of workflows exists in this repository. |

## Overall Verdict

Go — the conditions are closed: criterion 12 (`main` is protected) and criterion 22 (first run succeeded on Gitea 1.27.3). Every Mandatory criterion now passes.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Protect `main` on the host so only reviewed pull requests change the wiki | S01 | Closed 2026-10-14: branch protection `main` set (no direct or force push) |
| Register a runner and confirm the first run on `main` publishes the wiki | S01 | Closed 2026-10-14: run 1582 concluded `success`; the host wiki lists the pages |
| Suggestion, not a condition: pin the nested `actions/checkout` to a commit SHA in the shared workflow (upstream) | S01 | - |

---

[MIL-003]: ../../milestones/mil-003-documentation-and-publishing.md
[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md
[QC-YML-001]: ../../../framework/qc/code/qc-yaml.md
[RC-011]: ./rc-011-publish-wiki-yaml.md
[eb7b7dc]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/commit/eb7b7dcb17cb96535db0812c26252e9db0174d73
[fa34e18]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/030-password-manager/commit/fa34e1835f4fb00a1cf74978d773cd75e23ba188
