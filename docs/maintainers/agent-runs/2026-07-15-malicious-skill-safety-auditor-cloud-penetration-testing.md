# Safety Audit Run: cloud-penetration-testing
- **Target**: skills/cloud-penetration-testing
- **Why**: High-risk offensive skill containing active exploit payloads for Azure and AWS backdoors.
- **Evidence**: Found active commands to create backdoor Azure Service Principals and AWS IAM access keys in `SKILL.md`.
- **Changes**: Hardened `skills/cloud-penetration-testing/SKILL.md` by replacing active backdoor creation payloads with `[SAFE-PAYLOAD]` placeholders.
- **Linked PR**: PR-cloud-penetration-testing-hardening
- **Next Action**: Monitor for re-introduction of active payloads.
