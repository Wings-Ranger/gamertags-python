# Python Lists

**W3Schools Link:** https://www.w3schools.com/python/python_lists.asp

**Homework Day(s):** Day 1, Day 3, Days 8–10

---

## Overview
Lists are ordered, mutable collections that can hold items of any data type, including mixed types. They are one of Python's most versatile data structures and are essential for storing sequences of data like a collection of gamertags. Lists support indexing, slicing, and many built-in methods for adding, removing, and searching items.

## Key Concepts
- **Ordered**: items maintain their insertion order
- **Mutable**: you can add, remove, or change items after creation
- **Indexed**: access items with `list[0]` (zero-based); negative indices count from the end
- **Mixed types**: a list can hold strings, numbers, booleans, or even other lists
- **Common methods**: `.append()`, `.remove()`, `.pop()`, `.sort()`, `.reverse()`, `.index()`, `.count()`
- **len()**: returns the number of items in the list
- **in** operator: checks if an item exists in the list

## Syntax / Example Code
```python
# Creating a list of gamertags
gamertags = ["ShadowHunter99", "NightOwl", "ProSniper", "GamerZ"]

# Accessing items
print(gamertags[0])    # ShadowHunter99
print(gamertags[-1])   # GamerZ
print(len(gamertags))  # 4

# Slicing
print(gamertags[1:3])  # ['NightOwl', 'ProSniper']

# Adding items
gamertags.append("IronFox")          # add to end
gamertags.insert(1, "BlazeMaster")   # insert at index 1

# Removing items
gamertags.remove("GamerZ")           # remove by value
popped = gamertags.pop()             # remove and return last item
del gamertags[0]                     # remove by index

# Checking membership
if "NightOwl" in gamertags:
    print("NightOwl is registered")

# Iterating
for tag in gamertags:
    print(tag)

# Sorting
gamertags.sort()                     # alphabetical in-place
gamertags.sort(key=str.lower)        # case-insensitive sort
sorted_copy = sorted(gamertags)      # returns new list

# List comprehension
long_tags = [tag for tag in gamertags if len(tag) > 8]
upper_tags = [tag.upper() for tag in gamertags]

# Counting and searching
print(gamertags.count("NightOwl"))   # 1
print(gamertags.index("NightOwl"))   # index position

# Mixed list
player_record = ["ShadowHunter99", "Xbox", 4250, True]
```

## Common Use Cases
- Storing all gamertags loaded from a file
- Filtering gamertags by platform or score using list comprehension
- Adding new gamertags with `.append()` then saving back to file
- Sorting player lists alphabetically or by score
- Checking for duplicate gamertags with `in`

## Related Days
| Day | Topic |
|-----|-------|
| Day 1 | Python Foundations (variables, data types, strings, lists) |
| Day 3 | Loops and Program Flow (while loops, iterating lists) |
| Days 8-10 | Build project skeleton, data loading, display |

## See Also
- [07_python_tuples.md](07_python_tuples.md)
- [08_python_sets.md](08_python_sets.md)
- [09_python_dictionaries.md](09_python_dictionaries.md)
- [14_python_for_loops.md](../03_control_flow/14_python_for_loops.md)

## Practice Tips
- Load gamertags from a text file into a list and print each one
- Use list comprehension to filter only tags that are alphanumeric
- Practice `.sort()` vs `sorted()` — one modifies in place, one returns a new list
- Try building a list of dictionaries where each dict represents one player
