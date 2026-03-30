# Python Dictionaries

**W3Schools Link:** https://www.w3schools.com/python/python_dictionaries.asp

**Homework Day(s):** Day 1, Day 8, Day 9, Day 10

---

## Overview
Dictionaries are unordered (insertion-ordered since Python 3.7) collections of key-value pairs. They provide fast lookups by key and are ideal for representing structured data like player records. Each key must be unique and immutable (strings, numbers, tuples), while values can be any type.

## Key Concepts
- **Key-value pairs**: `{"name": "GamerX", "platform": "Xbox"}`
- **Keys are unique**: assigning to an existing key overwrites its value
- **Keys must be immutable**: strings and numbers are common keys
- **Fast lookups**: access a value by key in O(1) time
- **Common methods**: `.get()`, `.keys()`, `.values()`, `.items()`, `.update()`, `.pop()`
- **Nested dicts**: a value can itself be a dictionary (nested records)
- **Dict comprehensions**: `{k: v for k, v in pairs}`

## Syntax / Example Code

**C# reference (gamertag project context):**
```csharp
// The C# project stores each gamertag as a plain string.
// A Python dict lets you attach structured data to each gamertag —
// like upgrading from string[] to Dictionary<string, object>:
// player["gamertag"] = "ShadowHunter99";
// player["platform"] = "Xbox";
// player["score"]    = 4250;
```

**Python skeleton (fill in the blanks):**
```
# Creating a player dictionary
player = {
    _____: "ShadowHunter99",
    _____: "Xbox",
    _____: 4250,
    _____: True
}

# Accessing values by key
print(player[_____])                    # gamertag
print(player._____(_____, "Unranked"))  # safe access — returns default if key missing

# Modifying and adding fields
player[_____] = 5000         # update score
player[_____] = "Gold"       # add a new rank field

# Iterating over all key-value pairs
for _____, _____ in player._____(  ):
    print(f"{_____}: {_____}")

# List of player dicts (the main data structure you will build)
players = [
    {_____: "ShadowHunter99", _____: "Xbox",        _____: 4250},
    {_____: "NightOwl",       _____: "PlayStation",  _____: 3300},
]

# Filter to only Xbox players
xbox_players = [p for p in players if p[_____] == _____]
```

**Questions:**
- How do you access a value in a Python dict? What is the difference between `player["key"]` and `player.get("key", default)`?
- What happens if you try `player["rank"]` when `"rank"` is not a key? How does `.get()` handle this more safely?
- The C# project stores gamertags as a plain `string[]`. What advantage does a list of dicts give you over that approach?
- How do you loop over all key-value pairs in a dictionary?

**Test challenge:**
Create a player dictionary with `"gamertag"`, `"platform"`, and `"score"`. Print each field using `.get()` with a default value. Add a `"rank"` field. Update the score. Print the whole dict to confirm all changes.

## Common Use Cases
- Representing each gamertag entry as a dict with `gamertag`, `platform`, `score` fields
- Building a lookup table for fast gamertag-to-score mapping
- Parsing CSV rows into dictionaries with `csv.DictReader`
- Counting occurrences: `counts[platform] = counts.get(platform, 0) + 1`

## Related Days
| Day | Topic |
|-----|-------|
| Day 1 | Python Foundations (variables, data types, strings, lists) |
| Day 8 | Python Project Skeleton |
| Day 9 | Data Loading and Welcome Sequence |
| Day 10 | Display All Gamertags |

## See Also
- [06_python_lists.md](06_python_lists.md)
- [07_python_tuples.md](07_python_tuples.md)
- [14_python_for_loops.md](../03_control_flow/14_python_for_loops.md)
- [27_python_file_read.md](../06_file_io/27_python_file_read.md)

## Challenges

1. **Create a player record:** Fill in the blanks to build a dict for one player:
   ```
   player = {
       _____: "ShadowHunter99",
       _____: "Xbox",
       _____: 4250
   }
   print(player[_____])    # print the gamertag
   ```

2. **Safe access with .get():** What is the difference between these two lines?
   ```
   print(player["rank"])                     # ← what happens if "rank" doesn't exist?
   print(player._____(_____, "Unranked"))    # ← how is this safer?
   ```

3. **Iterate a dict:** Fill in the loop to print every field of a player record:
   ```
   for _____, _____ in player._____(  ):
       print(f"{_____}: {_____}")
   ```

4. **Filter a list of dicts:** Given a list of player dicts, filter to only Xbox players using a list comprehension:
   ```
   players = [
       {"gamertag": "ShadowX",  "platform": "Xbox", "score": 4250},
       {"gamertag": "NightOwl", "platform": "PS",   "score": 3300},
   ]
   xbox = [p for p in players if p[_____] == _____]
   ```
