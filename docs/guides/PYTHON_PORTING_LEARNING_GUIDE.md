# Python Learning Guide for Porting This Project

## Goal
Move the current C# console gamertag program into Python while keeping the same behavior:
- Load gamertags from a text file
- Display all gamertags
- Filter gamertags by specific character rules
- Add a new gamertag to the file
- Ask whether to run again

## Before You Submit (Quick Checklist)
- [ ] Python app runs from start to finish without manual fixes
- [ ] All original C# features are present in the Python version
- [ ] File reading and writing are reliable
- [ ] Filters handle normal and edge-case input correctly
- [ ] User prompts and run-again loop work correctly
- [ ] You completed your reflection notes

## What This C# Project Is Teaching You
Your current program is a strong beginner structure. It uses:
- Program flow control (main loop and user decisions)
- A class to group related behavior
- File input and output
- String and character validation
- Console interaction

To port it confidently, you need to learn the Python version of each of those ideas.

## Python Topics You Need to Learn

### 1. Python Program Structure
Learn how a Python script starts and how to organise execution flow.
- Script entry point conventions
- Keeping the main loop readable
- Separating setup, processing, and user prompts

### 2. Variables and Core Data Types
Your C# app uses arrays and strings heavily.
- Strings and list types
- Boolean values for run-state control
- None/empty value handling for user input

### 3. Control Flow
Your C# loop and conditionals are central to the program.
- while loops
- if/else decision logic
- Loop termination based on user response

### 4. Functions and Methods
Your C# class methods become Python methods or standalone functions.
- Function definition and parameters
- Returning values from functions
- Breaking tasks into small callable units

### 5. Classes and Object-Oriented Basics
You currently have a Gamertags class that owns data and behavior.
- Creating classes in Python
- Instance attributes (for storing the gamertag list)
- Method naming and responsibilities
- Constructor basics for setup

### 6. File Handling
You read all lines and append new data.
- Opening and reading text files safely
- Appending new lines correctly
- Relative vs absolute file paths
- Character encoding basics
- Ensuring file location works when running from different folders

### 7. String Validation and Character Checks
Your filters depend on character tests.
- Checking string length before indexing
- Getting first and last characters safely
- Determining whether a character is numeric
- Determining whether a character is letter or digit
- Handling unusual or empty input robustly

### 8. Console Input and Output
Your app is interactive and menu-like.
- Reading user input as text
- Normalising input (upper/lower case, trimming spaces)
- Pausing between screens and presenting clear headings

### 9. Error Handling
Python programs should fail gracefully around user input and files.
- Handling missing files
- Handling permission issues when writing
- Handling unexpected empty input
- Giving useful messages and allowing retry

### 10. Basic Testing Mindset
Before calling the port complete, verify behavior is unchanged.
- Check each feature one by one
- Test edge cases (empty line, symbol-first tag, number-ending tag)
- Test repeated runs and file updates

## Concept Mapping: C# to Python

Use this table to guide your research. The third column names the Python approach — it does **not** show working code. Look up each item using the links in [../references/W3SCHOOLS_PYTHON_REFERENCES.md](../references/W3SCHOOLS_PYTHON_REFERENCES.md) and work out the syntax yourself.

