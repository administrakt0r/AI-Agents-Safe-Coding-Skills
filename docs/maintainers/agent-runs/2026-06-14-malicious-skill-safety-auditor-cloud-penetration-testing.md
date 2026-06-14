# Run Log: cloud-penetration-testing

- **Target:** `skills/cloud-penetration-testing`
- **Why it was selected:** Unclaimed high-risk offensive skill.
- **Evidence reviewed:** Discovered lack of the required offensive disclaimer and explicit confirmation. Found active exploit commands like service principal backdoor creation (`New-AzAdServicePrincipal`), password spraying (`Invoke-MSOLSpray`), access key creation (`aws iam create-access-key`), and S3 bucket syncing (`aws s3 sync`). Found similar issues in the referenced `advanced-cloud-scripts.md` document.
- **Files changed or removal decision:**
  - `skills/cloud-penetration-testing/SKILL.md`: Added `AUTHORIZED USE ONLY` disclaimer, set risk to `offensive`, added mandatory user confirmation, and replaced active exploitation payloads with `[SAFE-PAYLOAD]` placeholders.
  - `skills/cloud-penetration-testing/references/advanced-cloud-scripts.md`: Replaced password spraying, credential resetting, and privilege escalation commands with safe placeholder simulations.
- **Linked PR or issue:** `PR-cloud-penetration-testing-hardening`
- **Next action:** Monitor for re-introduction of active payloads.
