# Python File Handling

**W3Schools Links:**
- [Python File Handling](https://www.w3schools.com/python/python_file_handling.asp) — `open()`, file modes overview, `with` statement
- [Python File Read](https://www.w3schools.com/python/python_file_read.asp) — read mode `"r"`, `.read()`, `.readlines()`
- [Python File Write](https://www.w3schools.com/python/python_file_write.asp) — write mode `"w"` and append mode `"a"`
- [Python Modules](https://www.w3schools.com/python/python_modules.asp) — `import os` and `os.path.exists()` used in exercises
- [Python Try Except](https://www.w3schools.com/python/python_try_except.asp) — handling `FileNotFoundError` when file doesn't exist

**Homework Day(s):** Day 5

---

## Overview
File handling is the ability to read from and write to files stored on disk. It is essential for any program that needs to persist data between runs — like a gamertag manager that saves and loads player records from a text or CSV file. Python's built-in `open()` function and the `with` statement are the primary tools.

## Key Concepts
- **`open(filename, mode)`**: opens a file and returns a file object
- **Modes**: `"r"` (read), `"w"` (write/overwrite), `"a"` (append), `"x"` (create new), add `"b"` for binary
- **`with` statement**: automatically closes the file when the block exits — always prefer this
- **File methods**: `.read()`, `.readline()`, `.readlines()`, `.write()`, `.writelines()`
- **`close()`**: closes the file — handled automatically by `with`
- **Paths**: use forward slashes or `os.path` / `pathlib` for cross-platform paths
- **Encoding**: specify `encoding="utf-8"` to handle special characters

## Syntax / Example Code

```
C# patterns (from the gamertag project):
    // Reading all lines at once
    gamerTagList = File.ReadAllLines("../Gamertags.txt");

    // Appending a new entry
    File.AppendAllText("../Gamertags.txt", "\n" + newGamerTag);

Python skeleton — open files with `open()` and `with` (fill in the blanks):

    # Reading a file (equivalent to File.ReadAllLines)
    with _____(_____, _____) as f:       # what function? what filename? what mode?
        lines = f._____()                # what method reads ALL lines into a list?

    # Writing (creating or overwriting)
    with _____(_____, _____) as f:       # what mode overwrites?
        f._____(_____)                   # write a single string

    # Appending (equivalent to File.AppendAllText)
    with _____(_____, _____) as f:       # what mode appends without overwriting?
        f.write("\n" + _____)            # what variable holds the new gamertag?

    # Checking if a file exists before opening (no C# equivalent shown)
    import _____                         # what module has path utilities?
    if _____.path.exists(_____):
        print("File found")
    else:
        print("File not found")

Questions:
- What Python keyword opens a file? (W3Schools: Python File Open)
- What three mode strings do you need for reading, writing, and appending?
- What does the `with` keyword do automatically that C# requires you to do manually?
- In C#, the path is `"../Gamertags.txt"`. How would you write that same relative
  path in Python?

Test challenge:
    Write a short program that:
    1. Opens "Gamertags.txt" in read mode and prints how many lines it has
    2. Opens it in append mode and adds a new gamertag
    3. Opens it in read mode again and confirms the count increased by 1
    What happens if "Gamertags.txt" does not exist when you try to open it in read mode?
```

## Common Use Cases
- Loading all gamertag records at program startup with `open("gamertags.txt", "r")`
- Saving changes back to file with `open("gamertags.txt", "w")`
- Appending a new gamertag with `open("gamertags.txt", "a")`
- Checking `os.path.exists()` before reading to avoid crashes

## Related Days
| Day | Topic |
|-----|-------|
| Day 5 | File Handling (reading, appending, file paths) |

## See Also
- [27_python_file_read.md](27_python_file_read.md)
- [28_python_file_write.md](28_python_file_write.md)
- [29_python_file_delete.md](29_python_file_delete.md)
- [36_python_try_except.md](../08_error_handling/36_python_try_except.md)

## Challenges
- **Blank 1**: Write `with open("Gamertags.txt", _____) as f:`. What mode string reads without modifying the file?
- **Blank 2**: Write `with open("Gamertags.txt", _____) as f: f.write(_____)`. What mode appends? What string do you write if the new gamertag is in a variable called `new_tag`?
- **Blank 3**: Write the `os.path.exists(_____)`  check before opening for reading. What string argument goes in the blank?
- **Challenge**: The C# project uses `"../Gamertags.txt"` — a relative path going up one directory. If your Python script is in the same folder as `Gamertags.txt`, what path string do you use instead? Test both `"Gamertags.txt"` and `"../Gamertags.txt"` from different working directories and observe the difference.
