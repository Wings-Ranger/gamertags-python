# Python If / Else

**W3Schools Link:** https://www.w3schools.com/python/python_conditions.asp

**Homework Day(s):** Day 2, Days 11–12

---

## Overview
Conditional statements allow your program to make decisions and execute different code paths based on whether conditions are true or false. Python uses `if`, `elif` (else if), and `else` to build branching logic. Proper use of conditionals is at the heart of any program that validates input, filters data, or responds to user choices.

## Key Concepts
- **`if`**: executes a block when the condition is `True`
- **`elif`**: checks an additional condition if the previous was `False`
- **`else`**: executes when all previous conditions were `False`
- **Indentation is mandatory**: the body of each clause must be indented 4 spaces
- **Short-circuit evaluation**: Python stops checking `and`/`or` as soon as the result is known
- **Ternary (one-liner)**: `value = x if condition else y`
- **Nested if**: you can nest `if` statements, but keep nesting shallow for readability

## Syntax / Example Code
```python
# Basic if/elif/else
score = 4250

if score >= 5000:
    print("Rank: Diamond")
elif score >= 3000:
    print("Rank: Gold")
elif score >= 1000:
    print("Rank: Silver")
else:
    print("Rank: Bronze")

# Gamertag validation
def validate_gamertag(tag):
    if not tag:
        return "Error: Gamertag cannot be empty"
    if len(tag) < 3:
        return "Error: Too short (minimum 3 characters)"
    if len(tag) > 15:
        return "Error: Too long (maximum 15 characters)"
    if not tag.isalnum():
        return "Error: Only letters and numbers allowed"
    return "Valid"

print(validate_gamertag("GX"))               # Too short
print(validate_gamertag("Shadow Hunter 99")) # Special characters
print(validate_gamertag("ShadowHunter99"))   # Valid

# Checking platform membership
VALID_PLATFORMS = {"Xbox", "PlayStation", "PC", "Nintendo Switch"}
platform = "Xbox"

if platform in VALID_PLATFORMS:
    print(f"{platform} is a valid platform")
else:
    print(f"Unknown platform: {platform}")

# Ternary expression (inline if/else)
status = "Active" if score > 0 else "Inactive"
print(status)

# Compound conditions
tag = "ShadowX"
if len(tag) >= 3 and tag.isalnum():
    print("Passes basic validation")

# Nested if (keep shallow)
if platform == "Xbox":
    if score > 5000:
        print("Top Xbox player")
    else:
        print("Xbox player")

# Using not
banned_tags = {"HackMaster", "CheatCode"}
tag = "HackMaster"
if tag not in banned_tags:
    print("Gamertag is allowed")
else:
    print("Gamertag is banned")
```

## Common Use Cases
- Validating gamertag input before saving to file
- Routing program flow based on user menu selections
- Filtering player records by platform or score range
- Assigning rank labels based on score thresholds

## Related Days
| Day | Topic |
|-----|-------|
| Day 2 | Conditions and Decisions (if/elif/else, boolean, comparisons) |
| Days 11-12 | Filters and logic |

## See Also
- [10_python_booleans.md](../02_data_types/10_python_booleans.md)
- [16_python_operators.md](16_python_operators.md)
- [34_python_string_validation.md](../07_strings/34_python_string_validation.md)

## Practice Tips
- Write a `validate_gamertag()` function with chained `if/elif/else` checks
- Practice the ternary: `label = "Long" if len(tag) > 10 else "Short"`
- Use `in` with a set of valid platforms rather than a long `or` chain
- Try refactoring deeply nested `if` blocks into early-return functions
