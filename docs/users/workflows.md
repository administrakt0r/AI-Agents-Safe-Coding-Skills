# AI-Agents-Safe-Coding Workflows

> Workflow playbooks for combining multiple skills into one concrete outcome.

## What Is a Workflow?

A workflow is a guided, step-by-step execution path that combines multiple skills for one real objective.

- **Bundles** tell you which skills are relevant for a role.
- **Workflows** tell you how to sequence those skills to complete the work safely.

If bundles are your toolbox, workflows are your execution playbook.

---

## How to Use Workflows

1. Install the repository once with `npx ai-agents-safe-coding-skills`.
2. Pick the workflow that matches the immediate goal.
3. Execute the steps in order and invoke the listed skills in each step.
4. Keep artifacts from each step: plans, decisions, tests, evidence, and handoff notes.

You can combine workflows with bundles from [bundles.md](bundles.md) when you need broader coverage.

---

## Workflow: Ship a SaaS MVP

Build and ship a minimal but production-minded SaaS product.

**Related bundles:** `Essentials`, `Full-Stack Developer`, `QA & Testing`, `DevOps & Cloud`

### Prerequisites

- Local repository and runtime configured.
- Clear user problem and MVP scope.
- Basic deployment target selected.

### Steps

1. **Plan the scope**
   - **Goal:** Define MVP boundaries and acceptance criteria.
   - **Skills:** [`@brainstorming`](../../skills/brainstorming/), [`@concise-planning`](../../skills/concise-planning/), [`@writing-plans`](../../skills/writing-plans/)
   - **Prompt example:** `Use @concise-planning to define milestones and acceptance criteria for my SaaS MVP.`

2. **Build backend and API**
   - **Goal:** Implement core entities, APIs, and auth baseline.
   - **Skills:** [`@backend-dev-guidelines`](../../skills/backend-dev-guidelines/), [`@api-patterns`](../../skills/api-patterns/), [`@database-design`](../../skills/database-design/)
   - **Prompt example:** `Use @backend-dev-guidelines to design the billing domain APIs and services.`

3. **Build frontend**
   - **Goal:** Ship the core user flow with clear UX states.
   - **Skills:** [`@frontend-developer`](../../skills/frontend-developer/), [`@react-patterns`](../../skills/react-patterns/), [`@frontend-design`](../../skills/frontend-design/)
   - **Prompt example:** `Use @frontend-developer to implement onboarding, empty states, and the first dashboard flow.`

4. **Test and validate**
   - **Goal:** Cover critical user journeys before release.
   - **Skills:** [`@test-driven-development`](../../skills/test-driven-development/), [`@browser-automation`](../../skills/browser-automation/), `@go-playwright` (optional, Go stack)
   - **Prompt example:** `Use @browser-automation to create end-to-end tests for signup and checkout.`

5. **Ship safely**
   - **Goal:** Release with observability and a rollback plan.
   - **Skills:** [`@deployment-procedures`](../../skills/deployment-procedures/), [`@observability-engineer`](../../skills/observability-engineer/)
   - **Prompt example:** `Use @deployment-procedures to draft a release checklist with rollback triggers.`

---

## Workflow: Security Audit for a Web App

Run a focused security review from scope definition to remediation validation.

**Related bundles:** `Security Engineer`, `Security Developer`, `Observability & Monitoring`

### Prerequisites

- Explicit authorization for testing.
- In-scope targets documented.
- Logging and environment details available.

### Steps

1. **Define scope and threat model**
   - **Goal:** Identify assets, trust boundaries, and attack paths.
   - **Skills:** [`@ethical-hacking-methodology`](../../skills/ethical-hacking-methodology/), [`@threat-modeling-expert`](../../skills/threat-modeling-expert/), [`@attack-tree-construction`](../../skills/attack-tree-construction/)
   - **Prompt example:** `Use @threat-modeling-expert to map critical assets and trust boundaries for this web app.`

