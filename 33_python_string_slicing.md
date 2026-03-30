# Python String Slicing

**W3Schools Link:** https://www.w3schools.com/python/python_strings_slicing.asp

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
```python
tag = "ShadowHunter99"
#      0123456789...

# Basic slicing
print(tag[0:6])     # Shadow  (index 0–5)
print(tag[6:12])    # Hunter  (index 6–11)
print(tag[12:])     # 99      (index 12 to end)
print(tag[:6])      # Shadow  (start to index 5)
print(tag[-2:])     # 99      (last 2 characters)
print(tag[:-2])     # ShadowHunter (all but last 2)

# Negative indexing
print(tag[-1])      # 9  (last character)
print(tag[-2])      # 9  (second to last)
print(tag[-6:-2])   # nter

# Step
print(tag[::2])     # SdwutrS  (every other character)
print(tag[::-1])    # 99retnuHwodahS  (reversed)

# Full copy
copy = tag[:]
print(copy == tag)   # True

# Practical gamertag uses

# Check if tag starts with a letter
if tag[0].isalpha():
    print("Starts with a letter — good!")

# Extract numeric suffix (if any)
# Find where digits start
for i, char in enumerate(tag):
    if char.isdigit():
        prefix = tag[:i]
        suffix = tag[i:]
        print(f"Name part: {prefix}, Number part: {suffix}")
        break

# Truncate for display (max 10 chars)
def truncate(text, max_len=10):
    if len(text) > max_len:
        return text[:max_len - 3] + "..."
    return text

print(truncate("ShadowHunter99"))  # ShadowH...
print(truncate("GamerX"))          # GamerX

# First character check
def starts_with_letter(tag):
    return len(tag) > 0 and tag[0].isalpha()

# Check last two characters for number suffix
def ends_with_digits(tag, n=2):
    return tag[-n:].isdigit()

print(ends_with_digits("ShadowX99"))  # True
print(ends_with_digits("NightOwl"))   # False

# Filtering by prefix
tags = ["ShadowX", "ShadowHunter", "NightOwl", "ProSniper", "Shadow99"]
shadow_tags = [t for t in tags if t[:6].lower() == "shadow"]
print(shadow_tags)   # ['ShadowX', 'ShadowHunter', 'Shadow99']

# Checking last character
for tag in tags:
    if tag[-1].isdigit():
        print(f"{tag} ends with a digit")
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
- [05_python_strings.md](05_python_strings.md)
- [32_python_string_methods.md](32_python_string_methods.md)
- [34_python_string_validation.md](34_python_string_validation.md)

## Practice Tips
- Practice all slice variations: `[2:]`, `[:5]`, `[1:4]`, `[-3:]`, `[::-1]`
- Build a `truncate(text, max_len)` function used in display formatting
- Use slicing to check first/last characters instead of calling `.startswith()`/`.endswith()`
- Remember: stop index is **exclusive** — always test your slice boundaries