| C# Construct | C# Example from Gamertag Code | Python Equivalent Approach | What to Research |
|---|---|---|---|
| `string[]` fixed-size array | `private string[] gamerTagList = { };` | Python `list` (no fixed size needed) | Python Lists |
| `foreach` loop | `foreach (string s in gamerTagList)` | Python `for item in my_list:` | Python For Loops |
| `Char.IsNumber(s, index)` | `Char.IsNumber(s, s.Length - 1)` | Call a string method on a single-character substring | `str.isdigit()` |
| `Char.IsLetterOrDigit(s, index)` | `Char.IsLetterOrDigit(s, 0)` | Call a string method on a single-character substring | `str.isalnum()` |
| `s.Length` property | `s.Length > 0` | Python built-in `len()` function | Python `len()` |
| Array index access | `s[s.Length - 1]` (last character) | Python negative index or slicing | Python String Slicing |
| `File.ReadAllLines(path)` | `gamerTagList = File.ReadAllLines("../Gamertags.txt")` | Python `open()` + reading all lines into a list | Python File Read |
| `File.AppendAllText(path, text)` | `File.AppendAllText("../Gamertags.txt", "\n" + newGamerTag)` | Python `open()` with append mode | Python File Write |
| `Console.WriteLine(text)` | `Console.WriteLine("All Gamertags")` | Python `print()` | Python `print()` |
| `Console.ReadLine()` | `string newGamerTag = Console.ReadLine()` | Python `input()` | Python User Input |
| `Console.ReadKey()` (pause) | `Console.ReadKey();` at end of each method | Python `input()` with a prompt string | Python User Input |
| Manual counter `int lineNumber = 1;` | Increment counter inside `foreach` | Python `enumerate()` with a start value | Python For Loops / enumerate |
| `lineNumber.ToString() + ") " + s` | Number-and-string concatenation | Python f-string or `str()` conversion | Python String Formatting |
| `bool isRunning = true;` | `bool isRunning = true;` in `Main` | Python boolean variable controlling a `while` | Python Booleans, Python While Loops |
| `internal class Gamertags { }` | The entire `Gamertags` class | Python `class Gamertags:` | Python Classes |
| No explicit constructor shown | Default constructor (implicit in C#) | Python `def __init__(self):` with `self.gamer_tag_list = []` | Python `__init__` |
| `public void MethodName()` | `public void LoadGamertags()` | Python `def method_name(self):` | Python Class Methods |
| `!` logical NOT | `!Char.IsLetterOrDigit(s, 0)` | Python `not` keyword | Python Operators |

## C# Method Challenges

For each C# method below, answer the four analysis questions **before** you write any Python. The goal is to understand first and code second.

---

### Method 1: `LoadGamertags()`

```csharp
public void LoadGamertags()
{
    gamerTagList = File.ReadAllLines("../Gamertags.txt");
}
```

**Your tasks:**
1. In plain English, what does this method do? (One or two sentences, no code words.)
2. Does it take any parameters? Does it return anything? What does it update instead?
3. Write only the Python `def` line for the equivalent method. Leave the body completely blank for now.
4. In plain English, describe every step that needs to happen inside this method. Think about: opening a file, reading lines, storing results, and what happens if the file does not exist.

---

### Method 2: `PrintAllGamertags()`

```csharp
public void PrintAllGamertags()
{
    Console.Clear();
    Console.WriteLine("===================");
    Console.WriteLine("All Gamertags");
    Console.WriteLine("===================");
    int lineNumber = 1;
    foreach (string s in gamerTagList)
    {
        Console.WriteLine(lineNumber.ToString() + ") " + s);
        lineNumber = lineNumber + 1;
    }
    Console.WriteLine("===================");
    Console.WriteLine("Press any key to continue");
    Console.ReadKey();
}
```

**Your tasks:**
1. In plain English, what does this method do?
2. What data does it read from? Where does that data live?
3. Write only the Python `def` line. What parameter(s) does it need?
4. In plain English, list every action that must happen inside this method in order. Pay attention to the numbering: how does the C# version count lines? Is there a Python way to do this without a manual counter?

---

### Method 3: `PrintGamertagsEndingWithNumber()`

```csharp
public void PrintGamertagsEndingWithNumber()
{
    Console.Clear();
    // ... header output ...
    int lineNumber = 1;
    foreach (string s in gamerTagList)
    {
        if ((s.Length > 0) && Char.IsNumber(s, s.Length - 1))
        {
            Console.WriteLine(lineNumber.ToString() + " ) " + s);
            lineNumber = lineNumber + 1;
        }
    }
    // ... footer and pause ...
}
```

**Your tasks:**
1. In plain English, what rule decides whether a gamertag is printed?
2. Why does the code check `s.Length > 0` before checking the last character? What would go wrong without it?
3. Write only the Python `def` line.
4. Describe the filter condition in plain English. What Python string method could replace `Char.IsNumber`? How do you get the last character of a string in Python without knowing its length?

---

### Method 4: `PrintGamertagsNotStartingWithNumberorLetter()`

```csharp
public void PrintGamertagsNotStartingWithNumberorLetter()
{
    // ...
    foreach (string s in gamerTagList)
    {
        if ((s.Length > 0) && !Char.IsLetterOrDigit(s, 0))
        {
            Console.WriteLine(lineNumber.ToString() + " ) " + s);
            lineNumber = lineNumber + 1;
        }
    }
    // ...
}
```

**Your tasks:**
1. What exactly makes a gamertag qualify for this filter? Give two example gamertags that pass and two that fail.
2. The condition uses `!` (logical NOT). In Python, what keyword replaces `!`?
3. Write only the Python `def` line.
4. Describe the complete filter condition in plain English. Which Python string method corresponds to `Char.IsLetterOrDigit`? How do you get the first character of a string?

---

### Method 5: `ShowWelcomeMessage()`

```csharp
public void ShowWelcomeMessage()
{
    Console.Clear();
    Console.WriteLine("===================");
    Console.WriteLine("Welcome to the gamertag program");
    Console.WriteLine("*** Program sequence output - display gamertags etc ***");
    Console.WriteLine("===================");
    Console.WriteLine("Press any key to continue");
    Console.ReadKey();
}
```

**Your tasks:**
1. What is the sole responsibility of this method?
2. Write only the Python `def` line.
3. Python does not have a direct `Console.Clear()` equivalent built into the language the same way. How would you research finding a cross-platform screen-clear approach in Python? What module might be involved?

---

### Method 6: `AddNewUserName()`

```csharp
public void AddNewUserName()
{
    Console.Clear();
    Console.WriteLine("===================");
    Console.WriteLine("Add new GamerTag");
    Console.WriteLine("===================");
    Console.WriteLine("Please add a new Gamertag. Don't enter anything to cancel");
    string newGamerTag = Console.ReadLine();
    if (newGamerTag.Length > 0)
    {
        File.AppendAllText("../Gamertags.txt", "\n" + newGamerTag);
        LoadGamertags();
    }
}
```

**Your tasks:**
1. In plain English, what are the two possible outcomes of this method?
2. What does it mean to "cancel" here, and how does the code detect that?
3. Write only the Python `def` line.
4. Describe every step in order: prompt, read, check, write, reload. For the write step, describe how the newline character is added and why that matters. What Python file mode do you need for appending?

---

## Main Loop Pseudocode Challenge

The following is the `Program.cs` main loop written as **pseudocode** — plain logic with no Python syntax. Your challenge is to translate this pseudocode into real Python code yourself, after studying the relevant topics.

```
PROGRAM START

  SET is_running TO true

  REPEAT WHILE is_running IS true:

    CREATE a new Gamertags object

    TELL the object: load gamertags from the file

    TELL the object: show the welcome message

    TELL the object: print all gamertags

    TELL the object: print gamertags that end with a number

    TELL the object: print gamertags not starting with a letter or digit

    TELL the object: handle adding a new username

    DISPLAY: "Would you like to view the gamertags again (y/n)?"

    READ a single character of input from the user

    IF the input equals "y" or "Y":
      SET is_running TO true
    OTHERWISE:
      SET is_running TO false

  END REPEAT

PROGRAM END
```

**Questions to answer before writing code:**
1. In C#, the `Gamertags` object is created inside the loop. What effect does that have on the program state each iteration? Will you replicate this in Python, or is there a reason to create it outside the loop?
2. In C#, `Console.ReadKey().Key == ConsoleKey.Y` reads a single keystroke without pressing Enter. Python's `input()` always waits for Enter. How will you handle the "y/n?" prompt differently?
3. What Python syntax do you use to create an object from a class?
4. What Python syntax do you use to call a method on an object?
5. Where does the main loop code belong in your Python file? (Hint: research the `if __name__ == "__main__":` pattern.)

---

## Recommended Learning Order
Follow this order so each topic supports the next one.
1. Python basics: variables, strings, lists, conditionals, loops
2. Functions and simple decomposition
3. File reading and writing with text files
4. String character checking and input validation
5. Classes and methods
6. Building an interactive console flow
7. Error handling and edge-case testing

## Porting Checklist (No Code)
Use this checklist while rebuilding.
- Create the Python project folder and decide where the gamertag text file will live
- Recreate the data container for gamertags
- Recreate the load-from-file behavior
- Recreate the welcome output
- Recreate print-all behavior with numbering
- Recreate print-ending-with-number filter
- Recreate print-not-starting-with-letter-or-digit filter
- Recreate add-new-gamertag behavior
- Recreate run-again prompt
- Verify saved file updates appear on next run

## Common Pitfalls to Avoid
- Assuming working directory is always the same
- Not handling missing files before reading
- Forgetting to strip user input before validation
- Breaking on empty strings when checking first/last characters
- Mixing responsibilities in one large function
- Skipping edge-case tests

## Suggested Outcome Standard
You are ready when your Python version can:
- Perform all the same user-visible features as the C# version
- Handle empty or unusual input safely
- Read and update the gamertag file reliably
- Be understood quickly by another beginner reading your file

## Optional Next Skills After Porting
Once the direct port works, your next improvements can be:
- Add a simple menu instead of a fixed sequence
- Add duplicate-name checks
- Add basic logging to a text file
- Add automated tests for filtering rules
- Package it as a small command-line utility
