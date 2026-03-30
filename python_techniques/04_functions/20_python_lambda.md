# Python Lambda Functions

**W3Schools Link:** https://www.w3schools.com/python/python_lambda.asp

---

## Overview
A lambda function is a small, anonymous function defined in a single expression using the `lambda` keyword. Lambdas are most useful when you need a short, one-off function as an argument to another function — particularly `sorted()`, `map()`, `filter()`, and `min()`/`max()`. They cannot contain statements, only expressions.

## Key Concepts
- **Syntax**: `lambda parameters: expression`
- **Anonymous**: has no name (unless assigned to a variable)
- **Single expression**: the expression's value is automatically returned
- **Cannot contain statements**: no `if/else` blocks (ternary is OK), no `for`, no assignments
- **Common use**: as the `key` argument in `sorted()`, `min()`, `max()`
- **Equivalent to a def**: `lambda x: x * 2` ≡ `def f(x): return x * 2`
- **Use sparingly**: for anything more complex, use a named `def` instead

## Syntax / Example Code
```python
# Basic lambda
double = lambda x: x * 2
print(double(5))   # 10

# Lambda with multiple parameters
add = lambda a, b: a + b
print(add(3, 4))   # 7

# Most common use: sorting with a key function
players = [
    {"gamertag": "ShadowX",   "score": 4250},
    {"gamertag": "NightOwl",  "score": 3300},
    {"gamertag": "ProSniper", "score": 5100},
    {"gamertag": "GamerZ",    "score": 900},
]

# Sort by score ascending
by_score = sorted(players, key=lambda p: p["score"])
for p in by_score:
    print(f"{p['gamertag']}: {p['score']}")

# Sort by score descending
by_score_desc = sorted(players, key=lambda p: p["score"], reverse=True)

# Sort alphabetically (case-insensitive)
by_name = sorted(players, key=lambda p: p["gamertag"].lower())

# min() and max() with lambda
top = max(players, key=lambda p: p["score"])
print(f"Top player: {top['gamertag']} with {top['score']}")

lowest = min(players, key=lambda p: p["score"])
print(f"Lowest scorer: {lowest['gamertag']}")

# filter() with lambda
high_scorers = list(filter(lambda p: p["score"] >= 3000, players))
print(f"High scorers: {[p['gamertag'] for p in high_scorers]}")

# map() with lambda
scores_only = list(map(lambda p: p["score"], players))
print(f"All scores: {scores_only}")

# Ternary in lambda (OK)
rank_label = lambda score: "Elite" if score >= 5000 else "Standard"
print(rank_label(5100))   # Elite
print(rank_label(3300))   # Standard

# When to use def instead of lambda
# Too complex for lambda — use def:
def sort_key(player):
    """Sort by platform first, then by score descending."""
    return (player.get("platform", ""), -player["score"])

sorted_players = sorted(players, key=sort_key)
```

## Common Use Cases
- `sorted(players, key=lambda p: p["score"])` — sorting player records
- `max(players, key=lambda p: p["score"])` — finding the top scorer
- `filter(lambda p: p["platform"] == "Xbox", players)` — filtering inline
- `sorted(tags, key=lambda t: t.lower())` — case-insensitive sort

## Related Days
| Day | Topic |
|-----|-------|
| Day 4 | Functions (decomposition, inputs/outputs, naming) |

## See Also
- [17_python_functions.md](17_python_functions.md)
- [14_python_for_loops.md](../03_control_flow/14_python_for_loops.md)
- [06_python_lists.md](../02_data_types/06_python_lists.md)

## Practice Tips
- Practice `sorted(players, key=lambda p: p["score"], reverse=True)` for a leaderboard
- Use `max()` and `min()` with a lambda key to find top/bottom scorers
- Replace complex lambdas with named `def` functions for readability
- Avoid assigning lambdas to variables — use `def` instead when naming is needed
