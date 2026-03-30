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
```python
# Basic booleans
is_active = True
is_banned = False

print(type(is_active))   # <class 'bool'>

# Comparison operators return booleans
score = 4250
print(score > 1000)    # True
print(score == 5000)   # False
print(score != 0)      # True

# Logical operators
tag = "ShadowHunter99"
platform = "Xbox"

# and: both must be True
if len(tag) >= 3 and len(tag) <= 15:
    print("Valid length")

# or: at least one must be True
if platform == "Xbox" or platform == "PlayStation":
    print("Console player")

# not: inverts the boolean
if not is_banned:
    print("Player is in good standing")

# Truthy and falsy values
gamertag = ""
if not gamertag:
    print("Gamertag is empty — please enter a value")

tags = []
if not tags:
    print("No gamertags loaded yet")

# bool() conversion
print(bool(""))         # False
print(bool("GamerX"))   # True
print(bool(0))          # False
print(bool(42))         # True
print(bool([]))         # False
print(bool(["a"]))      # True

# Chaining comparisons (Pythonic)
length = len(tag)
if 3 <= length <= 15:
    print("Valid gamertag length")

# Boolean as int (True == 1, False == 0)
valid_tags = ["GamerX", "AB", "ShadowHunter99", "A"]
valid_count = sum(3 <= len(t) <= 15 for t in valid_tags)
print(f"{valid_count} valid tags")   # 2
```

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

## Practice Tips
- Test every comparison operator in a Python REPL with gamertag examples
- Practice truthy/falsy by using `if tag:` instead of `if tag != ""`
- Use `bool()` to understand what values are falsy in Python
- Build a validation function that returns `True` or `False` for a gamertag
