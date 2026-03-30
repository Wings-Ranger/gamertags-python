# Two-Week Python Homework Plan (Porting Your Gamertag Project)

## How to Use This Plan
- Study for 60 to 90 minutes each day
- Keep notes of what you learned and what confused you
- At the end of each day, write a short reflection:
  - What did I understand?
  - What still feels hard?
  - What will I revise tomorrow?
- Do not move on until you can explain the topic in your own words

## Success Target by Day 14
By the end of two weeks, you should be able to rebuild your C# gamertag app in Python with the same behavior, without copying code from tutorials.

## Week 1: Core Python Skills

### Day 1: Python Foundations
Focus:
- How Python runs scripts
- Variables and basic data types
- Strings and lists

Homework tasks:
- Set up your Python environment
- Create a personal glossary for key terms (variable, list, function, class, loop, condition)
- Write plain-language notes comparing C# basics to Python basics

**Vocabulary Challenge — Day 1**
Write your own definition for each of these six terms. Do not copy from a tutorial — use your own words after reading about each one.

| Term | Your Definition (fill this in) |
|---|---|
| variable | |
| list | |
| function | |
| class | |
| loop | |
| condition | |

After writing your definitions, answer: Which of these six things exist in your C# gamertag project? Give one concrete example from the C# code for each term you identify.

Checkpoint:
- You can explain how Python stores and uses text and lists

### Day 2: Conditions and Decisions
Focus:
- if / elif / else logic
- Boolean thinking
- Comparing values

Homework tasks:
- Practice turning plain English rules into condition logic
- Write decision tables for your gamertag rules

**Decision Table Challenge — Day 2**
Complete the table below for each gamertag filter. Do not write Python code — describe the rules in plain English and test cases only.

**Filter 1: Gamertags ending with a number**

| Column | Your Answer |
|---|---|
| Rule in plain English | A gamertag should appear in this list when... |
| What C# checks first (before the character test) | |
| What C# checks about the last character | `Char.IsNumber(s, s.Length - 1)` — what does this do in plain English? |
| Python approach (name the method, do not write code) | |
| Example gamertags that PASS this filter | (write at least 3) |
| Example gamertags that FAIL this filter | (write at least 3) |
| Edge cases to test | (empty string? single digit? whitespace?) |

**Filter 2: Gamertags not starting with a letter or digit**

| Column | Your Answer |
|---|---|
| Rule in plain English | A gamertag should appear in this list when... |
| What C# checks first | |
| What C# checks about the first character | `!Char.IsLetterOrDigit(s, 0)` — what does the `!` do? |
| Python approach (name the method, do not write code) | |
| Example gamertags that PASS this filter | (write at least 3 — think symbols: `#`, `@`, `_`, `!`) |
| Example gamertags that FAIL this filter | (write at least 3) |
| Edge cases to test | |

Checkpoint:
- You can explain exactly when a gamertag should be shown in each filter

### Day 3: Loops and Program Flow
Focus:
- while loops and loop control
- Iterating through lists
- Stopping conditions

Homework tasks:
- Map your C# main loop to Python flow in plain language
- Describe how the run-again prompt should control the loop

**Main Loop Pseudocode Challenge — Day 3**
Below is the `Program.cs` logic written as plain pseudocode. Translate each line into Python — but only attempt the lines you already understand. Mark anything you cannot yet translate with `# TODO: research this`.

```
PROGRAM START

  SET is_running TO true

  REPEAT WHILE is_running IS true:

    CREATE a new Gamertags object

    TELL the object: load gamertags from the file
    TELL the object: show the welcome message
    TELL the object: print all gamertags
    TELL the object: print gamertags ending with a number
    TELL the object: print gamertags not starting with letter or digit
    TELL the object: handle adding a new username

    DISPLAY "Would you like to view the gamertags again (y/n)?"
    READ a single input from the user

    IF input equals "y" or "Y":
      SET is_running TO true
    OTHERWISE:
      SET is_running TO false

  END REPEAT

PROGRAM END
```

