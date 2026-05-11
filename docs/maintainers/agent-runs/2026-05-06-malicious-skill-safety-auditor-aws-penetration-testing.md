# Run Log: Malicious Skill Safety Auditor - aws-penetration-testing

## Selected skill
`skills/aws-penetration-testing`

## Risk evidence reviewed
The skill documentation and advanced reference (`references/advanced-aws-pentesting.md` and `SKILL.md`) included multiple active, executable malicious payloads that could cause harm.
Specific findings:
- Active payload to upload backdoors to AWS Lambda functions (`fileb://backdoor.zip` and `fileb://malicious.zip`).
- Active Remote Code Execution (RCE) payload links pointing to malicious web resources (`https://website.com/rce.php?cmd=ls /var/run/secrets/kubernetes.io/serviceaccount` and `https://website.com/rce.php?cmd=cat /var/run/secrets/kubernetes.io/serviceaccount/token`).
- Executable bash script instruction that directly interacts with the host filesystem to mount volumes associated with an EBS Shadow Copy Attack (`sudo mount /dev/xvdf1 /mnt/stolen`).

## Files changed
- `skills/aws-penetration-testing/references/advanced-aws-pentesting.md`: Replaced Lambda backdoor zip file and active web RCE payload with safe placeholders (`[REDACTED_LAMBDA_BACKDOOR_PAYLOAD]`, `[REDACTED_RCE_PAYLOAD]`).
- `skills/aws-penetration-testing/SKILL.md`: Replaced malicious Lambda zip file and mount command with safe placeholders (`[REDACTED_MALICIOUS_LAMBDA_PAYLOAD]`, `[REDACTED_MOUNT_COMMAND]`).

## Linked PR/issue
PR-aws-penetration-testing-hardening

## Next action
Monitor for re-introduction of active payloads.
