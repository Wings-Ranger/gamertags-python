# Python String Methods

**W3Schools Link:** https://www.w3schools.com/python/python_ref_string.asp

**Homework Day(s):** Day 6

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

```
C# patterns (from the gamertag project):
    // Check if last character is a number
    Char.IsNumber(s, s.Length - 1)

    // Check if first character is not a letter or digit
    !Char.IsLetterOrDigit(s, 0)

    // Reading a line and splitting
    string[] parts = line.Split(',');

Python skeleton — use string methods (fill in the blanks):

    s = "ShadowX99"

    # Equivalent to Char.IsNumber(s, s.Length - 1)
    # Check if the LAST character is a digit
    if s[_____]._____(  ):              # what index is the last character?
        print(f"{s} ends with a number")

    # Equivalent to !Char.IsLetterOrDigit(s, 0)
    # Check if the FIRST character is NOT a letter or digit
    if not s[_____]._____(  ):          # what index is the first character?
        print(f"{s} starts with special character")

    # Strip whitespace (always do this on user input and file lines)
    raw = "  ShadowX99  "
    cleaned = raw._____(  )             # what removes leading/trailing spaces?

    # Split a CSV line (like C#'s string.Split(','))
    line = "ShadowX,Xbox,4250"
    parts = line._____(_____)           # what method splits? what separator?
    tag      = parts[_____]             # index 0
    platform = parts[_____]             # index 1
    score    = parts[_____]             # index 2

    # Rejoin parts (reverse of split)
    rejoined = _____.join(parts)        # what separator? what method joins?

    # Case conversion
    platform_input = "xbox"
    normalized = platform_input._____(  )   # "xbox" -> "Xbox" (W3Schools: title())

    # Check if gamertag is all letters+digits
    tag = "ShadowX99"
    if tag._____(  ):                    # what .is*() method checks alphanumeric?
        print("Valid characters")

Questions:
- How do you access the last character of a string in Python without knowing
  its length? (Compare to C#'s `s[s.Length - 1]`)
- What is the Python equivalent of `Char.IsLetterOrDigit(s, 0)`?
- What does `.split(",")` return — a string or a list?
- What is the difference between `.strip()`, `.lstrip()`, and `.rstrip()`?

Test challenge:
    Implement `print_gamertags_ending_with_number(self)`: loop over
    `self.gamer_tag_list`, and for each tag where `tag[-1].isdigit()` is True,
    print it. Test with a list that includes "Shadow99", "NightOwl", "Pro7".
    Which ones print?
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

## Challenges
- **Blank 1**: Write the condition for `print_gamertags_ending_with_number`: `if s[_____]._____(  ):`. What is the Python index for the last character? What method checks if a character is a digit?
- **Blank 2**: Write the condition for `print_gamertags_not_starting_with_number_or_letter`: `if not s[_____]._____(  ):`. C# uses `Char.IsLetterOrDigit(s, 0)` — what is the Python equivalent call?
- **Blank 3**: Write `line.split(",")` to parse a CSV line, then access each part by index. Write `parts[0]`, `parts[1]`, `parts[2]` to get tag, platform, score.
- **Challenge**: The C# project checks `Char.IsNumber(s, s.Length - 1)` — it checks a specific index. Python's `s[-1].isdigit()` does the same with a negative index. Write both side by side as comments. What happens if `s` is an empty string in both languages? How do you protect against that in Python?