**Questions to answer before translating:**
1. Where in a Python file does the "main" execution start? (Research `if __name__ == "__main__":`)
2. C# uses `Console.ReadKey()` to read one keypress. Python's `input()` waits for Enter. How will you adapt the y/n prompt?
3. In C#, `new Gamertags()` creates an object. What is the Python syntax to create an object from a class?

Checkpoint:
- You can describe the full app flow from start to finish without looking at C#

### Revision Checkpoint (End of Day 3)
- What is working:
- What needs review:
- Confidence (1-5):

### Day 4: Functions
Focus:
- Function purpose and decomposition
- Inputs and outputs
- Naming and single responsibility

Homework tasks:
- Break your app into small function-sized responsibilities
- Write a function list for each app behavior

**C# Method Signature Challenge — Day 4**
Below are the six C# method signatures from `Gamertags.cs`. For each one, complete the three columns. Do not write the method body — just plan the interface.

| C# Method Signature | What it does (plain English) | Python `def` line (signature only, body blank) |
|---|---|---|
| `public void LoadGamertags()` | | |
| `public void PrintAllGamertags()` | | |
| `public void PrintGamertagsEndingWithNumber()` | | |
| `public void PrintGamertagsNotStartingWithNumberorLetter()` | | |
| `public void ShowWelcomeMessage()` | | |
| `public void AddNewUserName()` | | |

**Follow-up questions:**
1. All C# methods use `public void` — they take no parameters and return nothing. Will your Python methods need any parameters? Think about where `gamerTagList` lives in C# versus where it will live in Python.
2. In Python, every method in a class requires a specific first parameter. What is it, and what does it give you access to?
3. The C# class stores `gamerTagList` as a field. Where and how will you store this list in your Python class?

Checkpoint:
- You have a clean function plan for loading, displaying, filtering, adding, and repeating

### Day 5: File Handling
Focus:
- Reading text files
- Appending to files
- Paths and file locations

Homework tasks:
- Decide exactly where your gamertag text file should live
- Document what should happen if the file is missing or empty

**C# File Operations Challenge — Day 5**
Here are the two C# file operations used in the gamertag app:

```csharp
// In LoadGamertags() — reads the entire file into an array of strings:
gamerTagList = File.ReadAllLines("../Gamertags.txt");

// In AddNewUserName() — appends text to the file without overwriting:
File.AppendAllText("../Gamertags.txt", "\n" + newGamerTag);
```

**Research and answer these questions (no code yet):**

| Question | Your Answer |
|---|---|
| What Python function opens a file? | |
| What modes can you open a file in? (list at least three) | |
| Which mode is equivalent to `ReadAllLines` (read only)? | |
| Which mode is equivalent to `AppendAllText` (add without overwriting)? | |
| What Python method reads all lines from an open file into a list? | |
| What does Python's file `readlines()` include at the end of each line that `File.ReadAllLines()` does not? | |
| The C# path is `"../Gamertags.txt"` (relative, one folder up). How do you handle relative paths safely in Python? | |
| What exception does Python raise if you try to read a file that does not exist? | |
| What Python keyword pair ensures a file is closed even if an error occurs? | |

Checkpoint:
- You can explain safe file read/write behavior and error cases

### Day 6: String and Character Validation
Focus:
- Empty-string safety
- First/last character checks
- Number and letter-or-digit checks

Homework tasks:
- Write plain-language validation rules for each filter
- List edge cases (empty line, symbol-first, number-ending, whitespace-only)

**C# Filter Condition Translation Challenge — Day 6**
Below are the two filter conditions directly from the C# source code. Translate each condition into plain English first, then identify the Python building blocks — but do not write the complete Python code.

**Filter 1 — Gamertags ending with a number:**
```csharp
if ((s.Length > 0) && Char.IsNumber(s, s.Length - 1))
```

| Part of the condition | What it does in plain English | Python building block to use |
|---|---|---|
| `s.Length > 0` | | (name the function) |
| `s.Length - 1` (as an index) | | (how do you access the last character in Python without knowing length?) |
| `Char.IsNumber(s, s.Length - 1)` | | (name the string method) |
| `&&` operator | | (what is the Python keyword?) |

