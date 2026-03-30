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

**C# reference (fixed data in the gamertag project):**
```csharp
// C# uses const or readonly for values that must not change.
// Python uses tuples for immutable sequences of related data.
// Example: a fixed player record or a constant list of menu options.
readonly string[] MENU_OPTIONS = { "1", "2", "3", "4", "5" };
```

**Python skeleton (fill in the blanks):**
```
# Creating a tuple — uses PARENTHESES, not square brackets
player = (_____, _____, _____)    # (gamertag, platform, score)

# Accessing items by index (same as lists)
print(player[_____])    # first item: gamertag
print(player[_____])    # last item: score (use negative index)

# Tuple UNPACKING — extract all values at once into named variables
name, platform, score = _____
print(f"{_____} plays on {_____} with score {_____}")

# Tuples are IMMUTABLE — this line would raise an error:
# player[0] = "NewName"   # ← what kind of error would this raise?

# Single-item tuple REQUIRES a trailing comma
single = (_____,)        # without the comma it's just parentheses, not a tuple
print(_____(single))     # should show <class 'tuple'>

# List of tuples — useful for storing multiple player records
players = [
    (_____, _____, _____),
    (_____, _____, _____),
]

# Tuple unpacking in a for loop
for _____, _____, _____ in players:
    print(f"{_____} ({_____}): {_____}")
```

**Questions:**
- What is the key difference between a `list` and a `tuple`? Which one can you modify after creation?
- What does "tuple unpacking" do? How does `name, platform, score = player` save you from using three separate index accesses?
- Why does a single-item tuple need a trailing comma: `("Xbox",)` instead of `("Xbox")`?
- When would you choose a tuple over a list to store a player record?

**Test challenge:**
Create a tuple `("ShadowHunter99", "Xbox", 4250)`. Unpack it into three variables and print each. Then try to change the first value with `player[0] = "NewName"` — what error does Python give you?

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

## Challenges

1. **Create and unpack:** Fill in the blanks to build a player tuple and unpack it:
   ```
   player = (_____, _____, _____)    # (gamertag, platform, score)
   name, platform, score = _____
   print(f"{_____} plays on {_____}")
   ```

2. **Immutability test:** Create `player = ("GamerX", "Xbox", 4250)`. Try `player[0] = "NewName"`. What error do you get? Why is immutability sometimes useful — what does it protect against?

3. **Single-item tuple:** What is the difference between `single = ("Xbox")` and `single = ("Xbox",)`? Check `type()` of each. Why does the comma matter?

4. **List of tuples:** Store 3 player records as a list of tuples. Use a `for` loop with tuple unpacking to print each one:
   ```
   players = [(_____, _____), (_____, _____), (_____, _____)]
   for _____, _____ in players:
       print(f"{_____}: {_____}")
   ```
