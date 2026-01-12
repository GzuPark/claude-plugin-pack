#!/usr/bin/env python3
# Recommended: use ./run.sh to execute this script for proper dependency management
# /// script
# dependencies = ["pyyaml"]
# ///
"""
Enhanced validation script for skills with Evolution Scoring integration.
"""

import sys
import re
import ast
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Tuple
from enum import IntEnum

# Try to import yaml, fallback to simple parser
try:
    import yaml

    HAS_YAML = True
except ImportError:
    HAS_YAML = False


class ExitCode(IntEnum):
    """Standard exit codes for skill scripts."""

    SUCCESS = 0
    GENERAL_ERROR = 1
    INVALID_ARGUMENTS = 2
    FILE_NOT_FOUND = 3
    VALIDATION_FAILED = 10


@dataclass
class ValidationResult:
    """Validation result object for multi-check tracking."""

    passed: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    def check(
        self, name: str, condition: bool, message: str, warning_only: bool = False
    ):
        """Record validation check result."""
        if condition:
            self.passed.append(f"[PASS] {name}: {message}")
        elif warning_only:
            self.warnings.append(f"[WARN] {name}: {message}")
        else:
            self.errors.append(f"[FAIL] {name}: {message}")

    @property
    def is_valid(self) -> bool:
        """True if no errors (warnings are OK)."""
        return len(self.errors) == 0

    @property
    def summary(self) -> str:
        """Human-readable summary."""
        total = len(self.passed) + len(self.warnings) + len(self.errors)
        return f"{len(self.passed)}/{total} passed, {len(self.warnings)} warnings, {len(self.errors)} errors"

    def format_report(self) -> str:
        """Format full validation report."""
        lines = []

        if self.errors:
            lines.append("\n=== ERRORS ===")
            for e in self.errors:
                lines.append(e)

        if self.warnings:
            lines.append("\n=== WARNINGS ===")
            for w in self.warnings:
                lines.append(w)

        if self.passed:
            lines.append("\n=== PASSED ===")
            for p in self.passed:
                lines.append(p)

        lines.append(f"\n{self.summary}")
        return "\n".join(lines)


def parse_yaml_simple(text: str) -> dict:
    """Simple YAML parser fallback."""
    result = {}
    for line in text.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip("\"'")
    return result


def extract_frontmatter(content: str) -> Tuple[dict, str]:
    """Extract YAML frontmatter from content."""
    if not content.startswith("---"):
        raise ValueError("No YAML frontmatter found")

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        raise ValueError("Invalid frontmatter format")

    frontmatter_text = match.group(1)
    body = content[match.end() :]

    if HAS_YAML:
        frontmatter = yaml.safe_load(frontmatter_text)
    else:
        frontmatter = parse_yaml_simple(frontmatter_text)

    if not isinstance(frontmatter, dict):
        raise ValueError("Frontmatter must be a YAML dictionary")

    return frontmatter, body


def count_triggers(content: str) -> int:
    """Count trigger entries in the skill."""
    trigger_section = re.search(
        r"##\s*Triggers?\s*\n(.*?)(?=\n##|\Z)", content, re.DOTALL | re.IGNORECASE
    )
    if not trigger_section:
        return 0

    section_content = trigger_section.group(1)
    # Count list items (lines starting with -)
    triggers = re.findall(r"^\s*-\s+", section_content, re.MULTILINE)
    return len(triggers)


def count_extension_points(content: str) -> int:
    """Count extension points in the skill."""
    ext_section = re.search(
        r"##\s*Extension\s*Points?\s*\n(.*?)(?=\n##|\Z)",
        content,
        re.DOTALL | re.IGNORECASE,
    )
    if not ext_section:
        return 0

    section_content = ext_section.group(1)
    # Count numbered or bulleted items
    items = re.findall(r"^\s*(?:\d+\.|[-*])\s+", section_content, re.MULTILINE)
    return len(items)


def has_section(content: str, section_name: str) -> bool:
    """Check if a section exists."""
    pattern = rf"##\s*{re.escape(section_name)}"
    return bool(re.search(pattern, content, re.IGNORECASE))


