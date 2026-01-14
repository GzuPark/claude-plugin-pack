# Script Pattern Catalog

Standard Python patterns for skill scripts. Ensures consistency,
reliability, and autonomous execution capability.

---

## Core Patterns

### Pattern 1: Result Dataclass

Standard return object for all script operations.

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Result:
    """Standard result object for script operations."""
    success: bool
    message: str
    data: dict = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def __bool__(self) -> bool:
        """Usable in boolean context."""
        return self.success

# Usage example
def process_file(path: Path) -> Result:
    if not path.exists():
        return Result(
            success=False,
            message=f"File not found: {path}",
            errors=[f"File not found: {path}"]
        )

    # Process...
    return Result(
        success=True,
        message="Processing complete",
        data={"processed_lines": 42}
    )
```

**When to use**: Any script that returns status

---

### Pattern 2: ValidationResult Class

Specialized result object for multi-check validation scripts.

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class ValidationResult:
    """Validation result object for multi-check tracking."""
    passed: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

    def check(
        self,
        name: str,
        condition: bool,
        message: str,
        warning_only: bool = False
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
        return (
            f"{len(self.passed)}/{total} passed, "
            f"{len(self.warnings)} warnings, "
            f"{len(self.errors)} errors"
        )

# Usage example
def validate_skill(path: Path) -> ValidationResult:
    result = ValidationResult()

    result.check("file_exists", path.exists(), "SKILL.md exists")
    result.check(
        "has_triggers",
        "## Triggers" in content,
        "Has triggers",
        warning_only=True
    )

    return result
```

**When to use**: Validation scripts that check multiple criteria

---

### Pattern 3: Standard Exit Codes

Consistent exit codes for script chaining.

```python
import sys
from enum import IntEnum

class ExitCode(IntEnum):
    """Standard exit codes for skill scripts."""
    SUCCESS = 0           # Success
    GENERAL_ERROR = 1     # General failure
    INVALID_ARGUMENTS = 2 # Invalid arguments
    FILE_NOT_FOUND = 3    # File not found
    PERMISSION_DENIED = 4 # Permission denied
    VALIDATION_FAILED = 10    # Validation failed
    VERIFICATION_FAILED = 11  # Verification failed
    DEPENDENCY_ERROR = 20     # Dependency error

def main():
    try:
        result = process()

        if not result.success:
            if "validation" in result.message.lower():
                sys.exit(ExitCode.VALIDATION_FAILED)
            sys.exit(ExitCode.GENERAL_ERROR)

        sys.exit(ExitCode.SUCCESS)

    except FileNotFoundError:
        sys.exit(ExitCode.FILE_NOT_FOUND)
    except PermissionError:
        sys.exit(ExitCode.PERMISSION_DENIED)
```

**Quick Reference**:

| Code | Meaning |
| ---- | ------- |
| 0 | Success |
| 1 | General failure |
| 2 | Invalid arguments |
| 3 | File not found |
| 10 | Validation failed |
| 11 | Verification failed |

---

### Pattern 4: JSON State Persistence

Pattern for tracking state across sessions.

```python
from pathlib import Path
from datetime import datetime
import json

def get_state_path(skill_name: str) -> Path:
    """Return state file path."""
    return (
        Path.home() / ".claude" / "skills" / ".state"
        / f"{skill_name}.json"
    )

def load_state(path: Path) -> dict:
    """Load state (graceful fallback on corruption)."""
    if not path.exists():
        return {
            "version": "1.0",
            "created_at": datetime.now().isoformat(),
            "data": {}
        }

    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError:
        # Backup corrupted file
        backup = path.with_suffix(".json.bak")
        path.rename(backup)
        return {
            "version": "1.0",
            "data": {},
            "recovered_from": str(backup)
        }

def save_state(path: Path, state: dict) -> None:
    """Save state atomically."""
    path.parent.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = datetime.now().isoformat()

    # Write to temp file first (atomic save)
    temp_path = path.with_suffix(".json.tmp")
    temp_path.write_text(json.dumps(state, indent=2))
    temp_path.rename(path)
```

**When to use**: Progress tracking, multi-session workflows, caching

---

