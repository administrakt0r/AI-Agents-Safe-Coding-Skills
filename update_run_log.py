with open("docs/maintainers/agent-runs/2026-08-01-new-skill-import-curator-cold-email.md", "r") as f:
    content = f.read()

content = content.replace("Created skills/cold-email/SKILL.md", "Updated skills/cold-email/SKILL.md")
content = content.replace("Created skills/cold-email/references/*.md", "Imported skills/cold-email/references/*.md")

with open("docs/maintainers/agent-runs/2026-08-01-new-skill-import-curator-cold-email.md", "w") as f:
    f.write(content)
