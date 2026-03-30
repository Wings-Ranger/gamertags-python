# Python Numbers

**W3Schools Link:** https://www.w3schools.com/python/python_numbers.asp

**Homework Day(s):** Day 1

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

**C# pattern (from the gamertag project):**
```csharp
// C# uses .Length property on strings
if (gamerTag.Length > 15)
    Console.WriteLine("Too long!");
else if (gamerTag.Length < 3)
    Console.WriteLine("Too short!");
```

**Python skeleton (fill in the blanks):**
```
# Python uses the len() function — NOT a .Length property like C#
tag = "ShadowHunter99"
if _____(tag) > _____:
    print("Too long!")
elif _____(tag) < _____:
    print("Too short!")
else:
    print(f"Length {_____(tag)} is valid")

# Counting gamertags in a list
gamertags = ["ShadowX", "NightOwl", "ProSniper", "GamerZ"]
count = _____(gamertags)
print(f"Total gamertags: {_____}")

# Arithmetic
total_score = _____ + _____
average     = total_score _____ 2     # always float in Python 3
level       = total_score _____ 1000  # floor division — whole number only

# Built-in number functions
scores = [1200, 4500, 3300, 900]
print(_____(scores))   # smallest score
print(_____(scores))   # largest score
print(_____(scores))   # total of all scores
```

**Questions:**
- C# uses `gamerTag.Length` (a property on the object). Python uses `len(tag)` (a standalone function). How are these called differently?
- What is the difference between `/` (regular division) and `//` (floor division) in Python?
- What does `%` (modulo) return? How could you use it to check if a number is even?
- How would you write a single Python `if` condition that checks `len(tag)` is between 3 and 15?

**Test challenge:**
Write a length-validation `if/elif/else` block for a gamertag using `len()`. Test it with a tag that is too short (e.g., `"AB"`), one that is too long (e.g., `"SuperLongGamertagName"`), and one that is valid (e.g., `"GamerX"`).

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

## Challenges

1. **Translate the length check:** The C# project uses `gamerTag.Length`. Fill in the Python equivalent:
   ```
   tag = "ShadowHunter99"
   if _____(tag) > 15:
       print("Too long!")
   elif _____(tag) < _____:
       print("Too short!")
   ```

2. **Division types:** Predict the output before running:
   - `10 / 3` → `_____` (what type is the result?)
   - `10 // 3` → `_____` (what type is the result?)
   - `10 % 3` → `_____` (what does this represent?)

3. **Count and summarise:** Create a list of 5 gamertags and use `len()` to count them. Then use `min()`, `max()`, and `sum()` on a list of scores `[1200, 4500, 3300, 900, 2100]`. Fill in:
   ```
   scores = [1200, 4500, 3300, 900, 2100]
   print(_____(scores))   # smallest
   print(_____(scores))   # largest
   print(_____(scores))   # total
   ```

4. **Range challenge:** Use `range()` to print only even numbers from 2 to 10. Fill in the three arguments:
   ```
   for i in range(_____, _____, _____):
       print(i)
   ```
