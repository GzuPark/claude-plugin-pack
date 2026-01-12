#!/usr/bin/env python3
# Recommended: use ./run.sh to execute this script for proper dependency management
# /// script
# dependencies = ["pyyaml"]
# ///
"""
Skill Packager - Creates a distributable .skill file of a skill folder

Includes:
- Validation check
- Evolution score calculation (warning if below 7)
- Duplicate skill detection
- User confirmation for low scores

Usage:
    python scripts/package_skill.py <path/to/skill-folder> [output-directory]

Example:
    python scripts/package_skill.py skills/public/my-skill
    python scripts/package_skill.py skills/public/my-skill ./dist
"""

import sys
import re
import zipfile
from pathlib import Path
from enum import IntEnum

# Import from sibling modules
try:
    from quick_validate import validate_skill
    from score_evolution import calculate_evolution_score
    from check_duplicates import check_duplicates
except ImportError:
    # Fallback for direct execution
    import importlib.util

    script_dir = Path(__file__).parent

    def load_module(name):
        spec = importlib.util.spec_from_file_location(name, script_dir / f"{name}.py")
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    quick_validate = load_module("quick_validate")
    validate_skill = quick_validate.validate_skill
    ValidationResult = quick_validate.ValidationResult

    score_evolution = load_module("score_evolution")
    calculate_evolution_score = score_evolution.calculate_evolution_score

    check_duplicates_module = load_module("check_duplicates")
    check_duplicates = check_duplicates_module.check_duplicates


class ExitCode(IntEnum):
    SUCCESS = 0
    GENERAL_ERROR = 1
    VALIDATION_FAILED = 10
    USER_CANCELLED = 20


def extract_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter from content."""
    if not content.startswith("---"):
        return {}

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}

    # Simple parsing
    result = {}
    for line in match.group(1).split("\n"):
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip("\"'")

    return result


def prompt_continue(message: str) -> bool:
    """Prompt user to continue or cancel."""
    try:
        response = input(f"\n{message} [y/N]: ").strip().lower()
        return response in ("y", "yes")
    except (EOFError, KeyboardInterrupt):
        return False


def package_skill(skill_path, output_dir=None, force=False):
    """
    Package a skill folder into a .skill file.

    Args:
        skill_path: Path to the skill folder
        output_dir: Optional output directory for the .skill file
        force: Skip confirmation prompts

    Returns:
        Path to the created .skill file, or None if error/cancelled
    """
    skill_path = Path(skill_path).resolve()

    # Validate skill folder exists
    if not skill_path.exists():
        print(f"❌ Error: Skill folder not found: {skill_path}")
        return None

    if not skill_path.is_dir():
        print(f"❌ Error: Path is not a directory: {skill_path}")
        return None

    # Validate SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print(f"❌ Error: SKILL.md not found in {skill_path}")
        return None

    # Read skill content
    content = skill_md.read_text()
    frontmatter = extract_frontmatter(content)
    skill_name = frontmatter.get("name", skill_path.name)
    skill_description = frontmatter.get("description", "")

    # Run validation
    print("🔍 Validating skill...")
    result = validate_skill(skill_path)

    if not result.is_valid:
        print("\n❌ Validation failed:")
        for error in result.errors:
            print(f"   {error}")
        print("\n   Please fix the validation errors before packaging.")
        return None

    print(f"✅ Validation passed ({result.summary})")

    # Check for similar skills
    print("\n🔍 Checking for similar skills...")
    similar = check_duplicates(
        skill_name, skill_description, threshold=0.5, exclude_path=skill_path
    )

    if similar:
        print(f"\n⚠️  Found {len(similar)} similar skill(s):")
        for s in similar[:3]:  # Show top 3
            print(f"   - {s.skill.name} ({s.total_similarity*100:.0f}% similar)")
            print(f"     Path: {s.skill.path}")

        if not force:
            if not prompt_continue("Similar skills exist. Continue packaging?"):
                print("\n❌ Packaging cancelled by user.")
                return None
    else:
        print("✅ No similar skills found")

    # Calculate evolution score
    print("\n🔍 Calculating evolution score...")
    evo_score = calculate_evolution_score(content)

    if evo_score.meets_threshold:
        print(f"✅ Evolution score: {evo_score.total}/10 (meets threshold)")
    else:
        print(f"\n⚠️  Evolution score: {evo_score.total}/10 (recommended: 7+)")
        print("\nBreakdown:")
        for item in evo_score.items:
            status = "✓" if item.passed else "✗"
            print(f"   {status} {item.name}: {item.points}/{item.max_points}")

        if evo_score.suggestions:
            print("\nSuggestions for improvement:")
            for i, suggestion in enumerate(evo_score.suggestions, 1):
                print(f"   {i}. {suggestion}")

        if not force:
            if not prompt_continue(
                "Evolution score below threshold. Continue packaging?"
            ):
                print("\n❌ Packaging cancelled by user.")
                return None

    # Determine output location
    if output_dir:
        output_path = Path(output_dir).resolve()
        output_path.mkdir(parents=True, exist_ok=True)
    else:
        output_path = Path.cwd()

    skill_filename = output_path / f"{skill_path.name}.skill"

    # Create the .skill file (zip format)
    print(f"\n📦 Creating package...")
    try:
        with zipfile.ZipFile(skill_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
            # Walk through the skill directory
            file_count = 0
            for file_path in skill_path.rglob("*"):
                if file_path.is_file():
                    # Skip hidden files and __pycache__
                    if any(
                        part.startswith(".") or part == "__pycache__"
                        for part in file_path.parts
                    ):
                        continue
                    # Calculate the relative path within the zip
                    arcname = file_path.relative_to(skill_path.parent)
                    zipf.write(file_path, arcname)
                    file_count += 1
                    print(f"   Added: {arcname}")

        print(f"\n✅ Successfully packaged {file_count} files to: {skill_filename}")

        # Print summary
        print(f"\n📋 Summary:")
        print(f"   Skill: {skill_name}")
        print(f"   Validation: {result.summary}")
        print(f"   Evolution score: {evo_score.total}/10")
        print(f"   Similar skills: {len(similar)} found")
        print(f"   Output: {skill_filename}")

        return skill_filename

    except Exception as e:
        print(f"❌ Error creating .skill file: {e}")
        return None


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Package a skill folder into a .skill file"
    )
    parser.add_argument("skill_path", help="Path to the skill folder")
    parser.add_argument(
        "output_dir", nargs="?", help="Optional output directory for the .skill file"
    )
    parser.add_argument(
        "--force", "-f", action="store_true", help="Skip confirmation prompts"
    )

    args = parser.parse_args()

    print(f"📦 Packaging skill: {args.skill_path}")
    if args.output_dir:
        print(f"   Output directory: {args.output_dir}")
    print()

    result = package_skill(args.skill_path, args.output_dir, args.force)

    if result:
        sys.exit(ExitCode.SUCCESS)
    else:
        sys.exit(ExitCode.GENERAL_ERROR)


if __name__ == "__main__":
    main()
