# Agent Run: Modernize azure-ai-projects-py skill

- **Target**: skills/azure-ai-projects-py
- **Why it was selected**: The skill was found to be referencing an outdated beta version (v2.0.0b4) while the latest stable version on PyPI is v2.5.0.
- **Dedup check result**: Searched remote branches using `git branch -a | grep -i azure-ai-projects-py` and confirmed no open PRs conflict with this modernization effort.
- **Prompt injection scan result**: clean
- **Evidence reviewed**: Fetched package metadata from PyPI indicating `2.5.0` as the latest release version.
- **Files changed**: `skills/azure-ai-projects-py/SKILL.md`, `data/maintenance/ledger.json`
- **Linked PR/Issue**: PR-jules-modernize-azure-ai-projects-py
- **Next action**: Review updated SKILL.md for accuracy.
