# Python Scope

**W3Schools Link:** https://www.w3schools.com/python/python_scope.asp

**Homework Day(s):** Day 4, Day 8, Day 9, Day 10

---

## Overview
Scope determines where in your program a variable can be accessed. Python uses the LEGB rule to resolve names: Local → Enclosing → Global → Built-in. Understanding scope prevents subtle bugs like accidentally reading a global instead of a local variable, and makes your functions truly independent and testable.

## Key Concepts
- **Local scope**: variables defined inside a function — only accessible within that function
- **Enclosing scope**: variables in an outer function (for nested functions / closures)
- **Global scope**: variables defined at module level — accessible throughout the file
- **Built-in scope**: Python's built-in names (`print`, `len`, `int`, etc.)
- **`global` keyword**: declares that a name inside a function refers to the module-level variable
- **`nonlocal` keyword**: declares that a name refers to the enclosing function's variable
- **Best practice**: avoid `global` — pass values as arguments and return results instead
- **Constants**: module-level ALL_CAPS constants are the acceptable exception to global use

## Syntax / Example Code

```
C# context (from the gamertag project):
    // C# has class-level and method-level scope
    internal class Gamertags
    {
        private string[] gamerTagList = { };  // class (instance) scope

        public void LoadGamertags()
        {
            // local variable — only exists in this method
            string filePath = "../Gamertags.txt";
            gamerTagList = File.ReadAllLines(filePath);
        }
    }

Python skeleton — understand scope with LEGB (fill in the blanks):

    # Module-level constants (GLOBAL scope — all-caps by convention)
    _____ = "Gamertags.txt"          # the filename constant
    _____ = 15                        # max gamertag length
    _____ = 3                         # min gamertag length

    # Function with LOCAL variables
    def load_gamertags(filename):
        gamer_tag_list = _____        # LOCAL — only exists inside this function
        with open(filename) as f:
            for line in f:
                gamer_tag_list.append(line.strip())
        return _____                  # return the local variable to the caller

    # AVOID global mutation — pass data as arguments instead
    # BAD pattern (like C#'s static fields):
    gamer_tag_list = []               # global mutable state

    def bad_load():
        _____ gamer_tag_list          # declares intent to modify global
        gamer_tag_list = open(DATA_FILE).readlines()  # mutates global

    # GOOD pattern — pass and return:
    def good_load(filename):
        result = _____                # local
        # ... fill file ...
        return _____                  # caller gets the data

    # In your Gamertags class — instance scope (equivalent to C# 'private' fields)
    class Gamertags:
        def __init__(self, filename=_____):      # use the global constant
            self.filename = _____
            self.gamer_tag_list = _____

        def load_gamertags(self):
            # local variable inside method
            loaded = _____
            with open(self._____, _____) as f:
                for line in f:
                    loaded.append(line._____(  ))
            self.gamer_tag_list = _____          # assign to instance scope

Questions:
- What is the LEGB lookup order? What does each letter stand for?
- Why is using `global` keyword inside a function generally a bad idea?
- In your Gamertags class, what scope holds `self.gamer_tag_list`? (Local,
  global, or instance/enclosing?)
- In C#, `private string[] gamerTagList` is instance scope. What is the Python
  equivalent? How do you write it?

Test challenge:
    Write a small program WITHOUT a class: create `DATA_FILE = "Gamertags.txt"`
    at the top. Write `load_gamertags(filename)` that takes the filename as an
    argument (NOT reading the global directly). Call it with `load_gamertags(DATA_FILE)`.
    Why is it better to pass the filename as an argument rather than reading
    `DATA_FILE` directly inside the function?
```

## Common Use Cases
- Defining `MAX_GAMERTAG_LENGTH`, `MIN_GAMERTAG_LENGTH`, and `DATA_FILE` as module-level constants
- Passing data as function arguments instead of using `global` for mutable state
- Understanding why a function can't accidentally change a variable in an outer scope
- Using closures (`nonlocal`) for stateful helper functions when classes are overkill

## Related Days
| Day | Topic |
|-----|-------|
| Day 4 | Functions (decomposition, inputs/outputs, naming) |
| Day 8 | Python Project Skeleton |
| Day 9 | Data Loading and Welcome Sequence |
| Day 10 | Display All Gamertags |

## See Also
- [17_python_functions.md](../04_functions/17_python_functions.md)
- [03_python_variables.md](../01_introduction/03_python_variables.md)
- [39_python_modules.md](39_python_modules.md)

## Challenges
- **Blank 1**: At the top of your file, define three module-level constants: `DATA_FILE = _____`, `MAX_TAG_LENGTH = _____`, `MIN_TAG_LENGTH = _____`. What values come from the gamertag project rules?
- **Blank 2**: Write `validate_gamertag(tag)` that reads `MAX_TAG_LENGTH` and `MIN_TAG_LENGTH` from global scope. Then rewrite it so the limits are passed as parameters instead. Which version is easier to test?
- **Blank 3**: In `Gamertags.__init__`, set `self.filename = filename` where `filename` has a default of `_____`. What is the C# equivalent file path? What should the default be in Python?
- **Challenge**: C# uses `private` to keep `gamerTagList` inside the class. Python uses naming convention: a leading underscore `_gamer_tag_list` signals "private". Try naming your list `self._gamer_tag_list`. Can you still access it from outside the class? What does `_` tell other programmers? Does Python actually enforce it?
