#!/usr/bin/env python3
# Recommended: use ./run.sh to execute this script for proper dependency management
# /// script
# dependencies = ["pyyaml"]
# ///
"""
Skill duplicate checker - finds similar existing skills to prevent duplication.

Similarity calculation:
- Name similarity: 30% weight
- Description similarity: 70% weight
- Threshold: 50% (warns if similarity >= 50%)
"""

import sys
import re
import argparse
import json
from pathlib import Path
from dataclasses import dataclass
from typing import List, Optional
from enum import IntEnum

# Try to import yaml, fallback to simple parser
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
class SkillInfo:
    """Information about a skill."""

    name: str
    description: str
    path: Path


@dataclass
class SimilarityResult:
    """Result of similarity comparison."""

    skill: SkillInfo
    name_similarity: float
    description_similarity: float
    total_similarity: float

    def to_dict(self) -> dict:
        return {
            "name": self.skill.name,
            "path": str(self.skill.path),
            "name_similarity": round(self.name_similarity * 100, 1),
            "description_similarity": round(self.description_similarity * 100, 1),
            "total_similarity": round(self.total_similarity * 100, 1),
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


def extract_frontmatter(content: str) -> Optional[dict]:
    """Extract YAML frontmatter from content."""
    if not content.startswith("---"):
        return None

    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None

    frontmatter_text = match.group(1)

    try:
        if HAS_YAML:
            frontmatter = yaml.safe_load(frontmatter_text)
        else:
            frontmatter = parse_yaml_simple(frontmatter_text)
        return frontmatter if isinstance(frontmatter, dict) else None
    except Exception:
        return None


def tokenize(text: str) -> set:
    """Tokenize text into words for comparison."""
    # Convert to lowercase and extract words
    words = re.findall(r"[a-z]+", text.lower())
    # Also include hyphenated parts
    parts = text.lower().replace("-", " ").replace("_", " ").split()
    return set(words) | set(parts)


def jaccard_similarity(set1: set, set2: set) -> float:
    """Calculate Jaccard similarity between two sets."""
    if not set1 and not set2:
        return 0.0
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0.0


def calculate_similarity(skill1: SkillInfo, skill2: SkillInfo) -> SimilarityResult:
    """Calculate similarity between two skills."""
    # Name similarity (30% weight)
    name_tokens1 = tokenize(skill1.name)
    name_tokens2 = tokenize(skill2.name)
    name_sim = jaccard_similarity(name_tokens1, name_tokens2)

    # Description similarity (70% weight)
    desc_tokens1 = tokenize(skill1.description)
    desc_tokens2 = tokenize(skill2.description)
    desc_sim = jaccard_similarity(desc_tokens1, desc_tokens2)

    # Weighted total
    total_sim = (name_sim * 0.3) + (desc_sim * 0.7)

    return SimilarityResult(
        skill=skill2,
        name_similarity=name_sim,
        description_similarity=desc_sim,
        total_similarity=total_sim,
    )


def discover_skills(search_paths: List[Path]) -> List[SkillInfo]:
    """Discover all skills in given paths."""
    skills = []

    for base_path in search_paths:
        if not base_path.exists():
            continue

        # Look for SKILL.md files
        for skill_md in base_path.rglob("SKILL.md"):
            try:
                content = skill_md.read_text()
                frontmatter = extract_frontmatter(content)
                if frontmatter and "name" in frontmatter:
                    skills.append(
                        SkillInfo(
                            name=frontmatter.get("name", ""),
                            description=frontmatter.get("description", ""),
                            path=skill_md.parent,
                        )
                    )
            except Exception:
                continue

    return skills


def check_duplicates(
    skill_name: str,
    skill_description: str,
    threshold: float = 0.5,
    exclude_path: Optional[Path] = None,
) -> List[SimilarityResult]:
    """
    Check for duplicate or similar skills.

    Args:
        skill_name: Name of the skill to check
        skill_description: Description of the skill
        threshold: Similarity threshold (0.0 to 1.0)
        exclude_path: Path to exclude from comparison (e.g., the skill being created)

    Returns:
        List of similar skills above threshold
    """
    # Define search paths
    search_paths = [
        Path.home() / ".claude" / "skills",  # User skills
        Path.home()
        / ".claude"
        / "commands",  # User commands (may have overlapping functionality)
    ]

    # Also check project-local skills if in a project
    cwd = Path.cwd()
    project_skills = cwd / ".claude" / "skills"
    if project_skills.exists():
        search_paths.append(project_skills)

    # Discover existing skills
    existing_skills = discover_skills(search_paths)

    # Create skill info for comparison
    new_skill = SkillInfo(
        name=skill_name, description=skill_description, path=Path(".")
    )

    # Find similar skills
    similar = []
    for skill in existing_skills:
        # Skip if this is the same skill being created/updated
        if exclude_path and skill.path.resolve() == exclude_path.resolve():
            continue

        result = calculate_similarity(new_skill, skill)
        if result.total_similarity >= threshold:
            similar.append(result)

    # Sort by similarity (highest first)
    similar.sort(key=lambda x: x.total_similarity, reverse=True)

    return similar


def format_report(similar: List[SimilarityResult], threshold: float) -> str:
    """Format similarity report for display."""
    if not similar:
        return "No similar skills found."

    lines = [
        f"Found {len(similar)} similar skill(s) (threshold: {threshold*100:.0f}%):",
        "",
    ]

    for result in similar:
        lines.append(f"  - {result.skill.name}")
        lines.append(f"    Path: {result.skill.path}")
        lines.append(f"    Similarity: {result.total_similarity*100:.1f}%")
        lines.append(
            f"    (name: {result.name_similarity*100:.1f}%, description: {result.description_similarity*100:.1f}%)"
        )
        lines.append("")

    lines.append("Consider reviewing these skills before creating a new one.")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Check for similar existing skills")
    parser.add_argument("name", help="Skill name to check")
    parser.add_argument("description", help="Skill description to check")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.5,
        help="Similarity threshold (0.0-1.0, default: 0.5)",
    )
    parser.add_argument("--exclude", type=Path, help="Path to exclude from comparison")
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    if not 0.0 <= args.threshold <= 1.0:
        print("Error: threshold must be between 0.0 and 1.0", file=sys.stderr)
        sys.exit(ExitCode.INVALID_ARGUMENTS)

    similar = check_duplicates(
        args.name, args.description, args.threshold, args.exclude
    )

    if args.json:
        output = {
            "similar_skills": [r.to_dict() for r in similar],
            "threshold": args.threshold * 100,
            "found_duplicates": len(similar) > 0,
        }
        print(json.dumps(output, indent=2))
    else:
        print(format_report(similar, args.threshold))

    # Exit with status indicating if duplicates found
    sys.exit(ExitCode.SUCCESS)


if __name__ == "__main__":
    main()
