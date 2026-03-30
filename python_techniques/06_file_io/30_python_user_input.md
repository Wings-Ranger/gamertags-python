# Python User Input

**W3Schools Link:** https://www.w3schools.com/python/python_user_input.asp

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
```python
# Basic input
name = input("Enter your gamertag: ")
print(f"Hello, {name}!")

# Always strip whitespace
gamertag = input("Enter gamertag: ").strip()

# Case-insensitive platform entry
platform = input("Enter platform (Xbox/PlayStation/PC): ").strip().title()
# .title() converts "xbox" -> "Xbox", "playstation" -> "PlayStation"

# Numeric input with type conversion
def get_score():
    while True:
        raw = input("Enter score: ").strip()
        if raw.isdigit():
            return int(raw)
        print("Please enter a valid positive integer.")

score = get_score()
print(f"Score recorded: {score}")

# Yes/No confirmation
def confirm(prompt):
    """Ask a yes/no question; return True for yes, False for no."""
    while True:
        answer = input(f"{prompt} (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Please enter 'y' or 'n'.")

if confirm("Are you sure you want to delete this gamertag?"):
    print("Deleted.")
else:
    print("Cancelled.")

# Full gamertag input validation loop
VALID_PLATFORMS = {"Xbox", "PlayStation", "PC", "Nintendo Switch"}

def get_valid_gamertag():
    """Keep asking until a valid gamertag is entered."""
    while True:
        tag = input("Enter gamertag (3-15 alphanumeric chars): ").strip()
        if not tag:
            print("  Error: Cannot be empty.")
        elif len(tag) < 3:
            print("  Error: Too short (minimum 3 characters).")
        elif len(tag) > 15:
            print("  Error: Too long (maximum 15 characters).")
        elif not tag.isalnum():
            print("  Error: Letters and numbers only, no spaces or symbols.")
        else:
            return tag

def get_valid_platform():
    """Keep asking until a valid platform is entered."""
    while True:
        platform = input(f"Enter platform {sorted(VALID_PLATFORMS)}: ").strip().title()
        if platform in VALID_PLATFORMS:
            return platform
        print(f"  Error: Must be one of {sorted(VALID_PLATFORMS)}")

# Menu selection by number
def get_menu_choice(options):
    """Display numbered options and return the chosen number."""
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    while True:
        raw = input("Enter choice number: ").strip()
        if raw.isdigit():
            choice = int(raw)
            if 1 <= choice <= len(options):
                return choice
        print(f"  Please enter a number between 1 and {len(options)}.")

menu = ["View all gamertags", "Add a new gamertag", "Filter by platform", "Quit"]
choice = get_menu_choice(menu)
print(f"You selected: {menu[choice - 1]}")
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

## Practice Tips
- Always `.strip()` every `input()` call — make it a habit
- Write `get_valid_gamertag()` as a reusable function with a `while True:` validation loop
- Use `.title()` to normalize platform names so "xbox" becomes "Xbox" automatically
- Test your input functions with blank entries, spaces, and numbers to ensure they validate correctly
