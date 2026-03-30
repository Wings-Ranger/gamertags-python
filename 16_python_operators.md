# Python Operators

**W3Schools Link:** https://www.w3schools.com/python/python_operators.asp

---

## Overview
Operators are symbols that perform operations on values and variables. Python has several categories: arithmetic, comparison, logical, assignment, identity, membership, and bitwise. Mastering operators is fundamental to writing any logic — from score calculations to gamertag validation conditions.

## Key Concepts
- **Arithmetic**: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- **Comparison**: `==`, `!=`, `<`, `>`, `<=`, `>=` — always return a boolean
- **Logical**: `and`, `or`, `not` — combine boolean expressions
- **Assignment**: `=`, `+=`, `-=`, `*=`, `/=`, `//=`, `%=`, `**=`
- **Identity**: `is`, `is not` — checks if two variables point to the same object
- **Membership**: `in`, `not in` — checks if a value exists in a sequence
- **Operator precedence**: `**` > unary > `* / // %` > `+ -` > comparisons > `not` > `and` > `or`

## Syntax / Example Code
```python
# Arithmetic operators
score = 4250
bonus = 500
total = score + bonus          # 4750
avg = total / 2                # 2375.0
level = total // 1000          # 4  (floor division)
remainder = total % 1000       # 750
power = 2 ** 10                # 1024

# Comparison operators
print(score > 3000)    # True
print(score == 4250)   # True
print(score != 5000)   # True
print(score >= 4250)   # True

# Logical operators
tag = "ShadowHunter99"
valid = len(tag) >= 3 and len(tag) <= 15 and tag.isalnum()
print(valid)   # True

is_empty = not tag         # False (non-empty string is truthy)
console = tag == "Xbox" or tag == "PlayStation"

# Assignment operators (augmented)
score = 1000
score += 500    # score = 1500
score -= 100    # score = 1400
score *= 2      # score = 2800
score //= 10    # score = 280

# Membership operators
VALID_PLATFORMS = ["Xbox", "PlayStation", "PC", "Nintendo Switch"]
platform = "Xbox"

if platform in VALID_PLATFORMS:
    print("Valid platform")

if "Stadia" not in VALID_PLATFORMS:
    print("Stadia not supported")

# Identity operators (is vs ==)
a = [1, 2, 3]
b = a           # same object
c = [1, 2, 3]  # different object, same value

print(a is b)    # True  — same object
print(a is c)    # False — different objects
print(a == c)    # True  — same value

# Use 'is' for None checks (not ==)
result = None
if result is None:
    print("No result yet")

# Chained comparisons (Pythonic)
length = len(tag)
if 3 <= length <= 15:
    print("Length is valid")

# Operator precedence example
result = 2 + 3 * 4      # 14, not 20 (multiplication first)
result = (2 + 3) * 4    # 20 (parentheses override)
```

## Common Use Cases
- Validating gamertag length with chained comparisons: `3 <= len(tag) <= 15`
- Updating scores with augmented assignment: `score += bonus`
- Checking platform membership with `in`
- Combining validation rules with `and`/`or`

## Related Days
| Day | Topic |
|-----|-------|
| Day 2 | Conditions and Decisions (if/elif/else, boolean, comparisons) |
| Day 6 | String and Character Validation (empty-string safety, character checks) |

## See Also
- [10_python_booleans.md](10_python_booleans.md)
- [12_python_if_else.md](12_python_if_else.md)
- [04_python_numbers.md](04_python_numbers.md)

## Practice Tips
- Memorize operator precedence; when in doubt, use parentheses for clarity
- Always use `is None` instead of `== None`
- Practice augmented assignment operators (`+=`, `-=`) for score tracking
- Use chained comparisons `3 <= x <= 15` instead of `x >= 3 and x <= 15`
