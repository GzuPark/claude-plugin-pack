#!/usr/bin/env python3
# Recommended: use ./run.sh to execute this script for proper dependency management
# /// script
# dependencies = []
# ///
"""
Skill Initializer - Creates a new skill from template

Usage:
    init_skill.py <skill-name> --path <path>

Examples:
    init_skill.py my-new-skill --path skills/public
    init_skill.py my-api-helper --path skills/private
    init_skill.py custom-skill --path /custom/location
"""

import sys
from pathlib import Path


SKILL_TEMPLATE = """---
name: {skill_name}
description: [TODO: Complete and informative explanation of what the skill does and when to use it. Include WHEN to use this skill - specific scenarios, file types, or tasks that trigger it.]
---

# {skill_title}

## Overview

[TODO: 1-2 sentences explaining what this skill enables]

## Triggers

[TODO: Add 3-5 trigger phrases that invoke this skill]

- `{skill_name}` - [Primary trigger description]
- [TODO: Add more triggers - aim for 3-5 total]

## Structuring This Skill

[TODO: Choose the structure that best fits this skill's purpose. Common patterns:

**1. Workflow-Based** (best for sequential processes)
- Works well when there are clear step-by-step procedures
- Example: DOCX skill with "Workflow Decision Tree" → "Reading" → "Creating" → "Editing"
- Structure: ## Overview → ## Workflow Decision Tree → ## Step 1 → ## Step 2...

**2. Task-Based** (best for tool collections)
- Works well when the skill offers different operations/capabilities
- Example: PDF skill with "Quick Start" → "Merge PDFs" → "Split PDFs" → "Extract Text"
- Structure: ## Overview → ## Quick Start → ## Task Category 1 → ## Task Category 2...

**3. Reference/Guidelines** (best for standards or specifications)
- Works well for brand guidelines, coding standards, or requirements
- Example: Brand styling with "Brand Guidelines" → "Colors" → "Typography" → "Features"
- Structure: ## Overview → ## Guidelines → ## Specifications → ## Usage...

**4. Capabilities-Based** (best for integrated systems)
- Works well when the skill provides multiple interrelated features
- Example: Product Management with "Core Capabilities" → numbered capability list
- Structure: ## Overview → ## Core Capabilities → ### 1. Feature → ### 2. Feature...

Patterns can be mixed and matched as needed. Most skills combine patterns (e.g., start with task-based, add workflow for complex operations).

Delete this entire "Structuring This Skill" section when done - it's just guidance.]

## [TODO: Replace with the first main section based on chosen structure]

[TODO: Add content here. See examples in existing skills:
- Code samples for technical skills
- Decision trees for complex workflows
- Concrete examples with realistic user requests
- References to scripts/templates/references as needed]

## Anti-Patterns

[TODO: Document what to avoid when using this skill. Consider:
- Common mistakes users might make
- Misuse patterns that lead to poor results
- Edge cases that should be handled differently]

- **[Anti-pattern name]**: [Description of what to avoid and why]

## Extension Points

[TODO: Add at least 2 extension points for future customization]

1. **[Extension point 1]**: [How this skill can be extended or customized]
2. **[Extension point 2]**: [Another way to extend the skill]

## Resources

This skill includes example resource directories that demonstrate how to organize different types of bundled resources:

### scripts/
Executable code (Python/Bash/etc.) that can be run directly to perform specific operations.

**Running scripts:** Use the `run.sh` wrapper to execute Python scripts with proper dependency management:

```bash
./run.sh scripts/example.py [args...]
```

> **Note**: `run.sh` automatically handles dependencies. It uses `uv` if available,
> or falls back to a shared virtual environment (~/.claude/skills/.venv).

**Examples from other skills:**
- PDF skill: `fill_fillable_fields.py`, `extract_form_field_info.py` - utilities for PDF manipulation
- DOCX skill: `document.py`, `utilities.py` - Python modules for document processing

**Appropriate for:** Python scripts, shell scripts, or any executable code that performs automation, data processing, or specific operations.

**Note:** Scripts may be executed without loading into context, but can still be read by Claude for patching or environment adjustments.

### references/
Documentation and reference material intended to be loaded into context to inform Claude's process and thinking.

**Examples from other skills:**
- Product management: `communication.md`, `context_building.md` - detailed workflow guides
- BigQuery: API reference documentation and query examples
- Finance: Schema documentation, company policies

**Appropriate for:** In-depth documentation, API references, database schemas, comprehensive guides, or any detailed information that Claude should reference while working.

### assets/
Files not intended to be loaded into context, but rather used within the output Claude produces.

**Examples from other skills:**
- Brand styling: PowerPoint template files (.pptx), logo files
- Frontend builder: HTML/React boilerplate project directories
- Typography: Font files (.ttf, .woff2)

**Appropriate for:** Templates, boilerplate code, document templates, images, icons, fonts, or any files meant to be copied or used in the final output.

---

**Any unneeded directories can be deleted.** Not every skill requires all three types of resources.

## Design Rationale

[TODO: Explain WHY this skill was designed this way. Document:
- Key design decisions and their rationale
- Trade-offs that were considered
- Why certain approaches were chosen over alternatives]
"""

