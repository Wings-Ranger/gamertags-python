# Python Try / Except

**W3Schools Link:** https://www.w3schools.com/python/python_try_except.asp

---

## Overview
Exception handling with `try/except` allows your program to gracefully respond to errors rather than crashing. Python uses structured exception handling with four clauses: `try` (the risky code), `except` (handles specific errors), `else` (runs if no exception), and `finally` (always runs — used for cleanup). Proper exception handling makes programs robust and user-friendly.

## Key Concepts
- **`try`**: the block where exceptions might occur
- **`except ExceptionType`**: catches a specific type of exception
- **`except (A, B)`**: catches multiple exception types
- **`except Exception as e`**: catches the exception and binds it to variable `e`
- **`else`**: runs only if the `try` block succeeded (no exception raised)
- **`finally`**: always runs — use for cleanup (closing files, releasing resources)
- **Bare `except:`**: catches everything including `KeyboardInterrupt` — avoid
- **Specificity**: catch the most specific exception type possible

## Syntax / Example Code
```python
# Basic try/except
try:
    score = int("abc")
except ValueError:
    print("Error: not a valid integer")

# Catching multiple exceptions
try:
    with open("gamertags.txt") as f:
        line = f.readline()
        score = int(line.split(",")[2])
except FileNotFoundError:
    print("Error: gamertags.txt not found")
except IndexError:
    print("Error: malformed line — missing score field")
except ValueError:
    print("Error: score field is not a valid integer")

# Using 'as e' to get the error message
try:
    value = int("xyz")
except ValueError as e:
    print(f"Conversion failed: {e}")

# try / except / else / finally
def load_players(filename):
    """Load players from file with full exception handling."""
    players = []
    f = None
    try:
        f = open(filename, "r", encoding="utf-8")
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            player = {
                "gamertag": parts[0],
                "platform": parts[1],
                "score": int(parts[2])
            }
            players.append(player)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except (IndexError, ValueError) as e:
        print(f"Data error in file: {e}")
    else:
        print(f"Successfully loaded {len(players)} players")
    finally:
        if f:
            f.close()
    return players

# Safe integer conversion utility
def safe_int(value, default=0):
    """Convert value to int, returning default on failure."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return default

print(safe_int("4250"))     # 4250
print(safe_int("4250.5"))   # 0  (int() won't parse floats from strings)
print(safe_int(None))       # 0
print(safe_int("abc"))      # 0

# Nested try/except (avoid deeply nesting — use functions instead)
def get_player_score(players, gamertag):
    try:
        for player in players:
            if player["gamertag"] == gamertag:
                return player["score"]
        return None
    except (KeyError, TypeError) as e:
        print(f"Unexpected data format: {e}")
        return None

# Context manager (with) handles its own cleanup — preferred over finally for files
def load_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        print(f"'{filename}' does not exist yet.")
        return []
    except PermissionError:
        print(f"Cannot read '{filename}' — permission denied.")
        return []
```

## Common Use Cases
- Wrapping `open()` calls in `try/except FileNotFoundError` for graceful startup
- Wrapping `int()` conversion of file data in `try/except ValueError`
- Using `finally` to ensure files are closed in older code (prefer `with` instead)
- Building a `safe_int()` utility used throughout the project

## Related Days
| Day | Topic |
|-----|-------|
| Day 5 | File Handling (reading, appending, file paths) |
| Day 14 | Final test and submission prep |

## See Also
- [37_python_exceptions.md](37_python_exceptions.md)
- [38_python_raising_exceptions.md](38_python_raising_exceptions.md)
- [26_python_file_handling.md](26_python_file_handling.md)
- [11_python_type_casting.md](11_python_type_casting.md)

## Practice Tips
- Always catch the most specific exception type — avoid bare `except:`
- Write a `safe_int()` helper once and reuse it everywhere you convert strings to ints
- Use `with open(...)` instead of `try/finally` for file handling — it's cleaner
- Test your exception handlers by intentionally providing bad data (wrong filename, non-numeric score)
