#!/usr/bin/env python3
"""Validate data/maintenance/ledger.json structural integrity.

Checks that:
1. The file is valid JSON.
2. Top-level keys are ONLY: version, updatedAt, policies, entries.
3. No skill/source entries leak outside the "entries" block.
4. Each entry inside "entries" has all required fields.
5. Status values are from the allowed set.
6. lastReviewedAt uses YYYY-MM-DD format.

Usage:
    python3 tools/scripts/validate_ledger.py [--strict]

Exit codes:
    0 - valid
    1 - validation errors found
"""

import json
import re
import sys
from pathlib import Path

LEDGER_PATH = Path(__file__).resolve().parents[2] / "data" / "maintenance" / "ledger.json"

VALID_TOP_LEVEL_KEYS = {"version", "updatedAt", "policies", "entries"}

REQUIRED_ENTRY_FIELDS = {
    "status",
    "lastReviewedAt",
    "reviewerAgent",
    "outcome",
    "linkedIssueOrPr",
}

OPTIONAL_ENTRY_FIELDS = {"nextAction"}

VALID_STATUSES = {
    "active",
    "normalized",
    "reviewed",
    "removed",
    "monitoring",
    "blocked",
    "pending-review",
    "rejected-prompt-injection",
}

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def validate_ledger(strict: bool = False) -> list[str]:
    errors: list[str] = []

    if not LEDGER_PATH.exists():
        errors.append(f"Ledger file not found: {LEDGER_PATH}")
        return errors

    try:
        with open(LEDGER_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        errors.append(f"Invalid JSON: {e}")
        return errors

    if not isinstance(data, dict):
        errors.append("Ledger root must be a JSON object")
        return errors

    # --- Check top-level keys ---
    extra_keys = set(data.keys()) - VALID_TOP_LEVEL_KEYS
    if extra_keys:
        errors.append(
            f"Unexpected top-level key(s): {sorted(extra_keys)}. "
            f"Skill/source entries MUST be placed inside the \"entries\" block, "
            f"not as top-level siblings. Valid top-level keys: {sorted(VALID_TOP_LEVEL_KEYS)}"
        )

    entries = data.get("entries")
    if entries is None:
        errors.append("Missing top-level \"entries\" object")
        return errors

    if not isinstance(entries, dict):
        errors.append("\"entries\" must be a JSON object")
        return errors

    # --- Validate each entry ---
    for key, entry in entries.items():
        if not isinstance(entry, dict):
            errors.append(f"Entry \"{key}\" must be a JSON object")
            continue

        missing = REQUIRED_ENTRY_FIELDS - set(entry.keys())
        if missing:
            errors.append(f"Entry \"{key}\" missing required fields: {sorted(missing)}")

        extra = set(entry.keys()) - REQUIRED_ENTRY_FIELDS - OPTIONAL_ENTRY_FIELDS
        if strict and extra:
            errors.append(f"Entry \"{key}\" has unexpected fields: {sorted(extra)}")

        status = entry.get("status")
        if status and status not in VALID_STATUSES:
            errors.append(
                f"Entry \"{key}\" has invalid status \"{status}\". "
                f"Allowed: {sorted(VALID_STATUSES)}"
            )

        date = entry.get("lastReviewedAt")
        if date and not DATE_RE.match(date):
            errors.append(
                f"Entry \"{key}\" lastReviewedAt \"{date}\" must be YYYY-MM-DD"
            )

    return errors


def main() -> int:
    strict = "--strict" in sys.argv
    errors = validate_ledger(strict=strict)

    if errors:
        print("ledger.json validation FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("ledger.json: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
