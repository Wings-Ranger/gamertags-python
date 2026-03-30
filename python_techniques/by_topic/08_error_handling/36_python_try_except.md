# Python Try / Except

**W3Schools Link:** https://www.w3schools.com/python/python_try_except.asp

**Homework Day(s):** Day 5, Day 14

---

## Overview
Exception handling with `try/except` allows your program to gracefully respond to errors rather than crashing. Python uses structured exception handling with four clauses: `try` (the risky code), `except` (handles specific errors), `else` (runs if no exception), and `finally` (always runs — used for cleanup). Proper exception handling makes programs robust and user-friendly.

## Key Concepts
- **`try`**: the block where exceptions might occur
- **`except ExceptionType`**: catches a specific type of exception
- **`except (A, B)`**: catches multiple exception types
- **`except Exception as e`**: catches the exception and binds it to variable `e`
- **`else`**: runs only if the `try` block succeeded (no exception raised)
- **`finally`**: always runs — use for cleanup (closing files, releasing resources)
- **Bare `except:`**: catches everything including `KeyboardInterrupt` — avoid
- **Specificity**: catch the most specific exception type possible

## Syntax / Example Code

```
C# pattern (from the gamertag project):
    // C# try/catch
    try
    {
        gamerTagList = File.ReadAllLines("../Gamertags.txt");
    }
    catch (FileNotFoundException e)
    {
        Console.WriteLine("File not found: " + e.Message);
    }

Python skeleton — handle exceptions with try/except (fill in the blanks):

    # Basic try/except — equivalent to C#'s try/catch
    _____:
        gamer_tag_list = open(_____, _____).readlines()
    _____ _____ as e:               # what exception for missing file?
        print(f"File not found: {e}")

    # Catching multiple exceptions (like multiple catch blocks in C#)
    _____:
        with open("Gamertags.txt", "r") as f:
            line = f.readline()
            parts = line.split(",")
            score = int(parts[_____])
    _____ FileNotFoundError:
        print("File not found")
    _____ IndexError:
        print("Missing field in line")
    _____ _____:                     # what handles int("abc") failing?
        print("Score is not a number")

    # try / except / else / finally structure
    _____:
        with open("Gamertags.txt", "r") as f:
            lines = f._____()
    _____ FileNotFoundError:
        print("Starting with empty list")
        lines = _____               # what is an empty list?
    _____:                          # runs only if NO exception occurred
        print(f"Loaded {len(lines)} lines")
    _____:                          # always runs — use for cleanup
        print("Done loading")

    # Utility: safe int conversion
    def safe_int(value, default=_____):
        _____:
            return int(value)
        _____ (ValueError, TypeError):
            return _____            # return default on failure

Questions:
- What Python keyword starts exception handling? (C# uses `try`)
- What Python keyword catches an exception? (C# uses `catch`)
- What is the difference between `except ValueError` and `except Exception`?
- What does `else` do in a try/except block? What does `finally` do?

Test challenge:
    Wrap your `load_gamertags(filename)` method in try/except. Test three scenarios:
    1. The file exists and loads correctly
    2. The filename is wrong (FileNotFoundError)
    3. A line in the file has only 1 column (IndexError when you try parts[1])
    Does your exception handling give a useful message in each case?
```

## Common Use Cases
- Wrapping `open()` calls in `try/except FileNotFoundError` for graceful startup
- Wrapping `int()` conversion of file data in `try/except ValueError`
- Using `finally` to ensure files are closed in older code (prefer `with` instead)
- Building a `safe_int()` utility used throughout the project

## Related Days
| Day | Topic |
|-----|-------|
| Day 5 | File Handling (reading, appending, file paths) |
| Day 14 | Final test and submission prep |

## See Also
- [37_python_exceptions.md](37_python_exceptions.md)
- [38_python_raising_exceptions.md](38_python_raising_exceptions.md)
- [26_python_file_handling.md](../06_file_io/26_python_file_handling.md)
- [11_python_type_casting.md](../02_data_types/11_python_type_casting.md)

## Challenges
- **Blank 1**: Wrap your `load_gamertags` file open in `try:/except FileNotFoundError:`. What should the function return when the file is not found — `None`, `[]`, or raise again?
- **Blank 2**: Write `safe_int(value, default=0)`. Complete the try block: `return int(_____)`, and the except block: `return _____`. What two exception types does converting a non-number raise?
- **Blank 3**: Add an `else:` clause to your load function. What code runs there? Add a `finally:` clause. What would you put in it? (Hint: with `with open(...)`, is `finally` even needed?)
- **Challenge**: C# uses `catch (FileNotFoundException e)` — Python uses `except FileNotFoundError as e`. Try deliberately triggering each of these exceptions in your gamertag project: `FileNotFoundError`, `ValueError`, `IndexError`. Write the try/except that handles all three separately with different print messages for each.