EXAMPLE_SCRIPT = '''#!/usr/bin/env python3
# Recommended: use ./run.sh to execute this script for proper dependency management
# /// script
# dependencies = []
# ///
"""
Example helper script for {skill_name}

This is a placeholder script that can be executed directly.
Replace with actual implementation or delete if not needed.

Usage:
    ./run.sh scripts/example.py [args...]

Example real scripts from other skills:
- pdf/scripts/fill_fillable_fields.py - Fills PDF form fields
- pdf/scripts/convert_pdf_to_images.py - Converts PDF pages to images
"""

def main():
    print("This is an example script for {skill_name}")
    # TODO: Add actual script logic here
    # This could be data processing, file conversion, API calls, etc.

if __name__ == "__main__":
    main()
'''

EXAMPLE_REFERENCE = """# Reference Documentation for {skill_title}

This is a placeholder for detailed reference documentation.
Replace with actual reference content or delete if not needed.

Example real reference docs from other skills:
- product-management/references/communication.md - Comprehensive guide for status updates
- product-management/references/context_building.md - Deep-dive on gathering context
- bigquery/references/ - API references and query examples

## When Reference Docs Are Useful

Reference docs are ideal for:
- Comprehensive API documentation
- Detailed workflow guides
- Complex multi-step processes
- Information too lengthy for main SKILL.md
- Content that's only needed for specific use cases

## Structure Suggestions

### API Reference Example
- Overview
- Authentication
- Endpoints with examples
- Error codes
- Rate limits

### Workflow Guide Example
- Prerequisites
- Step-by-step instructions
- Common patterns
- Troubleshooting
- Best practices
"""

EXAMPLE_ASSET = """# Example Asset File

This placeholder represents where asset files would be stored.
Replace with actual asset files (templates, images, fonts, etc.) or delete if not needed.

Asset files are NOT intended to be loaded into context, but rather used within
the output Claude produces.

Example asset files from other skills:
- Brand guidelines: logo.png, slides_template.pptx
- Frontend builder: hello-world/ directory with HTML/React boilerplate
- Typography: custom-font.ttf, font-family.woff2
- Data: sample_data.csv, test_dataset.json

## Common Asset Types

- Templates: .pptx, .docx, boilerplate directories
- Images: .png, .jpg, .svg, .gif
- Fonts: .ttf, .otf, .woff, .woff2
- Boilerplate code: Project directories, starter files
- Icons: .ico, .svg
- Data files: .csv, .json, .xml, .yaml

Note: This is a text placeholder. Actual assets can be any file type.
"""

