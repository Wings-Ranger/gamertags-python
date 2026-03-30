# Python File Delete

**W3Schools Link:** https://www.w3schools.com/python/python_file_remove.asp

**Homework Day(s):** Day 5

---

## Overview
Python's `os` module provides functions for deleting files and directories. Deleting files is a destructive, irreversible operation, so it should always be done with care — first checking that the file exists, and optionally creating a backup before deletion. The `shutil` module can move files to a backup location as a safer alternative.

## Key Concepts
- **`os.remove(path)`**: deletes a file; raises `FileNotFoundError` if not found
- **`os.unlink(path)`**: same as `os.remove()` — an alias
- **`os.rmdir(path)`**: removes an empty directory
- **`shutil.rmtree(path)`**: removes a directory and all its contents — very destructive
- **`os.path.exists(path)`**: always check before deleting to avoid errors
- **`os.rename(src, dst)`**: rename or move a file — useful for creating backups
- **`shutil.copy(src, dst)`**: copy a file before deleting (safer pattern)

## Syntax / Example Code
```python
import os
import shutil
from datetime import datetime

# --- Basic file deletion ---
filename = "temp_export.txt"

# Always check first
if os.path.exists(filename):
    os.remove(filename)
    print(f"Deleted: {filename}")
else:
    print(f"File not found: {filename}")

# --- Safe deletion with try/except ---
def delete_file_safe(filename):
    """Delete a file if it exists, handling errors gracefully."""
    try:
        os.remove(filename)
        print(f"Deleted: {filename}")
        return True
    except FileNotFoundError:
        print(f"File not found: {filename}")
        return False
    except PermissionError:
        print(f"Permission denied: {filename}")
        return False

delete_file_safe("old_gamertags.txt")

# --- Backup before delete (safer pattern) ---
def backup_and_delete(filename):
    """Create a timestamped backup, then delete the original."""
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        return False

    # Create backup filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base, ext = os.path.splitext(filename)
    backup_name = f"{base}_backup_{timestamp}{ext}"

    # Copy to backup
    shutil.copy(filename, backup_name)
    print(f"Backup created: {backup_name}")

    # Delete original
    os.remove(filename)
    print(f"Original deleted: {filename}")
    return True

# --- Rename (move) a file instead of deleting ---
def archive_file(filename):
    """Rename file to .bak instead of deleting."""
    if os.path.exists(filename):
        backup = filename + ".bak"
        os.rename(filename, backup)
        print(f"Archived as: {backup}")

# --- Listing and cleaning up temp files ---
def cleanup_temp_files(directory="."):
    """Delete all .tmp files in a directory."""
    deleted = 0
    for fname in os.listdir(directory):
        if fname.endswith(".tmp"):
            fpath = os.path.join(directory, fname)
            os.remove(fpath)
            deleted += 1
    print(f"Cleaned up {deleted} temp file(s)")

# --- Gamertag project: delete and recreate data file ---
def reset_data_file(filename):
    """Delete the gamertags file and create a fresh empty one."""
    if os.path.exists(filename):
        # Backup first
        shutil.copy(filename, filename + ".bak")
        os.remove(filename)

    # Create a new empty file
    with open(filename, "w") as f:
        pass   # creates empty file
    print(f"Data file reset: {filename}")
```

## Common Use Cases
- Deleting a temporary export or report file after it's been processed
- Archiving an old gamertag file before creating a fresh one
- Cleaning up backup or `.tmp` files after a successful save
- Resetting the data file during testing

## Related Days
| Day | Topic |
|-----|-------|
| Day 5 | File Handling (reading, appending, file paths) |

## See Also
- [26_python_file_handling.md](26_python_file_handling.md)
- [27_python_file_read.md](27_python_file_read.md)
- [28_python_file_write.md](28_python_file_write.md)
- [36_python_try_except.md](../08_error_handling/36_python_try_except.md)

## Practice Tips
- Always check `os.path.exists()` or use `try/except FileNotFoundError` before deleting
- Create a backup with `shutil.copy()` before any destructive delete operation
- Test deletion in a separate folder with test files before using on real data
- Consider using `os.rename()` to a `.bak` extension as a safer alternative to permanent deletion
