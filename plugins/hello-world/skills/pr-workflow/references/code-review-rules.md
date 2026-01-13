# Code Review Rules

Code review rules for PR workflow. Reference this file during Step 6.

## Change Analysis

Categorize each changed file:

| Pattern | Category | Review Level |
|---------|----------|--------------|
| `*.ts`, `*.tsx`, `*.js`, `*.jsx` | Code (JS/TS) | Full review |
| `*.py` | Code (Python) | Full review |
| `*.go`, `*.rs`, `*.java` | Code (Other) | Full review |
| `*.json`, `*.yaml`, `*.toml` | Config | Secrets check only |
| `*.md`, `*.txt` | Documentation | Skip |
| Binary files | Binary | Skip (list only) |

Impact level:

- **Low**: < 50 lines changed, 1-2 files
- **Medium**: 50-200 lines changed, 3-5 files
- **High**: > 200 lines changed or > 5 files

## Readability Rules

### Variable/Function Naming

- Single-letter variables (except `i`, `j`, `k` in loops): **warning**
- Ambiguous names (`data`, `temp`, `result`, `value`) without context: **warning**
- Non-descriptive function names: **warning**

### Function Length

- Functions > 50 lines: **warning**
- Functions > 100 lines: **error** (autoFixable: false)

### Nesting Depth

- Nesting > 4 levels: **warning**
- Nesting > 6 levels: **error** (autoFixable: false)

## Error Handling Rules

### Async/Promise

- `async` function without try-catch or .catch(): **error** (autoFixable: true)
- Unhandled Promise: **error** (autoFixable: true)

### Null Safety

- Property access on potentially null without check: **warning**
- Optional chaining could be used: **warning** (autoFixable: true)

### Catch Blocks

- Empty catch block `catch (e) {}`: **error** (autoFixable: false)
- Catch block that only logs: **warning**

## Duplication Rules

- Identical code blocks (5+ lines) multiple times: **warning** (autoFixable: false)
- Similar patterns with minor variations: **warning**

Note: Duplication issues are always warnings, never blocking errors.

## Type Safety Rules (TypeScript)

### Explicit `any`

- `any` type annotation: **error** (autoFixable: true if inferrable)
- `any[]` or `Array<any>`: **error**

### Type Assertions

- More than 3 type assertions in one file: **warning**
- Force casting `as unknown as Type`: **error** (autoFixable: false)

### Missing Types

- Function parameters without type: **error** (autoFixable: true)
- Return type not specified for exported functions: **warning** (autoFixable: true)

## Config File Rules

- Hardcoded secrets/passwords/API keys: **error** (autoFixable: false)
- Localhost URLs in production config: **warning**

## Pass/Fail Criteria

- **PASS**: Zero errors (warnings allowed)
- **FAIL**: One or more errors present

## Auto-Fix Capabilities

| Issue Type | Fix Method | Risk |
|------------|------------|------|
| Formatting | prettier/eslint --fix | Low |
| Lint issues | eslint --fix | Low |
| Missing types | Add explicit types | Medium |
| Error handling | Add try-catch | Medium |

### Auto-Fix Transformations

**Missing try-catch**:

```typescript
// Before
async function foo() {
  const result = await someAsyncOperation();
  return result;
}

// After
async function foo() {
  try {
    const result = await someAsyncOperation();
    return result;
  } catch (error) {
    console.error('Error in foo:', error);
    throw error;
  }
}
```

**Optional chaining**:

```typescript
// Before
if (obj && obj.prop && obj.prop.value) { ... }

// After
if (obj?.prop?.value) { ... }
```
