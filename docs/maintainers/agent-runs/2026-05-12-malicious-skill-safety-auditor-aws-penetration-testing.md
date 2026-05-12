# Run Log: Malicious Skill Safety Auditor - aws-penetration-testing

## Selected target
`aws-penetration-testing`

## Why it was selected
The skill provides instructions and scripts for AWS penetration testing. As a high-risk capability, it must be evaluated for active malicious payloads and tools that could be abused or lead to unsafe behavior.

## Evidence reviewed
- `skills/aws-penetration-testing/SKILL.md`: Found instructions involving an active Lambda privilege escalation payload (`malicious.zip`).
- `skills/aws-penetration-testing/references/advanced-aws-pentesting.md`: Found active Lambda backdooring Python code, a reference to a `backdoor.zip` payload, an RCE payload (`cmd=env`), a file read payload (`cmd=file:///proc/self/environ`), and Kubernetes secrets extraction payloads (`cmd=ls /var/run/secrets/kubernetes.io/serviceaccount` and `cmd=cat /var/run/secrets/kubernetes.io/serviceaccount/token`).

## Files changed or removal decision
Hardened the skill by replacing active payloads and RCE commands with safe placeholders (`[REDACTED_...]` format).
- `skills/aws-penetration-testing/SKILL.md`: Replaced `malicious.zip` with safe placeholder, updated frontmatter risk level to `safe`, and shortened description.
- `skills/aws-penetration-testing/references/advanced-aws-pentesting.md`: Replaced Lambda backdooring Python code, `backdoor.zip`, RCE env command, file read command, and Kubernetes secrets extraction commands with safe placeholders.

## Linked PR or issue
PR-aws-penetration-testing-hardening

## Next action
Monitor for re-introduction of active payloads.