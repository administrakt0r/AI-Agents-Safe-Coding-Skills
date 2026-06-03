# Malicious Skill Safety Audit - red-team-tools

- **Target**: skills/red-team-tools
- **Why it was selected**: Unclaimed offensive tool without proper disclaimers, labeled as 'unknown' risk, and contained active payloads.
- **Evidence reviewed**: Checked `SKILL.md`. Found active XSS payload `` '"><script>alert(1)</script>' ``.
- **Files changed or removal decision**:
  - `skills/red-team-tools/SKILL.md`: Updated `risk` to `offensive`, added "AUTHORIZED USE ONLY" disclaimer, added user confirmation requirement, and replaced the active XSS payload with a safe placeholder.
  - `data/maintenance/ledger.json`: Updated with `normalized` status and log details.
- **Linked PR or issue**: PR-red-team-tools-hardening
- **Next action**: Monitor for re-introduction of active payloads.