**Filter 2 — Gamertags not starting with a letter or digit:**
```csharp
if ((s.Length > 0) && !Char.IsLetterOrDigit(s, 0))
```

| Part of the condition | What it does in plain English | Python building block to use |
|---|---|---|
| `s.Length > 0` | | |
| `s[0]` (index 0) | | (how do you get the first character in Python?) |
| `Char.IsLetterOrDigit(s, 0)` | | (name the string method) |
| `!` operator | | (what is the Python keyword?) |

**Edge case table — fill in the expected result for each filter:**

| Gamertag | Ends with number? | NOT starts with letter/digit? |
|---|---|---|
| `Xander99` | | |
| `99Xander` | | |
| `#shadow` | | |
| `ghost` | | |
| `` (empty string) | | |
| `7` | | |
| `@7` | | |

Checkpoint:
- You can confidently explain all filter rules and edge cases

### Day 7: Mini Review Day
Focus:
- Consolidation and weak spots

Homework tasks:
- Review your notes from days 1 to 6
- Rewrite confusing notes in simpler words
- Attempt a paper walkthrough of the full app behavior

**Paper Walkthrough Template — Day 7**
Use this sample gamertag list to trace through the program by hand. Write the expected output for each method in the "Expected Output" column — no code required.

Sample gamertag list (pretend this is loaded from the file):
```
DragonSlayer
xXNightOwlXx
Blaze99
#ShadowKing
ProGamer2024
@CoolCat
!!Destroyer
Falcon
7thLegend
```

| Method called | Expected output (write it out by hand) |
|---|---|
| `show_welcome_message()` | |
| `print_all_gamertags()` | (numbered list — what are the numbers and names?) |
| `print_gamertags_ending_with_number()` | (which ones qualify? why?) |
| `print_gamertags_not_starting_with_letter_or_digit()` | (which ones qualify? why?) |

**Follow-up checks:**
- Does `7thLegend` end with a number? (Careful — check the *last* character, not the first.)
- Does `Blaze99` start with a letter or digit?
- Does `!!Destroyer` start with a letter or digit?
- How many items appear in `print_all_gamertags()`?
- After `add_new_username()` adds `"Zephyr"`, how many items should appear on the next run?

Checkpoint:
- You can teach the project logic to someone else without showing code

### Revision Checkpoint (End of Day 7)
- What is working:
- What needs review:
- Confidence (1-5):

## Week 2: Build, Verify, and Improve

### Day 8: Python Project Skeleton
Focus:
- Project organization
- Planning class and method structure

Homework tasks:
- Create your Python project folder structure
- Plan where each responsibility lives
- Confirm naming consistency

**Day 8 Challenge: Project Skeleton Planning**
Before writing any code, answer these planning questions:

1. The C# class is called `Gamertags`. What will you name your Python class? (Python convention: `CapWords` — what does that look like here?)
2. The C# uses `gamerTagList` (camelCase). Python uses `snake_case`. What would `gamerTagList` become?
3. The C# method `PrintAllGamertags` (PascalCase) becomes what in Python's `snake_case` convention?
4. Convert all six C# method names to Python `snake_case`:
   - `LoadGamertags` → `_____`
   - `PrintAllGamertags` → `_____`
   - `PrintGamertagsEndingWithNumber` → `_____`
   - `PrintGamertagsNotStartingWithNumberorLetter` → `_____`
   - `ShowWelcomeMessage` → `_____`
   - `AddNewUserName` → `_____`
5. Sketch your file structure: what is the Python file called? Where does `Gamertags.txt` sit relative to it?

Checkpoint:
- Your project structure is clear and maintainable

### Day 9: Data Loading and Welcome Sequence
Focus:
- Initial startup behavior

Homework tasks:
- Implement and verify startup sequence behavior
- Confirm data loads correctly before processing

**Day 9 Challenge: Load and Welcome**
You are implementing `load_gamertags()` and `show_welcome_message()` today. Before writing, answer:

