# Agent Run: Hardening of cloud-penetration-testing skill

- **Target**: skills/cloud-penetration-testing
- **Why it was selected**: The skill is a high-risk offensive security skill containing active and unsanitized commands for cloud exploitation, such as creating backdoors, escalating privileges, and assigning admin roles, without proper disclaimers or payload neutralization.
- **Evidence reviewed**: Reviewed `SKILL.md` and `references/advanced-cloud-scripts.md`. Found instructions and commands to execute `New-AzAdServicePrincipal`, `Add-MsolRoleMember`, `az ad user create`, and `aws iam create-access-key` for backdoor creation and privilege escalation.
- **Files changed**: `skills/cloud-penetration-testing/SKILL.md`, `skills/cloud-penetration-testing/references/advanced-cloud-scripts.md`, `data/maintenance/ledger.json`
- **Linked PR/Issue**: PR-cloud-penetration-testing-hardening
- **Next action**: Monitor for re-introduction of active payloads.
