# What is Python

**W3Schools Links:**
- [Python Introduction](https://www.w3schools.com/python/python_intro.asp) — what Python is and why it's used
- [Python Variables](https://www.w3schools.com/python/python_variables.asp) — declaring and naming variables (used in exercises)
- [Python Output / print()](https://www.w3schools.com/python/ref_func_print.asp) — printing to the screen
- [Python String Formatting (f-strings)](https://www.w3schools.com/python/python_string_formatting.asp) — embedding variables in strings

**Homework Day(s):** Day 1

---

## Overview
Python is a high-level, interpreted programming language known for its clean, readable syntax. Created by Guido van Rossum and first released in 1991, Python emphasizes code readability and simplicity. It is one of the most popular languages in the world, used for web development, data science, automation, and more.

## Key Concepts
- Python is **interpreted**: code runs line by line, making debugging easier
- Python uses **indentation** (not curly braces) to define code blocks
- Python is **dynamically typed**: you don't declare variable types explicitly
- Python is **cross-platform**: runs on Windows, macOS, and Linux
- Python supports multiple programming paradigms: procedural, object-oriented, and functional

## Syntax / Example Code

**C# pattern (from the gamertag project):**
```csharp
Console.WriteLine("Welcome to the Gamertag Manager!");
string gamertag = "ShadowHunter99";
Console.WriteLine("Gamertag: " + gamertag);
```

**Python skeleton (fill in the blanks):**
```
# Your first Python program
_____("Welcome to the Gamertag Manager!")

# Python is case-sensitive — these are TWO different variables
gamertag = _____
Gamertag = _____

# Use an f-string to embed a variable in output
_____(_____"Gamertag '{_____}' is registered on {_____}")
```

**Questions:**
- What single Python function prints output to the screen? (C# uses `Console.WriteLine` — Python uses one lowercase word)
  *print*
- In C#, strings are joined with `+`. What does Python's f-string syntax `f"..."` let you do instead?
  *You can enter dsfjasdf = f "your text here"*
  *then display the words with*
  *print(dsfjasdf)*
- Do Python statements end with a semicolon?
  *no you do not need the semicolins*
- If you define both `gamertag` and `Gamertag`, are they the same variable or two different ones?
  *they are two different ones as they are case sensetive*
**Test challenge:**
Create a Python script that stores your own made-up gamertag in a variable and prints a formatted welcome message using that variable. Run it and confirm the output is exactly right.
>>> gamertag = "Wings_Ranger"
>>> welcome_message = f"Welcome to the program {gamertag}"
>>> print(welcome_message)
Welcome to the program Wings_Ranger
## Common Use Cases
- Learning to program: Python's simple syntax is ideal for beginners
- Scripting and automation: automate repetitive tasks
- Data processing: reading files, transforming data (like gamertag lists)
- Web development: building APIs and websites
- Game development utilities: managing player data, leaderboards

## Related Days
| Day | Topic |
|-----|-------|
| Day 1 | Python Foundations (variables, data types, strings, lists) |

## See Also
- [02_python_syntax.md](02_python_syntax.md)
- [03_python_variables.md](03_python_variables.md)
- [31_python_print.md](../06_file_io/31_python_print.md)

## Challenges

1. **Print challenge:** Fill in the blanks to print `"Welcome, ShadowHunter99!"` where the name is stored in a variable:
   ```
   player_name = _____
   _____(f"Welcome, {_____}!")
   ```

2. **Case sensitivity:** Declare `gamertag = "NightOwl"` and `Gamertag = "ProSniper"`. Print both. Are they the same variable? What error would occur if you only defined one but tried to print the other?

3. **No semicolons:** Rewrite this C# line as valid Python — what do you remove?
   ```csharp
   string platform = "Xbox";
   ```
   Python: `platform = _____`

4. **REPL experiment:** Open a Python terminal and type `Print("test")` (capital P). What error appears? Now correct it. Why does Python give this specific error?
