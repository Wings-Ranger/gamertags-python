# Python Lambda Functions

**W3Schools Links:**
- [Python Lambda Functions](https://www.w3schools.com/python/python_lambda.asp) — `lambda` syntax, use as `key=` argument
- [Python Built-in Functions](https://www.w3schools.com/python/python_ref_functions.asp) — `sorted()`, `max()`, `min()`, `filter()`, `list()` all used in exercises
- [Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp) — lambdas operate on lists of dicts (e.g., `lambda p: p["score"]`)
- [Python Lists](https://www.w3schools.com/python/python_lists.asp) — `sorted()` and `list(filter(...))` return lists

**Homework Day(s):** Day 4

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

**C# reference (gamertag project context):**
```csharp
// C# doesn't use lambdas in this project, but LINQ uses them for sorting/filtering:
// gamerTagList.OrderBy(tag => tag).ToList();
// gamerTagList.Where(tag => char.IsDigit(tag[tag.Length - 1])).ToList();
// Python uses lambda in sorted(), filter(), max(), min() the same way.
```

**Python skeleton (fill in the blanks):**
```
players = [
    {"gamertag": "ShadowX",   "score": 4250},
    {"gamertag": "NightOwl",  "score": 3300},
    {"gamertag": "ProSniper", "score": 5100},
    {"gamertag": "GamerZ",    "score": 900},
]

# Lambda syntax: lambda parameters: expression
# Sort by score ascending (lowest first)
by_score = _____(players, key=_____ p: p[_____])

# Sort by score descending (highest first — leaderboard)
by_score_desc = _____(players, key=_____ p: p[_____], reverse=_____)

# Sort alphabetically, case-insensitive
by_name = _____(players, key=_____ p: p[_____]._____(  ))

# Find highest and lowest scorer
top    = _____(players, key=_____ p: p[_____])
lowest = _____(players, key=_____ p: p[_____])
print(f"Top scorer: {top[_____]}")

# filter() with lambda — similar to PrintGamertagsEndingWithNumber idea
tags = ["ShadowX", "NightOwl", "ProSniper99", "GamerZ7"]
ending_digit = list(_____(_____ t: t[_____]._____(  ), tags))
print(ending_digit)

# When NOT to use lambda — use def instead for complex logic
def _____(player):
    """Sort key: sort by platform first, then score descending."""
    _____ (player._____(_____, ""), -player[_____])

sorted_players = sorted(players, key=_____)
```

**Questions:**
- What does `lambda p: p["score"]` mean? Break it down: what is `p` and what does the expression return?
- `sorted()` takes a `key=` argument. Why is a lambda useful here instead of defining a full named `def` function?
- What is the difference between `sorted(players, key=...)` and `players.sort(key=...)`? Which returns a new list?
- When should you replace a lambda with a named `def` function?

**Test challenge:**
Sort the player list by `"score"` descending using `sorted()` with a lambda key. Print the result as a numbered leaderboard. Then find the top scorer using `max()` with the same lambda pattern.

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

## Challenges

1. **Sort by score:** Fill in the lambda to create a leaderboard sorted by score (highest first):
   ```
   players = [
       {"gamertag": "ShadowX",  "score": 4250},
       {"gamertag": "NightOwl", "score": 3300},
       {"gamertag": "GamerZ",   "score": 900},
   ]
   leaderboard = _____(players, key=_____ p: p[_____], reverse=_____)
   for i, p in _____(leaderboard, 1):
       print(f"{_____}. {p['gamertag']}: {p['score']}")
   ```

2. **Find top and bottom:** Use `max()` and `min()` with a lambda to find the highest and lowest scorers:
   ```
   top    = _____(players, key=_____ p: p["score"])
   lowest = _____(players, key=_____ p: p["score"])
   print(f"Top: {top[_____]}, Lowest: {lowest[_____]}")
   ```

3. **Case-insensitive sort:** Sort gamertag names alphabetically ignoring case:
   ```
   tags = ["shadowX", "NightOwl", "PRSNIPER", "gamerZ"]
   sorted_tags = _____(tags, key=_____ t: t._____(  ))
   ```

4. **Lambda limit:** A lambda can only contain a single expression. Try writing a sort key that sorts players by platform first, then score descending. Why can't this be a lambda? Write it as a `def` instead:
   ```
   def sort_key(_____):
       _____ (_____[_____], -_____[_____])

   sorted_players = sorted(players, key=_____)
   ```
