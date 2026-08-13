# Agent Run: malicious-skill-safety-auditor

- **Target**: `skills/cloud-penetration-testing`
- **Why it was selected**: Selected by `malicious-skill-safety-auditor` as a high-risk offensive skill containing actionable payloads for cloud service exploitation, privilege escalation, and data exfiltration.
- **Evidence reviewed**: Checked `skills/cloud-penetration-testing/SKILL.md` and `skills/cloud-penetration-testing/references/advanced-cloud-scripts.md` for functional cloud exploitation techniques and unauthorized access commands. Checked `data/maintenance/ledger.json` for current status.
- **Files changed**:
  - `skills/cloud-penetration-testing/SKILL.md`: Redacted actionable commands for privilege escalation, persistence, secret retrieval, metadata exfiltration, and backdoor creation. Updated risk frontmatter to `offensive` and added an Authorized Use Only warning block.
  - `skills/cloud-penetration-testing/references/advanced-cloud-scripts.md`: Redacted commands for data exfiltration via runbooks, managed identity tokens exfiltration, and active service principal attack paths.
  - `data/maintenance/ledger.json`: Updated claim status to `normalized` and recorded run outcome.
- **Linked PR/Issue**: `PR-cloud-penetration-testing-hardening`
- **Next action**: Monitor for re-introduction of active payloads.
