import os
import re
import argparse
import sys
import io
import json
import yaml
from collections.abc import Mapping
from datetime import date, datetime
from _project_paths import find_repo_root


def configure_utf8_output() -> None:
    """Best-effort UTF-8 stdout/stderr on Windows without dropping diagnostics."""
    if sys.platform != "win32":
        return

    for stream_name in ("stdout", "stderr"):
        stream = getattr(sys, stream_name)
        try:
            stream.reconfigure(encoding="utf-8", errors="backslashreplace")
            continue
        except Exception:
            pass

        buffer = getattr(stream, "buffer", None)
        if buffer is not None:
            setattr(
                sys,
                stream_name,
                io.TextIOWrapper(buffer, encoding="utf-8", errors="backslashreplace"),
            )

WHEN_TO_USE_PATTERNS = [
    re.compile(r"^##\s+When\s+to\s+Use", re.MULTILINE | re.IGNORECASE),
    re.compile(r"^##\s+Use\s+this\s+skill\s+when", re.MULTILINE | re.IGNORECASE),
    re.compile(r"^##\s+When\s+to\s+Use\s+This\s+Skill", re.MULTILINE | re.IGNORECASE),
]

VALID_RISK_LEVELS = ["none", "safe", "critical", "offensive", "unknown"]
DATE_PATTERN = re.compile(r'^\d{4}-\d{2}-\d{2}$')  # YYYY-MM-DD format
SECURITY_DISCLAIMER_PATTERN = re.compile(r"AUTHORIZED USE ONLY", re.IGNORECASE)


def has_when_to_use_section(content):
    return any(pattern.search(content) for pattern in WHEN_TO_USE_PATTERNS)


def load_exclusion_policy():
    policy_path = find_repo_root(__file__) / "tools" / "config" / "skill-exclusion-policy.json"
    try:
        with policy_path.open(encoding="utf-8") as policy_file:
            return json.load(policy_file)
    except (OSError, json.JSONDecodeError) as error:
        raise RuntimeError(f"Unable to load skill exclusion policy: {error}") from error


def is_excluded_skill(skill_id, metadata, policy):
    blocked_risks = {str(value).lower() for value in policy.get("blocked_risk_levels", [])}
    blocked_categories = {str(value).lower() for value in policy.get("blocked_categories", [])}
    if str(metadata.get("risk", "")).lower() in blocked_risks:
        return True
    if str(metadata.get("category", "")).lower() in blocked_categories:
        return True
    return any(
        re.search(pattern, skill_id, re.IGNORECASE)
        for pattern in policy.get("blocked_name_patterns", [])
    )

def normalize_yaml_value(value):
    if isinstance(value, Mapping):
        return {key: normalize_yaml_value(val) for key, val in value.items()}
    if isinstance(value, list):
        return [normalize_yaml_value(item) for item in value]
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    return value

def parse_frontmatter(content, rel_path=None):
    """
    Parse frontmatter using PyYAML for robustness.
    Returns a dict of key-values and a list of error messages.
    """
    fm_match = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return None, ["Missing or malformed YAML frontmatter"]
    
    fm_text = fm_match.group(1)
    fm_errors = []
    try:
        metadata = yaml.safe_load(fm_text) or {}
        metadata = normalize_yaml_value(metadata)
        if not isinstance(metadata, Mapping):
            return None, ["Frontmatter must be a YAML mapping/object."]
        
        # Identification of the specific regression issue for better reporting
        if "description" in metadata:
            desc = metadata["description"]
            if not desc or (isinstance(desc, str) and not desc.strip()):
                fm_errors.append("description field is empty or whitespace only.")
            elif desc == "|":
                fm_errors.append("description contains only the YAML block indicator '|', likely due to a parsing regression.")
        
        return dict(metadata), fm_errors
    except yaml.YAMLError as e:
        return None, [f"YAML Syntax Error: {e}"]


def check_metadata_schema(metadata, rel_path, folder_name, strict_mode=False):
    """Run metadata schema validation checks on a parsed frontmatter dictionary."""
    errors = []
    warnings = []

    if "name" not in metadata:
        errors.append(f"❌ {rel_path}: Missing 'name' in frontmatter")
    elif metadata["name"] != folder_name:
        errors.append(f"❌ {rel_path}: Name '{metadata['name']}' does not match folder name '{folder_name}'")

    if "description" not in metadata or metadata["description"] is None:
        errors.append(f"❌ {rel_path}: Missing 'description' in frontmatter")
    else:
        desc = metadata["description"]
        if not isinstance(desc, str):
            errors.append(f"❌ {rel_path}: 'description' must be a string, got {type(desc).__name__}")
        elif len(desc) > 300:
            errors.append(f"❌ {rel_path}: Description is oversized ({len(desc)} chars). Must be concise.")

    # Risk Validation (Quality Bar)
    if "risk" not in metadata:
        msg = f"⚠️  {rel_path}: Missing 'risk' label (defaulting to 'unknown')"
        if strict_mode:
            errors.append(msg.replace("⚠️", "❌"))
        else:
            warnings.append(msg)
    elif metadata["risk"] not in VALID_RISK_LEVELS:
        errors.append(f"❌ {rel_path}: Invalid risk level '{metadata['risk']}'. Must be one of {VALID_RISK_LEVELS}")

    # Source Validation
    if "source" not in metadata:
        msg = f"⚠️  {rel_path}: Missing 'source' attribution"
        if strict_mode:
            errors.append(msg.replace("⚠️", "❌"))
        else:
            warnings.append(msg)

    # Date Added Validation (optional field)
    if "date_added" in metadata:
        if not DATE_PATTERN.match(str(metadata["date_added"])):
            errors.append(f"❌ {rel_path}: Invalid 'date_added' format. Must be YYYY-MM-DD (e.g., '2024-01-15'), got '{metadata['date_added']}'")
    else:
        msg = f"ℹ️  {rel_path}: Missing 'date_added' field (optional, but recommended)"
        if strict_mode:
            warnings.append(msg)

    return errors, warnings


