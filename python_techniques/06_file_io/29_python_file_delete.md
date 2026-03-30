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

```
C# context:
    // C# equivalent for deleting a file:
    System.IO.File.Delete("../Gamertags.txt");
    // The gamertag project doesn't delete files, but you may need this
    // for resetting test data or archiving old records.

Python skeleton — delete files safely (fill in the blanks):

    import _____                          # what module has file/path utilities?

    filename = "old_gamertags.txt"

    # Always check before deleting — prevents FileNotFoundError
    if _____.path._____(filename):        # what method checks existence?
        _____.remove(filename)            # what method deletes the file?
        print(f"Deleted: {filename}")
    else:
        print(f"File not found: {filename}")

    # Safe deletion using try/except
    def delete_file_safe(filename):
        try:
            _____.remove(_____)
            return _____                  # True = success
        except FileNotFoundError:
            print(f"Not found: {filename}")
            return _____                  # False = failed
        except PermissionError:
            print(f"Permission denied: {filename}")
            return _____

    # Backup before deleting (safer pattern)
    import shutil

    def backup_and_delete(filename):
        if not os.path.exists(filename):
            return False
        backup_name = filename + _____    # what extension marks a backup?
        shutil._____(filename, backup_name)  # copy original to backup
        os._____(filename)                   # then delete original
        return True

Questions:
- What module provides `os.remove()` and `os.path.exists()`?
- What exception does `os.remove()` raise if the file doesn't exist?
- Why is it safer to use `shutil.copy()` before `os.remove()` rather than
  deleting directly?
- How is deleting a file in Python different from writing over it with `"w"` mode?

Test challenge:
    Create a test file called "test_delete.txt", write some content to it, then
    call your `delete_file_safe()` function on it. Confirm it returns True.
    Call it again on the same (now deleted) file — what does it return? What
    gets printed?
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

## Challenges
- **Blank 1**: Write the `if os.path.exists(_____)` check for `"Gamertags.txt"`. What argument does `exists()` take?
- **Blank 2**: Inside `backup_and_delete`, complete `shutil._____(filename, backup_name)` and `os._____(filename)`. What are the correct function names?
- **Blank 3**: Write a `reset_data_file(filename)` function that backs up the file as `filename + ".bak"`, deletes the original, then creates a new empty file using `open(_____, "w")`.
- **Challenge**: Deleting files is irreversible — there is no "Recycle Bin" in Python. Design a safer workflow: before deleting `Gamertags.txt`, copy it to `Gamertags_backup.txt`. Write the two-line Python code for that using `shutil.copy`. When in the gamertag project lifecycle would you actually need to delete a file?
