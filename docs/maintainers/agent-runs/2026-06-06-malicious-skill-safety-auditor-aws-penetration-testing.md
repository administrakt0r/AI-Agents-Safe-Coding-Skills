# Run Log: malicious-skill-safety-auditor
Date: 2026-06-06
Target: skills/aws-penetration-testing

## Why it was selected
The skill is an unclaimed high-risk skill containing malicious prompt engineering, unsafe commands, and suspicious scripts.

## Evidence reviewed
- `skills/aws-penetration-testing/SKILL.md` missing offensive risk tag and authorization warning.
- `skills/aws-penetration-testing/SKILL.md` containing active `fileb://malicious.zip` lambda payload.
- `skills/aws-penetration-testing/references/advanced-aws-pentesting.md` containing active malicious lambda code and backdoored docker container instructions.

## Files changed or removal decision
- Modified `skills/aws-penetration-testing/SKILL.md` to add offensive tag and AUTHORIZED USE ONLY warning.
- Modified `skills/aws-penetration-testing/SKILL.md` to replace active payload with `[SAFE-PAYLOAD]` placeholder.
- Modified `skills/aws-penetration-testing/references/advanced-aws-pentesting.md` to replace active payloads with `[SAFE-PAYLOAD]` placeholders.

## Linked PR or issue
PR-aws-penetration-testing-hardening

## Next action
Monitor for re-introduction of active payloads.