def check_content_and_guardrails(content, metadata, rel_path, strict_mode=False):
    """Run content structure and security guardrail checks on a skill."""
    errors = []
    warnings = []

    if not has_when_to_use_section(content):
        msg = f"⚠️  {rel_path}: Missing '## When to Use' section"
        if strict_mode:
            errors.append(msg.replace("⚠️", "❌"))
        else:
            warnings.append(msg)

    if metadata.get("risk") == "offensive":
        if not SECURITY_DISCLAIMER_PATTERN.search(content):
            errors.append(f"🚨 {rel_path}: OFFENSIVE SKILL MISSING SECURITY DISCLAIMER! (Must contain 'AUTHORIZED USE ONLY')")

    return errors, warnings


def check_dangling_links(content, rel_path, root_dir):
    """Check markdown relative links to verify target local files exist."""
    errors = []
    links = re.findall(r'\[[^\]]*\]\(([^)]+)\)', content)
    for link in links:
        link_clean = link.split('#')[0].strip()
        if not link_clean or link_clean.startswith(('http://', 'https://', 'mailto:', '<', '>')):
            continue
        if os.path.isabs(link_clean):
            continue

        target_path = os.path.normpath(os.path.join(root_dir, link_clean))
        if not os.path.exists(target_path):
            errors.append(f"❌ {rel_path}: Dangling link detected. Path '{link_clean}' (from '...({link})') does not exist locally.")

    return errors


def validate_single_skill(skill_path, skills_dir, exclusion_policy, strict_mode=False):
    """Validate a single SKILL.md file, returning (errors, warnings)."""
    rel_path = os.path.relpath(skill_path, skills_dir)
    root = os.path.dirname(skill_path)

    try:
        with open(skill_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return [f"❌ {rel_path}: Unreadable file - {str(e)}"], []

    metadata, fm_errors = parse_frontmatter(content, rel_path)
    if not metadata:
        return [f"❌ {rel_path}: Missing or malformed YAML frontmatter"], []

    errors = []
    warnings = []

    if fm_errors:
        for fe in fm_errors:
            errors.append(f"❌ {rel_path}: YAML Structure Error - {fe}")

    skill_id = os.path.basename(root)
    if is_excluded_skill(skill_id, metadata, exclusion_policy):
        errors.append(f"❌ {rel_path}: Skill is excluded by the security-content policy.")
        return errors, warnings

    meta_errors, meta_warnings = check_metadata_schema(metadata, rel_path, skill_id, strict_mode=strict_mode)
    errors.extend(meta_errors)
    warnings.extend(meta_warnings)

    content_errors, content_warnings = check_content_and_guardrails(content, metadata, rel_path, strict_mode=strict_mode)
    errors.extend(content_errors)
    warnings.extend(content_warnings)

    link_errors = check_dangling_links(content, rel_path, root)
    errors.extend(link_errors)

    return errors, warnings


def collect_validation_results(skills_dir, strict_mode=False):
    """
    Run all validation rules for all skill directories in skills_dir, returning structured results.
    """
    errors = []
    warnings = []
    skill_count = 0
    exclusion_policy = load_exclusion_policy()

    for root, dirs, files in os.walk(skills_dir):
        # Skip .disabled or hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        if "SKILL.md" in files:
            skill_count += 1
            skill_path = os.path.join(root, "SKILL.md")
            if os.path.islink(skill_path):
                warnings.append(f"⚠️  {os.path.relpath(skill_path, skills_dir)}: Skipping symlinked SKILL.md")
                continue

            s_errors, s_warnings = validate_single_skill(
                skill_path, skills_dir, exclusion_policy, strict_mode=strict_mode
            )
            errors.extend(s_errors)
            warnings.extend(s_warnings)

    return {
        "skill_count": skill_count,
        "warnings": warnings,
        "errors": errors,
        "strict_mode": strict_mode,
    }


def validate_skills(skills_dir, strict_mode=False):
    configure_utf8_output()

    print(f"🔍 Validating skills in: {skills_dir}")
    print(f"⚙️  Mode: {'STRICT (CI)' if strict_mode else 'Standard (Dev)'}")

    results = collect_validation_results(skills_dir, strict_mode=strict_mode)
    warnings = results["warnings"]
    errors = results["errors"]
    skill_count = results["skill_count"]

    # Reporting
    print(f"\n📊 Checked {skill_count} skills.")
    
    if warnings:
        print(f"\n⚠️  Found {len(warnings)} Warnings:")
        for w in warnings:
            print(w)

    if errors:
        print(f"\n❌ Found {len(errors)} Critical Errors:")
        for e in errors:
            print(e)
        return False

    if strict_mode and warnings:
        print("\n❌ STRICT MODE: Failed due to warnings.")
        return False

    print("\n✨ All skills passed validation!")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate Antigravity Skills")
    parser.add_argument("--strict", action="store_true", help="Fail on warnings (for CI)")
    args = parser.parse_args()

    base_dir = str(find_repo_root(__file__))
    skills_path = os.path.join(base_dir, "skills")
    
    success = validate_skills(skills_path, strict_mode=args.strict)
    if not success:
        sys.exit(1)
