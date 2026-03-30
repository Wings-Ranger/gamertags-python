# Python Syntax

**W3Schools Link:** https://www.w3schools.com/python/python_syntax.asp

---

## Overview
Python syntax refers to the set of rules that define how Python programs are written and interpreted. Unlike many languages, Python uses indentation (whitespace) to define code blocks instead of curly braces or keywords. Clean, consistent syntax is a core principle of the Python language philosophy.

## Key Concepts
- **Indentation**: 4 spaces (or 1 tab) per level — this is mandatory, not stylistic
- **Comments**: use `#` for single-line comments; `"""` for multi-line docstrings
- **Case sensitivity**: `gamertag` and `Gamertag` are different variables
- **Line continuation**: use `\` or wrap in parentheses to continue across lines
- **Semicolons**: optional in Python; not idiomatic to use them
- **One statement per line** is the standard convention

## Syntax / Example Code
```python
# Single-line comment
print("Welcome to the Gamertag Manager")  # inline comment

"""
This is a multi-line
docstring or block comment
"""

# Indentation defines blocks — this is mandatory
platform = "PC"
if platform == "PC":
    print("PC Gaming")      # 4-space indent
    print("Master Race")    # same block
print("This runs always")   # back to top level

# Line continuation with backslash
long_message = "This gamertag is invalid because " \
               "it contains special characters"

# Line continuation with parentheses (preferred)
valid_platforms = (
    "Xbox",
    "PlayStation",
    "PC",
    "Nintendo Switch"
)

# Multiple assignments on one line
x, y, z = 1, 2, 3

# Checking Python version at runtime
import sys
print(sys.version)
```

## Common Use Cases
- Structuring `if/else` blocks and loops with proper indentation
- Writing readable multi-line conditions using parentheses
- Adding comments to explain complex gamertag validation logic
- Organizing code files for the gamertag project

## Related Days
| Day | Topic |
|-----|-------|
| Day 1 | Python Foundations (variables, data types, strings, lists) |
| Days 8-10 | Build project skeleton, data loading, display |

## See Also
- [01_python_intro.md](01_python_intro.md)
- [03_python_variables.md](03_python_variables.md)
- [17_python_functions.md](../04_functions/17_python_functions.md)

## Practice Tips
- Intentionally break indentation and observe the `IndentationError`
- Practice writing multi-line conditions with parentheses instead of backslashes
- Add meaningful comments to your gamertag project explaining each block
- Use a linter like `flake8` or `pylint` to catch syntax issues automatically
