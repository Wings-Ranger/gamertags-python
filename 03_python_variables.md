# Python Variables

**W3Schools Link:** https://www.w3schools.com/python/python_variables.asp

---

## Overview
Variables in Python are containers for storing data values. Python is dynamically typed, meaning you don't need to declare a variable's type before using it — the type is inferred from the value assigned. Variables are created the moment you assign a value to them.

## Key Concepts
- **Assignment**: use `=` to assign a value (`name = "GamerX"`)
- **Dynamic typing**: variables can change type by reassigning
- **Naming rules**: must start with a letter or `_`, no spaces, no special characters except `_`
- **Case sensitive**: `tag`, `Tag`, and `TAG` are three different variables
- **Snake_case**: the Python convention for variable names (`player_name`, `high_score`)
- **Constants**: by convention, written in `ALL_CAPS` (`MAX_GAMERTAG_LENGTH = 15`)
- **Multiple assignment**: `a = b = c = 0` or `x, y = 1, 2`

## Syntax / Example Code
```python
# Basic variable assignment
gamertag = "ShadowHunter99"
platform = "Xbox"
score = 4250
is_active = True

# Multiple assignment
x, y, z = "Xbox", "PlayStation", "PC"

# Same value to multiple variables
count = total = 0

# Dynamic typing — reassigning changes the type
value = 42          # int
value = "forty-two" # now a string

# Check the type
print(type(gamertag))   # <class 'str'>
print(type(score))      # <class 'int'>

# Constants (convention only — Python doesn't enforce immutability)
MAX_GAMERTAG_LENGTH = 15
MIN_GAMERTAG_LENGTH = 3
VALID_PLATFORMS = ["Xbox", "PlayStation", "PC", "Nintendo Switch"]

# Variable in an f-string
player = "NightOwl"
level = 42
print(f"Player {player} is at level {level}")

# Deleting a variable
temp = "temporary"
del temp
# print(temp)  # NameError: name 'temp' is not defined
```

## Common Use Cases
- Storing gamertag, platform, and score data for each player
- Using constants for configuration values like `MAX_GAMERTAG_LENGTH`
- Accumulating totals in loops (e.g., counting valid gamertags)
- Swapping values: `a, b = b, a`

## Related Days
| Day | Topic |
|-----|-------|
| Day 1 | Python Foundations (variables, data types, strings, lists) |

## See Also
- [04_python_numbers.md](04_python_numbers.md)
- [05_python_strings.md](05_python_strings.md)
- [40_python_scope.md](40_python_scope.md)

## Practice Tips
- Name variables descriptively: `gamertag` beats `g` or `x`
- Practice tuple unpacking: `name, platform = "GamerX", "Xbox"`
- Try assigning different types to the same variable and use `type()` to track changes
- Define all your gamertag project constants at the top of your file in ALL_CAPS
