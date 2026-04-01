# Python Strings

**W3Schools Links:**
- [Python Strings](https://www.w3schools.com/python/python_strings.asp) — string basics, indexing, immutability
- [Python String Methods](https://www.w3schools.com/python/python_ref_string.asp) — `.isdigit()`, `.isalnum()`, `.strip()`, `.lower()` (used in exercises)
- [Python String Slicing](https://www.w3schools.com/python/python_strings_slicing.asp) — `s[-1]` last character, `s[0]` first character
- [Python String Formatting](https://www.w3schools.com/python/python_string_formatting.asp) — f-strings used in output exercises
- [Python User Input](https://www.w3schools.com/python/python_user_input.asp) — `input()` and `.strip()` used in challenge 4

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

**C# pattern (from the gamertag project):**
```csharp
// C# uses character-level checks for gamertag validation
Char.IsNumber(s, s.Length - 1)      // is last character a digit?
!Char.IsLetterOrDigit(s, 0)         // does it NOT start with letter/digit?
string newTag = Console.ReadLine();  // read string from user
```

**Python skeleton (fill in the blanks):**
```
gamertag = "ShadowHunter99"

# Access the LAST character (Python uses negative indexing — no .Length - 1)
last_char  = gamertag[-1]    # -1 means last character

# Access the FIRST character
first_char = gamertag[0]    # 0 means first character

# Check if last character is a digit (replaces C#'s Char.IsNumber)
print(last_char.isdigit(  ))      # returns True or False

# Check if first character is a letter or digit (replaces Char.IsLetterOrDigit)
print(first_char.isalnum(  ))     # returns True or False

# Check if the ENTIRE gamertag is letters and digits only
print(gamertag._____(  ))       # one method to check the whole string

# Get length (replaces C#'s .Length property)
print(_____(gamertag))

# Strip whitespace from user input (always do this after input() or file reads)
raw_input = "  GamerX  "
clean = raw_input._____(  )

# f-string formatting
name  = _____
score = _____
print(_____"Player: {_____} | Score: {_____}")
```

**Questions:**
- C# uses `Char.IsNumber(s, s.Length - 1)` to check the last character. How does Python's index `-1` give you the last character more simply?
- What Python string method checks if a single character (or whole string) contains only digits? (Replaces `Char.IsNumber`)
- What Python string method checks if all characters are letters or digits? (Replaces `Char.IsLetterOrDigit`)
- Why should you always call `.strip()` on strings read from user input or files?

**Test challenge:**
Write Python code that checks `"ShadowHunter99"`: (1) does it end with a digit? (2) does it start with a letter or digit? (3) is the entire string alphanumeric? Print `True` or `False` for each check.

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

## Challenges

1. **Character checks:** The C# project uses `Char.IsNumber(s, s.Length - 1)` to check if the last character is a number. Fill in the Python equivalent:
   ```
   s = "ShadowHunter99"
   last_char = s[_____]           # get last character
   print(last_char._____(  ))     # is it a digit?
   ```

2. **Start character check:** C# uses `!Char.IsLetterOrDigit(s, 0)` to check the first character. Fill in Python:
   ```
   first_char = s[_____]                   # get first character
   print(_____ first_char._____(  ))       # does it NOT start with letter/digit?
   ```

3. **Whole-string check:** What single Python method checks if ALL characters in a string are alphanumeric? Test it on each and predict `True` or `False`:
   ```
   print("ShadowX"._____(  ))    # _____
   print("Shadow X"._____(  ))   # _____ (why different?)
   print("99"._____(  ))         # _____
   ```

4. **Input cleaning:** A user types `"  NightOwl  "` with extra spaces. Write Python to strip whitespace before using the value. Why must this step always happen when reading from `input()` or a file?
   ```
   raw   = "  NightOwl  "
   clean = raw._____(  )
   ```
