#!/usr/bin/env python3
# Recommended: use ./run.sh to execute this script for proper dependency management
# /// script
# dependencies = ["pyyaml"]
# ///
"""
Evolution Score Calculator for skills.

Evaluates a skill's future-readiness based on:
- Extension points (2+ required): +2 points
- No hardcoded versions: +2 points
- WHY/Design Rationale documented: +2 points
- Anti-patterns section: +2 points
- Base score: +2 points

Total: 10 points max, 7+ recommended
"""

import sys
import re
import argparse
import json
from pathlib import Path
from dataclasses import dataclass, field
from typing import List
from enum import IntEnum

# Try to import yaml
try:
    import yaml

    HAS_YAML = True
except ImportError:
    HAS_YAML = False


class ExitCode(IntEnum):
    SUCCESS = 0
    GENERAL_ERROR = 1
    INVALID_ARGUMENTS = 2
    FILE_NOT_FOUND = 3


@dataclass
class ScoreItem:
    """Individual score item."""

    name: str
    passed: bool
    points: int
    max_points: int
    evidence: str


@dataclass
class EvolutionScore:
    """Evolution score result."""

    items: List[ScoreItem] = field(default_factory=list)
    suggestions: List[str] = field(default_factory=list)

    @property
    def total(self) -> int:
        return sum(item.points for item in self.items)

    @property
    def max_total(self) -> int:
        return sum(item.max_points for item in self.items)

    @property
    def meets_threshold(self) -> bool:
        return self.total >= 7

    def to_dict(self) -> dict:
        return {
            "score": self.total,
            "max_score": self.max_total,
            "meets_threshold": self.meets_threshold,
            "threshold": 7,
            "items": [
                {
                    "name": item.name,
                    "passed": item.passed,
                    "points": item.points,
                    "max_points": item.max_points,
                    "evidence": item.evidence,
                }
                for item in self.items
            ],
            "suggestions": self.suggestions,
        }


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


def find_hardcoded_versions(content: str) -> List[str]:
    """Find hardcoded version strings and return matches."""
    patterns = [
        (r"claude-\d+-\d+-\w+-\d{8}", "Claude model version"),
        (r"gpt-\d+\.?\d*-\w+-\d{4}", "GPT model version"),
        (r"(?<![a-zA-Z])v\d+\.\d+\.\d+(?![a-zA-Z])", "Semantic version"),
        (r"@\d+\.\d+\.\d+", "Package version"),
    ]

    found = []
    for pattern, label in patterns:
        matches = re.findall(pattern, content)
        for match in matches:
            found.append(f"{match} ({label})")

    return found


def calculate_evolution_score(content: str) -> EvolutionScore:
    """Calculate evolution score for skill content."""
    result = EvolutionScore()

    # Base score (always granted)
    result.items.append(
        ScoreItem(
            name="base_score",
            passed=True,
            points=2,
            max_points=2,
            evidence="Base score always granted",
        )
    )

    # Extension points (2+ required)
    ext_count = count_extension_points(content)
    ext_passed = ext_count >= 2
    result.items.append(
        ScoreItem(
            name="extension_points",
            passed=ext_passed,
            points=2 if ext_passed else 0,
            max_points=2,
            evidence=f"Found {ext_count} extension points (need 2+)",
        )
    )
    if not ext_passed:
        result.suggestions.append(
            f"Add extension points section with at least 2 items (current: {ext_count})"
        )

    # No hardcoded versions
    hardcoded = find_hardcoded_versions(content)
    no_hardcoded = len(hardcoded) == 0
    result.items.append(
        ScoreItem(
            name="no_hardcoded_versions",
            passed=no_hardcoded,
            points=2 if no_hardcoded else 0,
            max_points=2,
            evidence=(
                "No hardcoded versions"
                if no_hardcoded
                else f"Found: {', '.join(hardcoded[:3])}"
            ),
        )
    )
    if not no_hardcoded:
        result.suggestions.append(
            "Remove hardcoded version strings, use configurable defaults instead"
        )

    # WHY documentation
    has_why = has_why_section(content)
    result.items.append(
        ScoreItem(
            name="why_documented",
            passed=has_why,
            points=2 if has_why else 0,
            max_points=2,
            evidence=(
                "Design rationale section exists"
                if has_why
                else "No WHY/Design Rationale section"
            ),
        )
    )
    if not has_why:
        result.suggestions.append(
            "Add '## Design Rationale' or '## WHY' section explaining design decisions"
        )

    # Anti-patterns section
    has_anti = has_anti_patterns_section(content)
    result.items.append(
        ScoreItem(
            name="anti_patterns",
            passed=has_anti,
            points=2 if has_anti else 0,
            max_points=2,
            evidence=(
                "Anti-patterns section exists"
                if has_anti
                else "No Anti-Patterns section"
            ),
        )
    )
    if not has_anti:
        result.suggestions.append(
            "Add '## Anti-Patterns' section documenting what to avoid"
        )

    return result


def format_report(score: EvolutionScore, skill_name: str = "Skill") -> str:
    """Format score report for display."""
    lines = [
        f"Evolution Score: {score.total}/{score.max_total}",
        f"Threshold: 7 ({"PASS" if score.meets_threshold else "BELOW THRESHOLD"})",
        "",
        "Breakdown:",
    ]

    for item in score.items:
        status = "✓" if item.passed else "✗"
        lines.append(f"  {status} {item.name}: {item.points}/{item.max_points}")
        lines.append(f"    {item.evidence}")

    if score.suggestions:
        lines.append("")
        lines.append("Suggestions for improvement:")
        for i, suggestion in enumerate(score.suggestions, 1):
            lines.append(f"  {i}. {suggestion}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Calculate evolution score for a skill"
    )
    parser.add_argument(
        "path", type=Path, help="Path to skill directory or SKILL.md file"
    )
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument(
        "--quiet", "-q", action="store_true", help="Only output score number"
    )

    args = parser.parse_args()

    # Determine SKILL.md path
    if args.path.is_file():
        skill_md = args.path
    else:
        skill_md = args.path / "SKILL.md"

    if not skill_md.exists():
        print(f"Error: SKILL.md not found at {skill_md}", file=sys.stderr)
        sys.exit(ExitCode.FILE_NOT_FOUND)

    # Read and score
    content = skill_md.read_text()
    score = calculate_evolution_score(content)

    # Output
    if args.quiet:
        print(score.total)
    elif args.json:
        print(json.dumps(score.to_dict(), indent=2))
    else:
        skill_name = args.path.name if args.path.is_dir() else args.path.parent.name
        print(format_report(score, skill_name))

    sys.exit(ExitCode.SUCCESS)


if __name__ == "__main__":
    main()
