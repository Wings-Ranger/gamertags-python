# Python Tuples

**W3Schools Link:** https://www.w3schools.com/python/python_tuples.asp

**Homework Day(s):** Day 1

---

## Overview
Tuples are ordered, immutable sequences — like lists, but they cannot be changed after creation. They are defined with parentheses and are commonly used for fixed collections of related values, function return values, and as dictionary keys. Their immutability makes them reliable for data that should not change.

## Key Concepts
- **Immutable**: cannot add, remove, or change items after creation
- **Ordered**: items maintain their order and can be accessed by index
- **Defined with parentheses**: `(1, 2, 3)` — though parentheses are sometimes optional
- **Single-item tuple**: requires a trailing comma `(item,)` to avoid being just parentheses
- **Tuple unpacking**: `name, platform, score = ("GamerX", "Xbox", 4500)`
- **Faster than lists**: slightly better performance for fixed data
- **Hashable**: can be used as dictionary keys (unlike lists)

## Syntax / Example Code
```python
# Creating a tuple
player = ("ShadowHunter99", "Xbox", 4250)

# Accessing items
print(player[0])    # ShadowHunter99
print(player[-1])   # 4250

# Tuple unpacking
name, platform, score = player
print(f"{name} plays on {platform} with score {score}")

# Single-item tuple (trailing comma is required)
single = ("OnlyOne",)
print(type(single))   # <class 'tuple'>

# Tuples are immutable
# player[0] = "NewName"  # TypeError: 'tuple' object does not support item assignment

# Iterating a tuple
for value in player:
    print(value)

# Tuple as function return (common pattern)
def get_player_info():
    return "NightOwl", "PlayStation", 3300

tag, plat, pts = get_player_info()
print(f"{tag} on {plat}: {pts} pts")

# List of tuples — common way to store structured player data
players = [
    ("ShadowHunter99", "Xbox", 4250),
    ("NightOwl", "PlayStation", 3300),
    ("ProSniper", "PC", 5100),
]

for name, platform, score in players:
    print(f"{name} ({platform}): {score}")

# Using a tuple as a dictionary key
location_map = {
    ("North", "East"): "Forest Zone",
    ("South", "West"): "Desert Zone",
}

# Tuple methods
coords = (10, 20, 10, 30, 10)
print(coords.count(10))   # 3
print(coords.index(20))   # 1
```

## Common Use Cases
- Storing fixed player records as `(name, platform, score)` tuples
- Returning multiple values from a function
- Storing configuration constants that should not change
- Using as keys in dictionaries when you need a composite key

## Related Days
| Day | Topic |
|-----|-------|
| Day 1 | Python Foundations (variables, data types, strings, lists) |

## See Also
- [06_python_lists.md](06_python_lists.md)
- [08_python_sets.md](08_python_sets.md)
- [09_python_dictionaries.md](09_python_dictionaries.md)
- [19_python_return_values.md](../04_functions/19_python_return_values.md)

## Practice Tips
- Convert between lists and tuples with `list()` and `tuple()` and observe the difference
- Use tuple unpacking in a `for` loop over a list of player tuples
- Try using a tuple as a dictionary key to see why immutability matters
- Practice returning multiple values from a function and unpacking them