RUN_SH_TEMPLATE = """#!/bin/bash
# run.sh - Python script runner with uv priority and fallback
#
# Usage: ./run.sh scripts/example.py [args...]
#
# Execution priority:
# 1. uv run (if uv is available)
# 2. Fallback to python with shared venv (~/.claude/skills/.venv)

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SHARED_VENV="$HOME/.claude/skills/.venv"
SCRIPT_PATH="$1"
shift || true

if [ -z "$SCRIPT_PATH" ]; then
    echo "Usage: ./run.sh <script.py> [args...]"
    exit 1
fi

# Resolve script path relative to skill directory
if [[ ! "$SCRIPT_PATH" = /* ]]; then
    SCRIPT_PATH="$SCRIPT_DIR/$SCRIPT_PATH"
fi

# Check if uv is available
if command -v uv &> /dev/null; then
    exec uv run "$SCRIPT_PATH" "$@"
fi

# Fallback: Parse inline metadata and use shared venv
echo "uv not found, using fallback with shared venv..."

# Parse dependencies from inline script metadata
# Supports: # /// script
#           # dependencies = ["pkg1", "pkg2>=1.0"]
#           # ///
parse_dependencies() {
    local script="$1"
    local in_metadata=0
    local deps=""

    while IFS= read -r line; do
        if [[ "$line" =~ ^#[[:space:]]*///[[:space:]]*script ]]; then
            in_metadata=1
            continue
        fi
        if [[ $in_metadata -eq 1 && "$line" =~ ^#[[:space:]]*/// ]]; then
            break
        fi
        if [[ $in_metadata -eq 1 && "$line" =~ ^#[[:space:]]*dependencies[[:space:]]*=[[:space:]]*\\[(.*)] ]]; then
            deps="${BASH_REMATCH[1]}"
            # Clean up: remove quotes and spaces
            deps=$(echo "$deps" | sed 's/"//g' | sed "s/'//g" | sed 's/[[:space:]]//g')
            break
        fi
    done < "$script"

    echo "$deps"
}

# Check for complex metadata that requires uv
check_complex_metadata() {
    local script="$1"
    if grep -q "^\\#[[:space:]]*\\(requires-python\\|optional-dependencies\\|\\[tool\\.\\)" "$script" 2>/dev/null; then
        echo "Warning: Complex PEP 723 metadata detected. Please install uv for full support:" >&2
        echo "  curl -LsSf https://astral.sh/uv/install.sh | sh" >&2
        echo "Continuing with basic dependency parsing..." >&2
    fi
}

# Create shared venv if it doesn't exist
ensure_venv() {
    if [ ! -d "$SHARED_VENV" ]; then
        echo "Creating shared venv at $SHARED_VENV..."
        python3 -m venv "$SHARED_VENV"
    fi
}

# Install dependencies to shared venv
install_deps() {
    local deps="$1"
    if [ -n "$deps" ]; then
        echo "Installing dependencies: $deps"
        IFS=',' read -ra DEP_ARRAY <<< "$deps"
        "$SHARED_VENV/bin/pip" install -q "${DEP_ARRAY[@]}"
    fi
}

# Main fallback logic
check_complex_metadata "$SCRIPT_PATH"
ensure_venv

DEPS=$(parse_dependencies "$SCRIPT_PATH")
install_deps "$DEPS"

exec "$SHARED_VENV/bin/python" "$SCRIPT_PATH" "$@"
"""


def title_case_skill_name(skill_name):
    """Convert hyphenated skill name to Title Case for display."""
    return " ".join(word.capitalize() for word in skill_name.split("-"))


