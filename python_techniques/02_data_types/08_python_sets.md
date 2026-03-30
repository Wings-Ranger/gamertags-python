# Python Sets

**W3Schools Link:** https://www.w3schools.com/python/python_sets.asp

---

## Overview
Sets are unordered collections of unique items. They are useful when you need to eliminate duplicates, check membership quickly, or perform mathematical set operations like union and intersection. Unlike lists, sets have no index and do not preserve insertion order.

## Key Concepts
- **Unique values**: automatically removes duplicates
- **Unordered**: items have no guaranteed order; cannot access by index
- **Mutable**: you can add and remove items
- **Frozen sets**: `frozenset()` creates an immutable version
- **Set operations**: union (`|`), intersection (`&`), difference (`-`), symmetric difference (`^`)
- **Fast membership testing**: `in` is O(1) for sets vs O(n) for lists
- **Cannot contain unhashable types**: lists and dicts cannot be set members

## Syntax / Example Code
```python
# Creating a set
platforms = {"Xbox", "PlayStation", "PC", "Nintendo Switch"}

# Duplicates are automatically removed
tags = {"GamerX", "NightOwl", "GamerX", "ProSniper"}
print(tags)   # {'GamerX', 'NightOwl', 'ProSniper'}  (only 3 items)

# Adding and removing
platforms.add("Mobile")
platforms.discard("Mobile")     # safe remove (no error if missing)
platforms.remove("Nintendo Switch")  # raises KeyError if missing

# Membership testing (very fast)
if "Xbox" in platforms:
    print("Xbox is supported")

# Deduplicating a list of gamertags
raw_tags = ["GamerX", "NightOwl", "GamerX", "ProSniper", "NightOwl"]
unique_tags = list(set(raw_tags))
print(f"Unique gamertags: {len(unique_tags)}")

# Set operations
xbox_players = {"ShadowX", "NightOwl", "ProSniper"}
ps_players = {"NightOwl", "IronFox", "GamerZ"}

both = xbox_players & ps_players     # intersection: play on both
either = xbox_players | ps_players   # union: play on either
xbox_only = xbox_players - ps_players  # difference

print(f"Multi-platform players: {both}")
print(f"All players: {either}")
print(f"Xbox exclusive: {xbox_only}")

# Iterating (order not guaranteed)
for platform in platforms:
    print(platform)

# Convert between set and list
tag_list = ["A", "B", "A", "C"]
tag_set = set(tag_list)   # deduplicate
tag_list = list(tag_set)  # back to list
```

## Common Use Cases
- Detecting and removing duplicate gamertags from a loaded list
- Checking if a gamertag is already registered (fast membership test)
- Finding players who are on multiple platforms (set intersection)
- Tracking valid platform names as a set for quick validation

## Related Days
| Day | Topic |
|-----|-------|
| Day 1 | Python Foundations (variables, data types, strings, lists) |

## See Also
- [06_python_lists.md](06_python_lists.md)
- [07_python_tuples.md](07_python_tuples.md)
- [09_python_dictionaries.md](09_python_dictionaries.md)

## Practice Tips
- Load a list with intentional duplicates and use `set()` to deduplicate it
- Compare speed: check membership in a list of 10,000 items vs a set
- Practice all four set operators (`|`, `&`, `-`, `^`) with player platform examples
- Use `frozenset` to create a constant set of valid platforms
