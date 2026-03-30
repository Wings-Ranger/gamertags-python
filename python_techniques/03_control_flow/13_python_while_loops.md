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
```python
# Basic while loop — count down
count = 3
while count > 0:
    print(f"Starting in {count}...")
    count -= 1
print("Go!")

# Input validation loop — keep asking until valid
def get_valid_gamertag():
    while True:
        tag = input("Enter gamertag: ").strip()
        if not tag:
            print("Gamertag cannot be empty. Try again.")
        elif len(tag) < 3:
            print("Too short — minimum 3 characters.")
        elif len(tag) > 15:
            print("Too long — maximum 15 characters.")
        elif not tag.isalnum():
            print("Letters and numbers only.")
        else:
            return tag  # valid — exit loop

# Run-again loop (Day 13 pattern)
running = True
while running:
    print("\n--- Gamertag Manager ---")
    print("1. View all gamertags")
    print("2. Add a new gamertag")
    print("3. Quit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        print("(displaying gamertags...)")
    elif choice == "2":
        print("(adding gamertag...)")
    elif choice == "3":
        running = False
        print("Goodbye!")
    else:
        print("Invalid option, please try again.")

# while with break
attempts = 0
while True:
    guess = input("Guess the gamertag: ")
    attempts += 1
    if guess == "ShadowHunter99":
        print(f"Correct in {attempts} attempt(s)!")
        break
    print("Wrong, try again.")

# while with continue
numbers = [1, 0, 3, 0, 5]
i = 0
while i < len(numbers):
    i += 1
    if numbers[i - 1] == 0:
        continue   # skip zeros
    print(numbers[i - 1])

# while/else
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    tag = input("Enter gamertag: ").strip()
    if tag:
        print("Accepted!")
        break
    attempts += 1
else:
    print("Too many failed attempts.")
```

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

## Practice Tips
- Write a `while True:` loop that asks for a gamertag and only exits when valid
- Build a simple numbered menu with `while True:` and `break` on quit
- Practice `while` with a counter variable and make sure the counter changes each iteration
- Use the `while/else` pattern to handle "max attempts exceeded" scenarios
