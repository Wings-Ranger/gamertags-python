# Python Syntax

**W3Schools Links:**
- [Python Syntax](https://www.w3schools.com/python/python_syntax.asp) — indentation, case sensitivity, and conventions
- [Python Comments](https://www.w3schools.com/python/python_comments.asp) — single-line and multi-line comments
- [Python If...Else](https://www.w3schools.com/python/python_conditions.asp) — used in the challenges section

**Homework Day(s):** Day 1, Day 8, Day 9, Day 10

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

**C# pattern (from the gamertag project):**
```csharp
// C# uses braces for code blocks — Python uses indentation instead
if (platform == "PC")
{
    Console.WriteLine("PC Gaming");
    Console.WriteLine("Master Race");
}
Console.WriteLine("This runs always");
```

**Python skeleton (fill in the blanks):**
```
# Single-line comment uses _____

_____
This is a multi-line docstring — uses triple _____
_____

# Indentation defines blocks — NOT braces
platform = "PC"
if platform _____ "PC":
_____print("PC Gaming")       # _____ spaces of indentation required
_____print("Master Race")     # same _____
print("This runs always")     # back to top-level — no indent

# Line continuation with parentheses (preferred over backslash)
valid_platforms = (
    _____,
    _____,
    _____
)

# Multiple assignment in one line (Python-specific)
x, y, z = _____, _____, _____
```

**Questions:**
- In C# you use `{` and `}` to open and close a block. What does Python use instead to define where a block begins and ends?
- How many spaces is the Python standard for one level of indentation?
- What character starts a single-line comment in Python? (C# uses `//`)
- What happens if you mix tabs and spaces in Python indentation?

**Test challenge:**
Write a Python `if` block that prints `"Console player"` if `platform` equals `"Xbox"` and `"PC player"` if it equals `"PC"`. Intentionally mis-indent one line and observe the exact error Python gives you.

## Common Use Cases
- Structuring `if/else` blocks and loops with proper indentation
- Writing readable multi-line conditions using parentheses
- Adding comments to explain complex gamertag validation logic
- Organizing code files for the gamertag project

## Related Days
| Day | Topic |
|-----|-------|
| Day 1 | Python Foundations (variables, data types, strings, lists) |
| Day 8 | Python Project Skeleton |
| Day 9 | Data Loading and Welcome Sequence |
| Day 10 | Display All Gamertags |

## See Also
- [01_python_intro.md](01_python_intro.md)
- [03_python_variables.md](03_python_variables.md)
- [17_python_functions.md](../04_functions/17_python_functions.md)

## Challenges

1. **Indentation error:** This code has an indentation problem — find and fix it:
   ```
   platform = "Xbox"
   if platform == "Xbox":
   print("Console player")    # ← what is wrong here?
       print("Valid")
   ```

2. **Add comments:** Take any two `if` conditions from your gamertag project and add a `#` comment above each one explaining what it checks. What style does PEP 8 recommend for comments?

3. **Line continuation:** Rewrite this as a single assignment using parentheses for line continuation:
   ```
   message = "This gamertag is invalid " + "because it has special characters"
   ```
   ```
   message = (
       _____
       _____
   )
   ```

4. **Observe the error:** Deliberately add a semicolon at the end of a Python line. Does it cause an error, a warning, or nothing? What does PEP 8 say about using semicolons in Python?
