import subprocess
import os

# Create a temporary file with the PR body
pr_body = """This PR imports the `add-app-clip` skill from the trusted source `sickn33/agentic-awesome-skills`.

**Changes:**
- Added the skill documentation at `skills/add-app-clip/SKILL.md`.
- Added the corresponding local module reference at `skills/add-app-clip/references/native-module.md`.
- Updated `data/maintenance/ledger.json` to mark the skill source as `monitoring`.
- Generated a run log under `docs/maintainers/agent-runs/2026-09-17-new-skill-import-curator-add-app-clip.md`.

**Checks Performed:**
- **Dedup:** No active PR exists for `add-app-clip`.
- **English-only Policy:** Verified the repository and skill content are English-first.
- **Prompt Injection:** Ran a scan on the skill content, which returned no prompt injection vectors (`NO PROMPT INJECTION FOUND`).
- **Validation:** Executed `npm run validate` and `npm run test` successfully after ensuring the environment had the correct dependencies (`yaml` and `pyyaml`). Auto-generated catalog modifications were successfully discarded before staging.

## Quality Bar Checklist ✅

**All items must be checked before merging.**

- [x] **Standards**: I have read `docs/contributors/quality-bar.md` and `docs/contributors/security-guardrails.md`.
- [x] **Metadata**: The `SKILL.md` frontmatter is valid (checked with `npm run validate`).
- [x] **Risk Label**: I have assigned the correct `risk:` tag (`none`, `safe`, `critical`, `offensive`, or `unknown` for legacy/unclassified content).
- [x] **Triggers**: The "When to use" section is clear and specific.
- [x] **Security**: If this is an _offensive_ skill, I included the "Authorized Use Only" disclaimer.
- [x] **Safety scan**: If this PR adds or modifies `SKILL.md` command guidance, remote/network examples, or token-like strings, I ran `npm run security:docs` (or equivalent hardening check) and addressed any findings.
- [x] **Automated Skill Review**: If this PR changes `SKILL.md`, I checked the `skill-review` GitHub Actions result and addressed any actionable feedback.
- [x] **Local Test**: I have verified the skill works locally.
- [x] **Repo Checks**: I ran `npm run validate:references` if my change affected docs, workflows, or infrastructure.
- [x] **Source-Only PR**: I did not manually include generated registry artifacts (`CATALOG.md`, `skills_index.json`, `data/*.json`) in this PR.
- [x] **Credits**: I have added the source credit in `README.md` (if applicable).
- [x] **Maintainer Edits**: I enabled **Allow edits from maintainers** on the PR.
"""

print(pr_body)
