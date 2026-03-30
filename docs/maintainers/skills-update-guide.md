# Skills Update Guide

This guide explains how to refresh generated skill artifacts after source changes.

## Recommended Command

```bash
npm run update:skills
```

This command regenerates the root skill index from `skills/`.

## Full Maintainer Refresh

If you want the broader maintainer sweep instead of only the index:

```bash
npm run sync:repo-state
```

This runs validation, plugin compatibility sync, index generation, bundle sync, metadata sync, catalog generation, contributor sync, and consistency checks.

## Manual Steps

```bash
python tools/scripts/generate_index.py
```

## Prerequisites

For index refreshes, you need:

- **Python 3.x**: Download from [python.org](https://python.org/)
- **PyYAML**: Install with `pip install PyYAML`

## Troubleshooting

### "Python is not recognized"

- Install Python from [python.org](https://python.org/)
- Make sure to check "Add Python to PATH" during installation

### "PyYAML not found"

- Install with: `pip install PyYAML`
- Or run the update script which will install it automatically

## What Gets Updated

The update process refreshes:

- The generated root skill index (`skills_index.json`)
- Any downstream repo artifacts that consume that index when you later run the broader sync commands

## When to Update

Update generated artifacts when:

- New skills are added to the repository
- You want the latest skill descriptions reflected in generated files
- Generated indexes appear out of date

## Git Users

If you have Git installed and want to update the entire repository:

```bash
git pull origin main
npm run update:skills
```

This pulls the latest code and refreshes the generated skill index.
