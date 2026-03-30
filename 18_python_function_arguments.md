# Python Function Arguments

**W3Schools Link:** https://www.w3schools.com/python/python_functions.asp

---

## Overview
Function arguments allow you to pass data into functions, making them flexible and reusable. Python supports positional arguments, keyword arguments, default parameter values, and variable-length argument lists (`*args`, `**kwargs`). Understanding how to design function signatures is key to writing clean, flexible code.

## Key Concepts
- **Positional arguments**: passed in order — `func(a, b, c)`
- **Keyword arguments**: passed by name — `func(name="GamerX", score=4250)`
- **Default parameter values**: used when an argument is not provided — `def func(platform="PC")`
- **`*args`**: collects extra positional arguments into a tuple
- **`**kwargs`**: collects extra keyword arguments into a dictionary
- **Argument order**: positional → `*args` → keyword with defaults → `**kwargs`
- **Immutable defaults**: avoid mutable defaults like `[]` or `{}` — use `None` instead

## Syntax / Example Code
```python
# Positional arguments
def display_player(gamertag, platform, score):
    print(f"{gamertag} | {platform} | {score}")

display_player("ShadowX", "Xbox", 4250)

# Keyword arguments — order doesn't matter
display_player(score=3300, gamertag="NightOwl", platform="PlayStation")

# Default parameter values
def create_player(gamertag, platform="PC", score=0, active=True):
    return {
        "gamertag": gamertag,
        "platform": platform,
        "score": score,
        "active": active
    }

p1 = create_player("ShadowX")                          # uses all defaults
p2 = create_player("NightOwl", "PlayStation", 3300)    # overrides platform and score
p3 = create_player("ProSniper", score=5100)            # keyword override, platform=default

print(p1)
print(p2)
print(p3)

# *args — variable number of positional arguments
def print_tags(*tags):
    """Print any number of gamertags."""
    for i, tag in enumerate(tags, 1):
        print(f"  {i}. {tag}")

print_tags("ShadowX", "NightOwl", "ProSniper", "GamerZ")

# **kwargs — variable number of keyword arguments
def create_player_record(gamertag, **details):
    """Create a player with any additional details."""
    record = {"gamertag": gamertag}
    record.update(details)
    return record

player = create_player_record("ShadowX", platform="Xbox", score=4250, rank="Gold")
print(player)

# Mixing argument types
def log_event(event, *tags, prefix="INFO", **extra):
    print(f"[{prefix}] {event}: {', '.join(tags)} | {extra}")

log_event("Login", "ShadowX", "NightOwl", prefix="AUTH", ip="192.168.1.1")

# AVOID mutable defaults — use None instead
def add_gamertag(tag, player_list=None):   # CORRECT
    if player_list is None:
        player_list = []
    player_list.append(tag)
    return player_list

# Unpacking a list/dict into arguments
args = ("ShadowX", "Xbox", 4250)
display_player(*args)   # unpacks tuple as positional args

kwargs = {"gamertag": "NightOwl", "platform": "PS", "score": 3300}
display_player(**kwargs)  # unpacks dict as keyword args
```

## Common Use Cases
- `create_player(tag, platform="PC")` — sensible defaults for optional fields
- `display_player(*player_tuple)` — unpacking stored tuples into function calls
- `filter_players(players, platform=None, min_score=0)` — optional filters
- `*args` for functions that accept variable numbers of gamertags

## Related Days
| Day | Topic |
|-----|-------|
| Day 4 | Functions (decomposition, inputs/outputs, naming) |

## See Also
- [17_python_functions.md](17_python_functions.md)
- [19_python_return_values.md](19_python_return_values.md)
- [07_python_tuples.md](07_python_tuples.md)
- [09_python_dictionaries.md](09_python_dictionaries.md)

## Practice Tips
- Redesign your `create_player()` to use default arguments for optional fields
- Practice calling functions with keyword arguments to improve readability
- Write a function using `*args` that accepts any number of gamertags to display
- Never use a mutable object (list, dict) as a default argument value
