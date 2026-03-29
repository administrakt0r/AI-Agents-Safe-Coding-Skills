---
title: Jetski/Cortex + Gemini Integration Guide
description: "How to use AI-Agents-Safe-Coding-Skills with Jetski/Cortex without overflowing the context window across 1,275+ skills."
---

# Jetski/Cortex + Gemini integration for 1,275+ skills

This guide shows how to use `AI-Agents-Safe-Coding-Skills` with a Jetski/Cortex + Gemini style agent without overloading the model context window.

The common failure mode looks like this:

> `TrajectoryChatConverter: could not convert a single message before hitting truncation`

That usually means the host is loading too many skills too early, not that the repository itself is too large to use safely.

## Core rule

Do not preload every `skills/*/SKILL.md` file.

Avoid these patterns:

- Loading every skill during agent startup.
- Concatenating the full library into one system prompt.
- Re-injecting the entire library on every turn.

With 1,275+ skills available, that approach fills the context window before the actual user request can be processed.

## Recommended loading pattern

Use a two-step model:

1. Load `skills_index.json` as a lightweight manifest at startup.
2. Load full `SKILL.md` files only when a skill is actually referenced.

Recommended flow:

1. Build an `id -> metadata` map from `skills_index.json`.
2. Parse the current messages for skill references such as `@skill-id`.
3. Resolve only those requested skills.
4. Enforce a strict per-turn skill cap.
5. Inject only the selected `SKILL.md` contents into the model prompt.

## Why this works

- The manifest stays small enough to keep startup cheap.
- Lazy loading prevents wasteful prompt expansion.
- Explicit limits stop silent truncation failures.
- Path validation keeps reads inside the expected skills directory.

## Reference loader shape

Minimal TypeScript-style sketch:

```ts
type SkillMeta = {
  id: string;
  path: string;
  name: string;
  description?: string;
};

function loadSkillIndex(indexPath: string): Map<string, SkillMeta> {
  const raw = fs.readFileSync(indexPath, "utf8");
  const items = JSON.parse(raw) as SkillMeta[];
  return new Map(items.map((item) => [item.id, item]));
}

function resolveReferencedSkills(
  messages: { content: string }[],
  index: Map<string, SkillMeta>,
  maxSkills: number,
): SkillMeta[] {
  const ids = new Set<string>();
  const skillIdPattern = /@([a-zA-Z0-9-_./]+)/g;

  for (const message of messages) {
    let match: RegExpExecArray | null;
    while ((match = skillIdPattern.exec(message.content)) !== null) {
      if (index.has(match[1])) ids.add(match[1]);
      if (ids.size >= maxSkills) break;
    }
  }

  return [...ids].map((id) => index.get(id)!).filter(Boolean);
}

async function loadSkillBodies(skillsRoot: string, metas: SkillMeta[]) {
  return Promise.all(
    metas.map((meta) =>
      fs.promises.readFile(path.join(skillsRoot, meta.path, "SKILL.md"), "utf8"),
    ),
  );
}
```

## Operational safeguards

Use all of these:

- A max-skills-per-turn limit.
- A token budget threshold before model invocation.
- Clear user-facing errors when too many skills are requested.
- Path normalization and boundary checks before reading `SKILL.md`.

Example error:

> Too many skills were requested in one turn. Reduce the number of `@skill-id` references or split the task into smaller steps.

## Windows crash-loop recovery

If your Jetski/Cortex host keeps reopening a broken trajectory after a truncation error:

1. Remove the problematic cached conversation state.
2. Clear Local Storage, Session Storage, or IndexedDB used by the host.
3. Clear `%TEMP%` if the host persists prompt state there.
4. Restart with lazy loading enabled and an explicit per-turn skill cap.

See [the Jetski Gemini loader README](./jetski-gemini-loader/README.md) for a fuller loader example.

## Summary

- Do not inject the full library into the prompt.
- Use `skills_index.json` as the manifest.
- Load `SKILL.md` files on demand.
- Cap per-turn skill usage.
- Fail explicitly before truncation instead of silently degrading behavior.

That pattern lets Jetski/Cortex + Gemini use the full `AI-Agents-Safe-Coding-Skills` library safely, even with 1,275+ skills available.
