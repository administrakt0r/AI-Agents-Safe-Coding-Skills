# Run Log: ai-engineering-toolkit

- **Target**: skills/ai-engineering-toolkit
- **Why it was selected**: High-risk offensive skill missing the top-level Authorized Use Only disclaimer and the mandatory "Ask the user to verify the target URL/IP before running" instruction.
- **Evidence reviewed**: Checked `skills/ai-engineering-toolkit/SKILL.md` and confirmed it's an offensive skill generating attack payloads (prompt injection, SQL injection). The disclaimer was nested in Skill 4 instead of right after the frontmatter, and it lacked the exact required agent instruction.
- **Files changed**: `skills/ai-engineering-toolkit/SKILL.md` to move the disclaimer and add the user confirmation instruction.
- **Linked PR or issue**: PR-ai-engineering-toolkit-hardening
- **Next action**: Monitor for compliance with offensive skill rules.
