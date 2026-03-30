# Python While Loops

**W3Schools Link:** https://www.w3schools.com/python/python_while_loops.asp

**Homework Day(s):** Day 3, Day 13

---

## Overview
A `while` loop repeats a block of code as long as a condition remains `True`. It is the go-to loop when you don't know in advance how many iterations are needed — for example, prompting the user until they enter valid input, or running a program menu until the user chooses to quit.

## Key Concepts
- **Condition checked before each iteration**: if `False` on first check, loop body never runs
- **`break`**: immediately exits the loop
- **`continue`**: skips the rest of the current iteration and re-checks the condition
- **`else`**: optional block that runs after the loop completes normally (not via `break`)
- **Infinite loop**: `while True:` — must use `break` to exit; common for menus
- **Avoid infinite loops**: ensure the loop variable is updated inside the loop

## Syntax / Example Code

**C# pattern (from the gamertag project):**
```csharp
// C# Program.cs uses a bool flag to run the main menu loop
bool isRunning = true;

while (isRunning)
{
    ShowWelcomeMessage();
    string userChoice = Console.ReadLine();
    if      (userChoice == "1") LoadGamertags();
    else if (userChoice == "2") PrintAllGamertags();
    // ...
    else if (userChoice == "5") isRunning = false;
}
```

**Python skeleton (fill in the blanks):**
```
# Direct translation of C#'s bool isRunning pattern
is_running = _____
while _____:
    print("\n--- Gamertag Manager ---")
    print("1. Load gamertags")
    print("2. Print all gamertags")
    print("3. Print tags ending with number")
    print("4. Print tags not starting with letter/digit")
    print("5. Add new gamertag")
    print("6. Quit")

    choice = _____(_____)._____(  )    # read input and strip whitespace

    if choice _____ "1":
        _____()                        # call load function
    _____ choice _____ "2":
        _____()                        # call print function
    _____ choice _____ "6":
        is_running = _____             # stop the loop
        print("Goodbye!")
    _____:
        print("Invalid option.")

# Alternative Pythonic pattern — while True with break
while _____:
    choice = input("Enter choice (q to quit): ").strip()
    if choice _____ "q":
        _____                          # exit the loop immediately
    print(f"You chose: {choice}")
```

**Questions:**
- C# uses `bool isRunning = true` and `while (isRunning)`. What is the direct Python translation of each line?
- What does `while True:` do, and how do you exit such a loop?
- In C#, `Console.ReadLine()` reads user input. What is the Python equivalent?
- What happens if you forget to set `is_running = False` or forget `break`? What kind of loop does that create?

**Test challenge:**
Write a `while` loop that keeps asking for a gamertag until the user enters a non-empty string. Print `"Please enter a value"` on each empty attempt and `"Accepted: {tag}"` when they provide something valid.

## Common Use Cases
- Looping until the user enters a valid gamertag (input validation)
- Running the main program menu until the user chooses to quit
- Retrying a failed file operation a limited number of times
- Processing items from a queue until it is empty

## Related Days
| Day | Topic |
|-----|-------|
| Day 3 | Loops and Program Flow (while loops, iterating lists) |
| Day 13 | Add new gamertag + run-again loop |

## See Also
- [14_python_for_loops.md](14_python_for_loops.md)
- [15_python_break_continue.md](15_python_break_continue.md)
- [10_python_booleans.md](../02_data_types/10_python_booleans.md)
- [30_python_user_input.md](../06_file_io/30_python_user_input.md)

## Challenges

1. **Translate the C# main loop:** The C# project uses `bool isRunning = true; while (isRunning)`. Fill in Python:
   ```
   is_running = _____
   while _____:
       choice = input("Your choice: ").strip()
       if choice == "6":
           is_running = _____
   ```

2. **while True with break:** Rewrite the same loop using `while True:` and `break` instead of a flag variable. Which style do you find clearer and why?
   ```
   while _____:
       choice = input("Your choice: ").strip()
       if choice == "6":
           _____
   ```

3. **Input validation loop:** Write a `while` loop that keeps prompting until the user enters a non-empty gamertag:
   ```
   while _____:
       tag = input("Enter gamertag: ")._____(  )
       if _____:            # what condition means "not empty"?
           _____            # how do you exit?
       print("Cannot be empty. Try again.")
   ```

4. **Max attempts:** Modify the validation loop to give up after 3 failed attempts. Use a counter variable. What should happen when `attempts >= 3`?
