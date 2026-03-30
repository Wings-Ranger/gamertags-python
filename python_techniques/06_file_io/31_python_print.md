# Python print()

**W3Schools Link:** https://www.w3schools.com/python/ref_func_print.asp

**Homework Day(s):** Day 1, Days 8–10

---

## Overview
The `print()` function outputs text to the console (standard output). It is one of the most frequently used functions in Python for displaying information to the user and for debugging. `print()` supports formatting options including custom separators, end characters, and outputting to files or other streams.

## Key Concepts
- **Signature**: `print(*objects, sep=" ", end="\n", file=sys.stdout, flush=False)`
- **Multiple arguments**: `print(a, b, c)` prints them separated by spaces by default
- **`sep`**: customizes the separator between multiple arguments (default: `" "`)
- **`end`**: customizes what's printed at the end (default: `"\n"` newline)
- **`file`**: redirect output to a file instead of the console
- **f-strings**: the modern, readable way to embed variables in output
- **Pretty printing**: use `pprint` module for nested data structures

## Syntax / Example Code
```python
# Basic print
print("Hello, World!")
print("Welcome to the Gamertag Manager")

# Multiple arguments (separated by spaces by default)
gamertag = "ShadowX"
platform = "Xbox"
score = 4250
print(gamertag, platform, score)   # ShadowX Xbox 4250

# Custom separator
print(gamertag, platform, score, sep=" | ")    # ShadowX | Xbox | 4250
print(gamertag, platform, score, sep=", ")     # ShadowX, Xbox, 4250
print("=", sep="", end="")  # no sep, no newline

# Custom end (suppress or change the newline)
print("Loading", end="")
print(".", end="")
print(".", end="")
print(". Done!")   # Loading... Done!

# f-strings — modern formatting (Python 3.6+)
print(f"Player: {gamertag}")
print(f"Score:  {score:,}")          # 4,250  (thousands separator)
print(f"Score:  {score:>10}")        # right-aligned in 10 chars
print(f"Name:   {gamertag:<15}")     # left-aligned in 15 chars

# Printing a formatted player table
players = [
    {"gamertag": "ShadowX",   "platform": "Xbox",        "score": 4250},
    {"gamertag": "NightOwl",  "platform": "PlayStation", "score": 3300},
    {"gamertag": "ProSniper", "platform": "PC",          "score": 5100},
]

print("\n" + "=" * 45)
print(f"{'#':<4} {'Gamertag':<16} {'Platform':<14} {'Score':>6}")
print("=" * 45)
for i, p in enumerate(players, 1):
    print(f"{i:<4} {p['gamertag']:<16} {p['platform']:<14} {p['score']:>6,}")
print("=" * 45)

# Printing to a file
import sys
with open("output.log", "w") as log:
    print("Gamertag Manager started", file=log)
    for p in players:
        print(f"{p['gamertag']},{p['platform']},{p['score']}", file=log)

# pprint for nested data structures
from pprint import pprint
pprint(players)

# Debug print with variable name (Python 3.8+)
debug_value = 4250
print(f"{debug_value=}")   # debug_value=4250

# Print a horizontal rule
def hr(char="=", width=45):
    print(char * width)

hr()
print("Gamertag Manager")
hr("-")
```

## Common Use Cases
- Displaying numbered player lists with aligned columns using f-string formatting
- Printing separator lines (`"=" * 45`) to structure console output
- Debug printing variables with `f"{var=}"` (Python 3.8+)
- Logging output to a file with `print(..., file=log_file)`

## Related Days
| Day | Topic |
|-----|-------|
| Day 1 | Python Foundations (variables, data types, strings, lists) |
| Days 8-10 | Build project skeleton, data loading, display |

## See Also
- [35_python_string_formatting.md](../07_strings/35_python_string_formatting.md)
- [05_python_strings.md](../02_data_types/05_python_strings.md)
- [09_python_dictionaries.md](../02_data_types/09_python_dictionaries.md)

## Practice Tips
- Practice the f-string alignment specifiers: `:<15` (left), `:>6` (right), `:^10` (center)
- Build a `display_players(players)` function that prints a clean, aligned table
- Use `sep=" | "` to quickly format multi-column output without f-strings
- Add `f"{score:,}"` for thousands separators in scores to improve readability
