# Malicious Skill Safety Auditor Run: metasploit-framework

- **Target**: `skills/metasploit-framework`
- **Why it was selected**: It is an unclaimed high-risk skill that contained active payload generation commands and malicious IPs, requiring hardening to ensure safety while preserving its educational intent.
- **Evidence reviewed**:
  - `skills/metasploit-framework/SKILL.md` was inspected for active reverse shell references (`reverse_tcp`, `bind_tcp`, etc.) and attacker/target IPs (e.g. `192.168.1.50`, `192.168.1.100`, `192.168.1.0/24`).
- **Files changed**:
  - `skills/metasploit-framework/SKILL.md`: Replaced specific payloads and IP addresses with safe placeholders like `[REDACTED_LHOST_IP]`, `[REDACTED_RHOST_IP]`, `[REDACTED_PORT]`, and `[REDACTED_PAYLOAD]`.
  - `data/maintenance/ledger.json`: Updated the ledger claim and status to `normalized`.
- **Linked PR or issue**: PR-metasploit-framework-hardening
- **Next action**: Monitor for re-introduction of active payloads.