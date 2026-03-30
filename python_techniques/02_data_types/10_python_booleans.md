# Python Booleans

**W3Schools Link:** https://www.w3schools.com/python/python_booleans.asp

**Homework Day(s):** Day 2

---

## Overview
Booleans represent one of two values: `True` or `False`. They are the foundation of all conditional logic in Python. Boolean values result from comparisons and logical operations and are used directly in `if` statements, `while` loops, and any conditional expression.

## Key Concepts
- **Two values only**: `True` and `False` (capital T and F — Python is case-sensitive)
- **Comparison operators**: `==`, `!=`, `<`, `>`, `<=`, `>=` all return booleans
- **Logical operators**: `and`, `or`, `not`
- **Truthy/Falsy**: many values evaluate as True or False in a boolean context
  - Falsy: `0`, `""`, `[]`, `{}`, `None`, `False`
  - Truthy: any non-zero number, non-empty string, non-empty container
- **bool()**: converts a value to its boolean equivalent
- **Short-circuit evaluation**: `and`/`or` stop as soon as the result is determined

## Syntax / Example Code

**C# pattern (from the gamertag project):**
```csharp
// C# uses a bool flag to control the main menu loop
bool isRunning = true;

while (isRunning)
{
    // ... menu code ...
    if (userChoice == "5")
        isRunning = false;
}
```

**Python skeleton (fill in the blanks):**
```
# Python booleans are True and False (capital first letter — case matters!)
is_running = _____
is_banned  = _____

print(_____(is_running))    # should show <class 'bool'>

# Comparison operators RETURN booleans
score = 4250
print(score _____ 1000)     # is score greater than 1000?
print(score _____ 5000)     # is score equal to 5000?
print(score _____ 0)        # is score not equal to 0?

# Logical operators: Python uses WORDS, not symbols like C#
tag      = "ShadowHunter99"
platform = "Xbox"

# C#: s.Length >= 3 && s.Length <= 15
if _____(tag) >= 3 _____ _____(tag) <= 15:
    print("Valid length")

# C#: platform == "Xbox" || platform == "PlayStation"
if platform _____ "Xbox" _____ platform _____ "PlayStation":
    print("Console player")

# C#: !isBanned  →  Python: not is_banned
if _____ is_banned:
    print("Player is in good standing")

# Truthy/falsy — Python shorthand (no C# equivalent)
gamertag = ""
if _____ gamertag:           # same as: if gamertag == ""
    print("Gamertag is empty!")

tags = []
if _____ tags:               # same as: if len(tags) == 0
    print("No gamertags loaded yet")

# Chained comparison — Pythonic (no direct C# equivalent)
length = _____(tag)
if _____ <= length <= _____:    # fill in min and max
    print("Valid gamertag length")
```

**Questions:**
- C# writes `bool isRunning = true`. How does Python write the same thing? What is different about the capitalisation of `True`/`False`?
- C# uses `!` for logical NOT. What does Python use instead?
- What does "truthy/falsy" mean? Give two examples of values that are falsy in Python.
- C# writes `length >= 3 && length <= 15`. What is the Python equivalent using chained comparison?

**Test challenge:**
Declare `is_running = True` and write a `while` loop that prints `"Menu is running"` once and then sets `is_running = False`. Confirm the loop only executes once.

## Common Use Cases
- Checking if a gamertag passes all validation rules
- Controlling loops with `while running:`
- Filtering lists: `[t for t in tags if is_valid(t)]`
- Tracking flags: `found = False`, set to `True` when a match is found

## Related Days
| Day | Topic |
|-----|-------|
| Day 2 | Conditions and Decisions (if/elif/else, boolean, comparisons) |

## See Also
- [12_python_if_else.md](../03_control_flow/12_python_if_else.md)
- [13_python_while_loops.md](../03_control_flow/13_python_while_loops.md)
- [16_python_operators.md](../03_control_flow/16_python_operators.md)

## Challenges

1. **Translate the flag:** The C# project uses `bool isRunning = true`. Translate to Python and explain why casing matters:
   ```
   is_running = _____    # True or False?
   ```
   What error would `is_running = true` (lowercase t) cause in Python?

2. **Logical operators:** C# uses `&&` and `||`. Fill in the Python equivalents:
   ```
   # C#: s.Length >= 3 && s.Length <= 15
   if len(tag) _____ 3 _____ len(tag) _____ 15:
       print("Valid length")

   # C#: !Char.IsLetterOrDigit(s, 0)
   if _____ tag[0]._____(  ):
       print("Invalid start character")
   ```

3. **Truthy/falsy:** Predict the output of each — then verify in a REPL:
   - `bool("")` → `_____`
   - `bool("GamerX")` → `_____`
   - `bool([])` → `_____`
   - `bool(0)` → `_____`

4. **Chained comparison:** Rewrite `len(tag) >= 3 and len(tag) <= 15` using Python's chained comparison syntax:
   ```
   if _____ <= _____(tag) <= _____:
       print("Valid length")
   ```
   What makes this more readable than the `and` version?
