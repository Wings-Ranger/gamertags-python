# Python Type Casting

**W3Schools Links:**
- [Python Type Casting](https://www.w3schools.com/python/python_casting.asp) — `int()`, `float()`, `str()`, `bool()` conversion functions
- [Python User Input](https://www.w3schools.com/python/python_user_input.asp) — `input()` always returns a string; must cast for arithmetic
- [Python String Methods](https://www.w3schools.com/python/python_ref_string.asp) — `.isdigit()` for safe check before `int()`; `.split()` for parsing CSV
- [Python Try Except](https://www.w3schools.com/python/python_try_except.asp) — handling `ValueError` when `int()` receives non-numeric input

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

**C# pattern (from the gamertag project):**
```csharp
// C# Console.ReadLine() returns a string — same as Python's input()
string userInput = Console.ReadLine();

// Parsing a value from a comma-separated file line
string[] parts = line.Split(',');
int score = int.Parse(parts[2]);    // C# int.Parse()
```

**Python skeleton (fill in the blanks):**
```
# input() ALWAYS returns a string — just like Console.ReadLine() in C#
user_input = input("Enter score: ")    # e.g., "4250"
score      = _____(user_input)         # convert string to int to do math

# File data also comes as strings — must cast for arithmetic
line  = "ShadowHunter99,Xbox,4250"
parts = line._____(_____)              # split on comma
gamertag = parts[_____]               # string — no cast needed
platform = parts[_____]               # string — no cast needed
score    = _____(parts[_____])         # MUST cast to int for math
print(f"{gamertag} has score {score + _____}")   # arithmetic now works

# int() TRUNCATES — it does NOT round
print(_____(9.9))    # what number does this produce?
print(_____(3.14))   # what number does this produce?

# str() for string concatenation
score   = 4250
message = "Score: " + _____(score)    # types must match for + concatenation

# Guard before casting — check first, then convert
raw = input("Enter a number: ")
if raw._____(  ):                      # what method checks for digits only?
    number = _____(raw)
else:
    print("That is not a valid number")
```

**Questions:**
- C# has `int.Parse()` and Python has `int()`. What happens in both languages when you pass a non-numeric string?
- Why must you always cast the result of `input()` if you want to do arithmetic with it?
- What is the difference between `int("9.5")` and `int(float("9.5"))`? Try both.
- What string method lets you check if a string contains only digits, before calling `int()`?

**Test challenge:**
Read a score from the user with `input()`. Try to add 100 to it WITHOUT casting — what error appears? Then add the `int()` cast and confirm the addition works correctly.

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

## Challenges

1. **Input casting:** `input()` always returns a string. Fill in the cast to do arithmetic:
   ```
   raw   = input("Enter your score: ")
   score = _____(raw)
   print(f"Score plus bonus: {score + 100}")
   ```

2. **File data parsing:** When you read a line from the gamertag file, all fields are strings. Fill in:
   ```
   line     = "ProSniper,PC,5100"
   parts    = line._____(_____)
   gamertag = parts[_____]
   score    = _____(parts[_____])    # which index? what cast?
   ```

3. **Truncation vs rounding:** Predict the output before running each line:
   - `int(9.9)` → `_____`
   - `int(-3.7)` → `_____`
   - `round(9.9)` → `_____`
   What is the difference between `int()` and `round()`?

4. **Safe integer check:** Use `.isdigit()` to guard against bad input before casting:
   ```
   raw = "abc"
   if raw._____(  ):
       number = int(raw)
   else:
       print("_____")    # what message should appear?
   ```
