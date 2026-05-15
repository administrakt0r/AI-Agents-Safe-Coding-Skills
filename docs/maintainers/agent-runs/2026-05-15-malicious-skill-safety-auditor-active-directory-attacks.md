# active-directory-attacks Maintenance Run

- **Target:** `skills/active-directory-attacks`
- **Why it was selected:** Unclaimed skill with active backdoor and exploit payloads in the references documentation.
- **Evidence reviewed:** Found active `MalSCCM.exe` backdoor deployment payloads and `SharpWSUS.exe` malicious update commands injecting `psexec.exe` and `net user` backdoors in `skills/active-directory-attacks/references/advanced-attacks.md`.
- **Files changed:**
  - `skills/active-directory-attacks/references/advanced-attacks.md` (replaced active payloads with safe placeholders)
  - `data/maintenance/ledger.json` (updated status and outcome)
- **Linked PR or issue:** `PR-active-directory-attacks-hardening`
- **Next action:** Monitor for re-introduction of active payloads.
