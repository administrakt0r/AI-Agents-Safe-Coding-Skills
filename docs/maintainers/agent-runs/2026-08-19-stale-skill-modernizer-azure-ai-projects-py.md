# Agent Run: Modernize azure-ai-projects-py

- **Target**: skills/azure-ai-projects-py
- **Why it was selected**: The documented SDK version was v2.0.0b4, which is obsolete compared to the latest stable PyPI release (v2.4.0).
- **Dedup check result**: Checked open PRs using `git branch -a | grep -i "azure-ai-projects-py"` (since gh cli was unavailable) and found no duplicates.
- **Prompt injection scan result**: clean
- **Evidence reviewed**: PyPI JSON API (https://pypi.org/pypi/azure-ai-projects/json) confirmed latest version is 2.4.0. Validated existing code snippets against current docs.
- **Files changed**: skills/azure-ai-projects-py/SKILL.md, data/maintenance/ledger.json
- **Linked PR/Issue**: PR-jules-modernize-azure-ai-projects-py
- **Next action**: Review updated SKILL.md for accuracy.
