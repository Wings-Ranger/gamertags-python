# Python Numbers

**W3Schools Link:** https://www.w3schools.com/python/python_numbers.asp

---

## Overview
Python has three numeric types: integers (`int`), floating-point numbers (`float`), and complex numbers (`complex`). Numbers are used extensively in programs for counting, calculations, and comparisons. Python handles large integers natively without overflow, making it ideal for numeric operations.

## Key Concepts
- **int**: whole numbers, positive or negative, no decimal point (`42`, `-7`, `1000000`)
- **float**: numbers with a decimal point (`3.14`, `-0.5`, `2.0`)
- **complex**: numbers with a real and imaginary part (`3+5j`) — rarely used in beginner projects
- **Arithmetic operators**: `+`, `-`, `*`, `/`, `//` (floor division), `%` (modulo), `**` (power)
- **Type conversion**: `int()`, `float()`, `str()` to cast between types
- **Built-in functions**: `abs()`, `round()`, `min()`, `max()`, `sum()`

## Syntax / Example Code
```python
# Integer and float
score = 4250
accuracy = 87.5

# Arithmetic operations
total_score = 4250 + 1100       # 5350
average = total_score / 2       # 2675.0  (always float in Python 3)
integer_div = total_score // 2  # 2675    (floor division)
remainder = total_score % 100   # 50      (modulo)
squared = 5 ** 2                # 25      (power)

# Counting gamertags
gamertags = ["ShadowX", "NightOwl", "ProSniper", "GamerZ"]
count = len(gamertags)
print(f"Total gamertags: {count}")  # 4

# Using range with numbers
for i in range(1, 6):
    print(f"Player {i}")

# abs, round, min, max
print(abs(-42))         # 42
print(round(87.567, 1)) # 87.6
scores = [1200, 4500, 3300, 900]
print(min(scores))      # 900
print(max(scores))      # 4500
print(sum(scores))      # 9900

# Checking gamertag length (numeric comparison)
tag = "ShadowHunter99"
if len(tag) > 15:
    print("Too long!")
elif len(tag) < 3:
    print("Too short!")
else:
    print(f"Length {len(tag)} is valid")
```

## Common Use Cases
- Tracking player scores and rankings
- Validating gamertag length with `len()` compared to min/max constants
- Calculating averages, totals, or statistics over a player list
- Using `range()` to iterate a fixed number of times

## Related Days
| Day | Topic |
|-----|-------|
| Day 1 | Python Foundations (variables, data types, strings, lists) |

## See Also
- [03_python_variables.md](../01_introduction/03_python_variables.md)
- [11_python_type_casting.md](11_python_type_casting.md)
- [16_python_operators.md](../03_control_flow/16_python_operators.md)

## Practice Tips
- Experiment with `//` vs `/` to understand floor division
- Use `%` (modulo) to check if a number is even or odd: `n % 2 == 0`
- Practice with `len()` on gamertag strings to enforce length rules
- Try `sum(len(tag) for tag in gamertags)` to get total character count