2. **Review auth and access control**
   - **Goal:** Detect account-takeover and authorization flaws.
   - **Skills:** [`@broken-authentication`](../../skills/broken-authentication/), [`@auth-implementation-patterns`](../../skills/auth-implementation-patterns/), [`@idor-testing`](../../skills/idor-testing/)
   - **Prompt example:** `Use @idor-testing to verify unauthorized access paths in these multitenant endpoints.`

3. **Assess API and input security**
   - **Goal:** Uncover high-impact API and injection vulnerabilities.
   - **Skills:** [`@api-security-best-practices`](../../skills/api-security-best-practices/), [`@api-fuzzing-bug-bounty`](../../skills/api-fuzzing-bug-bounty/), [`@top-web-vulnerabilities`](../../skills/top-web-vulnerabilities/)
   - **Prompt example:** `Use @api-security-best-practices to audit auth, billing, and admin endpoints.`

4. **Harden and verify**
   - **Goal:** Convert findings into fixes and verify the mitigation evidence.
   - **Skills:** [`@security-auditor`](../../skills/security-auditor/), [`@sast-configuration`](../../skills/sast-configuration/), [`@verification-before-completion`](../../skills/verification-before-completion/)
   - **Prompt example:** `Use @verification-before-completion to prove the remediations are effective.`

---

## Workflow: Build an AI Agent System

Design and deliver a production-grade agent with measurable reliability.

**Related bundles:** `Agent Architect`, `LLM Application Developer`, `Data Engineering`

### Prerequisites

- Narrow use case with measurable outcomes.
- Access to model providers and observability tooling.
- Initial dataset or knowledge corpus.

### Steps

1. **Define target behavior and KPIs**
   - **Goal:** Set quality, latency, and failure thresholds.
   - **Skills:** [`@ai-agents-architect`](../../skills/ai-agents-architect/), [`@agent-evaluation`](../../skills/agent-evaluation/), [`@product-manager-toolkit`](../../skills/product-manager-toolkit/)
   - **Prompt example:** `Use @agent-evaluation to define benchmarks and success criteria for my agent.`

2. **Design retrieval and memory**
   - **Goal:** Build reliable retrieval and context architecture.
   - **Skills:** [`@llm-app-patterns`](../../skills/llm-app-patterns/), [`@rag-implementation`](../../skills/rag-implementation/), [`@vector-database-engineer`](../../skills/vector-database-engineer/)
   - **Prompt example:** `Use @rag-implementation to design the chunking, embedding, and retrieval pipeline.`

3. **Implement orchestration**
   - **Goal:** Implement deterministic orchestration and tool boundaries.
   - **Skills:** [`@langgraph`](../../skills/langgraph/), [`@mcp-builder`](../../skills/mcp-builder/), [`@workflow-automation`](../../skills/workflow-automation/)
   - **Prompt example:** `Use @langgraph to implement the agent graph with fallbacks and human review points.`

4. **Evaluate and iterate**
   - **Goal:** Improve weak points with a structured loop.
   - **Skills:** [`@agent-evaluation`](../../skills/agent-evaluation/), [`@langfuse`](../../skills/langfuse/), [`@kaizen`](../../skills/kaizen/)
   - **Prompt example:** `Use @kaizen to prioritize fixes for the failure modes found in evaluation.`

---

## Workflow: QA and Browser Automation

Create resilient browser automation with deterministic execution in CI.

**Related bundles:** `QA & Testing`, `Full-Stack Developer`

### Prerequisites

- Test environments and stable credentials.
- Critical user journeys identified.
- CI pipeline available.

### Steps

1. **Prepare test strategy**
   - **Goal:** Scope journeys, fixtures, and execution environments.
   - **Skills:** [`@e2e-testing-patterns`](../../skills/e2e-testing-patterns/), [`@test-driven-development`](../../skills/test-driven-development/)
   - **Prompt example:** `Use @e2e-testing-patterns to define a minimal but high-impact end-to-end suite.`

