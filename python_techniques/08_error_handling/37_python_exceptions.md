# Python Built-in Exceptions

**W3Schools Link:** https://www.w3schools.com/python/python_ref_exceptions.asp

---

## Overview
Python has a hierarchy of built-in exception classes. Understanding which exception is raised in which situation helps you write precise `except` clauses and produce meaningful error messages. All exceptions inherit from `BaseException`; most user-relevant exceptions inherit from `Exception`.

## Key Concepts
- **`Exception`**: the base class for all non-system-exiting exceptions — catch-all for most use cases
- **`ValueError`**: value is the right type but wrong content (e.g., `int("abc")`)
- **`TypeError`**: operation applied to an object of inappropriate type
- **`FileNotFoundError`**: file or directory does not exist (subclass of `OSError`)
- **`IndexError`**: sequence index out of range
- **`KeyError`**: dictionary key not found
- **`AttributeError`**: object has no such attribute
- **`ZeroDivisionError`**: division or modulo by zero
- **`StopIteration`**: raised by `next()` when iterator is exhausted
- **Exception hierarchy**: catch child classes before parent classes in `except` chains

## Syntax / Example Code
```python
# ValueError — wrong value, right type
try:
    score = int("not_a_number")
except ValueError as e:
    print(f"ValueError: {e}")

# Also ValueError when value is out of range for a custom context:
def set_score(score):
    if score < 0:
        raise ValueError(f"Score cannot be negative: {score}")
    return score

# TypeError — wrong type
try:
    result = "Score: " + 4250    # can't concatenate str and int
except TypeError as e:
    print(f"TypeError: {e}")

# FileNotFoundError
try:
    with open("nonexistent.txt") as f:
        pass
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")

# IndexError — list index out of range
try:
    parts = "ShadowX,Xbox".split(",")   # only 2 parts
    score = int(parts[2])               # index 2 doesn't exist
except IndexError as e:
    print(f"IndexError: {e}")

# KeyError — dict key missing
try:
    player = {"gamertag": "ShadowX", "platform": "Xbox"}
    print(player["score"])   # key doesn't exist
except KeyError as e:
    print(f"KeyError: {e}")

# AttributeError
try:
    x = 42
    x.upper()   # int has no upper() method
except AttributeError as e:
    print(f"AttributeError: {e}")

# ZeroDivisionError
try:
    average = 100 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

# Catching multiple in one except
try:
    line = "ShadowX,Xbox"
    parts = line.split(",")
    score = int(parts[2])   # IndexError, and if parts[2] existed but wasn't int: ValueError
except (IndexError, ValueError) as e:
    print(f"Data parsing error: {type(e).__name__}: {e}")

# Catching parent class (less specific — use with care)
try:
    with open("gamertags.txt") as f:
        data = f.read()
except OSError as e:
    # Catches FileNotFoundError, PermissionError, etc.
    print(f"OS error: {e}")

# Inspecting exception type
def describe_error(e):
    print(f"  Type   : {type(e).__name__}")
    print(f"  Message: {e}")
    print(f"  Module : {type(e).__module__}")

try:
    {}["missing_key"]
except Exception as e:
    describe_error(e)

# Exception hierarchy summary (partial)
# BaseException
#   ├── KeyboardInterrupt
#   ├── SystemExit
#   └── Exception
#         ├── ValueError
#         ├── TypeError
#         ├── AttributeError
#         ├── IndexError
#         ├── KeyError
#         ├── StopIteration
#         ├── ZeroDivisionError
#         └── OSError
#               ├── FileNotFoundError
#               └── PermissionError
```

## Common Use Cases
- `ValueError` — converting CSV score strings to int
- `FileNotFoundError` — opening the gamertag data file at startup
- `IndexError` — parsing CSV lines with unexpected field counts
- `KeyError` — accessing player dict fields that may be missing

## Related Days
| Day | Topic |
|-----|-------|
| Day 14 | Final test and submission prep |

## See Also
- [36_python_try_except.md](36_python_try_except.md)
- [38_python_raising_exceptions.md](38_python_raising_exceptions.md)
- [27_python_file_read.md](../06_file_io/27_python_file_read.md)

## Practice Tips
- Intentionally trigger each exception type to learn exactly when they occur
- Use `type(e).__name__` in debug output to display the exception class name
- Catch `OSError` (not just `FileNotFoundError`) when you want to handle all file system errors
- Never catch `KeyboardInterrupt` — users need Ctrl+C to exit hanging programs
