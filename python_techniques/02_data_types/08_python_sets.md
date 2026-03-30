# Python Sets

**W3Schools Link:** https://www.w3schools.com/python/python_sets.asp

**Homework Day(s):** Day 1

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

**C# reference (gamertag project context):**
```csharp
// C# has HashSet<string> for unique collections.
// In the gamertag project, a set is useful for detecting duplicates
// or fast membership checks before adding a new tag.
// HashSet<string> seen = new HashSet<string>();
// if (seen.Contains(gamerTag)) { /* duplicate! */ }
```

**Python skeleton (fill in the blanks):**
```
# Creating a set — curly braces, but NO key:value pairs (that's a dict)
platforms = {_____, _____, _____}

# Duplicates are AUTOMATICALLY removed when converting a list to a set
raw_tags  = ["GamerX", "NightOwl", "GamerX", "ProSniper", "NightOwl"]
unique    = _____(raw_tags)          # convert list → set, duplicates gone
print(_____(unique))                 # how many unique tags remain?

# Check if a tag is already registered (very fast)
if _____ in unique:
    print("Already registered!")

# Adding and removing safely
unique._____(_____)                  # add a new tag
unique._____(_____)                  # safe remove — no error if missing

# Convert back to a sorted list
tag_list = _____(_____(unique))      # sorted list built from the set

# Set operations — finding overlap between platform groups
xbox_players = {_____, _____, _____}
ps_players   = {_____, _____, _____}

both_platforms = xbox_players _____ ps_players    # intersection: on BOTH
all_players    = xbox_players _____ ps_players    # union: on EITHER
xbox_only      = xbox_players _____ ps_players    # difference: Xbox not PS
```

**Questions:**
- What makes a set different from a list? (Think about: order, duplicate values, index access)
- If you load gamertags from a file and some are duplicated, how does wrapping the list in `set()` solve the problem?
- Which operator (`&`, `|`, `-`) finds the players that appear on BOTH platforms?
- Can you access a set item by index like `my_set[0]`? Why or why not?

**Test challenge:**
Create a list `["GamerX", "NightOwl", "GamerX", "ProSniper", "NightOwl"]` with intentional duplicates. Convert it to a set, then back to a sorted list. How many items does the final list have?

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

## Challenges

1. **Deduplication:** Load a list with duplicates and remove them using a set:
   ```
   raw_tags = ["GamerX", "NightOwl", "GamerX", "ProSniper", "NightOwl"]
   unique   = _____(raw_tags)
   print(f"Started with {_____(raw_tags)}, ended with {_____(unique)}")
   ```

2. **Membership check:** Use a set of registered tags to quickly test if a new tag is taken:
   ```
   registered = {"GamerX", "NightOwl", "ProSniper"}
   new_tag    = "NightOwl"
   if new_tag _____ registered:
       print("_____")
   else:
       print("_____")
   ```

3. **Set operations:** Given `xbox_players = {"ShadowX", "NightOwl"}` and `ps_players = {"NightOwl", "GamerZ"}`, find players on BOTH platforms. Fill in the operator:
   ```
   multi_platform = xbox_players _____ ps_players
   ```
   What symbol did you use? What does `|` do instead?

4. **Why not a list?** For checking membership, a set is faster than a list for large data. Explain in your own words why — what does a set do internally that a list does not?
