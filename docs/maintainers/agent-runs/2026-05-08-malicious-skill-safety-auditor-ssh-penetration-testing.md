# Run Log: 2026-05-08

## Selected skill
`skills/ssh-penetration-testing`

## Risk evidence reviewed
The skill contained instructions with active network payloads for establishing reverse shell connections and modifying user configurations for backdoor persistence.

## Files changed
- `skills/ssh-penetration-testing/SKILL.md`: Redacted active reverse shell callback (`ssh -R 4444...`) and persistence payloads (`echo "ssh-rsa..." >> ~/.ssh/authorized_keys`) with safe placeholders (`[REDACTED_REVERSE_SHELL_PAYLOAD]` and `[REDACTED_PERSISTENCE_PAYLOAD]`).
- `data/maintenance/ledger.json`: Claimed the skill and recorded the hardening outcome.

## Linked PR/issue
PR-ssh-penetration-testing-hardening

## Next action
Monitor for re-introduction of active payloads.
