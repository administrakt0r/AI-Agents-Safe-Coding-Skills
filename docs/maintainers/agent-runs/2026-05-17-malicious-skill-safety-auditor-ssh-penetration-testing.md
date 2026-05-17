# Safety Audit Run Log: ssh-penetration-testing

- **Date**: 2026-05-17
- **Agent**: jules
- **Role**: Malicious-skill safety auditor

## Selected skill
`skills/ssh-penetration-testing`

## Risk evidence reviewed
The skill contained an active reverse shell callback payload using `ssh -R` and an active SSH authorized_keys persistence payload.

## Files changed
- `skills/ssh-penetration-testing/SKILL.md`: Redacted reverse shell and persistence payloads.
- `data/maintenance/ledger.json`: Added entry for the audit.

## Linked PR/issue
PR-ssh-penetration-testing-hardening

## Next action
None