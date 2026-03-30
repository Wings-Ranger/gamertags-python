# Python Return Values

**W3Schools Links:**
- [Python Return Values](https://www.w3schools.com/python/python_functions.asp) — `return`, implicit `None`, early returns (guard clauses)
- [Python Tuples](https://www.w3schools.com/python/python_tuples.asp) — multiple return values are returned and unpacked as tuples
- [Python File Read](https://www.w3schools.com/python/python_file_read.asp) — `with open()` file reading in `load_gamertags` skeleton
- [Python If...Else](https://www.w3schools.com/python/python_conditions.asp) — early-return guard clauses use `if` to exit early

**Homework Day(s):** Day 4

---

## Overview
The `return` statement sends a value back from a function to the caller. It immediately exits the function — any code after `return` in the same block is not executed. Functions without an explicit `return` (or with a bare `return`) implicitly return `None`. Well-designed return values are key to composable, testable functions.

## Key Concepts
- **`return value`**: exits the function and sends `value` back to the caller
- **`return` alone**: exits the function and returns `None`
- **No return statement**: function implicitly returns `None`
- **Multiple return values**: Python returns a tuple — `return a, b` is `return (a, b)`
- **Early return**: returning early on error conditions avoids deeply nested `if` blocks
- **Return type consistency**: avoid functions that sometimes return a value and sometimes `None`

## Syntax / Example Code

**C# pattern (from the gamertag project):**
```csharp
// C# void methods return nothing — they modify class fields directly
public void LoadGamertags()
{
    gamerTagList = File.ReadAllLines("../Gamertags.txt");
    // modifies the field — returns nothing
}
// In Python, functions return data to the caller instead of mutating globals
```

**Python skeleton (fill in the blanks):**
```
# Python function returns data — caller decides what to do with it
def load_gamertags(filename):
    """Load gamertags from file and RETURN the list."""
    gamer_tag_list = []
    with open(filename, _____) as f:
        for line in f:
            line = line._____(  )
            if line:
                gamer_tag_list._____(line)
    _____ gamer_tag_list        # return the list to the caller

# Caller stores the returned value
tags = _____(_____)             # what goes in the blanks?

# Early return (guard clauses) — exit as soon as a problem is found
def validate_gamertag(tag):
    """Return (is_valid, message) for the given gamertag."""
    if _____ tag:
        _____ False, "Gamertag cannot be empty"
    if len(tag) < _____:
        _____ False, "Too short"
    if len(tag) > _____:
        _____ False, "Too long"
    if _____ tag._____(  ):
        _____ False, "Only letters and numbers allowed"
    _____ True, "Valid"

# Unpack the returned tuple on the calling side
is_valid, message = _____("ShadowHunter99")
print(is_valid, message)

is_valid, message = _____("AB")
if _____ is_valid:
    print(message)

# Functions that display only — return None (like C# void)
def show_welcome_message():
    print("Welcome to the Gamertag Manager!")
    # no return statement — implicitly returns _____

result = show_welcome_message()
print(result)    # what does this print?
```

**Questions:**
- C# `void` methods return nothing. What does a Python function return when it has no `return` statement?
- Why is `return gamer_tag_list` at the end of `load_gamertags` better than modifying a global variable?
- What is an "early return" / "guard clause"? How does it reduce nesting compared to a long `if/elif/else` chain?
- When a function `return`s a tuple like `return True, "Valid"`, how do you receive both values on the calling side?

**Test challenge:**
Write `validate_gamertag(tag)` with early-return guard clauses checking: empty, too short (< 3), too long (> 15), and non-alphanumeric. Return `(True, "Valid")` or `(False, reason)`. Test all four failure cases plus one success.

## Common Use Cases
- `validate_gamertag()` returning `(True/False, message)` for clean error handling
- `load_players()` returning the populated list to the caller
- `find_player()` returning the matching dict or `None`
- `filter_by_platform()` returning a new filtered list

## Related Days
| Day | Topic |
|-----|-------|
| Day 4 | Functions (decomposition, inputs/outputs, naming) |

## See Also
- [17_python_functions.md](17_python_functions.md)
- [18_python_function_arguments.md](18_python_function_arguments.md)
- [07_python_tuples.md](../02_data_types/07_python_tuples.md)
- [12_python_if_else.md](../03_control_flow/12_python_if_else.md)

## Challenges

1. **Return vs void:** C# `LoadGamertags()` sets a field (void). Python returns the list. Fill in:
   ```
   def load_gamertags(filename):
       tags = []
       # ... load file ...
       _____ tags             # return to caller

   my_tags = _____(_____)    # store what was returned
   ```

2. **Early return pattern:** Write `validate_gamertag(tag)` using guard clauses (one `return` per failure, no `else` needed):
   ```
   def validate_gamertag(tag):
       if _____ tag:
           _____ False, "_____"
       if len(tag) < _____:
           _____ False, "_____"
       if len(tag) > _____:
           _____ False, "_____"
       _____ True, "Valid"
   ```

3. **Unpack the tuple:** Call `validate_gamertag` and capture both return values separately:
   ```
   _____, _____ = validate_gamertag("AB")
   if _____ is_valid:
       print(message)
   ```

4. **None return:** What does a Python function return if there is no `return` statement? Write a `show_welcome_message()` function, call it, and print its return value to confirm. When is returning `None` the right choice?
