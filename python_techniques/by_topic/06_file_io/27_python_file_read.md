# Python File Read

**W3Schools Link:** https://www.w3schools.com/python/python_file_read.asp

**Homework Day(s):** Day 5, Day 9, Day 10

---

## Overview
Reading files in Python is done with the `open()` function in read mode (`"r"`). Python provides multiple ways to read file content: all at once, one line at a time, or all lines as a list. For a gamertag project, reading a CSV or text file line by line and parsing each record is a fundamental skill.

## Key Concepts
- **`f.read()`**: reads the entire file as a single string
- **`f.readline()`**: reads one line at a time (including the newline character)
- **`f.readlines()`**: reads all lines into a list of strings
- **`for line in f:`**: most memory-efficient way to iterate lines — preferred for large files
- **`.strip()`**: removes leading/trailing whitespace and newlines from each line — always apply
- **Empty line handling**: skip blank lines with `if not line.strip(): continue`
- **`encoding="utf-8"`**: specify encoding to handle international characters correctly

## Syntax / Example Code

```
C# pattern (from the gamertag project):
    gamerTagList = File.ReadAllLines("../Gamertags.txt");
    // Returns a string[] with one element per line

Python skeleton — three ways to read a file (fill in the blanks):

    # Method 1: read entire file as one string
    with open("Gamertags.txt", _____) as f:
        content = f._____()         # one big string, includes \n characters

    # Method 2: readlines() — closest to File.ReadAllLines
    with open("Gamertags.txt", _____) as f:
        lines = f._____()           # returns a list — equivalent to string[]
    # lines still has "\n" at the end of each item — how do you remove it?
    for line in lines:
        print(line._____(  ))       # what method strips whitespace/newlines?

    # Method 3: for loop (most Pythonic — reads one line at a time)
    with open("Gamertags.txt", _____) as f:
        for line in f:
            line = line._____()
            if not _____:           # how do you skip blank lines?
                continue
            print(line)

    # Load into a list (replacing C#'s string[] gamerTagList)
    def load_gamertags(filename):
        gamer_tag_list = _____      # start with an empty list
        with open(_____, _____) as f:
            for line in f:
                line = line._____()
                if line:
                    gamer_tag_list._____(line)   # what method adds to a list?
        return gamer_tag_list

Questions:
- What is the difference between `f.read()`, `f.readline()`, and `f.readlines()`?
- Why should you always call `.strip()` on lines read from a file?
- What exception is raised if the file does not exist? How do you handle it?
- C# `File.ReadAllLines` returns `string[]`. What Python type does `readlines()` return?

Test challenge:
    Create a text file with 5 gamertags, one per line, with a blank line in the middle.
    Read it using Method 3 (the for loop). Confirm that blank lines are skipped and
    you end up with exactly 5 items. Then read it using Method 2 — what is different
    about the raw values in the list?
```

## Common Use Cases
- Loading all gamertag records at startup into a list of dicts
- Counting how many records are in the file
- Parsing CSV-formatted player data with `.split(",")`
- Using `csv.reader` for more robust CSV parsing

## Related Days
| Day | Topic |
|-----|-------|
| Day 5 | File Handling (reading, appending, file paths) |
| Day 9 | Data Loading and Welcome Sequence |
| Day 10 | Display All Gamertags |

## See Also
- [26_python_file_handling.md](26_python_file_handling.md)
- [28_python_file_write.md](28_python_file_write.md)
- [09_python_dictionaries.md](../02_data_types/09_python_dictionaries.md)
- [36_python_try_except.md](../08_error_handling/36_python_try_except.md)

## Challenges
- **Blank 1**: Complete `load_gamertags(filename)` using a `for line in f:` loop. What do you call on each line to remove `\n`? What method adds a cleaned line to the list?
- **Blank 2**: Wrap your `open()` call in a `try/except _____` block. What exception class handles a missing file? What should the function return in that case?
- **Blank 3**: After loading, write `print(f"Loaded _____ gamertags")`. What expression gives you the count of items in a list?
- **Challenge**: The C# code assigns directly: `gamerTagList = File.ReadAllLines(...)`. In Python, your `load_gamertags` function returns a list that you assign to `self.gamer_tag_list`. Write that call: `self.gamer_tag_list = self.load_gamertags(_____)`. Where does the filename come from?
