# Python String Slicing

**W3Schools Link:** https://www.w3schools.com/python/python_strings_slicing.asp

**Homework Day(s):** Day 6, Days 11–12

---

## Overview
String slicing extracts a portion of a string using bracket notation with start, stop, and step indices. Since strings are sequences, the same slicing syntax works for lists and tuples too. Slicing is useful for extracting parts of gamertags, checking prefixes/suffixes, or truncating long strings for display.

## Key Concepts
- **Syntax**: `string[start:stop:step]`
- **Zero-based indexing**: first character is index `0`
- **Negative indices**: `-1` is the last character, `-2` is second-to-last
- **Stop is exclusive**: `s[0:3]` returns characters at index 0, 1, 2 (not 3)
- **Omitting start/stop**: `s[:3]` from beginning; `s[3:]` to end; `s[:]` full copy
- **Step**: `s[::2]` every other character; `s[::-1]` reverses the string
- **Strings are immutable**: slicing creates a new string; original unchanged

## Syntax / Example Code

```
C# patterns (from the gamertag project):
    // Access last character using length
    char lastChar = s[s.Length - 1];

    // Access first character
    char firstChar = s[0];

    // Check last character is a number
    Char.IsNumber(s, s.Length - 1)

Python skeleton — use slicing and index access (fill in the blanks):

    tag = "ShadowHunter99"
    #      0123456789...

    # Access first character (equivalent to s[0] in C#)
    first = tag[_____]       # index 0

    # Access last character (equivalent to s[s.Length - 1] in C#)
    last = tag[_____]        # what negative index means "last"?

    # Get last 2 characters
    suffix = tag[_____:]     # what negative index for "last 2"?

    # Get all but the last character
    without_last = tag[:_____]

    # Basic slice — first 6 characters
    prefix = tag[_____:_____]   # start: 0, stop: 6 (stop is exclusive)

    # Gamertag project: check if last char is a digit
    # C# equivalent: Char.IsNumber(s, s.Length - 1)
    if tag[_____]._____(  ):
        print(f"{tag} ends with a digit")

    # Gamertag project: check if first char is NOT letter or digit
    # C# equivalent: !Char.IsLetterOrDigit(s, 0)
    if not tag[_____]._____(  ):
        print(f"{tag} starts with a special character")

    # Truncate for display (max 10 chars shown)
    def truncate(text, max_len=_____):
        if len(text) > _____:
            return text[:_____] + "..."   # slice + ellipsis
        return _____

    # Reversed string (interview classic)
    reversed_tag = tag[_____:_____:_____]   # what step reverses a string?

Questions:
- In C#, the last character index is `s.Length - 1`. What is the Python shortcut?
- What does `tag[2:5]` return for `tag = "ShadowX"`? (Remember: stop is exclusive)
- What does a negative step in a slice do?
- Why does slicing never raise an IndexError, even with out-of-range values?

Test challenge:
    For each gamertag in your list, use slicing to check if the last character
    is a digit (`tag[-1].isdigit()`). Print only the ones that end with a digit.
    Now try `tag[-2:].isdigit()` — this checks the last TWO characters. What
    happens with "Shadow9X"? Does it still work as expected?
```

## Common Use Cases
- Extracting the alphabetic prefix of a gamertag (`tag[:i]` before first digit)
- Checking the first character with `tag[0]`
- Truncating long names for fixed-width display
- Reversing a string with `[::-1]` (interview question favorite)
- Filtering tags by prefix using `tag[:n]`

## Related Days
| Day | Topic |
|-----|-------|
| Day 6 | String and Character Validation (empty-string safety, character checks) |
| Days 11-12 | Filters and logic |

## See Also
- [05_python_strings.md](../02_data_types/05_python_strings.md)
- [32_python_string_methods.md](32_python_string_methods.md)
- [34_python_string_validation.md](34_python_string_validation.md)

## Challenges
- **Blank 1**: Fill in `tag[_____]` to get the last character. Then check if it's a digit: `tag[_____]._____(  )`. What two blanks are needed?
- **Blank 2**: Write a `truncate(text, max_len=10)` function. Use `text[:_____]` to keep only `max_len - 3` characters, then add `"..."`. What goes in the blank?
- **Blank 3**: Write a filter that finds all gamertags starting with "Shadow": `[t for t in tags if t[:_____].lower() == "_____"]`. What length prefix do you slice? What string do you compare to?
- **Challenge**: The C# index `s[s.Length - 1]` and Python index `s[-1]` both access the last character. Write a function `split_tag(tag)` that uses slicing to separate the alphabetic prefix from any trailing digits. For "Shadow99", it should return `("Shadow", "99")`. Hint: you'll need a loop or string methods to find where digits start.