def has_anti_patterns_section(content: str) -> bool:
    """Check for anti-patterns section."""
    return has_section(content, "Anti-Patterns") or has_section(
        content, "Anti Patterns"
    )


def has_why_section(content: str) -> bool:
    """Check for WHY/Design Rationale section."""
    return (
        has_section(content, "WHY")
        or has_section(content, "Design Rationale")
        or has_section(content, "Design Reason")
    )


def has_hardcoded_versions(content: str) -> bool:
    """Check for hardcoded version strings."""
    # Common version patterns to detect
    patterns = [
        r"claude-\d+-\d+-\w+-\d{8}",  # claude-3-5-sonnet-20241022
        r"gpt-\d+\.?\d*-\w+-\d{4}",  # gpt-4-turbo-2024
        r"v\d+\.\d+\.\d+",  # v1.2.3 (semver)
        r"@\d+\.\d+\.\d+",  # @1.2.3 (npm style)
    ]

    for pattern in patterns:
        if re.search(pattern, content):
            return True
    return False


def remove_code_blocks(content: str) -> str:
    """Remove fenced code blocks from content."""
    # Remove triple-backtick code blocks (including language specifier)
    return re.sub(r"```[^\n]*\n.*?```", "", content, flags=re.DOTALL)


def validate_internal_links(skill_path: Path, content: str) -> List[str]:
    """Validate internal links in the skill (excluding code blocks)."""
    invalid_links = []

    # Remove code blocks first to avoid checking example links
    content_without_code = remove_code_blocks(content)

    # Find markdown links to local files
    links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content_without_code)

    for text, href in links:
        # Skip external links
        if href.startswith("http://") or href.startswith("https://"):
            continue
        # Skip anchor links
        if href.startswith("#"):
            continue

        # Resolve relative path
        link_path = skill_path / href
        if not link_path.exists():
            invalid_links.append(f"{href} (referenced as '{text}')")

    return invalid_links


def validate_python_scripts(skill_path: Path) -> List[str]:
    """Validate Python syntax in scripts."""
    syntax_errors = []
    scripts_dir = skill_path / "scripts"

    if not scripts_dir.exists():
        return []

    for py_file in scripts_dir.glob("*.py"):
        try:
            content = py_file.read_text()
            ast.parse(content)
        except SyntaxError as e:
            syntax_errors.append(f"{py_file.name}: line {e.lineno}: {e.msg}")

    return syntax_errors


def calculate_evolution_score(content: str) -> Tuple[int, List[str]]:
    """Calculate evolution score (0-10) and return improvement suggestions."""
    score = 2  # Base score
    suggestions = []

    # Check extension points (2+ required for points)
    ext_count = count_extension_points(content)
    if ext_count >= 2:
        score += 2
    else:
        suggestions.append(
            f"Add extension points section (current: {ext_count}, need: 2+)"
        )

    # Check for hardcoded versions
    if not has_hardcoded_versions(content):
        score += 2
    else:
        suggestions.append("Remove hardcoded version strings")

    # Check for WHY documentation
    if has_why_section(content):
        score += 2
    else:
        suggestions.append("Add 'Design Rationale' or 'WHY' section")

    # Check for anti-patterns section
    if has_anti_patterns_section(content):
        score += 2
    else:
        suggestions.append("Add 'Anti-Patterns' section")

    return score, suggestions


