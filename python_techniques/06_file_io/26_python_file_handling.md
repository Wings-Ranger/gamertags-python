# Python File Handling

**W3Schools Link:** https://www.w3schools.com/python/python_file_handling.asp

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
```python
import os

# --- Opening modes ---
# "r"  — read (file must exist)
# "w"  — write (creates or overwrites)
# "a"  — append (creates or adds to end)
# "x"  — create (fails if file exists)
# "rb" — read binary

# Always use the 'with' statement
with open("gamertags.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# Writing (creates or overwrites)
with open("gamertags.txt", "w", encoding="utf-8") as f:
    f.write("ShadowX,Xbox,4250\n")
    f.write("NightOwl,PlayStation,3300\n")

# Appending (adds to end without overwriting)
with open("gamertags.txt", "a", encoding="utf-8") as f:
    f.write("ProSniper,PC,5100\n")

# Checking if a file exists before opening
filename = "gamertags.txt"
if os.path.exists(filename):
    with open(filename, "r") as f:
        print(f.read())
else:
    print(f"File not found: {filename}")

# Getting file size and info
if os.path.exists(filename):
    size = os.path.getsize(filename)
    print(f"File size: {size} bytes")

# Listing files in a directory
for fname in os.listdir("."):
    if fname.endswith(".txt"):
        print(fname)

# Safe file operations with try/except
def load_file_safe(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return ""
    except PermissionError:
        print(f"Permission denied: {filename}")
        return ""

content = load_file_safe("gamertags.txt")

# File path construction (cross-platform)
import os
data_dir = "data"
filename = os.path.join(data_dir, "gamertags.txt")
print(filename)   # data/gamertags.txt (Linux/Mac) or data\gamertags.txt (Windows)
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

## Practice Tips
- Always use `with open(...)` — never call `f.close()` manually
- Specify `encoding="utf-8"` to handle international characters in gamertags
- Check `os.path.exists()` before reading to give a friendly error message
- Practice all three modes: `"r"`, `"w"`, and `"a"` to understand their differences
