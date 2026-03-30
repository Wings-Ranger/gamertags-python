# Python Functions

**W3Schools Link:** https://www.w3schools.com/python/python_functions.asp

**Homework Day(s):** Day 4, Day 8, Day 9, Day 10

---

## Overview
Functions are reusable blocks of code that perform a specific task. Defining functions is how you organize a program into logical, testable units — a core principle of software design called decomposition. In Python, functions are defined with the `def` keyword and can accept parameters and return values.

## Key Concepts
- **Defined with `def`**: `def function_name(parameters):`
- **Called (invoked)**: `function_name(arguments)`
- **Parameters vs arguments**: parameters are in the definition; arguments are the actual values passed
- **`return`**: sends a value back to the caller; without it, the function returns `None`
- **Docstrings**: triple-quoted strings immediately after `def` to document the function
- **Single responsibility**: each function should do one thing well
- **DRY principle**: Don't Repeat Yourself — extract repeated code into a function

## Syntax / Example Code

**C# pattern (from the gamertag project):**
```csharp
// C# Gamertags class has named methods for each action
public void LoadGamertags()                              { ... }
public void PrintAllGamertags()                          { ... }
public void PrintGamertagsEndingWithNumber()             { ... }
public void PrintGamertagsNotStartingWithNumberorLetter(){ ... }
public void ShowWelcomeMessage()                         { ... }
public void AddNewUserName()                             { ... }
```

**Python skeleton (fill in the blanks):**
```
# Python uses 'def' instead of C#'s access modifier + return type + method name

# C#: public void PrintAllGamertags()
def _____(_____)  :
    """_____ — describe what this function does."""
    for _____ in _____:
        print(_____)

# C#: public void LoadGamertags()
def _____(filename):
    """Load gamertags from a file and return them as a list."""
    gamer_tag_list = _____
    with _____(filename, _____) as f:
        for line in _____:
            line = line._____(  )
            if _____:
                gamer_tag_list._____(line)
    _____ gamer_tag_list

# C#: public void ShowWelcomeMessage()
def _____():
    """Display the main menu options."""
    print("1. Load gamertags")
    print("2. Print all gamertags")
    print("3. _____")
    print("4. _____")
    print("5. _____")
    print("6. Quit")

# C#: public void AddNewUserName()
def _____():
    """Ask user for a new gamertag and return it."""
    new_tag = input("_____")._____(  )
    if _____:
        _____ new_tag
```

**Questions:**
- C# methods start with `public void MethodName()`. What single keyword does Python use to define a function?
- C# `void` means the method returns nothing. What does a Python function return when it has no `return` statement?
- C# method names use PascalCase (`PrintAllGamertags`). What naming convention does Python use for functions?
- What is a docstring and where does it go inside a Python function?

**Test challenge:**
Write empty stub functions (using `pass`) for all six methods from the C# `Gamertags` class. Give each a descriptive docstring. Confirm you can call each one without an error.

## Common Use Cases
- `is_valid_gamertag(tag)` — validation function called before saving
- `load_players(filename)` — data loading abstracted into one place
- `display_player(player)` — display logic separated from data logic
- `get_rank(score)` — business logic encapsulated for reuse

## Related Days
| Day | Topic |
|-----|-------|
| Day 4 | Functions (decomposition, inputs/outputs, naming) |
| Day 8 | Python Project Skeleton |
| Day 9 | Data Loading and Welcome Sequence |
| Day 10 | Display All Gamertags |

## See Also
- [18_python_function_arguments.md](18_python_function_arguments.md)
- [19_python_return_values.md](19_python_return_values.md)
- [20_python_lambda.md](20_python_lambda.md)
- [40_python_scope.md](../09_advanced/40_python_scope.md)

## Challenges

1. **Translate the class methods:** The C# project has six methods. Write Python stub functions (with `pass`) for each — use correct snake_case naming:
   ```
   def load_gamertags(_____):
       """_____"""
       _____

   def print_all_gamertags(_____):
       """_____"""
       _____

   def print_gamertags_ending_with_number(_____):
       """_____"""
       _____
   ```

2. **Name the parameters:** `PrintAllGamertags` in C# accesses `gamerTagList` as a class field — no parameter needed. In Python you pass it as a parameter. What should you name the parameter and what type will it be?

3. **Return vs void:** `LoadGamertags` in C# sets a class field (void). In Python it is cleaner to return the list. Fill in:
   ```
   def load_gamertags(filename):
       gamer_tag_list = []
       # ... load lines ...
       _____ gamer_tag_list    # return the list to the caller
   ```

4. **Call order:** In `Program.cs`, `LoadGamertags()` runs before `PrintAllGamertags()`. In Python, how do you pass the loaded list from one function to the next?
   ```
   tags = _____(_____)      # call load, store the returned list
   _____(_____)             # pass that list to print
   ```
