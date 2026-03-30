# Python Lists

**W3Schools Links:**
- [Python Lists](https://www.w3schools.com/python/python_lists.asp) — ordered mutable collections, `.append()`, `.sort()`, `in` operator
- [Python For Loops](https://www.w3schools.com/python/python_for_loops.asp) — `for item in list` (replaces C# `foreach`)
- [Python User Input](https://www.w3schools.com/python/python_user_input.asp) — `input().strip()` used in challenge 3
- [Python Built-in Functions](https://www.w3schools.com/python/python_ref_functions.asp) — `len()`, `enumerate()` used with lists

**Homework Day(s):** Day 1, Day 3, Day 8, Day 9, Day 10

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

**C# pattern (from the gamertag project):**
```csharp
// C# LoadGamertags() reads the file into a string array
string[] gamerTagList = File.ReadAllLines("../Gamertags.txt");

// Iterate and print each one
foreach (string s in gamerTagList)
    Console.WriteLine(s);
```

**Python skeleton (fill in the blanks):**
```
# Creating a list (Python's equivalent of C#'s string array)
gamer_tag_list = [_____, _____, _____, _____]

# Accessing items (zero-based index, same as C#)
print(gamer_tag_list[_____])    # first item
print(gamer_tag_list[_____])    # last item (use negative index)
print(_____(gamer_tag_list))    # total count

# Iterating (replaces C#'s foreach)
for _____ in gamer_tag_list:
    print(_____)

# Adding a new gamertag (eventually replaces File.AppendAllText logic)
new_tag = _____
gamer_tag_list._____(new_tag)   # add to end of list

# Checking if a tag already exists
if _____ in gamer_tag_list:
    print("Already registered!")

# Sorting alphabetically
gamer_tag_list._____(  )        # sorts the list in place

# List comprehension — compact filter
long_tags = [tag for tag in gamer_tag_list if _____(tag) > _____]
```

**Questions:**
- C# declares `string[] gamerTagList`. Python uses a `list`. What is one key difference between a C# array and a Python list?
- C# `foreach (string s in gamerTagList)` iterates the array. What is the exact Python equivalent syntax?
- How do you add a new gamertag to the end of a Python list? (C# equivalent: `List.Add()`)
- Python lets you use `list[-1]` to get the last item. How is this more convenient than C#'s `array[array.Length - 1]`?

**Test challenge:**
Create a list of 4 gamertags. Print the first item, last item (using negative index), and total count. Add a new gamertag with `.append()`. Check if a specific tag is `in` the list. Sort the list and print it again.

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
| Day 8 | Python Project Skeleton |
| Day 9 | Data Loading and Welcome Sequence |
| Day 10 | Display All Gamertags |

## See Also
- [07_python_tuples.md](07_python_tuples.md)
- [08_python_sets.md](08_python_sets.md)
- [09_python_dictionaries.md](09_python_dictionaries.md)
- [14_python_for_loops.md](../03_control_flow/14_python_for_loops.md)

## Challenges

1. **Create and access:** Fill in the blanks to build a gamertag list and access elements:
   ```
   gamer_tag_list = [_____, _____, _____, _____]
   print(gamer_tag_list[_____])     # first item
   print(gamer_tag_list[_____])     # last item using negative index
   print(_____(gamer_tag_list))     # total count
   ```

2. **Iterate like foreach:** The C# project uses `foreach (string s in gamerTagList)`. Fill in the Python equivalent:
   ```
   for _____ in gamer_tag_list:
       print(_____)
   ```

3. **Add a tag:** After loading gamertags, a new one is added. Fill in:
   ```
   new_tag = input("Enter new gamertag: ").strip()
   gamer_tag_list._____(new_tag)
   print(f"Now have {_____(gamer_tag_list)} gamertags")
   ```

4. **Membership check:** Before adding a new tag, check if it already exists. Fill in:
   ```
   if new_tag _____ gamer_tag_list:
       print("Already registered!")
   else:
       gamer_tag_list._____(new_tag)
   ```
