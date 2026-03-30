# Python Type Casting

**W3Schools Link:** https://www.w3schools.com/python/python_casting.asp

**Homework Day(s):** Day 1, Day 6

---

## Overview
Type casting (also called type conversion) is the process of converting a value from one data type to another. Python provides built-in functions like `int()`, `float()`, `str()`, and `bool()` for explicit conversion. This is especially important when reading user input (which is always a string) or reading data from files.

## Key Concepts
- **Explicit casting**: manually convert using `int()`, `float()`, `str()`, `list()`, `tuple()`, `set()`
- **Implicit casting**: Python automatically promotes `int` to `float` in mixed arithmetic
- **`input()` always returns a string**: must cast to `int` or `float` for numeric operations
- **`int()`**: converts float or numeric string to integer (truncates, doesn't round)
- **`float()`**: converts int or decimal string to float
- **`str()`**: converts any value to its string representation
- **Failure mode**: invalid conversions raise `ValueError` — always use try/except

## Syntax / Example Code
```python
# input() returns a string — must cast for math
age_str = input("Enter your age: ")   # e.g., "17"
age = int(age_str)                     # now it's an integer
print(age + 1)                         # 18

# Converting score from a file (read as string)
line = "ShadowHunter99,Xbox,4250"
parts = line.split(",")
gamertag = parts[0]           # str
platform = parts[1]           # str
score = int(parts[2])         # cast to int

print(f"{gamertag} has score {score + 100}")  # arithmetic works

# int() truncates (does not round)
print(int(9.9))     # 9
print(int(-3.7))    # -3

# float() from int or string
print(float(5))     # 5.0
print(float("3.14")) # 3.14

# str() for building output
score = 4250
message = "Score: " + str(score)   # concatenation requires str
print(message)

# Safe casting with try/except
def safe_int(value, default=0):
    try:
        return int(value)
    except ValueError:
        return default

print(safe_int("4250"))    # 4250
print(safe_int("abc"))     # 0  (default)
print(safe_int("4250.5"))  # 0  (int() won't convert float strings directly)

# Checking type before casting
raw = "123"
if raw.isdigit():
    number = int(raw)
    print(f"Valid number: {number}")
else:
    print("Not a valid integer string")

# Converting between collection types
tags_tuple = ("GamerX", "NightOwl", "ProSniper")
tags_list = list(tags_tuple)
tags_set = set(tags_list)       # removes duplicates
tags_tuple_again = tuple(tags_set)
```

## Common Use Cases
- Converting scores read from CSV files from strings to integers
- Casting `input()` results to the expected type
- Using `.isdigit()` before `int()` to validate user input safely
- Converting between list, tuple, and set as needed

## Related Days
| Day | Topic |
|-----|-------|
| Day 1 | Python Foundations (variables, data types, strings, lists) |
| Day 6 | String and Character Validation (empty-string safety, character checks) |

## See Also
- [04_python_numbers.md](04_python_numbers.md)
- [05_python_strings.md](05_python_strings.md)
- [34_python_string_validation.md](../07_strings/34_python_string_validation.md)
- [36_python_try_except.md](../08_error_handling/36_python_try_except.md)

## Practice Tips
- Always wrap `int(input(...))` in a `try/except ValueError` block
- Use `.isdigit()` on string input before casting to `int()`
- Test `int("4250.5")` to see why you may need `float()` first then `int()`
- Practice writing a `safe_int()` helper and reuse it throughout your project
