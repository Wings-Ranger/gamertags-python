# Python Iterators

**W3Schools Link:** https://www.w3schools.com/python/python_iterators.asp

**Homework Day(s):** Day 3, Days 8–10

---

## Overview
An iterator is an object that implements the iterator protocol: `__iter__()` and `__next__()`. Python's `for` loop works by calling these methods automatically. You can create custom iterators to define how an object is traversed, and generators provide a simpler way to build iterators using the `yield` keyword.

## Key Concepts
- **Iterable**: any object you can loop over — lists, strings, files, ranges, dicts
- **Iterator**: an iterable that tracks its current position; has `__iter__` and `__next__`
- **`iter(obj)`**: converts an iterable to an iterator
- **`next(iterator)`**: returns the next item; raises `StopIteration` when exhausted
- **Generator**: a function that uses `yield` to produce items one at a time — the simplest way to create an iterator
- **Lazy evaluation**: generators produce items on demand, saving memory for large datasets
- **`yield` vs `return`**: `yield` pauses the function and resumes on the next `next()` call

## Syntax / Example Code
```python
# Every for loop uses the iterator protocol internally
gamertags = ["ShadowX", "NightOwl", "ProSniper"]

# Behind the scenes of: for tag in gamertags:
it = iter(gamertags)
print(next(it))   # ShadowX
print(next(it))   # NightOwl
print(next(it))   # ProSniper
# next(it)  # would raise StopIteration

# Custom iterator class
class PlayerIterator:
    """Iterates over a list of players, yielding only active ones."""

    def __init__(self, players):
        self.players = players
        self.index = 0

    def __iter__(self):
        return self   # iterator returns itself

    def __next__(self):
        while self.index < len(self.players):
            player = self.players[self.index]
            self.index += 1
            if player.get("active", True):
                return player
        raise StopIteration


players = [
    {"gamertag": "ShadowX",   "active": True},
    {"gamertag": "NightOwl",  "active": False},
    {"gamertag": "ProSniper", "active": True},
]

for player in PlayerIterator(players):
    print(player["gamertag"])   # ShadowX, ProSniper (NightOwl skipped)

# Generator function (simpler than a full iterator class)
def active_players(players):
    """Yield only active players."""
    for player in players:
        if player.get("active", True):
            yield player

for player in active_players(players):
    print(player["gamertag"])

# Generator for reading large files line by line (memory efficient)
def read_gamertag_lines(filename):
    """Yield one non-blank line at a time from a file."""
    try:
        with open(filename) as f:
            for line in f:
                line = line.strip()
                if line:
                    yield line
    except FileNotFoundError:
        return

for line in read_gamertag_lines("gamertags.txt"):
    print(line)

# Generator expression (like list comprehension but lazy)
scores = [4250, 3300, 5100, 900, 1500]
high_scores = (s for s in scores if s >= 3000)   # generator expression
for s in high_scores:
    print(s)   # 4250, 3300, 5100

# Using next() with a default (no StopIteration)
tags = iter(["ShadowX", "NightOwl"])
print(next(tags, "None"))   # ShadowX
print(next(tags, "None"))   # NightOwl
print(next(tags, "None"))   # None  (default, no exception)
```

## Common Use Cases
- Reading large gamertag files lazily with a generator (avoids loading all into memory)
- Building a custom `PlayerIterator` that filters as it iterates
- Using generator expressions for memory-efficient data transformations
- Implementing `__iter__` on a `GamertagManager` class so it's directly loopable

## Related Days
| Day | Topic |
|-----|-------|
| Day 3 | Loops and Program Flow (while loops, iterating lists) |
| Days 8-10 | Build project skeleton, data loading, display |

## See Also
- [14_python_for_loops.md](../03_control_flow/14_python_for_loops.md)
- [06_python_lists.md](../02_data_types/06_python_lists.md)
- [21_python_classes.md](21_python_classes.md)
- [27_python_file_read.md](../06_file_io/27_python_file_read.md)

## Practice Tips
- Use a generator function to read your gamertag file instead of reading all lines at once
- Implement `__iter__` on your `GamertagManager` so you can write `for p in manager:`
- Practice converting a list comprehension to a generator expression with `()` instead of `[]`
- Use `next(iter_obj, default)` to safely get the first item without a try/except
