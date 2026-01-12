# Validation Patterns

Patterns for implementing validation in skill scripts. Ensures consistent, reliable validation across all skill operations.

---

## Core Validation Pattern

### ValidationResult Class

Standard result object for multi-check validation:

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class ValidationResult:
    """Validation result object for multi-check tracking."""
    passed: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    def check(self, name: str, condition: bool, message: str, warning_only: bool = False):
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
```

**When to use**: Any validation that checks multiple criteria

---

## Validation Check Categories

### Required vs Optional Checks

| Category | Failure Behavior | Use For |
|----------|------------------|---------|
| Required | Blocks operation | Critical structure, syntax errors |
| Warning | Allows continuation | Best practices, recommendations |
| Informational | Display only | Scores, metrics, suggestions |

**Example**:

```python
def validate_skill(path: Path) -> ValidationResult:
    result = ValidationResult()

    # Required check - blocks if failed
    result.check("skill_md", skill_md.exists(), "SKILL.md exists")

    # Warning check - allows continuation
    result.check(
        "triggers",
        trigger_count >= 3,
        f"Has {trigger_count} triggers (recommended: 3+)",
        warning_only=True
    )

    # Informational - always passes, just reports
    result.passed.append(f"[INFO] evolution_score: {score}/10")

    return result
```

---

## YAML Frontmatter Validation

### Required Fields

```python
REQUIRED_FIELDS = {'name', 'description'}

def validate_frontmatter(frontmatter: dict) -> ValidationResult:
    result = ValidationResult()

    for field in REQUIRED_FIELDS:
        result.check(
            field,
            field in frontmatter,
            f"{field} field present"
        )

    return result
```

### Allowed Properties

```python
ALLOWED_PROPERTIES = {'name', 'description', 'license', 'allowed-tools', 'metadata'}

def check_unexpected_keys(frontmatter: dict) -> List[str]:
    return list(set(frontmatter.keys()) - ALLOWED_PROPERTIES)
```

### Name Format Validation

```python
import re

def validate_name(name: str) -> bool:
    """Validate skill name follows hyphen-case convention."""
    return (
        re.match(r'^[a-z0-9-]+$', name) and
        not name.startswith('-') and
        not name.endswith('-') and
        '--' not in name and
        len(name) <= 64
    )
```

---

## Content Validation

### Section Detection

```python
def has_section(content: str, section_name: str) -> bool:
    """Check if a markdown section exists."""
    pattern = rf'##\s*{re.escape(section_name)}'
    return bool(re.search(pattern, content, re.IGNORECASE))

# Common sections to check
RECOMMENDED_SECTIONS = [
    'Triggers',
    'Anti-Patterns',
    'Extension Points',
    'Design Rationale'
]
```

### Counting Items in Sections

```python
def count_section_items(content: str, section_name: str) -> int:
    """Count list items in a section."""
    pattern = rf'##\s*{re.escape(section_name)}\s*\n(.*?)(?=\n##|\Z)'
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)

    if not match:
        return 0

    section_content = match.group(1)
    # Count numbered or bulleted items
    items = re.findall(r'^\s*(?:\d+\.|[-*])\s+', section_content, re.MULTILINE)
    return len(items)
```

---

## Link Validation

### Internal Link Checking

```python
def validate_internal_links(skill_path: Path, content: str) -> List[str]:
    """Find broken internal links."""
    invalid_links = []

    # Find markdown links
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)

    for text, href in links:
        # Skip external links
        if href.startswith(('http://', 'https://', '#')):
            continue

        # Check if file exists
        link_path = skill_path / href
        if not link_path.exists():
            invalid_links.append(f"{href} (referenced as '{text}')")

    return invalid_links
```

---

## Python Script Validation

### Syntax Checking

```python
import ast

def validate_python_syntax(script_path: Path) -> tuple[bool, str]:
    """Check Python file for syntax errors."""
    try:
        content = script_path.read_text()
        ast.parse(content)
        return True, "Valid syntax"
    except SyntaxError as e:
        return False, f"line {e.lineno}: {e.msg}"
```

### Batch Script Validation

```python
def validate_all_scripts(skill_path: Path) -> List[str]:
    """Validate all Python scripts in skill."""
    errors = []
    scripts_dir = skill_path / 'scripts'

    if not scripts_dir.exists():
        return []

    for py_file in scripts_dir.glob('*.py'):
        valid, message = validate_python_syntax(py_file)
        if not valid:
            errors.append(f"{py_file.name}: {message}")

    return errors
```

---

## Validation Report Format

### Console Output

```python
def format_report(result: ValidationResult) -> str:
    """Format validation result for console output."""
    lines = []

    if result.errors:
        lines.append("\n=== ERRORS ===")
        for e in result.errors:
            lines.append(e)

    if result.warnings:
        lines.append("\n=== WARNINGS ===")
        for w in result.warnings:
            lines.append(w)

    if result.passed:
        lines.append("\n=== PASSED ===")
        for p in result.passed:
            lines.append(p)

    lines.append(f"\n{result.summary}")
    return "\n".join(lines)
```

### JSON Output

```python
import json

def format_json(result: ValidationResult) -> str:
    """Format validation result as JSON."""
    output = {
        "passed": result.passed,
        "warnings": result.warnings,
        "errors": result.errors,
        "is_valid": result.is_valid,
        "summary": result.summary
    }
    return json.dumps(output, indent=2)
```

---

## Validation Checklist Template

For comprehensive skill validation:

```text
STRUCTURE
[ ] SKILL.md exists
[ ] Valid YAML frontmatter
[ ] Required fields (name, description)
[ ] No unexpected properties

CONTENT
[ ] Triggers section (3+ items)
[ ] Extension Points section (2+ items)
[ ] Anti-Patterns section exists
[ ] Design Rationale section exists
[ ] No hardcoded versions

LINKS
[ ] All internal links valid
[ ] Reference files exist

SCRIPTS
[ ] All Python files have valid syntax
[ ] PEP 723 metadata present (if dependencies needed)

QUALITY
[ ] Evolution score >= 7
[ ] No similar skills found
```

---

## Exit Code Conventions

| Code | Meaning | When to Use |
|------|---------|-------------|
| 0 | Success | All checks passed |
| 1 | General error | Unexpected failure |
| 2 | Invalid arguments | Bad CLI input |
| 3 | File not found | Missing required files |
| 10 | Validation failed | Required checks failed |
| 11 | Verification failed | Post-operation verification failed |

```python
from enum import IntEnum

class ExitCode(IntEnum):
    SUCCESS = 0
    GENERAL_ERROR = 1
    INVALID_ARGUMENTS = 2
    FILE_NOT_FOUND = 3
    VALIDATION_FAILED = 10
    VERIFICATION_FAILED = 11
```
