# Python print()

**W3Schools Link:** https://www.w3schools.com/python/ref_func_print.asp

**Homework Day(s):** Day 1, Days 8–10

---

## Overview
The `print()` function outputs text to the console (standard output). It is one of the most frequently used functions in Python for displaying information to the user and for debugging. `print()` supports formatting options including custom separators, end characters, and outputting to files or other streams.

## Key Concepts
- **Signature**: `print(*objects, sep=" ", end="\n", file=sys.stdout, flush=False)`
- **Multiple arguments**: `print(a, b, c)` prints them separated by spaces by default
- **`sep`**: customizes the separator between multiple arguments (default: `" "`)
- **`end`**: customizes what's printed at the end (default: `"\n"` newline)
- **`file`**: redirect output to a file instead of the console
- **f-strings**: the modern, readable way to embed variables in output
- **Pretty printing**: use `pprint` module for nested data structures

## Syntax / Example Code

```
C# pattern (from the gamertag project):
    // Printing to the console
    Console.WriteLine("Welcome to the Gamertag Manager!");
    Console.WriteLine(s);   // printing each gamertag in the foreach loop

    // C# string interpolation
    Console.WriteLine($"Found {count} gamertags.");

Python skeleton — use print() (fill in the blanks):

    # Basic print — equivalent to Console.WriteLine()
    _____("Welcome to the Gamertag Manager!")

    # Printing a variable — equivalent to Console.WriteLine(s)
    tag = "ShadowX99"
    _____(tag)

    # f-string — equivalent to C#'s $"..." interpolation
    count = 5
    _____(f"Found _____ gamertags.")      # embed count variable in the string

    # Printing each gamertag — translating the C# foreach loop
    gamer_tag_list = ["ShadowX", "NightOwl", "ProSniper"]
    for _____ in _____:
        _____(_____)

    # Custom separator — print without newline at end
    _____(">", end=_____)     # what end value suppresses the newline?
    _____(tag)                # prints on same line as ">"

    # Print a separator line
    _____(_____ * 40)         # print "=" repeated 40 times

    # Formatted table row
    _____(f"{'Gamertag':<_____} {'Platform':>_____}")   # what widths align nicely?
    for tag in gamer_tag_list:
        _____(f"{tag:<_____}")

Questions:
- What is the Python equivalent of C#'s `Console.WriteLine()`?
- How do you embed a variable in a string in Python? (C# uses `$"{variable}"`)
- What parameter controls what `print()` puts at the end of its output?
- How do you print multiple items on the same line?

Test challenge:
    Implement `print_all_gamertags(self)` for your Gamertags class. It should print
    a header line, then each gamertag numbered (1. ShadowX, 2. NightOwl, etc.).
    Use `enumerate()` to get the number. How do you use `enumerate()` with a
    starting index of 1?
```

## Common Use Cases
- Displaying numbered player lists with aligned columns using f-string formatting
- Printing separator lines (`"=" * 45`) to structure console output
- Debug printing variables with `f"{var=}"` (Python 3.8+)
- Logging output to a file with `print(..., file=log_file)`

## Related Days
| Day | Topic |
|-----|-------|
| Day 1 | Python Foundations (variables, data types, strings, lists) |
| Days 8-10 | Build project skeleton, data loading, display |

## See Also
- [35_python_string_formatting.md](../07_strings/35_python_string_formatting.md)
- [05_python_strings.md](../02_data_types/05_python_strings.md)
- [09_python_dictionaries.md](../02_data_types/09_python_dictionaries.md)

## Challenges
- **Blank 1**: Write `print_all_gamertags(self)` using a `for` loop. Print each tag. Then improve it to use `enumerate(self.gamer_tag_list, _____)` so each line is numbered starting from 1.
- **Blank 2**: Write `show_welcome_message(self)`. It should print a header (`"=" * _____`), a title, and another separator. What width looks good on a standard terminal?
- **Blank 3**: Write an f-string that prints: `f"{i}. {tag}"` where `i` is the number and `tag` is the gamertag. Now add left-alignment: `f"{i:<_____} {tag:<_____}"`. What widths give clean columns?
- **Challenge**: The C# code uses `Console.WriteLine(s)` inside a `foreach` loop. Your Python version uses `print(s)` inside a `for` loop. Write both side by side as comments. Now add numbering to the Python version using `enumerate` — C# would need a separate counter variable. Which is more concise?
