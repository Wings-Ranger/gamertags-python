# Python For Loops

**W3Schools Link:** https://www.w3schools.com/python/python_for_loops.asp

**Homework Day(s):** Day 3, Day 10, Day 11, Day 12

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

**C# pattern (from the gamertag project):**
```csharp
// C# PrintAllGamertags uses foreach
public void PrintAllGamertags()
{
    foreach (string s in gamerTagList)
        Console.WriteLine(s);
}
```

**Python skeleton (fill in the blanks):**
```
# Replicating C#'s PrintAllGamertags with a Python for loop
def print_all_gamertags(gamer_tag_list):
    for _____ in _____:
        print(_____)

# Numbered output using enumerate() — no manual counter needed
def print_all_gamertags_numbered(gamer_tag_list):
    for _____, _____ in _____(gamer_tag_list, 1):
        print(f"{_____}. {_____}")

# range() — iterate a fixed number of times
for i in _____(5):         # 0 through 4
    print(i)

for i in _____(1, 6):      # 1 through 5
    print(i)

# Iterating over a string character by character
tag = "GamerX"
for _____ in _____:
    print(_____)            # prints each character on its own line

# List comprehension — compact filter to replace PrintGamertagsEndingWithNumber
gamer_tag_list = ["ShadowX", "NightOwl", "99Stars", "ProSniper9"]
ending_with_digit = [s for s in _____ if s[_____]._____(  )]
print(ending_with_digit)
```

**Questions:**
- C# uses `foreach (string s in gamerTagList)`. What is the Python equivalent syntax?
- Python's `enumerate()` gives you both index and value. Why is this better than a manual counter variable like `i = 0; i += 1`?
- What does `range(1, 6)` produce? What about `range(0, 10, 2)`?
- A list comprehension `[s for s in tags if condition]` replaces what common for-loop-plus-append pattern?

**Test challenge:**
Write `print_all_gamertags` as a Python function. Call it with a list of 5 gamertags. Then write a second version using `enumerate()` that prints `"1. ShadowX"`, `"2. NightOwl"`, etc.

## Common Use Cases
- Displaying all gamertags with numbered index using `enumerate()`
- Filtering or transforming lists with list comprehensions
- Searching for a specific gamertag with `for/break/else`
- Processing each line of a file after loading it

## Related Days
| Day | Topic |
|-----|-------|
| Day 3 | Loops and Program Flow (while loops, iterating lists) |
| Day 10 | Display All Gamertags |
| Day 11 | Filter 1 (Ending with Number) |
| Day 12 | Filter 2 (Not Starting with Letter or Number) |

## See Also
- [13_python_while_loops.md](13_python_while_loops.md)
- [15_python_break_continue.md](15_python_break_continue.md)
- [06_python_lists.md](../02_data_types/06_python_lists.md)
- [25_python_iterators.md](../05_oop/25_python_iterators.md)

## Challenges

1. **Translate foreach:** C# `PrintAllGamertags` uses `foreach`. Write the Python function:
   ```
   def print_all_gamertags(gamer_tag_list):
       for _____ in _____:
           print(_____)
   ```

2. **Numbered list with enumerate():** Print gamertags with numbers (1, 2, 3...) without a manual counter:
   ```
   for _____, _____ in _____(gamer_tag_list, _____):
       print(f"{_____}. {_____}")
   ```
   What is the second argument to `enumerate()` used for?

3. **Filter with comprehension:** Replicate `PrintGamertagsEndingWithNumber` as a list comprehension, then iterate the result:
   ```
   ending_in_digit = [s for s in gamer_tag_list if s[_____]._____(  )]
   for tag in _____:
       print(tag)
   ```

4. **Iterate a string:** Write a `for` loop that prints each character of `"GamerX"` on its own line. Then count how many characters are digits using a counter variable inside the loop.
