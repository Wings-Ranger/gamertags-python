# Python String Validation

**W3Schools Link:** https://www.w3schools.com/python/ref_string_isdigit.asp

**Homework Day(s):** Day 6, Day 11, Day 12

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

```
C# patterns (from the gamertag project):
    // Check last character is a number
    Char.IsNumber(s, s.Length - 1)

    // Check first character is NOT a letter or digit
    !Char.IsLetterOrDigit(s, 0)

Python skeleton — use .is*() validation methods (fill in the blanks):

    s = "ShadowX99"

    # Equivalent to Char.IsNumber(s, s.Length - 1)
    # isdigit() checks a single character or whole string
    if s[_____]._____(  ):                  # last char, is it a digit?
        print(f"{s} ends with a number")

    # Equivalent to !Char.IsLetterOrDigit(s, 0)
    if not s[_____]._____(  ):              # first char, is it alphanumeric?
        print(f"{s} does NOT start with a letter or digit")

    # Validate entire gamertag (letters and digits only, no spaces)
    tag = "Shadow X"
    if tag._____(  ):                        # what .is*() checks the whole string?
        print("Valid")
    else:
        print("Invalid — has spaces or symbols")

    # Check for digits only (for score validation)
    score_str = "4250"
    if score_str._____(  ):                  # what .is*() checks digits only?
        score = int(score_str)
    else:
        print("Not a valid score")

    # Full validation function skeleton
    def validate_gamertag(tag):
        if not _____:                        # what checks if tag is empty/None?
            return False, "Cannot be empty"
        if not tag._____(  ):               # alphanumeric check
            return False, "Letters and numbers only"
        if len(tag) < _____ or len(tag) > _____:  # length bounds
            return False, "Must be 3-15 characters"
        return True, _____                   # what string means success?

    # Test your function
    tests = ["", "AB", "Shadow X", "Shadow@X", "ValidTag99"]
    for t in tests:
        valid, msg = validate_gamertag(t)
        print(f"'{t}': {msg}")

Questions:
- What is the difference between `.isdigit()`, `.isalpha()`, and `.isalnum()`?
- What do ALL `.is*()` methods return for an empty string? Why does that matter?
- C# uses `Char.IsNumber()` on a specific index. Python uses `s[-1].isdigit()`.
  What is the Python equivalent of `Char.IsLetterOrDigit()`?
- Why should you always check `if not tag:` BEFORE calling `.isalnum()`?

Test challenge:
    Create a list of test gamertags that covers every failing case:
    empty string, too short (1-2 chars), too long (16+ chars), has a space,
    has a symbol like "@", all digits, and a valid one. Run each through
    your validate_gamertag function. Do all cases return the right message?
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
| Day 11 | Filter 1 (Ending with Number) |
| Day 12 | Filter 2 (Not Starting with Letter or Number) |

## See Also
- [05_python_strings.md](../02_data_types/05_python_strings.md)
- [32_python_string_methods.md](32_python_string_methods.md)
- [12_python_if_else.md](../03_control_flow/12_python_if_else.md)
- [11_python_type_casting.md](../02_data_types/11_python_type_casting.md)

## Challenges
- **Blank 1**: Implement `print_gamertags_ending_with_number(self)`. The condition is `if s[_____]._____(  ):`. Fill both blanks. Which gamertags from `["Shadow99", "NightOwl", "7ProX", "GamerZ"]` would print?
- **Blank 2**: Implement `print_gamertags_not_starting_with_number_or_letter(self)`. The condition is `if not s[_____]._____(  ):`. Fill both blanks. What gamertags like `"@Shadow"` or `"_Pro"` would this catch?
- **Blank 3**: Complete `validate_gamertag(tag)`. Write the empty check, the `.isalnum()` check, and the length check. What two length values do the gamertag rules require?
- **Challenge**: Python's `.isdigit()` returns `False` for an empty string. Test `"".isdigit()` and `"".isalnum()`. Now test `" ".isalnum()` (a single space). What do these return? Why does this mean you must ALWAYS check `if not tag.strip():` as your FIRST validation step?
