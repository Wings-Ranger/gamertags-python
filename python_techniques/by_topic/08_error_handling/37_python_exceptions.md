# Python Built-in Exceptions

**W3Schools Links:**
- [Python Built-in Exceptions](https://www.w3schools.com/python/python_ref_exceptions.asp) — exception hierarchy, `ValueError`, `TypeError`, `IndexError`, `KeyError`, etc.
- [Python Try Except](https://www.w3schools.com/python/python_try_except.asp) — `try/except` syntax used in all exercises
- [Python Type Casting](https://www.w3schools.com/python/python_casting.asp) — `int("abc")` raises `ValueError`; context for casting exercises
- [Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp) — `KeyError` context when accessing missing dict keys
- [Python File Read](https://www.w3schools.com/python/python_file_read.asp) — `FileNotFoundError` context when opening missing files

**Homework Day(s):** Day 14

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

```
C# context:
    // C# exceptions for similar situations:
    // FileNotFoundException  → Python: FileNotFoundError
    // ArgumentException      → Python: ValueError
    // InvalidOperationException → Python: RuntimeError or custom exception
    // IndexOutOfRangeException → Python: IndexError
    // NullReferenceException  → Python: AttributeError or TypeError

Python skeleton — identify which exception is raised when (fill in the blanks):

    # ValueError — right type, wrong value
    # Raised by: int("abc"), int(""), float("xyz")
    try:
        score = int("not_a_number")
    except _____ as e:
        print(f"ValueError: {e}")

    # FileNotFoundError — file does not exist
    try:
        with open("missing_file.txt") as f:
            _____
    except _____ as e:
        print(f"File error: {e}")

    # IndexError — list index out of range
    # This happens when a CSV line has fewer fields than expected
    try:
        parts = "ShadowX,Xbox".split(",")   # only 2 parts
        score_str = parts[_____]            # this index does not exist
    except _____ as e:
        print(f"Missing field: {e}")

    # TypeError — wrong type for an operation
    try:
        result = "Score: " + _____          # can't add str and int
    except _____ as e:
        print(f"Type error: {e}")

    # KeyError — dictionary key missing
    try:
        player = {"gamertag": "ShadowX"}    # no "score" key
        print(player[_____])
    except _____ as e:
        print(f"Missing key: {e}")

    # Catching multiple exceptions together
    try:
        parts = "ShadowX".split(",")
        score = int(parts[_____])
    except (_____, _____) as e:             # IndexError OR ValueError
        print(f"Data error: {type(e).__name__}: {e}")

Questions:
- What exception does `int("abc")` raise? What about `int("")`?
- What is the difference between `IndexError` and `KeyError`?
- What exception does `open("nonexistent.txt")` raise?
- Why should you catch the MOST SPECIFIC exception type rather than `Exception`?

Test challenge:
    Write a function `parse_gamertag_line(line)` that splits a CSV line and converts
    the score to int. Intentionally test it with:
    - `"ShadowX,Xbox,4250"` (valid)
    - `"ShadowX,Xbox"` (missing score → IndexError)
    - `"ShadowX,Xbox,abc"` (bad score → ValueError)
    Which exception handler catches each case?
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

## Challenges
- **Blank 1**: In `parse_gamertag_line(line)`, write `except (_____, _____)` to catch both a missing field and a bad score in the same block. What are the two exception class names?
- **Blank 2**: What exception does `parts[2]` raise when `parts` only has 2 elements? What does `int("abc")` raise? Write them both in a `except (_____, _____)` block.
- **Blank 3**: Use `type(e).__name__` to print the exception class name: `print(f"Error type: {_____(e)._____(  )}")`. Fill the two blanks.
- **Challenge**: Intentionally trigger each of the five exceptions in the skeleton (ValueError, FileNotFoundError, IndexError, TypeError, KeyError) by writing short test lines. Then write ONE `try` block around code that could raise any of them, with a separate `except` clause for each. What order do the `except` clauses need to be in?
