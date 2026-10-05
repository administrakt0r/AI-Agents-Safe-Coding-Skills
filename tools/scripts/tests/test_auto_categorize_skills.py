import os
import sys
from pathlib import Path
import pytest

# Ensure tools/scripts is in sys.path so we can import auto_categorize_skills
SCRIPTS_DIR = Path(__file__).resolve().parent.parent
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from auto_categorize_skills import auto_categorize, categorize_skill


def test_categorize_skill_matching():
    cat = categorize_skill("react-component", "A frontend React component skill")
    assert cat == "web-development"


def test_categorize_skill_no_match():
    cat = categorize_skill("unknown-xyz", "something completely unrelated 12345")
    assert cat is None


def test_auto_categorize_workflow(tmp_path):
    # Setup test directory structure
    skills_dir = tmp_path / "skills"
    skills_dir.mkdir()

    # Skill 1: uncategorized -> web-development
    s1 = skills_dir / "react-helper"
    s1.mkdir()
    s1_file = s1 / "SKILL.md"
    s1_file.write_text(
        "---\nname: react-helper\ndescription: React component helper\ncategory: uncategorized\n---\n\nBody content\n",
        encoding="utf-8"
    )

    # Skill 2: already categorized -> skip
    s2 = skills_dir / "existing-cat"
    s2.mkdir()
    s2_file = s2 / "SKILL.md"
    s2_file.write_text(
        "---\nname: existing-cat\ndescription: Backend skill\ncategory: backend\n---\n\nBody content\n",
        encoding="utf-8"
    )

    # Skill 3: uncategorized -> no match (failed)
    s3 = skills_dir / "no-match"
    s3.mkdir()
    s3_file = s3 / "SKILL.md"
    s3_file.write_text(
        "---\nname: no-match\ndescription: zzzqqq123\ncategory: uncategorized\n---\n\nBody content\n",
        encoding="utf-8"
    )

    # Test Dry Run
    count_dry = auto_categorize(str(skills_dir), dry_run=True)
    assert count_dry == 1
    # Confirm file was NOT modified in dry run
    assert "category: uncategorized" in s1_file.read_text(encoding="utf-8")

    # Test Actual Execution
    count_actual = auto_categorize(str(skills_dir), dry_run=False)
    assert count_actual == 1
    # Confirm file WAS updated
    updated_content = s1_file.read_text(encoding="utf-8")
    assert "category: web-development" in updated_content
