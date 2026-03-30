# Python Modules

**W3Schools Link:** https://www.w3schools.com/python/python_modules.asp

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
```python
# --- Standard library modules useful for the gamertag project ---

# os — file system operations
import os
if os.path.exists("gamertags.txt"):
    size = os.path.getsize("gamertags.txt")
    print(f"Data file: {size} bytes")

# os.path — path manipulation
data_file = os.path.join("data", "gamertags.txt")
base, ext = os.path.splitext("gamertags.txt")
print(base, ext)   # gamertags .txt

# csv — CSV reading and writing
import csv
with open("gamertags.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ShadowX", "Xbox", 4250])

# random — random selection (for testing)
import random
tags = ["ShadowX", "NightOwl", "ProSniper", "GamerZ"]
random.shuffle(tags)
print(tags)
winner = random.choice(tags)
print(f"Random winner: {winner}")

# datetime — timestamps
from datetime import datetime
now = datetime.now()
print(f"Generated at: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# sys — system information and argv
import sys
print(f"Python version: {sys.version}")
print(f"Script name: {sys.argv[0]}")

# string — useful constants
import string
print(string.ascii_letters)    # abcdefg...XYZ
print(string.digits)           # 0123456789
valid_chars = set(string.ascii_letters + string.digits)

# --- Creating your own module ---
# In file: gamertag_utils.py
"""
def validate_gamertag(tag):
    if not tag or not tag.isalnum():
        return False
    return 3 <= len(tag) <= 15

def format_player(player):
    return f"{player['gamertag']:<16} {player['platform']:<14} {player['score']:>6,}"

MAX_LENGTH = 15
MIN_LENGTH = 3
"""

# In your main file:
# import gamertag_utils
# valid = gamertag_utils.validate_gamertag("ShadowX")

# Or:
# from gamertag_utils import validate_gamertag, format_player
# valid = validate_gamertag("ShadowX")

# --- The __name__ guard ---
# In gamertag_utils.py:
"""
def validate_gamertag(tag):
    return bool(tag) and tag.isalnum() and 3 <= len(tag) <= 15

if __name__ == "__main__":
    # This code only runs when the file is executed directly, not when imported
    test_tags = ["ShadowX", "AB", "Shadow Hunter"]
    for tag in test_tags:
        print(f"{tag}: {validate_gamertag(tag)}")
"""

# --- Import aliases ---
import os.path as path
import datetime as dt

print(path.exists("gamertags.txt"))
today = dt.date.today()
print(today)
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
- [26_python_file_handling.md](26_python_file_handling.md)
- [27_python_file_read.md](27_python_file_read.md)
- [40_python_scope.md](40_python_scope.md)

## Practice Tips
- Organize your gamertag project: `main.py`, `utils.py` (validation), `data.py` (file I/O)
- Add `if __name__ == "__main__":` to every module so it can be both imported and run standalone
- Explore `dir(module)` to see all names in a module
- Use `import os.path as path` to save typing when using many `os.path` functions
