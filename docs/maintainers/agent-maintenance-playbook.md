# Agent Maintenance Playbook

This playbook governs recurring autonomous maintenance for `AI-Agents-Safe-Coding-Skills`.

## Scope

Autonomous agents may:

- refresh obsolete skills,
- audit skills for malicious or unsafe behavior,
- import or modernize one new skill at a time,
- enforce the English-only policy for skills and workflows.

Human maintainers remain the merge gate.

## Required Protocol

1. Read [english-only-policy.md](../contributors/english-only-policy.md).
2. Read `data/maintenance/ledger.json`.
3. Read `data/maintenance/english-only-candidates.json`.
4. Read recent logs in `docs/maintainers/agent-runs/`.
5. Select exactly one skill or source for the run.
6. Refuse work that is already `active`, `blocked`, or recently resolved in the ledger.
7. Apply the English-only policy before deeper modernization or safety review work.
8. Perform the scoped change.
9. Update the ledger entry.
10. Write a dated run log.
11. Link the resulting PR or issue for human review.

## One-Skill Rule

- Each run may handle exactly one skill or one upstream source.
- Do not batch multiple stale fixes into one maintenance run.
- Do not start a second skill because the first one looked easy.

## Duplicate-Work Guardrails

- If the ledger says `active`, stop and pick another target.
- If the ledger says `resolved` or `removed` within the recent review window, stop unless there is new evidence.
- If a recent run log already covers the same target and no new upstream change exists, stop.

## Required Ledger Fields

Each target entry in `data/maintenance/ledger.json` must include:

- `status`
- `lastReviewedAt`
- `reviewerAgent`
- `outcome`
- `linkedIssueOrPr`
- `nextAction`

Recommended statuses:

- `active`
- `normalized`
- `reviewed`
- `removed`
- `monitoring`
- `blocked`

## Run Log Format

Create one dated Markdown file in `docs/maintainers/agent-runs/` using:

- `YYYY-MM-DD-agent-name-target.md`

Each log must include:

- target
- why it was selected
- evidence reviewed
- files changed or removal decision
- linked PR or issue
- next action

## Human Review Requirement

- Agents do not self-approve.
- Agents do not declare the library permanently safe or permanently fresh.
- Agents provide evidence, logs, and a handoff for human maintainers.
