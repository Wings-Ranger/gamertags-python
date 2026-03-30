# Python Return Values

**W3Schools Link:** https://www.w3schools.com/python/python_functions.asp

**Homework Day(s):** Day 4

---

## Overview
The `return` statement sends a value back from a function to the caller. It immediately exits the function — any code after `return` in the same block is not executed. Functions without an explicit `return` (or with a bare `return`) implicitly return `None`. Well-designed return values are key to composable, testable functions.

## Key Concepts
- **`return value`**: exits the function and sends `value` back to the caller
- **`return` alone**: exits the function and returns `None`
- **No return statement**: function implicitly returns `None`
- **Multiple return values**: Python returns a tuple — `return a, b` is `return (a, b)`
- **Early return**: returning early on error conditions avoids deeply nested `if` blocks
- **Return type consistency**: avoid functions that sometimes return a value and sometimes `None`

## Syntax / Example Code
```python
# Basic return value
def get_rank(score):
    if score >= 5000:
        return "Diamond"
    elif score >= 3000:
        return "Gold"
    elif score >= 1000:
        return "Silver"
    else:
        return "Bronze"

rank = get_rank(4250)
print(rank)   # Gold

# Early return pattern — "guard clauses"
def validate_gamertag(tag):
    """Return (is_valid, message) for the given gamertag."""
    if not tag:
        return False, "Gamertag cannot be empty"
    if len(tag) < 3:
        return False, "Too short (minimum 3 characters)"
    if len(tag) > 15:
        return False, "Too long (maximum 15 characters)"
    if not tag.isalnum():
        return False, "Only letters and numbers allowed"
    return True, "Valid gamertag"

is_valid, message = validate_gamertag("ShadowHunter99")
print(is_valid, message)   # True Valid gamertag

is_valid, message = validate_gamertag("SH")
print(is_valid, message)   # False Too short (minimum 3 characters)

# Returning multiple values (returns a tuple)
def get_player_stats(players, gamertag):
    """Return (found, player_dict) for the given gamertag."""
    for player in players:
        if player["gamertag"].lower() == gamertag.lower():
            return True, player
    return False, None

players = [
    {"gamertag": "ShadowX", "platform": "Xbox", "score": 4250},
    {"gamertag": "NightOwl", "platform": "PS",   "score": 3300},
]
found, player = get_player_stats(players, "nightowl")
if found:
    print(player)

# Returning None (implicit)
def log_player(player):
    print(f"Logged: {player['gamertag']}")
    # no return — implicitly returns None

result = log_player(players[0])
print(result)    # None

# Returning computed data
def filter_by_platform(players, platform):
    """Return a new list of players on the given platform."""
    return [p for p in players if p["platform"] == platform]

xbox_players = filter_by_platform(players, "Xbox")
print(xbox_players)

# Return in a loop — exit on first match
def find_player(players, tag):
    for player in players:
        if player["gamertag"] == tag:
            return player   # exits function immediately
    return None             # not found
```

## Common Use Cases
- `validate_gamertag()` returning `(True/False, message)` for clean error handling
- `load_players()` returning the populated list to the caller
- `find_player()` returning the matching dict or `None`
- `filter_by_platform()` returning a new filtered list

## Related Days
| Day | Topic |
|-----|-------|
| Day 4 | Functions (decomposition, inputs/outputs, naming) |

## See Also
- [17_python_functions.md](17_python_functions.md)
- [18_python_function_arguments.md](18_python_function_arguments.md)
- [07_python_tuples.md](../02_data_types/07_python_tuples.md)
- [12_python_if_else.md](../03_control_flow/12_python_if_else.md)

## Practice Tips
- Use early `return` to eliminate deeply nested `if/else` blocks
- Return a tuple `(success, message)` from validation functions for clean error handling
- Always check for `None` when a function can return it as a "not found" signal
- Avoid mixing `return value` and bare `return` in the same function
