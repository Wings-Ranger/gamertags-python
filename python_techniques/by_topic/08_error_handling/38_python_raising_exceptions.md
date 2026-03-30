# Python Raising Exceptions

**W3Schools Link:** https://www.w3schools.com/python/python_try_except.asp

**Homework Day(s):** Day 14

---

## Overview
The `raise` statement lets you throw an exception intentionally — either a built-in exception or a custom one. Raising exceptions is how you enforce preconditions, validate inputs at function boundaries, and signal error conditions to callers. Custom exception classes make your program's error handling expressive and specific.

## Key Concepts
- **`raise ExceptionType("message")`**: raises an exception with a descriptive message
- **`raise`** (bare): re-raises the current exception — used inside `except` blocks
- **`raise ... from e`**: chains exceptions to preserve context (Python 3)
- **Custom exceptions**: subclass `Exception` (or a more specific class) for domain-specific errors
- **When to raise**: at function entry when preconditions are not met
- **`assert`**: a lightweight way to raise `AssertionError` for developer-facing checks (not for user input)

## Syntax / Example Code

```
C# context:
    // C# throws exceptions with the 'throw' keyword
    if (string.IsNullOrEmpty(tag))
        throw new ArgumentException("Gamertag cannot be empty");

    // C# custom exception:
    public class InvalidGamertagException : Exception
    {
        public InvalidGamertagException(string message) : base(message) { }
    }

Python skeleton — raise exceptions (fill in the blanks):

    # Raise a built-in exception — equivalent to C#'s 'throw'
    def validate_tag(tag):
        if not tag:
            _____ _____("Gamertag cannot be empty")   # what keyword? what class?
        if len(tag) < 3:
            _____ ValueError(f"Too short: '{tag}'")
        if not tag.isalnum():
            _____ ValueError(f"Invalid characters: '{tag}'")
        return tag   # valid

    # Custom exception class — equivalent to C#'s custom exception
    class GamertagError(_____):   # what built-in class do you inherit from?
        _____

    class GamertagTooShortError(_____):   # inherit from GamertagError
        def _____(self, tag, min_len=3):
            self.tag = tag
            # Call parent constructor with a message
            _____.__init__(self, f"'{tag}' is too short (min {min_len})")

    class InvalidCharactersError(_____):
        def _____(self, tag):
            super()._____(f"'{tag}' has invalid characters")

    # Use custom exceptions in validation
    def validate_gamertag(tag):
        if not tag:
            _____ GamertagError("Cannot be empty")
        if len(tag) < 3:
            _____ GamertagTooShortError(tag)
        if not tag.isalnum():
            _____ InvalidCharactersError(tag)
        return tag

    # Catching custom exceptions
    try:
        validate_gamertag("AB")
    except GamertagTooShortError as e:
        print(f"Too short: {e}")
    except GamertagError as e:      # catches parent — more general
        print(f"Gamertag error: {e}")

    # Re-raise (equivalent to C#'s 'throw;' with no argument)
    def load_gamertags_strict(filename):
        try:
            with open(filename) as f:
                return f.readlines()
        except FileNotFoundError:
            print(f"Warning: {filename} not found")
            _____       # re-raise to let the caller handle it

Questions:
- What Python keyword raises an exception? (C# uses `throw`)
- What class should a custom exception inherit from?
- Why might you create a custom `GamertagError` instead of using `ValueError`?
- What does a bare `raise` (with no argument) do inside an `except` block?

Test challenge:
    Implement `validate_gamertag(tag)` using your custom `GamertagError` hierarchy.
    Test it with these tags: `""`, `"AB"`, `"Shadow X"`, `"ValidTag99"`.
    Catch `GamertagTooShortError` separately from `InvalidCharactersError`.
    Can you catch all gamertag errors with just `except GamertagError`? Why?
```

## Common Use Cases
- `raise ValueError` in `set_score()` when score is negative
- Custom `GamertagError` hierarchy for detailed validation feedback
- Re-raising with `raise` in `except` to log then propagate
- Using `assert` in internal/developer-facing code to check preconditions

## Related Days
| Day | Topic |
|-----|-------|
| Day 14 | Final test and submission prep |

## See Also
- [36_python_try_except.md](36_python_try_except.md)
- [37_python_exceptions.md](37_python_exceptions.md)
- [22_python_constructors.md](../05_oop/22_python_constructors.md)

## Challenges
- **Blank 1**: Write `raise _____(f"Too short: '{tag}'")` — what exception class is appropriate for a bad value?
- **Blank 2**: Define `class GamertagError(_____):` — what built-in class does it inherit from? Then define `class GamertagTooShortError(_____)` — what class does IT inherit from?
- **Blank 3**: Inside `GamertagTooShortError.__init__`, call the parent constructor: `super().__init__(f"_____ is too short")`. Write a useful message that includes the tag and its length.
- **Challenge**: The C# project uses `throw new ArgumentException(...)`. Python uses `raise ValueError(...)`. Create a mini test: write `validate_gamertag("AB")` and catch it with `except GamertagTooShortError`. Then catch the same call with just `except GamertagError`. Does `GamertagError` catch `GamertagTooShortError`? Why? What does this tell you about exception inheritance?
