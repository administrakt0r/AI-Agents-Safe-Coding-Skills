# Agent Run: malicious-skill-safety-auditor

**Date**: 2026-04-16
**Target**: skills/metasploit-framework
**Why it was selected**: The skill contains instructions and examples for using the Metasploit Framework, including generating active reverse shell payloads using `msfvenom`. This poses a risk of misuse if not properly hardened.
**Evidence reviewed**: Reviewed `skills/metasploit-framework/SKILL.md` and found multiple instances of active `msfvenom` commands generating malicious payloads (e.g., `windows/x64/meterpreter/reverse_tcp`, `linux/x86/meterpreter/reverse_tcp`).
**Files changed**:
- `skills/metasploit-framework/SKILL.md`: Hardened by replacing active `msfvenom` payload generation commands with the `[REDACTED_MSFVENOM_PAYLOAD]` placeholder.
- `data/maintenance/ledger.json`: Added entry for `skills/metasploit-framework`.
**Linked PR/Issue**: PR-metasploit-framework-hardening
**Next action**: Monitor for re-introduction of active payloads.
