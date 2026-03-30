# Python Functions

**W3Schools Link:** https://www.w3schools.com/python/python_functions.asp

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
```python
# Basic function definition
def greet_player(name):
    """Display a welcome message for a player."""
    print(f"Welcome, {name}!")

greet_player("ShadowHunter99")  # Welcome, ShadowHunter99!

# Function with return value
def get_rank(score):
    """Return the rank label for a given score."""
    if score >= 5000:
        return "Diamond"
    elif score >= 3000:
        return "Gold"
    elif score >= 1000:
        return "Silver"
    else:
        return "Bronze"

rank = get_rank(4250)
print(f"Rank: {rank}")   # Rank: Gold

# Gamertag validation function (Day 6 core skill)
def is_valid_gamertag(tag):
    """Return True if the gamertag meets all requirements."""
    if not tag:
        return False
    if len(tag) < 3 or len(tag) > 15:
        return False
    if not tag.isalnum():
        return False
    return True

print(is_valid_gamertag("ShadowX"))      # True
print(is_valid_gamertag("AB"))           # False — too short
print(is_valid_gamertag("Shadow X 99")) # False — spaces

# Function to display a player record
def display_player(player):
    """Print a formatted player record."""
    print(f"  Gamertag : {player['gamertag']}")
    print(f"  Platform : {player['platform']}")
    print(f"  Score    : {player['score']}")
    print(f"  Rank     : {get_rank(player['score'])}")

player = {"gamertag": "NightOwl", "platform": "PlayStation", "score": 3300}
display_player(player)

# Function to load players from a file
def load_players(filename):
    """Load and return a list of player dicts from a CSV file."""
    players = []
    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) == 3:
                    players.append({
                        "gamertag": parts[0],
                        "platform": parts[1],
                        "score": int(parts[2])
                    })
    except FileNotFoundError:
        print(f"File not found: {filename}")
    return players

# Calling functions in sequence (pipeline pattern)
players = load_players("gamertags.csv")
for p in players:
    display_player(p)
```

## Common Use Cases
- `is_valid_gamertag(tag)` — validation function called before saving
- `load_players(filename)` — data loading abstracted into one place
- `display_player(player)` — display logic separated from data logic
- `get_rank(score)` — business logic encapsulated for reuse

## Related Days
| Day | Topic |
|-----|-------|
| Day 4 | Functions (decomposition, inputs/outputs, naming) |
| Days 8-10 | Build project skeleton, data loading, display |

## See Also
- [18_python_function_arguments.md](18_python_function_arguments.md)
- [19_python_return_values.md](19_python_return_values.md)
- [20_python_lambda.md](20_python_lambda.md)
- [40_python_scope.md](../09_advanced/40_python_scope.md)

## Practice Tips
- Start every project by sketching function names and what they do before writing code
- Write a docstring for every function you define
- Each function should fit on one screen and do one thing
- Test each function independently by calling it with different inputs
