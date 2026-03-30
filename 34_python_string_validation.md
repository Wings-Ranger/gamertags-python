# Python String Validation

**W3Schools Link:** https://www.w3schools.com/python/ref_string_isdigit.asp

---

## Overview
Python strings have a family of `.is*()` validation methods that check the composition of a string without needing regular expressions. These methods are the primary tools for validating gamertag input — checking for alphanumeric-only characters, digit-only strings, non-empty values, and more. They all return `True` or `False`.

## Key Concepts
- **`.isalpha()`**: all characters are letters (no digits, spaces, or symbols)
- **`.isdigit()`**: all characters are digits `0-9`
- **`.isalnum()`**: all characters are letters or digits (no spaces or symbols)
- **`.isspace()`**: all characters are whitespace (`" "`, `"\t"`, `"\n"`)
- **`.isupper()` / `.islower()`**: all cased characters are upper/lowercase
- **`.istitle()`**: each word starts with uppercase followed by lowercase
- **Empty string caveat**: all `.is*()` methods return `False` on an empty string — always check `if not tag:` first
- **Partial validation**: use `all()` with a generator for custom character rules

## Syntax / Example Code
```python
# --- Core validation methods ---
print("ShadowX".isalpha())      # True  — only letters
print("ShadowX99".isalpha())    # False — has digits
print("4250".isdigit())         # True  — only digits
print("4250.5".isdigit())       # False — decimal point is not a digit
print("ShadowX99".isalnum())    # True  — letters and digits only
print("Shadow X".isalnum())     # False — space is not alnum
print("   ".isspace())          # True
print("".isdigit())             # False — empty string returns False!

# --- Gamertag validation function ---
def validate_gamertag(tag):
    """
    Validate a gamertag against all rules.
    Returns (is_valid: bool, message: str).
    """
    if not tag:                    # check empty first
        return False, "Cannot be empty"
    if not tag.isalnum():
        return False, "Letters and numbers only (no spaces or symbols)"
    if len(tag) < 3:
        return False, "Too short (minimum 3 characters)"
    if len(tag) > 15:
        return False, "Too long (maximum 15 characters)"
    if tag.isdigit():
        return False, "Must contain at least one letter"
    return True, "Valid"

tests = [
    "",
    "AB",
    "Shadow Hunter",
    "Shadow@X",
    "123456",
    "ShadowX99",
    "ShadowHunter99Valid",
    "ValidTag",
]

for test in tests:
    valid, msg = validate_gamertag(test)
    status = "✓" if valid else "✗"
    print(f"  {status} '{test}': {msg}")

# --- Score validation (digit check before int conversion) ---
def get_score_from_string(s):
    """Safely convert a score string to int."""
    s = s.strip()
    if not s:
        return None, "Empty value"
    if not s.isdigit():
        return None, f"'{s}' is not a valid score (digits only)"
    return int(s), "OK"

score, msg = get_score_from_string("4250")
print(score, msg)   # 4250 OK

score, msg = get_score_from_string("abc")
print(score, msg)   # None 'abc' is not a valid score (digits only)

# --- Custom character set validation ---
# Allow letters, digits, and underscore only
def is_valid_extended_tag(tag):
    allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")
    return bool(tag) and all(c in allowed for c in tag)

print(is_valid_extended_tag("Shadow_X99"))   # True
print(is_valid_extended_tag("Shadow-X99"))   # False (hyphen not allowed)

# --- Checking first character is a letter ---
def starts_with_letter(tag):
    return bool(tag) and tag[0].isalpha()

print(starts_with_letter("ShadowX"))   # True
print(starts_with_letter("99Shadow"))  # False

# --- Checking for all-whitespace (before stripping) ---
raw = "   "
if raw.isspace() or not raw.strip():
    print("Input is blank")
```

## Common Use Cases
- `.isalnum()` — the core gamertag character check
- `.isdigit()` — validate score input before calling `int()`
- Empty check `if not tag:` — always the first validation step
- `all(c.isalnum() or c == "_" for c in tag)` — custom character set check

## Related Days
| Day | Topic |
|-----|-------|
| Day 6 | String and Character Validation (empty-string safety, character checks) |
| Days 11-12 | Filters and logic |

## See Also
- [05_python_strings.md](05_python_strings.md)
- [32_python_string_methods.md](32_python_string_methods.md)
- [12_python_if_else.md](12_python_if_else.md)
- [11_python_type_casting.md](11_python_type_casting.md)

## Practice Tips
- Always check `if not tag:` before calling `.isalnum()` (empty string returns `False` from `.isalnum()` but your error message should say "empty")
- Build a complete `validate_gamertag(tag)` function and test it with edge cases
- Use `.isdigit()` before every `int()` conversion on user-provided or file-read data
- Test with tricky inputs: all digits, all spaces, Unicode characters, very long strings
