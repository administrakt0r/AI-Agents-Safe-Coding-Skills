import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
TOOLS_SCRIPTS_DIR = REPO_ROOT / "tools" / "scripts"
if str(TOOLS_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(TOOLS_SCRIPTS_DIR))


def load_module(relative_path: str, module_name: str):
    module_path = REPO_ROOT / relative_path
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


validate_skills = load_module("tools/scripts/validate_skills.py", "validate_skills")


class ValidateSkillsHelpersTests(unittest.TestCase):
    def test_check_metadata_schema_valid(self):
        metadata = {
            "name": "sample-skill",
            "description": "A short concise description.",
            "risk": "safe",
            "source": "official",
            "date_added": "2024-01-15",
        }
        errors, warnings = validate_skills.check_metadata_schema(
            metadata, "skills/sample-skill/SKILL.md", "sample-skill"
        )
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_check_metadata_schema_mismatch_and_missing(self):
        metadata = {
            "name": "wrong-name",
            "description": "a" * 305,
            "risk": "invalid-risk",
        }
        errors, warnings = validate_skills.check_metadata_schema(
            metadata, "skills/sample-skill/SKILL.md", "sample-skill", strict_mode=True
        )
        self.assertTrue(any("Name 'wrong-name' does not match" in e for e in errors))
        self.assertTrue(any("oversized" in e for e in errors))
        self.assertTrue(any("Invalid risk level" in e for e in errors))
        self.assertTrue(any("Missing 'source' attribution" in e for e in errors))

    def test_check_content_and_guardrails_offensive(self):
        metadata = {"risk": "offensive"}
        content = "## Overview\nNo disclaimer here."
        errors, warnings = validate_skills.check_content_and_guardrails(
            content, metadata, "skills/off-skill/SKILL.md", strict_mode=False
        )
        self.assertTrue(any("Missing '## When to Use' section" in w for w in warnings))
        self.assertTrue(any("OFFENSIVE SKILL MISSING SECURITY DISCLAIMER" in e for e in errors))

    def test_check_dangling_links(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            skill_dir = Path(temp_dir)
            (skill_dir / "exists.md").write_text("hello", encoding="utf-8")

            content = "Link 1: [valid](exists.md)\nLink 2: [missing](nonexistent.md)"
            errors = validate_skills.check_dangling_links(
                content, "skills/demo/SKILL.md", str(skill_dir)
            )
            self.assertEqual(len(errors), 1)
            self.assertIn("nonexistent.md", errors[0])

    def test_validate_single_skill_and_collect_validation_results(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            skills_dir = Path(temp_dir) / "skills"
            skill_folder = skills_dir / "my-skill"
            skill_folder.mkdir(parents=True)

            skill_md = skill_folder / "SKILL.md"
            skill_md.write_text(
                "---\n"
                "name: my-skill\n"
                "description: A valid skill.\n"
                "risk: safe\n"
                "source: community\n"
                "----\n\n"
                "## When to Use\n"
                "Use this skill when needed.\n",
                encoding="utf-8",
            )

            results = validate_skills.collect_validation_results(str(skills_dir))
            self.assertEqual(results["skill_count"], 1)
            self.assertEqual(results["errors"], [])


if __name__ == "__main__":
    unittest.main()
