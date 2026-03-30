# Python Scope

**W3Schools Link:** https://www.w3schools.com/python/python_scope.asp

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
```python
# --- Local scope ---
def validate_gamertag(tag):
    MIN = 3      # local to this function
    MAX = 15     # local to this function
    return bool(tag) and tag.isalnum() and MIN <= len(tag) <= MAX

# MIN and MAX are not accessible here
# print(MIN)   # NameError: name 'MIN' is not defined

# --- Global scope ---
MAX_GAMERTAG_LENGTH = 15   # module-level constant (GLOBAL, read-only)
MIN_GAMERTAG_LENGTH = 3
VALID_PLATFORMS = {"Xbox", "PlayStation", "PC", "Nintendo Switch"}

def is_valid_length(tag):
    # Reads globals — OK for constants
    return MIN_GAMERTAG_LENGTH <= len(tag) <= MAX_GAMERTAG_LENGTH

# --- global keyword (generally avoid) ---
player_count = 0   # global

def increment_count():
    global player_count    # declare intent to modify global
    player_count += 1

increment_count()
increment_count()
print(player_count)   # 2

# BETTER: use a return value instead of global mutation
def load_players(filename):
    players = []   # local — returned to caller
    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(",")
                    if len(parts) == 3:
                        players.append({"gamertag": parts[0],
                                        "platform": parts[1],
                                        "score": int(parts[2])})
    except FileNotFoundError:
        pass
    return players   # caller owns the result

# --- LEGB resolution order example ---
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(x)   # local

    inner()
    print(x)   # enclosing

outer()
print(x)   # global

# --- nonlocal (closures) ---
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter = make_counter()
print(counter())   # 1
print(counter())   # 2
print(counter())   # 3

# --- Scope in the gamertag project ---

# Module-level constants (good use of global scope)
DATA_FILE = "gamertags.txt"
MAX_GAMERTAG_LENGTH = 15
MIN_GAMERTAG_LENGTH = 3

def add_player(players, gamertag, platform, score):
    """
    All data is passed in as arguments and modified list returned.
    No global mutation — clean, testable function.
    """
    players.append({
        "gamertag": gamertag,
        "platform": platform,
        "score": score
    })
    return players

def save_players(filename, players):
    """Saves players to file. Takes filename as argument (not global)."""
    with open(filename, "w") as f:
        for p in players:
            f.write(f"{p['gamertag']},{p['platform']},{p['score']}\n")

# Main program
players = load_players(DATA_FILE)   # local in main, passed to functions
players = add_player(players, "ShadowX", "Xbox", 4250)
save_players(DATA_FILE, players)
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
| Days 8-10 | Build project skeleton, data loading, display |

## See Also
- [17_python_functions.md](17_python_functions.md)
- [03_python_variables.md](03_python_variables.md)
- [39_python_modules.md](39_python_modules.md)

## Practice Tips
- Define all configuration constants at the top of your file in ALL_CAPS
- Avoid `global` — if a function needs data, pass it as an argument
- Test each function in isolation; if it relies on globals, it's harder to test
- Use `nonlocal` only in closures — don't use it as a workaround for poor design
