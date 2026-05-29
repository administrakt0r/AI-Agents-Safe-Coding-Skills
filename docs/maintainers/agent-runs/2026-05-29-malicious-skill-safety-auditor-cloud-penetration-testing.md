# Agent Run: malicious-skill-safety-auditor

## Target
skills/cloud-penetration-testing

## Why it was selected
This skill contained explicit malicious strings including reverse shell parameters, persistence backdoor creation code, and active exploit commands but lacked the `AUTHORIZED USE ONLY` disclaimer and was missing the `offensive` risk tag.

## Risk evidence reviewed
- Backdoor service principal creation (`New-AzAdServicePrincipal`)
- Malicious backdoor access key creation (`aws iam create-access-key`)
- Backdoor user creation (`az ad user create`)
- O365 Password spraying scripts using `Invoke-MSOLSpray` and `Connect-AzAccount` loops

## Files changed
- `skills/cloud-penetration-testing/SKILL.md`: Added offensive tags and disclaimer. Replaced Phase 5, Phase 9, Phase 11, and Example 1 active payloads with safe placeholders.
- `skills/cloud-penetration-testing/references/advanced-cloud-scripts.md`: Replaced password spraying script and service principal attack path payloads with safe placeholders.

## Linked PR or issue
PR-cloud-penetration-testing-hardening

## Next action
Monitor for re-introduction of active payloads.
