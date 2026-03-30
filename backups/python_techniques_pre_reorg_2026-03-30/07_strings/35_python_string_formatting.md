# Python String Formatting

**W3Schools Link:** https://www.w3schools.com/python/python_string_formatting.asp

**Homework Day(s):** Day 1, Day 8, Day 9, Day 10

---

## Overview
Python offers multiple ways to format strings: f-strings (Python 3.6+), `.format()`, and the older `%` operator. F-strings are the modern standard — they are readable, fast, and support format specifications directly inside the curly braces. Format specifiers control alignment, padding, decimal places, and number formatting.

## Key Concepts
- **f-strings**: `f"Name: {variable}"` — embed expressions directly
- **Format specifiers**: `{value:format_spec}` inside f-strings or `.format()`
- **Alignment**: `<` left, `>` right, `^` center, with optional width `{x:<15}`
- **Number formatting**: `,` for thousands separator, `.2f` for 2 decimal places
- **Padding character**: `{x:=^20}` pads with `=` centered in 20 chars
- **`.format()`**: `"Name: {}".format(name)` — older style, still valid
- **`%` formatting**: `"Name: %s" % name` — legacy style, avoid in new code

## Syntax / Example Code

```
C# pattern (from the gamertag project):
    // C# string interpolation
    Console.WriteLine($"Found {count} gamertags ending with a number.");
    Console.WriteLine($"Gamertag: {s}");

    // C# also uses string.Format() — older style
    Console.WriteLine(string.Format("Count: {0}", count));

Python skeleton — format strings with f-strings (fill in the blanks):

    tag   = "ShadowX99"
    count = 3

    # Basic f-string — equivalent to C#'s $"..." interpolation
    print(f"Gamertag: _____")            # embed tag variable
    print(f"Found _____ gamertags.")     # embed count variable

    # Expression inside f-string
    tags = ["ShadowX", "NightOwl", "Pro7"]
    print(f"Total: _____")              # call len() inside the f-string

    # Alignment for display output
    # Left-align in 20 characters wide:
    print(f"{tag:_____}")               # format spec: < means left, number is width

    # Right-align a number in 8 characters wide:
    score = 4250
    print(f"{score:_____}")             # format spec: > means right

    # Center with fill character
    print(f"{'LEADERBOARD':_____^_____}")  # fill char, alignment, width

    # Print a separator line
    print("_____" * _____)              # what character * what count?

    # Formatted display function for print_all_gamertags
    def format_gamertag_line(number, tag):
        return f"{number:<_____} {tag:<_____}"   # what widths look good?

    # Older .format() style (you may see this in existing Python code)
    msg = "Gamertag: {}, Count: {}"._____(tag, count)
    print(msg)

Questions:
- Python uses `f"..."` and C# uses `$"..."`. What goes inside the curly braces?
- What format specifier left-aligns text in a field of width 20?
- How do you display a number with a thousands separator (e.g., 4,250)?
- What is the `*` operator doing when used with a string like `"=" * 40`?

Test challenge:
    Write a `show_welcome_message(self)` method that uses f-strings to print:
    - A separator line: `"=" * 40`
    - A centered title: `f"{'Gamertag Manager':^40}"`
    - A line showing the count: `f"  {len(self.gamer_tag_list)} gamertags loaded"`
    - Another separator line
    What do you need to fill in for each blank?
```

## Common Use Cases
- Building aligned, fixed-width leaderboard tables with `:<15` and `:>8`
- Displaying scores with thousands separators: `f"{score:,}"`
- Printing section headers: `f"{'LEADERBOARD':=^40}"`
- Generating CSV-compatible output: `f"{tag},{platform},{score}"`

## Related Days
| Day | Topic |
|-----|-------|
| Day 1 | Python Foundations (variables, data types, strings, lists) |
| Day 8 | Python Project Skeleton |
| Day 9 | Data Loading and Welcome Sequence |
| Day 10 | Display All Gamertags |

## See Also
- [05_python_strings.md](../02_data_types/05_python_strings.md)
- [31_python_print.md](../06_file_io/31_python_print.md)
- [32_python_string_methods.md](32_python_string_methods.md)

## Challenges
- **Blank 1**: Write `show_welcome_message(self)` using f-strings. Print a separator `"=" * _____`, a centered title `f"{'Gamertag Manager':^_____}"`, and a count line `f"  {len(self.gamer_tag_list)} gamertags loaded"`. What width gives a nice output?
- **Blank 2**: Write `format_gamertag_line(i, tag)` that returns `f"{i:<_____} {tag:<_____}"`. What widths should you pick so the numbers and tags align cleanly?
- **Blank 3**: In `print_all_gamertags(self)`, use `enumerate(self.gamer_tag_list, _____)` to get 1-based numbers. Write the `print(f"_____")` line using those numbers.
- **Challenge**: C# uses `$"Gamertag: {s}"` and Python uses `f"Gamertag: {s}"`. They look almost identical — but Python f-strings can include expressions: `f"{len(tags) * 2}"`. Write three f-strings that each embed a different kind of expression: a method call, a math operation, and a conditional expression (`x if condition else y`).
