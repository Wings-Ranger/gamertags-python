# Python Modules

**W3Schools Link:** https://www.w3schools.com/python/python_modules.asp

**Homework Day(s):** Days 8–10

---

## Overview
A module is a Python file containing functions, classes, and variables that can be imported and reused in other programs. Python ships with a rich standard library of modules (like `os`, `csv`, `datetime`, `random`), and you can create your own. Modules are the primary unit of code organization in Python.

## Key Concepts
- **`import module`**: imports the whole module; access with `module.function()`
- **`from module import name`**: imports a specific name directly into scope
- **`from module import *`**: imports all public names — generally avoid
- **`import module as alias`**: imports with a shorter alias
- **Standard library**: built-in modules available without installation
- **`__name__`**: equals `"__main__"` when a file is run directly; module name when imported
- **`if __name__ == "__main__":`**: guards code that should only run when executed directly
- **Creating modules**: any `.py` file is a module; import it by filename (without `.py`)

## Syntax / Example Code

```
C# pattern (from the gamertag project):
    // C# imports are at the top using 'using'
    using System;
    using System.IO;

    // Using the imported namespace
    string[] lines = File.ReadAllLines("../Gamertags.txt");

Python skeleton — import and use modules (fill in the blanks):

    # Import the whole module (like 'using System.IO')
    _____ os

    # Use it with the module name as prefix
    if os.path._____(  "Gamertags.txt"):      # what checks if a file exists?
        print("File found")

    # Import a specific name from a module (more targeted)
    from os.path _____ exists, join

    if _____(  "Gamertags.txt"):              # call directly, no prefix needed
        path = _____("data", "Gamertags.txt") # os.path.join equivalent

    # Import with an alias (shorter name)
    _____ os.path _____ path                  # keyword? alias?
    if path.exists("Gamertags.txt"):
        print("Found")

    # Standard library modules useful for the gamertag project:
    _____ os          # file system: os.path.exists(), os.remove()
    _____ csv         # CSV reading/writing
    from datetime _____ datetime   # timestamps

    # Using csv module (robust alternative to manual split)
    with open("Gamertags.txt", "r") as f:
        reader = csv._____(f)            # what creates a CSV reader?
        for row in reader:
            print(row[0], row[1])

    # Creating your own module (split your project across files)
    # In gamertag_utils.py:
    #   def validate_gamertag(tag): ...
    #   def load_gamertags(filename): ...

    # In main.py:
    _____ gamertag_utils                      # import your own module
    valid = gamertag_utils.validate_gamertag("ShadowX")

    # The __name__ guard — runs only when file is executed directly
    if _____ == "_____":
        print("Running directly")            # fill both blanks

Questions:
- What Python keyword imports a module? (C# uses `using`)
- What is the difference between `import os` and `from os import path`?
- What does `if __name__ == "__main__":` protect against?
- Why might you split your gamertag project into multiple `.py` files?

Test challenge:
    Split your gamertag project into two files: `gamertags.py` (the class) and
    `main.py` (the main loop). In `main.py`, write `import gamertags` and create
    a `gamertags.Gamertags()` instance. Add `if __name__ == "__main__":` to
    `gamertags.py`. Does the class file run its own code when imported? Should it?
```

## Common Use Cases
- `import os` — check file existence, build paths with `os.path.join()`
- `import csv` — robust CSV reading/writing for the gamertag data file
- `from datetime import datetime` — timestamping records
- Splitting your project into `gamertag_utils.py`, `file_handler.py`, `main.py`

## Related Days
| Day | Topic |
|-----|-------|
| Days 8-10 | Build project skeleton, data loading, display |

## See Also
- [26_python_file_handling.md](../06_file_io/26_python_file_handling.md)
- [27_python_file_read.md](../06_file_io/27_python_file_read.md)
- [40_python_scope.md](40_python_scope.md)

## Challenges
- **Blank 1**: Write the import line for `os` and use `os.path.exists("Gamertags.txt")`. Then rewrite using `from os.path import _____` — which is more readable?
- **Blank 2**: Write `from datetime import _____` then use it: `now = _____.now()`. What class name are you importing?
- **Blank 3**: Add `if _____ == "_____":` at the bottom of your `gamertags.py` file and put a quick test inside. What are the two blanks? What happens when another file imports `gamertags.py` — does the test code run?
- **Challenge**: C# uses `using System.IO` to access `File.ReadAllLines`. Python uses `import os` for file utilities. Both organize code into namespaces/modules. Create a file `utils.py` with a `validate_gamertag(tag)` function, then import it in your main file using two different styles: `import utils` and `from utils import validate_gamertag`. How does the call syntax differ between the two?