### Pattern 5: Graceful Dependency Fallback

Handles optional dependencies gracefully.

```python
# YAML parsing fallback
def parse_yaml(text: str) -> dict:
    """Parse with fallback if PyYAML unavailable."""
    try:
        import yaml
        return yaml.safe_load(text)
    except ImportError:
        # Fallback: basic key-value parsing for simple YAML
        result = {}
        for line in text.split('\n'):
            stripped = line.strip()
            if not stripped or stripped.startswith('#'):
                continue
            if ':' in line and not line.startswith(' '):
                key, value = line.split(':', 1)
                result[key.strip()] = value.strip().strip('"\'')
        return result

# Styled output fallback
def print_styled(message: str, style: str = "normal"):
    """Print with optional rich styling."""
    try:
        from rich.console import Console
        console = Console()
        styles = {
            "success": "[green]",
            "error": "[red]",
            "warning": "[yellow]"
        }
        console.print(f"{styles.get(style, '')}{message}")
    except ImportError:
        prefixes = {
            "success": "[OK] ",
            "error": "[ERROR] ",
            "warning": "[WARN] "
        }
        print(f"{prefixes.get(style, '')}{message}")
```

**When to use**: Always provide fallback when using non-standard libraries

---

### Pattern 6: Simple Argparse

Pattern for single-purpose scripts.

```python
import argparse
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(
        description="Validate skill directory"
    )

    # Positional argument
    parser.add_argument("path", type=Path, help="Skill directory path")

    # Optional flags
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Verbose output"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output as JSON"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors"
    )

    args = parser.parse_args()

    # Input validation
    if not args.path.exists():
        print(f"Error: Path not found: {args.path}", file=sys.stderr)
        sys.exit(2)

    # Process
    result = validate(args.path, verbose=args.verbose)

    # Output
    if args.json:
        print(json.dumps(result.to_dict()))
    else:
        print(result.format_report())

    sys.exit(0 if result.is_valid else 1)

if __name__ == "__main__":
    main()
```

**When to use**: Single-purpose scripts for validation, generation,
transformation

---

## Script Category Guide

| Category | Purpose | Patterns |
| -------- | ------- | -------- |
| Validation | Verify standards | ValidationResult + Simple argparse |
| State Mgmt | Progress, data | JSON state + Subcommand argparse |
| Generation | Create artifacts | Result + Template substitution |
| Transform | Data convert | Result + Input/output argparse |
| Calculation | Metrics/score | Result + JSON output |

---

## Self-Verification Pattern

Scripts verify their own output.

```python
def execute_with_verification(input_data, verify_func):
    """Execute operation then verify result."""
    try:
        output = process(input_data)
        is_valid, reason = verify_func(output)

        if not is_valid:
            return Result(
                success=False,
                message=f"Verification failed: {reason}",
                errors=[reason]
            )

        return Result(
            success=True,
            message="Operation complete and verified",
            data={"output": output, "verified": True}
        )
    except Exception as e:
        return Result(
            success=False,
            message=f"Execution failed: {e}",
            errors=[str(e)]
        )

# Verification function example
def verify_file_exists(path):
    """Verify file creation."""
    if Path(path).exists():
        return True, f"File exists: {path}"
    return False, f"File not created: {path}"
```

**When to use**: All scripts that generate verifiable output

---

## PEP 723 Inline Metadata

Dependency declaration for use with run.sh.

```python
#!/usr/bin/env python3
# /// script
# dependencies = ["pyyaml", "requests>=2.28"]
# ///
"""
Script description.
"""

import yaml
import requests
# ...
```

run.sh automatically installs dependencies via uv or shared venv.

---

## Quick Reference

| Pattern | Use Case | Key Imports |
| ------- | -------- | ----------- |
| Result dataclass | Return values | `dataclasses`, `typing` |
| ValidationResult | Multi-check | `dataclasses`, `typing` |
| Standard Exit codes | Script chaining | `sys`, `enum` |
| JSON state | State persistence | `json`, `pathlib` |
| Graceful fallback | Optional deps | try/except ImportError |
| Simple argparse | Single-purpose | `argparse` |
| Self-verification | Autonomous ops | (pattern, no imports) |