2. **Implement browser tests**
   - **Goal:** Build robust test coverage with stable selectors.
   - **Skills:** [`@browser-automation`](../../skills/browser-automation/), `@go-playwright` (optional, Go stack)
   - **Prompt example:** `Use @go-playwright to implement browser automation for this Go-based app.`

3. **Triage and harden**
   - **Goal:** Remove flaky behavior and enforce repeatability.
   - **Skills:** [`@systematic-debugging`](../../skills/systematic-debugging/), [`@test-fixing`](../../skills/test-fixing/), [`@verification-before-completion`](../../skills/verification-before-completion/)
   - **Prompt example:** `Use @systematic-debugging to classify and remove this CI flakiness.`

---

## Workflow: Design a DDD Core Domain

Model a complex domain coherently, then implement tactical and evented patterns only where justified.

**Related bundles:** `Architecture & Design`, `DDD & Evented Architecture`

### Prerequisites

- Access to at least one domain expert or product owner proxy.
- Current system context and integration landscape available.
- Agreement on business goals and key domain outcomes.

### Steps

1. **Assess DDD fit and scope**
   - **Goal:** Decide whether full DDD, partial DDD, or simple modular architecture is appropriate.
   - **Skills:** [`@domain-driven-design`](../../skills/domain-driven-design/), [`@architecture-decision-records`](../../skills/architecture-decision-records/)
   - **Prompt example:** `Use @domain-driven-design to evaluate whether full DDD is justified for our billing and fulfillment platform.`

2. **Create strategic model**
   - **Goal:** Define subdomains, bounded contexts, and ubiquitous language.
   - **Skills:** [`@ddd-strategic-design`](../../skills/ddd-strategic-design/)
   - **Prompt example:** `Use @ddd-strategic-design to classify subdomains and propose bounded contexts with ownership.`

3. **Map context relationships**
   - **Goal:** Define upstream and downstream contracts and anti-corruption boundaries.
   - **Skills:** [`@ddd-context-mapping`](../../skills/ddd-context-mapping/)
   - **Prompt example:** `Use @ddd-context-mapping to model Checkout, Billing, and Inventory interactions.`

4. **Implement tactical model**
   - **Goal:** Encode invariants with aggregates, value objects, and domain events.
   - **Skills:** [`@ddd-tactical-patterns`](../../skills/ddd-tactical-patterns/), [`@test-driven-development`](../../skills/test-driven-development/)
   - **Prompt example:** `Use @ddd-tactical-patterns to design aggregates and invariants for order lifecycle transitions.`

5. **Adopt evented patterns selectively**
   - **Goal:** Apply CQRS, event store, projections, and sagas only where complexity and scale require them.
   - **Skills:** [`@cqrs-implementation`](../../skills/cqrs-implementation/), [`@event-store-design`](../../skills/event-store-design/), [`@projection-patterns`](../../skills/projection-patterns/), [`@saga-orchestration`](../../skills/saga-orchestration/)
   - **Prompt example:** `Use @cqrs-implementation and @projection-patterns to scale read-side reporting safely.`

---

## Workflow: Refresh an Obsolete Skill

Review one skill for staleness and modernize it without duplicating work already in progress.

**Related bundles:** `Essentials`, `OSS Maintainer`, `QA & Testing`

### Prerequisites

- Read `data/maintenance/ledger.json` first.
- Confirm the skill is not already claimed or recently resolved.
- Have access to current primary documentation for the technology the skill covers.

### Steps

1. **Claim one skill**
   - **Goal:** Reserve exactly one target and avoid duplicate maintenance work.
   - **Skills:** [`@project-skill-audit`](../../skills/project-skill-audit/), [`@writing-skills`](../../skills/writing-skills/)
   - **Prompt example:** `Use @project-skill-audit to help me choose one stale skill that is not already active in the maintenance ledger.`

2. **Verify obsolescence**
   - **Goal:** Separate genuinely outdated guidance from still-valid content.
   - **Skills:** [`@verification-before-completion`](../../skills/verification-before-completion/)
   - **Prompt example:** `Use @verification-before-completion to check this skill against current primary docs and list what is obsolete.`

