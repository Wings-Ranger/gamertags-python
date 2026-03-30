# Python String Methods

**W3Schools Link:** https://www.w3schools.com/python/python_ref_string.asp

---

## Overview
Python strings come with a rich library of built-in methods for searching, transforming, splitting, and validating text. These methods do not modify the original string (strings are immutable) — they return new strings. Mastering string methods is essential for processing gamertag input, parsing file data, and formatting output.

## Key Concepts
- **Immutable**: all methods return new strings; the original is unchanged
- **Case methods**: `.upper()`, `.lower()`, `.title()`, `.capitalize()`, `.swapcase()`
- **Whitespace methods**: `.strip()`, `.lstrip()`, `.rstrip()`
- **Search methods**: `.find()`, `.index()`, `.count()`, `.startswith()`, `.endswith()`
- **Replace/split/join**: `.replace()`, `.split()`, `.join()`
- **Validation methods**: `.isalpha()`, `.isdigit()`, `.isalnum()`, `.isspace()`, `.isupper()`, `.islower()`
- **Padding methods**: `.center()`, `.ljust()`, `.rjust()`, `.zfill()`

## Syntax / Example Code
```python
tag = "  ShadowHunter99  "

# --- Whitespace ---
print(tag.strip())      # ShadowHunter99
print(tag.lstrip())     # ShadowHunter99  (trailing spaces remain)
print(tag.rstrip())     #   ShadowHunter99 (leading spaces remain)

tag = tag.strip()   # cleaned version

# --- Case ---
print(tag.upper())       # SHADOWHUNTER99
print(tag.lower())       # shadowhunter99
print("xbox".title())    # Xbox
print("xbox".capitalize())  # Xbox

# --- Search ---
print(tag.find("Hunter"))      # 6  (index of first match, -1 if not found)
print(tag.index("99"))         # 12 (raises ValueError if not found)
print(tag.count("9"))          # 2
print(tag.startswith("Shadow"))  # True
print(tag.endswith("99"))        # True
print("99" in tag)               # True (membership test)

# --- Replace ---
clean = tag.replace("99", "")
print(clean)   # ShadowHunter

# --- Split and join ---
csv_line = "ShadowX,Xbox,4250"
parts = csv_line.split(",")        # ['ShadowX', 'Xbox', '4250']
print(parts[0])                    # ShadowX

words = "Shadow Hunter 99".split()  # split on whitespace
print(words)                        # ['Shadow', 'Hunter', '99']

rejoined = ",".join(parts)         # ShadowX,Xbox,4250
spaced = " | ".join(parts)         # ShadowX | Xbox | 4250

# --- Validation ---
print("ShadowX".isalpha())     # True  (letters only)
print("4250".isdigit())        # True  (digits only)
print("ShadowX99".isalnum())   # True  (letters and digits)
print("   ".isspace())         # True  (only whitespace)
print("SHADOW".isupper())      # True
print("shadow".islower())      # True

# --- Padding / alignment ---
print("ShadowX".ljust(15))          # ShadowX        (left, padded to 15)
print("ShadowX".rjust(15))          #         ShadowX
print("ShadowX".center(15, "-"))    # ----ShadowX----
print("42".zfill(6))                # 000042

# --- Practical: clean and validate gamertag ---
def clean_and_validate(raw_tag):
    tag = raw_tag.strip()
    if not tag:
        return None, "Empty gamertag"
    if not tag.isalnum():
        return None, f"Invalid characters in '{tag}'"
    if not (3 <= len(tag) <= 15):
        return None, f"Length {len(tag)} out of range (3-15)"
    return tag, "OK"

tag, msg = clean_and_validate("  ShadowX  ")
print(tag, msg)   # ShadowX OK

tag, msg = clean_and_validate("Shadow Hunter")
print(tag, msg)   # None Invalid characters in 'Shadow Hunter'
```

## Common Use Cases
- `.strip()` on every `input()` call and every line read from a file
- `.isalnum()` to validate that a gamertag contains only letters and numbers
- `.split(",")` to parse CSV lines into fields
- `.lower()` for case-insensitive comparisons and `.title()` to normalize platform names

## Related Days
| Day | Topic |
|-----|-------|
| Day 6 | String and Character Validation (empty-string safety, character checks) |

## See Also
- [05_python_strings.md](../02_data_types/05_python_strings.md)
- [33_python_string_slicing.md](33_python_string_slicing.md)
- [34_python_string_validation.md](34_python_string_validation.md)
- [35_python_string_formatting.md](35_python_string_formatting.md)

## Practice Tips
- Build a `clean_gamertag(raw)` utility that strips, validates, and returns the tag
- Test `.find()` vs `.index()` — notice `.find()` returns -1 while `.index()` raises an exception
- Practice `.split(",")` and `.join(",")` as a round-trip on CSV data
- Use `tag.lower() == other.lower()` for case-insensitive gamertag comparison