1. The C# `__init__`-equivalent sets `gamerTagList = { }` (empty array). What should your Python `__init__` set `self.gamer_tag_list` to? (An empty list or something else?)
2. In `load_gamertags()`, after reading the file, lines may have a trailing newline character (`\n`). Which string method removes whitespace from the ends of a string? Should you apply it to each line?
3. The C# path `"../Gamertags.txt"` goes one folder up. In Python, how do you construct a path relative to the script's location rather than where the script is *run from*? (Research `__file__` and `os.path`.)
4. What should happen if `Gamertags.txt` does not exist yet? Write a plain-English error-handling plan — no code.

Checkpoint:
- Program starts cleanly and loads data every run

### Day 10: Display All Gamertags
Focus:
- Iteration and numbering output

Homework tasks:
- Implement full listing behavior
- Verify numbering and output readability

**Day 10 Challenge: Print All Gamertags**
You are implementing `print_all_gamertags()` today. Answer before writing the body:

1. The C# version uses a manual counter: `int lineNumber = 1;` then `lineNumber = lineNumber + 1`. What Python built-in function lets you get both the index and the item in a loop — without a manual counter?
2. The C# output format is `"1) DragonSlayer"`. Using Python string formatting, how would you describe this format? (The number, a closing parenthesis, a space, then the name.)
3. The C# ends with `Console.ReadKey()` — waits for a keypress. How will your Python version pause and wait? What prompt text will you show?
4. Skeleton check — your method body should follow this shape:
   ```
   def print_all_gamertags(self):
       # clear the screen (or print blank lines)
       # print the header separator
       # print "All Gamertags"
       # print the header separator
       # TODO: loop with numbering — use _____ to get index and item
       # print the footer separator
       # TODO: pause — use _____ to wait for user
   ```
   Fill in the two blanks above.

Checkpoint:
- All gamertags display in expected order with expected numbering

### Revision Checkpoint (End of Day 10)
- What is working:
- What needs review:
- Confidence (1-5):

### Day 11: Filter 1 (Ending with Number)
Focus:
- Character-based filtering logic

Homework tasks:
- Implement number-ending filter
- Test with multiple valid and invalid examples

**Day 11 Challenge: Filter — Ending with Number**
You are implementing the number-ending filter today. Before writing, complete this:

1. The C# filter condition is:
   ```csharp
   (s.Length > 0) && Char.IsNumber(s, s.Length - 1)
   ```
   Write this as a plain English sentence: "Include this gamertag if _____ AND _____."

2. The last character in C# is accessed with index `s.Length - 1`. In Python, what shorthand index gives you the last character without needing `len()`?

3. `Char.IsNumber` checks a single character. In Python, you call a method directly on a one-character string. What is that method's name?

4. Write a skeleton for the filter condition only (not the full method) — use underscores for the parts you still need to research:
   ```
   if len(s) > _____ and s[_____]._____(  ):
   ```

5. Test your logic mentally against these gamertags before running any code:
   - `Blaze99` — does it qualify? Which character is checked?
   - `9Lives` — does it qualify? Which character is checked?
   - `Falcon` — does it qualify?
   - `7` — does it qualify?

Checkpoint:
- Only correct gamertags are shown for this rule

### Day 12: Filter 2 (Not Starting with Letter or Number)
Focus:
- Start-character classification

Homework tasks:
- Implement second filter
- Test symbol-leading and edge cases

**Day 12 Challenge: Filter — Not Starting with Letter or Digit**
You are implementing the second filter today. The C# condition is:
```csharp
(s.Length > 0) && !Char.IsLetterOrDigit(s, 0)
```

1. Translate this into a plain English rule: "Include this gamertag if _____ AND _____."

2. `Char.IsLetterOrDigit(s, 0)` checks the first character. In Python, you call a method on a one-character string. What is the Python method that checks if a character is a letter *or* a digit?

3. The `!` (NOT) in C# inverts a boolean. In Python, what keyword does the same thing?

4. Fill in the blanks for the filter condition skeleton:
   ```
   if len(s) > _____ and not s[_____]._____(  ):
   ```

5. Verify your understanding against these gamertags:
   - `#ShadowKing` — qualifies? What is the first character?
   - `@CoolCat` — qualifies?
   - `!!Destroyer` — qualifies?
   - `Xander99` — qualifies? Why not?
   - `99Xander` — qualifies? Why not?
   - `` (empty string) — what does the length check prevent?

