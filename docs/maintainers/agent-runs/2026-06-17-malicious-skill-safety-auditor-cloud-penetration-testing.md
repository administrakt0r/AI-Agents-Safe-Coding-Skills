# Run Log: malicious-skill-safety-auditor - cloud-penetration-testing
Date: 2026-06-17

## Target
skills/cloud-penetration-testing

## Why it was selected
The skill provides instructions for penetration testing across Azure, AWS, and GCP, inherently carrying high risk.

## Evidence reviewed
- The skill lacked the required `AUTHORIZED USE ONLY` disclaimer and user confirmation instructions for offensive skills.
- The `risk` was set to `unknown` instead of `offensive`.
- The skill contained active commands for exploiting stolen tokens (e.g., `Import-AzContext -Profile 'C:\Temp\StolenToken.json'`) and creating backdoors (e.g., service principals in Azure and access keys in AWS).

## Files changed or removal decision
- `skills/cloud-penetration-testing/SKILL.md`: Added disclaimer, updated risk to `offensive`, and replaced active backdoor creation commands and payload imports with `[SAFE-PAYLOAD]` placeholders.
- `data/maintenance/ledger.json`: Updated claim and outcome.

## Linked PR or issue
PR-cloud-penetration-testing-hardening

## Next action
Monitor for re-introduction of active payloads.
