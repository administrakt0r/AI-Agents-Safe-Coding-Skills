# Agent Run Logs

Store one Markdown file per autonomous maintenance run in this directory.

Naming format:

- `YYYY-MM-DD-agent-name-target.md`

Each log should include:

- target
- reason selected
- evidence reviewed
- files changed or removal decision
- linked PR or issue
- next action

Agents must read recent logs here before starting work so they do not duplicate active or recently resolved tasks.
