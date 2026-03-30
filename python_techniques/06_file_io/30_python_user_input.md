# Python User Input

**W3Schools Link:** https://www.w3schools.com/python/python_user_input.asp

**Homework Day(s):** Day 13

---

## Overview
The `input()` function pauses program execution and waits for the user to type something and press Enter. It always returns a string, regardless of what the user types. Handling user input safely — stripping whitespace, validating content, and handling type conversion — is critical for any interactive program like the gamertag manager.

## Key Concepts
- **`input(prompt)`**: displays the prompt string and returns user input as a string
- **Always returns a string**: even if the user types `"42"`, you get `"42"`, not `42`
- **`.strip()`**: always call on input to remove accidental leading/trailing spaces
- **Type conversion**: use `int()` or `float()` to convert numeric inputs
- **Validation loop**: use `while True:` to keep asking until valid input is received
- **EOFError**: raised if input stream ends unexpectedly (e.g., piped input) — handle in production
- **Case normalization**: use `.lower()` or `.upper()` for case-insensitive comparisons

## Syntax / Example Code

```
C# patterns (from the gamertag project):
    // Reading a line of text from the user
    string newGamerTag = Console.ReadLine();

    // Waiting for any key press (used in the main loop)
    Console.ReadKey();

Python skeleton — get input from the user (fill in the blanks):

    # Basic input — equivalent to Console.ReadLine()
    new_tag = _____("Enter your gamertag: ")   # what Python function reads input?

    # IMPORTANT: input() always returns a _____ (what type?)
    # Always strip whitespace the user may have accidentally typed
    new_tag = _____("Enter your gamertag: ")._____(  )

    # The gamertag project's AddNewUserName() equivalent:
    def add_new_user_name(self):
        new_tag = _____("Enter new gamertag: ")._____(  )
        self.gamer_tag_list._____(new_tag)       # add to in-memory list
        with open(self.filename, _____) as f:    # append to file
            f.write(_____ + new_tag)

    # Validation loop — keep asking until valid input is received
    def get_valid_gamertag():
        while _____:                              # what condition runs forever?
            tag = _____("Enter gamertag: ")._____(  )
            if not tag:
                print("Cannot be empty.")
            elif not tag._____(  ):               # what checks letters+digits only?
                print("Letters and numbers only.")
            elif len(tag) < _____ or len(tag) > _____:
                print("Must be 3-15 characters.")
            else:
                return _____                      # valid — exit the loop

    # Menu selection (equivalent to Console.ReadKey() for menu choice)
    choice = _____("Choose: 1) View  2) Add  3) Quit: ")._____(  )
    if choice == _____:
        print("Viewing...")

Questions:
- What Python function is equivalent to C#'s `Console.ReadLine()`?
- What type does `input()` always return, even if the user types a number?
- How do you use a `while` loop to keep asking until the user gives valid input?
- C# uses `Console.ReadKey()` to pause. What could you use in Python instead?

Test challenge:
    Write a `get_valid_gamertag()` function with a while loop. Test it with:
    an empty string, a string with spaces, a 2-character string, and finally
    a valid gamertag. How many times did the loop run before accepting input?
```

## Common Use Cases
- Getting a gamertag from the user with full validation
- Selecting a platform from a numbered menu
- Confirming destructive actions (delete, overwrite) with a yes/no prompt
- Reading a numeric score with `isdigit()` validation before `int()` conversion

## Related Days
| Day | Topic |
|-----|-------|
| Day 13 | Add new gamertag + run-again loop |

## See Also
- [13_python_while_loops.md](../03_control_flow/13_python_while_loops.md)
- [34_python_string_validation.md](../07_strings/34_python_string_validation.md)
- [11_python_type_casting.md](../02_data_types/11_python_type_casting.md)
- [36_python_try_except.md](../08_error_handling/36_python_try_except.md)

## Challenges
- **Blank 1**: Write `new_tag = input(_____).strip()`. What prompt string tells the user what to type?
- **Blank 2**: Write the validation inside a `while True:` loop. Fill in the condition that checks for letters and digits only: `if not tag._____(  ):`. What method is that?
- **Blank 3**: The C# main loop uses `bool isRunning = true; while (isRunning)`. Python version: `is_running = _____; while _____:`. What value starts the loop, and when do you set it to `False`?
- **Challenge**: C# uses `Console.ReadKey()` to wait for any keypress. Python's `input()` always waits for Enter. Write a short menu loop using `input()` that accepts "1", "2", or "3" and repeats until "3" (quit) is entered — mirroring the C# `isRunning` pattern.
