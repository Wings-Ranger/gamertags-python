# Python Variables

**W3Schools Links:**
- [Python Variables](https://www.w3schools.com/python/python_variables.asp) — declaring, naming, and assigning variables
- [Python Data Types](https://www.w3schools.com/python/python_datatypes.asp) — `type()` and Python's built-in types
- [Python Booleans](https://www.w3schools.com/python/python_booleans.asp) — `True`/`False` (used for `is_running`)
- [Python Type Casting](https://www.w3schools.com/python/python_casting.asp) — converting between types
- [Python String Formatting (f-strings)](https://www.w3schools.com/python/python_string_formatting.asp) — used in variable output exercises

**Homework Day(s):** Day 1

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

**C# pattern (from the gamertag project):**
```csharp
string gamerTag = "ShadowHunter99";
string platform  = "Xbox";
int score        = 4250;
bool isRunning   = true;
const int MAX_GAMERTAG_LENGTH = 15;
```

**Python skeleton (fill in the blanks):**
```
# Python does NOT declare types — just assign a value directly
gamertag   = "ShadowHunter99"
platform   = "Xbox"
score      = 4250
is_running = True

# Check what type Python inferred
print(_____(gamertag))   # should show <class 'str'>
print(_____(score))      # should show <class 'int'>

# Constants: ALL_CAPS by convention (Python does NOT enforce immutability)
MAX_GAMERTAG_LENGTH = _____
MIN_GAMERTAG_LENGTH = _____

# Multiple assignment in one line (Python-specific)
x, y, z = _____, _____, _____

# Variable in an f-string
player = _____
level  = _____
print(_____"Player {_____} is at level {_____}")
```

**Questions:**
- In C# you write `string gamerTag = "value"`. What is different about variable assignment in Python?
- C# uses camelCase (`gamerTag`). What naming convention does Python use for variables? (e.g., `gamerTag` becomes `_____`)
- How do you check what type Python assigned to a variable?
- Can you reassign a Python variable to a completely different type? Try assigning `score = 4250` then `score = "unknown"` — what happens?

**Test challenge:**
Declare the five variables your gamertag project will need: `gamertag`, `is_running`, `MAX_GAMERTAG_LENGTH`, `MIN_GAMERTAG_LENGTH`, and `score`. Print each one along with `type()` to confirm Python inferred the right types.

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
- [04_python_numbers.md](../02_data_types/04_python_numbers.md)
- [05_python_strings.md](../02_data_types/05_python_strings.md)
- [40_python_scope.md](../09_advanced/40_python_scope.md)

## Challenges

1. **Translate C# to Python:** Rewrite these C# declarations as Python variables using snake_case naming:
   ```csharp
   string gamerTag  = "ProSniper";
   bool   isRunning = true;
   int    maxLength = 15;
   ```
   ```
   gamer_tag  = _____
   is_running = _____
   max_length = _____
   ```

2. **Naming convention:** Rename these C# camelCase names to Python snake_case:
   - `isRunning` → `_____`
   - `gamerTagList` → `_____`
   - `newGamerTag` → `_____`

3. **Dynamic typing:** Assign `value = 42`, print `type(value)`. Then assign `value = "forty-two"` and print `type(value)` again. What changed? What does this mean for your gamertag project?

4. **Constants:** Define `MAX_GAMERTAG_LENGTH` and `MIN_GAMERTAG_LENGTH` at the top of a Python file. Try changing one of them later in the file. Does Python stop you? What does ALL_CAPS convention communicate to other programmers?
