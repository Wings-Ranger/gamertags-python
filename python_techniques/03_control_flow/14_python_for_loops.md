# Python For Loops

**W3Schools Link:** https://www.w3schools.com/python/python_for_loops.asp

---

## Overview
A `for` loop iterates over any iterable — a list, string, tuple, dictionary, range, or file — executing a block of code for each item. Unlike `while` loops, `for` loops are used when you know exactly what you are iterating over. They are the most common loop in Python and are essential for processing collections like gamertag lists.

## Key Concepts
- **Iterates over iterables**: lists, strings, tuples, dicts, sets, ranges, files
- **Loop variable**: holds the current item each iteration
- **`range()`**: generates a sequence of numbers — `range(n)`, `range(start, stop)`, `range(start, stop, step)`
- **`enumerate()`**: provides both index and value — `for i, item in enumerate(list)`
- **`zip()`**: pairs items from two iterables — `for a, b in zip(list1, list2)`
- **`break`**: exit the loop early
- **`continue`**: skip the current iteration
- **`else`**: optional block that runs if loop was not exited with `break`

## Syntax / Example Code
```python
# Iterating over a list of gamertags
gamertags = ["ShadowHunter99", "NightOwl", "ProSniper", "GamerZ"]

for tag in gamertags:
    print(tag)

# Using range()
for i in range(5):       # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):    # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2):  # 0, 2, 4, 6, 8
    print(i)

# enumerate() — index + value
for i, tag in enumerate(gamertags, 1):
    print(f"{i}. {tag}")

# Iterating over a string
for char in "GamerX":
    print(char)

# Iterating over a dictionary
player = {"gamertag": "ShadowX", "platform": "Xbox", "score": 4250}
for key, value in player.items():
    print(f"  {key}: {value}")

# zip() — pairing two lists
tags = ["ShadowX", "NightOwl"]
scores = [4250, 3300]
for tag, score in zip(tags, scores):
    print(f"{tag}: {score}")

# List comprehension (compact for loop)
valid_tags = [tag for tag in gamertags if len(tag) >= 3]
upper_tags = [tag.upper() for tag in gamertags]

# Nested for loop — compare all pairs
for i, tag1 in enumerate(gamertags):
    for j, tag2 in enumerate(gamertags):
        if i < j and tag1.lower() == tag2.lower():
            print(f"Duplicate: {tag1} and {tag2}")

# for with break — search
target = "NightOwl"
for tag in gamertags:
    if tag == target:
        print(f"Found: {tag}")
        break
else:
    print(f"{target} not found")

# Reading file lines (for loop over file)
with open("gamertags.txt") as f:
    for line in f:
        print(line.strip())
```

## Common Use Cases
- Displaying all gamertags with numbered index using `enumerate()`
- Filtering or transforming lists with list comprehensions
- Searching for a specific gamertag with `for/break/else`
- Processing each line of a file after loading it

## Related Days
| Day | Topic |
|-----|-------|
| Day 3 | Loops and Program Flow (while loops, iterating lists) |
| Days 10–12 | Data loading, display, filters and logic |

## See Also
- [13_python_while_loops.md](13_python_while_loops.md)
- [15_python_break_continue.md](15_python_break_continue.md)
- [06_python_lists.md](../02_data_types/06_python_lists.md)
- [25_python_iterators.md](../05_oop/25_python_iterators.md)

## Practice Tips
- Always use `enumerate()` instead of managing a manual index counter
- Practice writing list comprehensions to replace simple `for` + `append` patterns
- Use `for/else` when searching a list — the `else` runs only if `break` was never hit
- Read a gamertag file line by line using `for line in file:` pattern
