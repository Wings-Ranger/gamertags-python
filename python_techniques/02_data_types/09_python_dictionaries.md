# Python Dictionaries

**W3Schools Link:** https://www.w3schools.com/python/python_dictionaries.asp

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
```python
# Creating a player dictionary
player = {
    "gamertag": "ShadowHunter99",
    "platform": "Xbox",
    "score": 4250,
    "active": True
}

# Accessing values
print(player["gamertag"])          # ShadowHunter99
print(player.get("score"))         # 4250
print(player.get("rank", "N/A"))   # N/A (default if key missing)

# Modifying values
player["score"] = 5000
player["rank"] = "Gold"

# Removing entries
del player["active"]
removed = player.pop("rank", None)  # safe pop with default

# Iterating
for key in player:
    print(key, "->", player[key])

for key, value in player.items():
    print(f"  {key}: {value}")

print(list(player.keys()))    # ['gamertag', 'platform', 'score']
print(list(player.values()))  # ['ShadowHunter99', 'Xbox', 5000]

# List of player dicts — typical data structure for gamertag project
players = [
    {"gamertag": "ShadowHunter99", "platform": "Xbox",         "score": 4250},
    {"gamertag": "NightOwl",       "platform": "PlayStation",  "score": 3300},
    {"gamertag": "ProSniper",      "platform": "PC",           "score": 5100},
]

# Filter players by platform
xbox_players = [p for p in players if p["platform"] == "Xbox"]

# Sort by score descending
ranked = sorted(players, key=lambda p: p["score"], reverse=True)
for i, p in enumerate(ranked, 1):
    print(f"{i}. {p['gamertag']} - {p['score']}")

# Checking if a key exists
if "email" not in player:
    print("No email on record")

# Dict comprehension
score_map = {p["gamertag"]: p["score"] for p in players}
print(score_map)  # {'ShadowHunter99': 4250, 'NightOwl': 3300, ...}
```

## Common Use Cases
- Representing each gamertag entry as a dict with `gamertag`, `platform`, `score` fields
- Building a lookup table for fast gamertag-to-score mapping
- Parsing CSV rows into dictionaries with `csv.DictReader`
- Counting occurrences: `counts[platform] = counts.get(platform, 0) + 1`

## Related Days
| Day | Topic |
|-----|-------|
| Day 1 | Python Foundations (variables, data types, strings, lists) |
| Days 8-10 | Build project skeleton, data loading, display |

## See Also
- [06_python_lists.md](06_python_lists.md)
- [07_python_tuples.md](07_python_tuples.md)
- [14_python_for_loops.md](../03_control_flow/14_python_for_loops.md)
- [27_python_file_read.md](../06_file_io/27_python_file_read.md)

## Practice Tips
- Model each player record as a dict and store them in a list
- Practice `.get()` with a default to safely handle missing keys
- Build a dict comprehension that maps gamertag → score from your player list
- Use `sorted(..., key=lambda p: p["score"])` to rank players
