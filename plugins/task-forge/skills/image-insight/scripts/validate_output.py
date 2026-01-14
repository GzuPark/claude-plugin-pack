#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = []
# ///

"""Validates image analyzer JSON output structure and completeness."""

import json
import sys
from pathlib import Path
from typing import Any

REQUIRED_SECTIONS = [
    "metadata",
    "composition",
    "color_profile",
    "lighting",
    "technical_specs",
    "artistic_elements",
    "subject_analysis",
    "background",
    "generation_parameters",
]

METADATA_FIELDS = ["confidence_score", "image_type", "primary_purpose"]
COMPOSITION_FIELDS = ["rule_applied", "aspect_ratio", "layout", "focal_points"]
COLOR_FIELDS = ["dominant_colors", "color_palette", "temperature", "saturation"]
LIGHTING_FIELDS = ["type", "direction", "quality", "shadows", "highlights"]


def validate_structure(data: dict[str, Any]) -> list[str]:
    """Validate JSON structure and required sections."""
    errors = []

    # Check required sections
    for section in REQUIRED_SECTIONS:
        if section not in data:
            errors.append(f"Missing required section: {section}")

    # Validate metadata
    if "metadata" in data:
        for field in METADATA_FIELDS:
            if field not in data["metadata"]:
                errors.append(f"metadata missing field: {field}")

    # Validate composition
    if "composition" in data:
        for field in COMPOSITION_FIELDS:
            if field not in data["composition"]:
                errors.append(f"composition missing field: {field}")

    # Validate color_profile
    if "color_profile" in data:
        colors = data["color_profile"].get("dominant_colors", [])
        if not colors:
            errors.append("color_profile.dominant_colors is empty")
        for i, color in enumerate(colors):
            if "hex" not in color:
                errors.append(f"color_profile.dominant_colors[{i}] missing hex code")
            elif not color["hex"].startswith("#"):
                errors.append(
                    f"color_profile.dominant_colors[{i}] hex must start with #"
                )

    # Validate lighting
    if "lighting" in data:
        for field in LIGHTING_FIELDS:
            if field not in data["lighting"]:
                errors.append(f"lighting missing field: {field}")

    # Validate generation_parameters
    if "generation_parameters" in data:
        if "prompts" not in data["generation_parameters"]:
            errors.append("generation_parameters missing prompts")
        elif not data["generation_parameters"]["prompts"]:
            errors.append("generation_parameters.prompts is empty")
        if "keywords" not in data["generation_parameters"]:
            errors.append("generation_parameters missing keywords")

    return errors


def validate_quality(data: dict[str, Any]) -> list[str]:
    """Check for quality anti-patterns."""
    warnings = []

    # Check for vague terms
    vague_terms = ["nice", "good", "beautiful", "pretty", "great", "perfect"]
    json_str = json.dumps(data).lower()

    for term in vague_terms:
        if f'"{term}"' in json_str or f" {term} " in json_str:
            warnings.append(
                f"Quality warning: Found vague term '{term}' - use specific descriptions"
            )

    # Check hair description for "perfect"
    if "subject_analysis" in data and "hair" in data.get("subject_analysis", {}):
        hair = data["subject_analysis"]["hair"]
        hair_str = json.dumps(hair).lower()
        if "perfect" in hair_str:
            warnings.append(
                "Quality warning: Hair described as 'perfect' - describe natural imperfections instead"
            )

    return warnings


def validate_output(json_path: str) -> tuple[bool, list[str], list[str]]:
    """
    Validate JSON output file.

    Returns:
        (success, errors, warnings)
    """
    errors = []
    warnings = []

    path = Path(json_path)
    if not path.exists():
        return False, [f"File not found: {json_path}"], []

    try:
        with open(path) as f:
            content = f.read().strip()
            # Remove markdown code blocks if present
            if content.startswith("```"):
                lines = content.split("\n")
                content = "\n".join(lines[1:-1] if lines[-1] == "```" else lines[1:])
            data = json.loads(content)
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON: {e}"], []

    errors.extend(validate_structure(data))
    warnings.extend(validate_quality(data))

    return len(errors) == 0, errors, warnings


def main():
    if len(sys.argv) != 2:
        print("Usage: validate_output.py <json_file>")
        print("\nValidates image analyzer JSON output for structure and quality.")
        sys.exit(2)

    success, errors, warnings = validate_output(sys.argv[1])

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"  - {warning}")
        print()

    if success:
        print("Validation passed")
        sys.exit(0)
    else:
        print("Validation failed:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(10)


if __name__ == "__main__":
    main()
