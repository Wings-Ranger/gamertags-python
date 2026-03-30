# Python Operators

**W3Schools Links:**
- [Python Operators](https://www.w3schools.com/python/python_operators.asp) — arithmetic, comparison, logical, assignment, membership, identity
- [Python If...Else](https://www.w3schools.com/python/python_conditions.asp) — all exercises are `if` statements built with these operators
- [Python Booleans](https://www.w3schools.com/python/python_booleans.asp) — operators return booleans; `and`/`or`/`not` explained
- [Python String Methods](https://www.w3schools.com/python/python_ref_string.asp) — `.isalnum()`, `.isdigit()` referenced in gamertag validation conditions

**Homework Day(s):** Day 2, Day 6

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

**C# pattern (from the gamertag project):**
```csharp
// C# uses symbol-based operators; Python uses words for logical operators
if (Char.IsNumber(s, s.Length - 1))           // comparison
if (!Char.IsLetterOrDigit(s, 0))              // logical NOT with !
if (s.Length >= 3 && s.Length <= 15)          // logical AND with &&
if (platform == "Xbox" || platform == "PS")   // logical OR with ||
score += 500;                                  // augmented assignment
```

**Python skeleton (fill in the blanks):**
```
# Comparison operators — return True or False
score = 4250
tag   = "ShadowHunter99"
print(score _____ 3000)      # greater than?
print(score _____ 4250)      # equal to?
print(score _____ 5000)      # not equal to?

# Logical operators — Python uses WORDS instead of C#'s &&, ||, !
# C#: s.Length >= 3 && s.Length <= 15
if len(tag) _____ 3 _____ len(tag) _____ 15:
    print("Valid length")

# C#: platform == "Xbox" || platform == "PlayStation"
platform = "Xbox"
if platform _____ "Xbox" _____ platform _____ "PlayStation":
    print("Console player")

# C#: !isRunning  →  Python uses 'not'
is_running = True
if _____ is_running:
    print("Program stopped")

# Membership operator — replaces a long chain of == checks
VALID_PLATFORMS = {"Xbox", "PlayStation", "PC", "Nintendo Switch"}
if platform _____ VALID_PLATFORMS:
    print("Valid platform")

# Augmented assignment operators
score _____ 500     # same as: score = score + 500
score _____ 100     # same as: score = score - 100

# Chained comparison — Pythonic, no direct C# equivalent
length = len(tag)
if _____ <= length <= _____:    # fill in min and max values
    print("Valid length — Pythonic style")
```

**Questions:**
- C# uses `&&` for AND and `||` for OR. What does Python use instead?
- C# uses `!` for NOT. What does Python use instead?
- What does the `in` operator do? How does it replace a long `or` chain of equality checks against a set of valid values?
- What is the difference between `==` (equality) and `is` (identity)? When should you use `is` instead of `==`?

**Test challenge:**
Rewrite this C# condition in Python: `s.Length >= 3 && s.Length <= 15 && Char.IsLetterOrDigit(s, 0)`. Use Python's `and` operator and string methods. Test it on `"GamerX"`, `"AB"`, and `"!GamerX"`.

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
- [10_python_booleans.md](../02_data_types/10_python_booleans.md)
- [12_python_if_else.md](12_python_if_else.md)
- [04_python_numbers.md](../02_data_types/04_python_numbers.md)

## Challenges

1. **Translate logical operators:** Rewrite these C# conditions in Python:
   ```
   # C#: s.Length >= 3 && s.Length <= 15
   if len(tag) _____ 3 _____ len(tag) _____ 15:
       print("Valid")

   # C#: !isRunning
   if _____ is_running:
       print("Stopped")

   # C#: platform == "Xbox" || platform == "PS"
   if platform _____ "Xbox" _____ platform _____ "PS":
       print("Console")
   ```

2. **Membership with in:** Replace a long `or` chain with `in` and a set:
   ```
   # Replace this:
   if platform == "Xbox" or platform == "PlayStation" or platform == "PC":

   # With this:
   VALID_PLATFORMS = {_____, _____, _____}
   if platform _____ VALID_PLATFORMS:
   ```

3. **Augmented assignment:** Track score changes using `+=` and `-=`:
   ```
   score = 4250
   score _____ 500     # bonus added
   score _____ 100     # penalty deducted
   print(score)        # what is the final score?
   ```

4. **Chained comparison:** Rewrite `len(tag) >= 3 and len(tag) <= 15` as a chained comparison:
   ```
   if _____ <= _____(tag) <= _____:
       print("Valid length")
   ```
   Why is this considered more Pythonic?