3. **Update safely**
   - **Goal:** Modernize the skill without introducing stale or unsafe guidance.
   - **Skills:** [`@writing-skills`](../../skills/writing-skills/), [`@skill-creator`](../../skills/skill-creator/)
   - **Prompt example:** `Use @writing-skills to rewrite this skill so it reflects current APIs, conventions, and best practices.`

4. **Log and hand off**
   - **Goal:** Record the work and route it to human review.
   - **Required artifacts:** ledger update, run log, linked PR or issue.

---

## Workflow: Audit a Skill for Malicious or Unsafe Behavior

Review one skill for malicious prompt patterns, unsafe tool guidance, suspicious scripts, or removal-worthy behavior.

**Related bundles:** `Security Engineer`, `Security Developer`

### Prerequisites

- Read `data/maintenance/ledger.json` first.
- Confirm the skill is not already claimed or recently resolved.
- Apply the English-only policy before doing deeper review work.

### Steps

1. **Select one review target**
   - **Goal:** Pick one skill with high risk or no recent audit history.
   - **Skills:** [`@project-skill-audit`](../../skills/project-skill-audit/), [`@audit-skills`](../../skills/audit-skills/)
   - **Prompt example:** `Use @audit-skills to identify one high-risk skill that is not already active in the maintenance ledger.`

2. **Inspect prompts, commands, and scripts**
   - **Goal:** Detect malicious prompt engineering, dangerous command delivery, suspicious network or filesystem behavior, and hidden tool abuse.
   - **Skills:** [`@skill-scanner`](../../skills/skill-scanner/), [`@security-auditor`](../../skills/security-auditor/)
   - **Prompt example:** `Use @skill-scanner and @security-auditor to audit this skill for hidden instructions, dangerous commands, or removal-worthy content.`

3. **Harden or mark for removal**
   - **Goal:** Either make the skill safe or create a removal recommendation with evidence.
   - **Skills:** [`@verification-before-completion`](../../skills/verification-before-completion/)
   - **Prompt example:** `Use @verification-before-completion to verify whether this skill can be safely kept after hardening.`

4. **Log and hand off**
   - **Goal:** Record the outcome and route it to human review.
   - **Required artifacts:** ledger update, run log, linked PR or issue.

---

## Workflow: Import or Modernize a Skill

Add one new high-value skill or refresh one trusted upstream skill source.

**Related bundles:** `Essentials`, `OSS Maintainer`, `Marketing & Growth`

### Prerequisites

- Read `data/maintenance/ledger.json` first.
- Confirm the target source or skill is not already active.
- Apply the English-only policy before import or update work begins.

### Steps

1. **Choose one gap or source**
   - **Goal:** Pick one high-value addition or update target.
   - **Skills:** [`@project-skill-audit`](../../skills/project-skill-audit/), [`@skill-creator`](../../skills/skill-creator/)
   - **Prompt example:** `Use @project-skill-audit to identify one missing or outdated skill worth importing or creating next.`

2. **Validate the source**
   - **Goal:** Prefer trusted upstream material and reject unsafe or non-English-first imports.
   - **Skills:** [`@skill-scanner`](../../skills/skill-scanner/), [`@audit-skills`](../../skills/audit-skills/)
   - **Prompt example:** `Use @skill-scanner to review this upstream skill before import and note any safety or language-policy problems.`

3. **Create or update the skill**
   - **Goal:** Land one scoped improvement with current guidance and repository conventions.
   - **Skills:** [`@skill-creator`](../../skills/skill-creator/), [`@writing-skills`](../../skills/writing-skills/)
   - **Prompt example:** `Use @skill-creator to produce an English-first skill that matches this repository's current structure and policy.`

4. **Log and hand off**
   - **Goal:** Record the work and route it to human review.
   - **Required artifacts:** ledger update, run log, linked PR or issue.

---

## Machine-Readable Workflows

For tooling and automation, workflow metadata is available in [data/workflows.json](../../data/workflows.json).
