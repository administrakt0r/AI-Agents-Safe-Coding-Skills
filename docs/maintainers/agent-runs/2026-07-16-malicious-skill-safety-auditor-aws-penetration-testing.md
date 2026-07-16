# Run Log: AWS Penetration Testing Hardening

**Selected skill:** skills/aws-penetration-testing

**Risk evidence reviewed:** The skill contains explicit, actionable commands for IAM privilege escalation (attaching AdministratorAccess policy), malicious Lambda zip injection, active S3 bucket finding scripts, and NTDS credential extraction without the necessary "offensive" frontmatter risk label and Authorized Use Only disclaimer.

**Files changed:**
- `skills/aws-penetration-testing/SKILL.md`: Updated risk tag to "offensive", added Authorized Use Only disclaimer, and redacted active privilege escalation and payload execution commands.
- `skills/aws-penetration-testing/references/advanced-aws-pentesting.md`: Redacted backdoored Lambda payloads.
- `data/maintenance/ledger.json`: Updated review status and outcome.

**Linked PR/issue:** PR-aws-penetration-testing-hardening

**Next action:** Monitor for re-introduction of active payloads.
