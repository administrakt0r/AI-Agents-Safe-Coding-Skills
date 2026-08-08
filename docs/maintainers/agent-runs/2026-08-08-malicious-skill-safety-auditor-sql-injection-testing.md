# Agent Run: Harden sql-injection-testing

- **Target**: skills/sql-injection-testing
- **Why it was selected**: Unclaimed skill containing active SQL injection out-of-band exfiltration payloads.
- **Evidence reviewed**: Reviewed `skills/sql-injection-testing/SKILL.md` and identified active OOB payloads (DNS exfiltration for MSSQL and MySQL, HTTP request for Oracle) without an offensive risk designation or warning.
- **Files changed**: `skills/sql-injection-testing/SKILL.md`, `data/maintenance/ledger.json`
- **Linked PR/Issue**: PR-sql-injection-testing-hardening
- **Next action**: Monitor for re-introduction of active payloads.