def init_skill(skill_name, path):
    """
    Initialize a new skill directory with template SKILL.md.

    Args:
        skill_name: Name of the skill
        path: Path where the skill directory should be created

    Returns:
        Path to created skill directory, or None if error
    """
    # Determine skill directory path
    skill_dir = Path(path).resolve() / skill_name

    # Check if directory already exists
    if skill_dir.exists():
        print(f"❌ Error: Skill directory already exists: {skill_dir}")
        return None

    # Create skill directory
    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"✅ Created skill directory: {skill_dir}")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        return None

    # Create SKILL.md from template
    skill_title = title_case_skill_name(skill_name)
    skill_content = SKILL_TEMPLATE.format(
        skill_name=skill_name, skill_title=skill_title
    )

    skill_md_path = skill_dir / "SKILL.md"
    try:
        skill_md_path.write_text(skill_content)
        print("✅ Created SKILL.md")
    except Exception as e:
        print(f"❌ Error creating SKILL.md: {e}")
        return None

    # Create resource directories with example files
    try:
        # Create scripts/ directory with example script
        scripts_dir = skill_dir / "scripts"
        scripts_dir.mkdir(exist_ok=True)
        example_script = scripts_dir / "example.py"
        example_script.write_text(EXAMPLE_SCRIPT.format(skill_name=skill_name))
        example_script.chmod(0o755)
        print("✅ Created scripts/example.py")

        # Create references/ directory with example reference doc
        references_dir = skill_dir / "references"
        references_dir.mkdir(exist_ok=True)
        example_reference = references_dir / "api_reference.md"
        example_reference.write_text(EXAMPLE_REFERENCE.format(skill_title=skill_title))
        print("✅ Created references/api_reference.md")

        # Create assets/ directory with example asset placeholder
        assets_dir = skill_dir / "assets"
        assets_dir.mkdir(exist_ok=True)
        example_asset = assets_dir / "example_asset.txt"
        example_asset.write_text(EXAMPLE_ASSET)
        print("✅ Created assets/example_asset.txt")

        # Create run.sh for Python script execution
        run_sh = skill_dir / "run.sh"
        run_sh.write_text(RUN_SH_TEMPLATE)
        run_sh.chmod(0o755)
        print("✅ Created run.sh")
    except Exception as e:
        print(f"❌ Error creating resource directories: {e}")
        return None

    # Print next steps
    print(f"\n✅ Skill '{skill_name}' initialized successfully at {skill_dir}")
    print("\nNext steps:")
    print("1. Edit SKILL.md to complete the TODO items and update the description")
    print(
        "2. Customize or delete the example files in scripts/, references/, and assets/"
    )
    print("3. Run the validator when ready to check the skill structure")

    return skill_dir


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Initialize a new skill from template",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Skill name requirements:
  - Hyphen-case identifier (e.g., 'data-analyzer')
  - Lowercase letters, digits, and hyphens only
  - Max 40 characters
  - Must match directory name exactly

Examples:
  init_skill.py my-new-skill --path skills/public
  init_skill.py my-api-helper --path skills/private --mode complex
  init_skill.py custom-skill --path /custom/location
        """,
    )

    parser.add_argument("skill_name", help="Name of the skill (hyphen-case)")
    parser.add_argument(
        "--path", required=True, help="Path where skill directory will be created"
    )
    parser.add_argument(
        "--mode",
        choices=["simple", "complex"],
        default="simple",
        help="Skill complexity mode: 'simple' for basic skills, 'complex' for skills with external integrations (default: simple)",
    )

    args = parser.parse_args()

    print(f"🚀 Initializing skill: {args.skill_name}")
    print(f"   Location: {args.path}")
    print(f"   Mode: {args.mode}")
    if args.mode == "complex":
        print(
            "   (Complex mode: 6-Lens Framework and Regression Questioning recommended)"
        )
    print()

    result = init_skill(args.skill_name, args.path)

    if result:
        if args.mode == "complex":
            print("\n📚 For complex skills, consider applying:")
            print("   - 6-Lens Framework (see references/analysis-lenses.md)")
            print(
                "   - Regression Questioning Protocol (see references/regression-questioning.md)"
            )
        sys.exit(0)
    else:
        sys.exit(1)


if __name__ == "__main__":
    main()
