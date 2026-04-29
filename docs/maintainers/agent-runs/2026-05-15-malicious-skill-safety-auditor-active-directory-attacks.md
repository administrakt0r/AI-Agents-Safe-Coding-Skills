# Maintenance Run Log

**Date:** 2026-05-15
**Agent:** malicious-skill-safety-auditor
**Target:** skills/active-directory-attacks

## Why it was selected
The `skills/active-directory-attacks` skill is a high-risk security testing skill that includes active exploitation commands, making it a candidate for safety review.

## Evidence reviewed
- `skills/active-directory-attacks/SKILL.md` contained an active exploit payload `\\attacker\share\evil.dll` for CVE-2021-1675.
- `skills/active-directory-attacks/references/advanced-attacks.md` contained active system execution and backdoor creation commands, such as `net user backdoor Password123! /add` and `evil.exe`.

## Files changed or removal decision
- Hardened `skills/active-directory-attacks/SKILL.md` by replacing the active `evil.dll` payload with `[REDACTED_PAYLOAD].dll`.
- Hardened `skills/active-directory-attacks/references/advanced-attacks.md` by replacing active system execution and backdoor creation commands with safe placeholders (`[REDACTED_SYSTEM_EXECUTION_PAYLOAD]` and `[REDACTED_PAYLOAD].exe`).
- Updated `data/maintenance/ledger.json` to record the outcome.

## Linked PR or issue
PR-active-directory-attacks-hardening

## Next action
Monitor for re-introduction of active payloads.