6. Both filters share a common structure (length check + character check). After implementing both, look at your two methods. Could any part be extracted into a shared helper? (You do not have to do this yet — just think about it.)

Checkpoint:
- Filter output exactly matches rule definition

### Day 13: Add New Gamertag + Run-Again Loop
Focus:
- User input and persistence

Homework tasks:
- Implement add-new behavior
- Verify write-to-file and reload behavior
- Confirm run-again prompt loops correctly

**Day 13 Challenge: Add New Gamertag and Run-Again Loop**
You are implementing `add_new_username()` and the main loop's run-again prompt today.

**For `add_new_username()`:**
1. The C# writes `"\n" + newGamerTag` to the file. What does the `\n` do, and why is it written *before* the new gamertag rather than after?
2. After appending, C# calls `LoadGamertags()` again. Why is this necessary? What would happen if you skipped it?
3. What Python file mode do you pass to `open()` to append without overwriting the existing content?
4. The C# checks `if (newGamerTag.Length > 0)` before writing. In Python, what check would you use? (Hint: an empty string is "falsy" in Python — research this.)

**For the run-again loop:**
1. In C#, `Console.ReadKey().Key == ConsoleKey.Y` captures a single keypress. Python's `input()` returns a full string after Enter is pressed. How will you compare the user's response to `"y"` while being case-insensitive?
2. Write the run-again logic in pseudocode (not Python) before translating it:
   ```
   ASK "Would you like to view the gamertags again (y/n)?"
   GET user_response
   IF user_response is "y" (case-insensitive):
       SET is_running TO _____
   ELSE:
       SET is_running TO _____
   ```
3. Fill in the two blanks.

Checkpoint:
- New entries persist and appear on the next display cycle

### Day 14: Final Test and Submission Prep
Focus:
- Stability and confidence

Homework tasks:
- Run a complete end-to-end test several times
- Test error scenarios (empty input, missing file, unexpected characters)
- Clean up naming, comments, and structure
- Prepare a short written reflection on what you learned

**Day 14 Challenge: Final Verification Checklist**
Work through each check systematically. For any failure, describe the bug in plain English and how you fixed it.

| Feature to test | Test steps | Pass/Fail | Bug description (if failed) | Fix applied |
|---|---|---|---|---|
| Program starts without errors | Run from the command line | | | |
| File loads successfully | Check that gamertags print on first run | | | |
| All gamertags display with correct numbering | Count the items against the file | | | |
| Ending-with-number filter is correct | Check each result against your Day 7 walkthrough | | | |
| Not-starting-with-letter-or-digit filter is correct | Check each result against your Day 7 walkthrough | | | |
| Adding a blank gamertag does nothing | Press Enter without typing anything | | | |
| Adding a gamertag saves it | Add one, run again, verify it appears | | | |
| Run-again "y" loops correctly | Type y and verify the sequence restarts | | | |
| Run-again "n" exits cleanly | Type n and verify the program ends | | | |
| Missing file is handled gracefully | Temporarily rename the file and run | | | |
| Empty gamertag list is handled | Clear the file contents and run | | | |

**Reflection questions (write your answers in your notes):**
1. What was the hardest single concept to translate from C# to Python?
2. What Python feature made something *easier* than the C# equivalent?
3. If you were starting this project from scratch, what would you plan differently?
4. What topic from this two-week plan do you still feel uncertain about?

Checkpoint:
- Your Python version is feature-complete and reliable

### Revision Checkpoint (End of Day 14)
- What is working:
- What needs review:
- Confidence (1-5):

## Daily Reflection Template
- Today I learned:
- I still find this difficult:
- I solved this problem by:
- Tomorrow I will focus on:

## Risk Management (If You Fall Behind)
If you miss a day:
1. Combine two lighter theory days into one session
2. Keep implementation days (Day 10 to Day 14) in order
3. Prioritize core behavior over optional improvements

## Final Submission Checklist
- Project runs without manual fixes
- All original C# features are present
- File reading and writing work consistently
- Filters handle edge cases safely
- App loop and user prompt behave correctly
- Notes/reflection are complete and understandable
