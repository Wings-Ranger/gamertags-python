# Python Raising Exceptions

**W3Schools Link:** https://www.w3schools.com/python/python_try_except.asp

---

## Overview
The `raise` statement lets you throw an exception intentionally — either a built-in exception or a custom one. Raising exceptions is how you enforce preconditions, validate inputs at function boundaries, and signal error conditions to callers. Custom exception classes make your program's error handling expressive and specific.

## Key Concepts
- **`raise ExceptionType("message")`**: raises an exception with a descriptive message
- **`raise`** (bare): re-raises the current exception — used inside `except` blocks
- **`raise ... from e`**: chains exceptions to preserve context (Python 3)
- **Custom exceptions**: subclass `Exception` (or a more specific class) for domain-specific errors
- **When to raise**: at function entry when preconditions are not met
- **`assert`**: a lightweight way to raise `AssertionError` for developer-facing checks (not for user input)

## Syntax / Example Code
```python
# --- Raising built-in exceptions ---

def set_score(score):
    """Set a player's score; must be non-negative."""
    if not isinstance(score, int):
        raise TypeError(f"Score must be an integer, got {type(score).__name__}")
    if score < 0:
        raise ValueError(f"Score cannot be negative: {score}")
    return score

try:
    set_score(-100)
except ValueError as e:
    print(f"Error: {e}")

try:
    set_score("4250")
except TypeError as e:
    print(f"Error: {e}")

# --- Custom exception classes ---

class GamertagError(Exception):
    """Base exception for gamertag validation errors."""
    pass

class GamertagTooShortError(GamertagError):
    """Raised when a gamertag is shorter than the minimum length."""
    def __init__(self, tag, min_length=3):
        self.tag = tag
        self.min_length = min_length
        super().__init__(
            f"Gamertag '{tag}' is too short "
            f"(length {len(tag)}, minimum {min_length})"
        )

class GamertagTooLongError(GamertagError):
    def __init__(self, tag, max_length=15):
        self.tag = tag
        self.max_length = max_length
        super().__init__(
            f"Gamertag '{tag}' is too long "
            f"(length {len(tag)}, maximum {max_length})"
        )

class InvalidCharactersError(GamertagError):
    def __init__(self, tag):
        super().__init__(f"Gamertag '{tag}' contains invalid characters")

# --- Validation function using custom exceptions ---

def validate_gamertag(tag):
    """Validate a gamertag, raising descriptive exceptions on failure."""
    if not tag:
        raise GamertagError("Gamertag cannot be empty")
    if len(tag) < 3:
        raise GamertagTooShortError(tag)
    if len(tag) > 15:
        raise GamertagTooLongError(tag)
    if not tag.isalnum():
        raise InvalidCharactersError(tag)
    return tag  # valid

# Using the validator
test_tags = ["", "AB", "Shadow Hunter", "ShadowHunter99VeryLong", "ShadowX"]
for tag in test_tags:
    try:
        result = validate_gamertag(tag)
        print(f"  ✓ '{result}' is valid")
    except GamertagTooShortError as e:
        print(f"  ✗ Too short: {e}")
    except GamertagTooLongError as e:
        print(f"  ✗ Too long: {e}")
    except InvalidCharactersError as e:
        print(f"  ✗ Bad chars: {e}")
    except GamertagError as e:
        print(f"  ✗ Error: {e}")

# --- Re-raising exceptions ---
def load_and_validate(filename):
    try:
        with open(filename) as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Warning: {filename} not found, starting fresh")
        raise   # re-raise to let caller decide

# --- Exception chaining ---
def parse_score(value):
    try:
        return int(value)
    except ValueError as original:
        raise ValueError(f"Cannot convert score '{value}' to integer") from original

# --- assert (developer checks, not user input) ---
def calculate_average(scores):
    assert len(scores) > 0, "Cannot calculate average of empty list"
    return sum(scores) / len(scores)
```

## Common Use Cases
- `raise ValueError` in `set_score()` when score is negative
- Custom `GamertagError` hierarchy for detailed validation feedback
- Re-raising with `raise` in `except` to log then propagate
- Using `assert` in internal/developer-facing code to check preconditions

## Related Days
| Day | Topic |
|-----|-------|
| Day 14 | Final test and submission prep |

## See Also
- [36_python_try_except.md](36_python_try_except.md)
- [37_python_exceptions.md](37_python_exceptions.md)
- [22_python_constructors.md](../05_oop/22_python_constructors.md)

## Practice Tips
- Create a `GamertagError` base class with subclasses for each type of validation failure
- Use `raise ValueError` in `__init__` when constructor arguments are invalid
- Practice exception chaining with `raise NewError(...) from original_error`
- Keep exception messages user-friendly — they may be displayed directly to the end user
