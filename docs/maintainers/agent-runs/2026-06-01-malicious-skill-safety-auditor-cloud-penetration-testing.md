# Run Log: 2026-06-01

- **Target:** `skills/cloud-penetration-testing`
- **Why it was selected:** Unclaimed high-risk skill containing potentially offensive and dangerous commands to test cloud environments.
- **Evidence reviewed:** Found real attack payloads, password spraying scripts, and malicious commands such as creating backdoor service principals, access keys, and remote script execution. The risk tag in the frontmatter was `unknown`.
- **Files changed or removal decision:** Hardened `skills/cloud-penetration-testing/SKILL.md` and `skills/cloud-penetration-testing/references/advanced-cloud-scripts.md` by replacing the malicious payloads with safe placeholders (`# [SAFE-PAYLOAD] echo 'Simulating...'`). Updated risk tag to `offensive`. Added the required offensive disclaimer and user confirmation requirements.
- **Linked PR or issue:** PR-cloud-penetration-testing-hardening
- **Next action:** Monitor for re-introduction of active payloads.
