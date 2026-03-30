# Python If / Else

**W3Schools Links:**
- [Python If...Else](https://www.w3schools.com/python/python_conditions.asp) — `if`, `elif`, `else`, ternary expressions
- [Python Operators](https://www.w3schools.com/python/python_operators.asp) — `not` (replaces C#'s `!`), `and`/`or`, comparison operators
- [Python For Loops](https://www.w3schools.com/python/python_for_loops.asp) — `for` loop used inside all filter function examples
- [Python String Methods](https://www.w3schools.com/python/python_ref_string.asp) — `.isdigit()`, `.isalnum()` used in gamertag filter exercises
- [Python Booleans](https://www.w3schools.com/python/python_booleans.asp) — truthy/falsy values used in conditions

**Homework Day(s):** Day 2, Day 11, Day 12

---

## Overview
Conditional statements allow your program to make decisions and execute different code paths based on whether conditions are true or false. Python uses `if`, `elif` (else if), and `else` to build branching logic. Proper use of conditionals is at the heart of any program that validates input, filters data, or responds to user choices.

## Key Concepts
- **`if`**: executes a block when the condition is `True`
- **`elif`**: checks an additional condition if the previous was `False`
- **`else`**: executes when all previous conditions were `False`
- **Indentation is mandatory**: the body of each clause must be indented 4 spaces
- **Short-circuit evaluation**: Python stops checking `and`/`or` as soon as the result is known
- **Ternary (one-liner)**: `value = x if condition else y`
- **Nested if**: you can nest `if` statements, but keep nesting shallow for readability

## Syntax / Example Code

**C# pattern (from the gamertag project):**
```csharp
// C# gamertag methods use character checks inside conditionals
public void PrintGamertagsEndingWithNumber()
{
    foreach (string s in gamerTagList)
        if (Char.IsNumber(s, s.Length - 1))
            Console.WriteLine(s);
}

public void PrintGamertagsNotStartingWithNumberorLetter()
{
    foreach (string s in gamerTagList)
        if (!Char.IsLetterOrDigit(s, 0))
            Console.WriteLine(s);
}
```

**Python skeleton (fill in the blanks):**
```
# Python: if / elif / else — no braces, uses indentation

# Replicating PrintGamertagsEndingWithNumber:
def print_gamertags_ending_with_number(gamer_tag_list):
    for s in _____:
        if s[_____]._____(  ):     # check the LAST character
            print(_____)

# Replicating PrintGamertagsNotStartingWithNumberorLetter:
def print_gamertags_not_starting_with_letter_or_digit(gamer_tag_list):
    for s in _____:
        if _____ s[_____]._____(  ):    # NOT starting with letter or digit
            print(_____)

# General if/elif/else for score ranking
score = 4250
if score _____ 5000:
    print("Rank: Diamond")
_____ score _____ 3000:
    print("Rank: Gold")
_____ score _____ 1000:
    print("Rank: Silver")
_____:
    print("Rank: Bronze")

# Ternary (one-liner if/else)
status = _____ if score > 0 _____ _____
```

**Questions:**
- C# uses `Char.IsNumber(s, s.Length - 1)` to check the last character. In Python, what index gives you the last character? What method on a single character checks if it is a digit?
- C# uses `!Char.IsLetterOrDigit(s, 0)`. What Python keyword replaces `!`? What method replaces `IsLetterOrDigit`?
- C# uses `else if`. What is the Python keyword for the same thing?
- In C#, `if` blocks use `{ }`. What does Python use instead to define the block body?

**Test challenge:**
Write a Python function that loops through a list of gamertags and prints only those that end with a digit — replicating `PrintGamertagsEndingWithNumber`. Test it with at least 5 gamertags, some ending in digits and some not.

## Common Use Cases
- Validating gamertag input before saving to file
- Routing program flow based on user menu selections
- Filtering player records by platform or score range
- Assigning rank labels based on score thresholds

## Related Days
| Day | Topic |
|-----|-------|
| Day 2 | Conditions and Decisions (if/elif/else, boolean, comparisons) |
| Day 11 | Filter 1 (Ending with Number) |
| Day 12 | Filter 2 (Not Starting with Letter or Number) |

## See Also
- [10_python_booleans.md](../02_data_types/10_python_booleans.md)
- [16_python_operators.md](16_python_operators.md)
- [34_python_string_validation.md](../07_strings/34_python_string_validation.md)

## Challenges

1. **Translate the C# filter:** `PrintGamertagsEndingWithNumber` prints tags whose last character is a digit. Fill in Python:
   ```
   for s in gamer_tag_list:
       if s[_____]._____(  ):    # last char is a digit?
           print(_____)
   ```

2. **Translate the NOT check:** `PrintGamertagsNotStartingWithNumberorLetter` uses `!Char.IsLetterOrDigit(s, 0)`. Fill in Python:
   ```
   for s in gamer_tag_list:
       if _____ s[_____]._____(  ):    # NOT a letter or digit at position 0?
           print(_____)
   ```

3. **elif chain:** Write an `if/elif/else` block that assigns a rank label based on a score:
   - 5000+ → `"Diamond"`, 3000–4999 → `"Gold"`, 1000–2999 → `"Silver"`, below 1000 → `"Bronze"`
   ```
   if score _____ _____:
       rank = _____
   _____ score _____ _____:
       rank = _____
   ...
   ```

4. **Ternary shortcut:** Rewrite this as a one-line ternary expression:
   ```
   if is_running:
       label = "Active"
   else:
       label = "Stopped"
   ```
   ```
   label = _____ if _____ else _____
   ```
