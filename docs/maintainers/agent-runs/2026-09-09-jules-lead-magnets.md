# Agent Run: Import lead-magnets skill

- **Target**: coreyhaines31/marketingskills/lead-magnets
- **Why it was selected**: High value lead magnet planning skill for marketing, complying with the english-only policy and safety checks.
- **Dedup check result**: Checked open PRs using `gh pr list --state open --limit 200 --json number,title,headRefName || git branch -a`. No existing PR for lead-magnets found.
- **Prompt injection scan result**: Clean. Read full file using `sed` and found no red flags like "ignore previous instructions" or base64.
- **Evidence reviewed**: Checked full SKILL.md contents and English-only candidates.
- **Files changed**: `skills/lead-magnets/SKILL.md`, `data/maintenance/ledger.json`, `docs/maintainers/agent-runs/2026-09-09-jules-lead-magnets.md`
- **Linked PR/Issue**: PR-jules-import-lead-magnets
- **Next action**: Monitor the imported skill for upstream updates.