def validate_skill(skill_path: str, verbose: bool = False) -> ValidationResult:
    """Comprehensive validation of a skill."""
    result = ValidationResult()
    skill_path = Path(skill_path)

    # Check directory exists
    if not skill_path.exists():
        result.errors.append(f"[FAIL] path: Skill directory not found: {skill_path}")
        return result

    # Check SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    result.check("skill_md", skill_md.exists(), "SKILL.md exists")
    if not skill_md.exists():
        return result

    # Read content
    content = skill_md.read_text()

    # Validate frontmatter
    try:
        frontmatter, body = extract_frontmatter(content)
        result.check("frontmatter", True, "Valid YAML frontmatter")
    except ValueError as e:
        result.check("frontmatter", False, str(e))
        return result

    # Allowed properties
    ALLOWED_PROPERTIES = {"name", "description", "license", "allowed-tools", "metadata"}
    unexpected_keys = set(frontmatter.keys()) - ALLOWED_PROPERTIES
    result.check(
        "properties",
        len(unexpected_keys) == 0,
        (
            f"Unexpected keys: {', '.join(sorted(unexpected_keys))}"
            if unexpected_keys
            else "All properties valid"
        ),
    )

    # Required fields
    result.check("name", "name" in frontmatter, "Name field present")
    result.check(
        "description", "description" in frontmatter, "Description field present"
    )

    if "name" in frontmatter:
        name = frontmatter["name"]
        if isinstance(name, str):
            name = name.strip()
            # Naming convention
            valid_name = (
                re.match(r"^[a-z0-9-]+$", name)
                and not name.startswith("-")
                and not name.endswith("-")
                and "--" not in name
                and len(name) <= 64
            )
            result.check(
                "name_format",
                valid_name,
                f"Name '{name}' follows hyphen-case convention",
            )

    if "description" in frontmatter:
        desc = frontmatter["description"]
        if isinstance(desc, str):
            desc = desc.strip()
            valid_desc = "<" not in desc and ">" not in desc and len(desc) <= 1024
            result.check("description_format", valid_desc, "Description format valid")

    # Trigger count (warning only)
    trigger_count = count_triggers(content)
    result.check(
        "triggers",
        trigger_count >= 3,
        f"Has {trigger_count} triggers (recommended: 3+)",
        warning_only=True,
    )

    # Extension points (warning only)
    ext_count = count_extension_points(content)
    result.check(
        "extension_points",
        ext_count >= 2,
        f"Has {ext_count} extension points (recommended: 2+)",
        warning_only=True,
    )

    # Anti-patterns section (warning only)
    result.check(
        "anti_patterns",
        has_anti_patterns_section(content),
        "Anti-patterns section exists",
        warning_only=True,
    )

    # WHY section (warning only)
    result.check(
        "why_section",
        has_why_section(content),
        "Design rationale (WHY) section exists",
        warning_only=True,
    )

    # Hardcoded versions (warning only)
    result.check(
        "no_hardcoded_versions",
        not has_hardcoded_versions(content),
        "No hardcoded version strings",
        warning_only=True,
    )

    # Internal links
    invalid_links = validate_internal_links(skill_path, content)
    result.check(
        "internal_links",
        len(invalid_links) == 0,
        (
            f"Invalid links: {', '.join(invalid_links)}"
            if invalid_links
            else "All internal links valid"
        ),
        warning_only=True,
    )

    # Python syntax
    syntax_errors = validate_python_scripts(skill_path)
    result.check(
        "python_syntax",
        len(syntax_errors) == 0,
        (
            f"Syntax errors: {'; '.join(syntax_errors)}"
            if syntax_errors
            else "All Python scripts valid"
        ),
    )

    # Evolution score (informational)
    evo_score, suggestions = calculate_evolution_score(content)
    if evo_score >= 7:
        result.passed.append(
            f"[INFO] evolution_score: {evo_score}/10 (meets recommended threshold)"
        )
    else:
        result.warnings.append(
            f"[INFO] evolution_score: {evo_score}/10 (recommended: 7+)"
        )
        if verbose and suggestions:
            for s in suggestions:
                result.warnings.append(f"[INFO] suggestion: {s}")

    return result


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Validate skill directory")
    parser.add_argument("path", type=Path, help="Skill directory path")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument(
        "--strict", action="store_true", help="Treat warnings as errors"
    )

    args = parser.parse_args()

    if not args.path.exists():
        print(f"Error: Path not found: {args.path}", file=sys.stderr)
        sys.exit(ExitCode.INVALID_ARGUMENTS)

    result = validate_skill(args.path, verbose=args.verbose)

    if args.json:
        import json

        output = {
            "passed": result.passed,
            "warnings": result.warnings,
            "errors": result.errors,
            "is_valid": result.is_valid,
            "summary": result.summary,
        }
        print(json.dumps(output, indent=2))
    else:
        print(result.format_report())

    if args.strict and result.warnings:
        sys.exit(ExitCode.VALIDATION_FAILED)

    sys.exit(ExitCode.SUCCESS if result.is_valid else ExitCode.VALIDATION_FAILED)


if __name__ == "__main__":
    main()
