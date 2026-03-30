# Python Strings

**W3Schools Link:** https://www.w3schools.com/python/python_strings.asp

**Homework Day(s):** Day 1, Day 6

---

## Overview
Strings in Python are sequences of characters enclosed in single or double quotes. They are one of the most commonly used data types and come with a rich set of built-in methods for manipulation, searching, and formatting. Strings are immutable — once created, they cannot be modified in place.

## Key Concepts
- **Immutable**: string methods return new strings, they don't modify the original
- **Indexing**: `s[0]` gets the first character; `s[-1]` gets the last
- **Slicing**: `s[1:4]` extracts a substring
- **len()**: returns the number of characters
- **Concatenation**: `"Hello" + " " + "World"` joins strings
- **Repetition**: `"ab" * 3` gives `"ababab"`
- **f-strings**: `f"Name: {name}"` — the modern way to embed variables
- **Multiline strings**: use triple quotes `"""..."""`

## Syntax / Example Code
```python
# Creating strings
gamertag = "ShadowHunter99"
platform = 'Xbox'
bio = """This player is a competitive
shooter who specializes in stealth."""

# Indexing and length
print(gamertag[0])       # S
print(gamertag[-1])      # 9
print(len(gamertag))     # 14

# Slicing
print(gamertag[0:6])     # Shadow
print(gamertag[6:])      # Hunter99
print(gamertag[:6])      # Shadow

# Common string methods
print(gamertag.upper())           # SHADOWHUNTER99
print(gamertag.lower())           # shadowhunter99
print("  gamerx  ".strip())       # gamerx
print(gamertag.replace("99", ""))  # ShadowHunter
print(gamertag.startswith("Shadow"))  # True
print(gamertag.endswith("99"))        # True
print("99" in gamertag)               # True

# f-strings (formatted string literals)
name = "NightOwl"
score = 4250
print(f"Player: {name} | Score: {score}")

# Splitting and joining
csv_line = "GamerX,Xbox,4500"
parts = csv_line.split(",")
print(parts)             # ['GamerX', 'Xbox', '4500']
rejoined = ", ".join(parts)
print(rejoined)          # GamerX, Xbox, 4500

# Checking if gamertag is empty
tag = input("Enter gamertag: ").strip()
if not tag:
    print("Gamertag cannot be empty")
```

## Common Use Cases
- Reading and cleaning gamertag names from user input (`.strip()`)
- Validating gamertag format (`.isalnum()`, `.startswith()`)
- Displaying formatted player records with f-strings
- Parsing CSV lines from a gamertag file with `.split(",")`
- Converting case for case-insensitive comparisons (`.lower()`)

## Related Days
| Day | Topic |
|-----|-------|
| Day 1 | Python Foundations (variables, data types, strings, lists) |
| Day 6 | String and Character Validation (empty-string safety, character checks) |

## See Also
- [32_python_string_methods.md](../07_strings/32_python_string_methods.md)
- [33_python_string_slicing.md](../07_strings/33_python_string_slicing.md)
- [34_python_string_validation.md](../07_strings/34_python_string_validation.md)
- [35_python_string_formatting.md](../07_strings/35_python_string_formatting.md)

## Practice Tips
- Practice `.strip()` on every string read from user input or files
- Try splitting a CSV line and accessing each field by index
- Build a gamertag validator that checks length and character type
- Experiment with f-strings to format player display output neatly
