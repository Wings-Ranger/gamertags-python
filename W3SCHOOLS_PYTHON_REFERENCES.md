# W3Schools Python Reference Links

Curated W3Schools links covering every Python topic mentioned in the learning documents for this project.
Use these alongside [PYTHON_PORTING_LEARNING_GUIDE.md](PYTHON_PORTING_LEARNING_GUIDE.md) and [TWO_WEEK_PYTHON_HOMEWORK_PLAN.md](TWO_WEEK_PYTHON_HOMEWORK_PLAN.md).

---

## Quick Day Reference (from Two-Week Homework Plan)

| Days | Topic | Relevant Sections |
|------|-------|-------------------|
| Day 1 | Python Foundations | [Getting Started](#getting-started), [1. Python Program Structure](#1-python-program-structure), [2. Variables and Core Data Types](#2-variables-and-core-data-types) |
| Day 2 | Conditions and Decisions | [3. Control Flow](#3-control-flow) |
| Day 3 | Loops and Program Flow | [3. Control Flow](#3-control-flow) |
| Day 4 | Functions | [4. Functions and Methods](#4-functions-and-methods) |
| Day 5 | File Handling | [6. File Handling](#6-file-handling) |
| Day 6 | String and Character Validation | [7. String Validation and Character Checks](#7-string-validation-and-character-checks) |
| Day 7 | Mini Review Day | All sections from Days 1-6 |
| Days 8-10 | Build and Implement (Project Skeleton, Data Loading, Display) | [1. Python Program Structure](#1-python-program-structure), [4. Functions and Methods](#4-functions-and-methods), [5. Classes and Object-Oriented Basics](#5-classes-and-object-oriented-basics) |
| Days 11-12 | Filters and Logic | [3. Control Flow](#3-control-flow), [7. String Validation and Character Checks](#7-string-validation-and-character-checks) |
| Day 13 | Add New Gamertag + Loop | [8. Console Input and Output](#8-console-input-and-output), [6. File Handling](#6-file-handling) |
| Day 14 | Testing and Refinement | [9. Error Handling](#9-error-handling), [10. Basic Testing Mindset](#10-basic-testing-mindset) |

---

## Table of Contents
- [Getting Started](#getting-started)
- [1. Python Program Structure](#1-python-program-structure)
- [2. Variables and Core Data Types](#2-variables-and-core-data-types)
- [3. Control Flow](#3-control-flow)
- [4. Functions and Methods](#4-functions-and-methods)
- [5. Classes and Object-Oriented Basics](#5-classes-and-object-oriented-basics)
- [6. File Handling](#6-file-handling)
- [7. String Validation and Character Checks](#7-string-validation-and-character-checks)
- [8. Console Input and Output](#8-console-input-and-output)
- [9. Error Handling](#9-error-handling)
- [10. Basic Testing Mindset](#10-basic-testing-mindset)

---

## Getting Started

| Topic | W3Schools Link |
|---|---|
| Python Home | [https://www.w3schools.com/python/](https://www.w3schools.com/python/) |
| Python Introduction | [https://www.w3schools.com/python/python_intro.asp](https://www.w3schools.com/python/python_intro.asp) |
| Python Get Started (install and run) | [https://www.w3schools.com/python/python_getstarted.asp](https://www.w3schools.com/python/python_getstarted.asp) |
| Python Syntax | [https://www.w3schools.com/python/python_syntax.asp](https://www.w3schools.com/python/python_syntax.asp) |
| Python Comments | [https://www.w3schools.com/python/python_comments.asp](https://www.w3schools.com/python/python_comments.asp) |

### Gamertag-Specific Challenge: Getting Started

1. The C# project runs via `static void Main(string[] args)`. Python does not have this. After reading the Python Syntax and Introduction pages, what is the conventional way to mark where a Python script should start executing? (Look for the `if __name__` pattern.)
2. Python uses indentation to define code blocks — C# uses curly braces `{ }`. Look at any method in `Gamertags.cs` and rewrite just its opening lines using Python-style indentation rules. What happens if you get the indentation wrong in Python?

---

## 1. Python Program Structure

Covers how a Python script starts, entry-point conventions, and separating setup from processing.

| Topic | W3Schools Link |
|---|---|
| Python Syntax | [https://www.w3schools.com/python/python_syntax.asp](https://www.w3schools.com/python/python_syntax.asp) |
| Python Indentation | [https://www.w3schools.com/python/python_syntax.asp#indentation](https://www.w3schools.com/python/python_syntax.asp#indentation) |
| Python Modules | [https://www.w3schools.com/python/python_modules.asp](https://www.w3schools.com/python/python_modules.asp) |
| Python Scope | [https://www.w3schools.com/python/python_scope.asp](https://www.w3schools.com/python/python_scope.asp) |

### Gamertag-Specific Challenge: Python Program Structure

1. The C# `Gamertags` class contains all its methods inside a class body. After reading about Python Modules and Scope, where would you put the main loop code — inside the class or outside it? Why?
2. In C#, `static void Main` is the guaranteed entry point. In Python, what guard clause do you write to make sure code only runs when you execute the file directly, not when it is imported as a module?

---

## 2. Variables and Core Data Types

Covers strings, lists, booleans, and None — the types used heavily in this project.

| Topic | W3Schools Link |
|---|---|
| Python Variables | [https://www.w3schools.com/python/python_variables.asp](https://www.w3schools.com/python/python_variables.asp) |
| Python Data Types | [https://www.w3schools.com/python/python_datatypes.asp](https://www.w3schools.com/python/python_datatypes.asp) |
| Python Numbers | [https://www.w3schools.com/python/python_numbers.asp](https://www.w3schools.com/python/python_numbers.asp) |
| Python Strings | [https://www.w3schools.com/python/python_strings.asp](https://www.w3schools.com/python/python_strings.asp) |
| Python Lists | [https://www.w3schools.com/python/python_lists.asp](https://www.w3schools.com/python/python_lists.asp) |
| Python Booleans | [https://www.w3schools.com/python/python_booleans.asp](https://www.w3schools.com/python/python_booleans.asp) |
| Python None / Null Values | [https://www.w3schools.com/python/python_datatypes.asp](https://www.w3schools.com/python/python_datatypes.asp) |
| Python Type Casting | [https://www.w3schools.com/python/python_casting.asp](https://www.w3schools.com/python/python_casting.asp) |

### Gamertag-Specific Challenge: Variables and Core Data Types

1. The C# class declares `private string[] gamerTagList = { };` — a fixed-size array of strings, initialised empty. After reading the Python Lists page, what Python type replaces `string[]`? How do you create an empty one?
2. The C# main loop uses `bool isRunning = true;`. After reading Python Booleans, what is the Python equivalent? (Note: Python capitalises boolean values differently than C# — what is the difference?)
3. The C# code uses `lineNumber.ToString() + ") " + s` to combine a number and a string. After reading Python Type Casting and String Formatting, what are two different Python approaches to achieve this kind of number-and-string combination?

---

## 3. Control Flow

Covers while loops, if/else decisions, loop termination, and iterating through lists.

| Topic | W3Schools Link |
|---|---|
| Python If...Else | [https://www.w3schools.com/python/python_conditions.asp](https://www.w3schools.com/python/python_conditions.asp) |
| Python While Loops | [https://www.w3schools.com/python/python_while_loops.asp](https://www.w3schools.com/python/python_while_loops.asp) |
| Python For Loops | [https://www.w3schools.com/python/python_for_loops.asp](https://www.w3schools.com/python/python_for_loops.asp) |
| Python Break and Continue | [https://www.w3schools.com/python/python_for_loops.asp](https://www.w3schools.com/python/python_for_loops.asp) |
| Python Operators (comparison and logical) | [https://www.w3schools.com/python/python_operators.asp](https://www.w3schools.com/python/python_operators.asp) |

### Gamertag-Specific Challenge: Control Flow

1. The C# filter condition uses `&&` and `!` operators:
   ```csharp
   (s.Length > 0) && !Char.IsLetterOrDigit(s, 0)
   ```
   After reading the Python Operators page, what are the Python keywords that replace `&&` and `!`?

2. The C# main loop uses `while (isRunning)` with a `bool` flag. After reading the Python While Loops page, write just the `while` line (not the body) that you would use in Python to replicate this loop. What value does `isRunning` need to be to start the loop? To stop it?

3. The C# `foreach` loop iterates over every gamertag in the list. After reading Python For Loops, what Python keyword and syntax replaces `foreach (string s in gamerTagList)`?

---

## 4. Functions and Methods

Covers function definitions, parameters, return values, and single-responsibility decomposition.

| Topic | W3Schools Link |
|---|---|
| Python Functions | [https://www.w3schools.com/python/python_functions.asp](https://www.w3schools.com/python/python_functions.asp) |
| Python Lambda | [https://www.w3schools.com/python/python_lambda.asp](https://www.w3schools.com/python/python_lambda.asp) |
| Python Function Arguments | [https://www.w3schools.com/python/python_functions.asp](https://www.w3schools.com/python/python_functions.asp) |
| Python Return Values | [https://www.w3schools.com/python/python_functions.asp](https://www.w3schools.com/python/python_functions.asp) |
| Python Built-in Functions | [https://www.w3schools.com/python/python_ref_functions.asp](https://www.w3schools.com/python/python_ref_functions.asp) |

### Gamertag-Specific Challenge: Functions and Methods

1. All six C# methods are declared as `public void MethodName()` — they take no parameters and return nothing. After reading Python Functions, what is the Python `def` syntax for a function that takes no parameters and returns nothing? How does Python signal "no return value" (do you need to do anything explicit)?
2. The C# `foreach` loop in `PrintAllGamertags` uses a manual `lineNumber` counter. After reading Python For Loops (specifically the `enumerate` built-in), describe in plain English how `enumerate` works and why it would replace the manual counter. (Find the Built-in Functions page and look up `enumerate`.)
3. In C#, methods inside a class call each other directly: `LoadGamertags()` is called inside `AddNewUserName()`. After reading Python Class Methods, what extra step is needed in Python to call one method from inside another method of the same class?

---

## 5. Classes and Object-Oriented Basics

Covers creating classes, instance attributes, constructors, and method naming.

| Topic | W3Schools Link |
|---|---|
| Python Classes and Objects | [https://www.w3schools.com/python/python_classes.asp](https://www.w3schools.com/python/python_classes.asp) |
| Python Constructors (`__init__`) | [https://www.w3schools.com/python/python_classes.asp](https://www.w3schools.com/python/python_classes.asp) |
| Python Class Methods | [https://www.w3schools.com/python/python_classes.asp](https://www.w3schools.com/python/python_classes.asp) |
| Python Inheritance | [https://www.w3schools.com/python/python_inheritance.asp](https://www.w3schools.com/python/python_inheritance.asp) |
| Python Iterators | [https://www.w3schools.com/python/python_iterators.asp](https://www.w3schools.com/python/python_iterators.asp) |

### Gamertag-Specific Challenge: Classes and Object-Oriented Basics

1. The C# class has no explicit constructor — C# provides a default one automatically. After reading Python Classes and Objects (specifically the `__init__` section), what method do you write in Python to initialise instance data? Write just the `def` line (not the body) for a Python `Gamertags` class that stores an empty list of gamertags.
2. The C# field is `private string[] gamerTagList`. In Python, instance variables are created in `__init__`. After reading about Python class attributes, what keyword do you use to refer to the current instance when setting and accessing instance variables inside a method?
3. The C# methods are all `public`. Python does not enforce access modifiers the same way. After reading about Python classes, what naming convention signals that an attribute or method is intended to be "private" or "internal" in Python?

---

## 6. File Handling

Covers reading text files, appending new lines, file paths, and character encoding.

| Topic | W3Schools Link |
|---|---|
| Python File Handling overview | [https://www.w3schools.com/python/python_file_handling.asp](https://www.w3schools.com/python/python_file_handling.asp) |
| Python Open a File | [https://www.w3schools.com/python/python_file_open.asp](https://www.w3schools.com/python/python_file_open.asp) |
| Python Read Files | [https://www.w3schools.com/python/python_file_read.asp](https://www.w3schools.com/python/python_file_read.asp) |
| Python Write / Create Files | [https://www.w3schools.com/python/python_file_write.asp](https://www.w3schools.com/python/python_file_write.asp) |
| Python Delete Files | [https://www.w3schools.com/python/python_file_remove.asp](https://www.w3schools.com/python/python_file_remove.asp) |

### Gamertag-Specific Challenge: File Handling

1. The C# reads the file with: `gamerTagList = File.ReadAllLines("../Gamertags.txt");`
   After reading Python File Read, what Python function opens a file and what method reads all its lines into a list? When you read lines this way, does each line include the newline character `\n` at the end? How would you remove it?

2. The C# appends with: `File.AppendAllText("../Gamertags.txt", "\n" + newGamerTag);`
   After reading Python File Write, what file mode string do you pass to `open()` to append to a file without erasing existing content? Why does the C# version put `"\n"` *before* the new gamertag — and would you do the same in Python?

3. The C# uses the path `"../Gamertags.txt"` (relative, one folder up). After reading Python File Handling, what is the risk of using relative paths? How would you find the directory of your Python script at runtime to build a reliable path?

---

## 7. String Validation and Character Checks

Covers checking string length, first/last characters, numeric checks, and letter-or-digit checks.

| Topic | W3Schools Link |
|---|---|
| Python Strings | [https://www.w3schools.com/python/python_strings.asp](https://www.w3schools.com/python/python_strings.asp) |
| Python String Methods reference | [https://www.w3schools.com/python/python_ref_string.asp](https://www.w3schools.com/python/python_ref_string.asp) |
| Python String Slicing (first/last character) | [https://www.w3schools.com/python/python_strings_slicing.asp](https://www.w3schools.com/python/python_strings_slicing.asp) |
| Python `str.isdigit()` | [https://www.w3schools.com/python/ref_string_isdigit.asp](https://www.w3schools.com/python/ref_string_isdigit.asp) |
| Python `str.isnumeric()` | [https://www.w3schools.com/python/ref_string_isnumeric.asp](https://www.w3schools.com/python/ref_string_isnumeric.asp) |
| Python `str.isalpha()` | [https://www.w3schools.com/python/ref_string_isalpha.asp](https://www.w3schools.com/python/ref_string_isalpha.asp) |
| Python `str.isalnum()` | [https://www.w3schools.com/python/ref_string_isalnum.asp](https://www.w3schools.com/python/ref_string_isalnum.asp) |
| Python `str.strip()` (trimming whitespace) | [https://www.w3schools.com/python/ref_string_strip.asp](https://www.w3schools.com/python/ref_string_strip.asp) |
| Python `str.startswith()` | [https://www.w3schools.com/python/ref_string_startswith.asp](https://www.w3schools.com/python/ref_string_startswith.asp) |
| Python `str.endswith()` | [https://www.w3schools.com/python/ref_string_endswith.asp](https://www.w3schools.com/python/ref_string_endswith.asp) |
| Python `len()` function | [https://www.w3schools.com/python/ref_func_len.asp](https://www.w3schools.com/python/ref_func_len.asp) |

### Gamertag-Specific Challenge: String Validation and Character Checks

1. The C# filter for gamertags ending with a number uses:
   ```csharp
   Char.IsNumber(s, s.Length - 1)
   ```
   This accesses the last character by index. After reading Python String Slicing, what index value in Python always refers to the last character of a string, regardless of its length? After reading `str.isdigit()`, what method would you call on that single character to check if it is a digit?

2. The C# filter for gamertags not starting with a letter or digit uses:
   ```csharp
   !Char.IsLetterOrDigit(s, 0)
   ```
   Index `0` is the first character. After reading `str.isalnum()`, what does that method check? How does it differ from `str.isalpha()` and `str.isdigit()`? Which one is the right replacement for `Char.IsLetterOrDigit`?

3. Both C# conditions guard against empty strings with `s.Length > 0`. After reading `len()` and Python String Slicing, why would accessing `s[-1]` or `s[0]` on an empty string cause an error? What check prevents this — and is there a Pythonic way to test for an empty string without using `len()` at all?

---

## 8. Console Input and Output

Covers reading user input, normalising case and whitespace, and printing output.

| Topic | W3Schools Link |
|---|---|
| Python User Input (`input()`) | [https://www.w3schools.com/python/python_user_input.asp](https://www.w3schools.com/python/python_user_input.asp) |
| Python `print()` function | [https://www.w3schools.com/python/ref_func_print.asp](https://www.w3schools.com/python/ref_func_print.asp) |
| Python String Formatting | [https://www.w3schools.com/python/python_string_formatting.asp](https://www.w3schools.com/python/python_string_formatting.asp) |
| Python `str.upper()` / `str.lower()` | [https://www.w3schools.com/python/ref_string_upper.asp](https://www.w3schools.com/python/ref_string_upper.asp) |
| Python `str.strip()` | [https://www.w3schools.com/python/ref_string_strip.asp](https://www.w3schools.com/python/ref_string_strip.asp) |

### Gamertag-Specific Challenge: Console Input and Output

1. The C# `PrintAllGamertags` method uses:
   ```csharp
   Console.WriteLine(lineNumber.ToString() + ") " + s);
   ```
   After reading Python String Formatting, describe two different ways to produce the same output in Python. Which approach do experienced Python developers generally prefer, and why? (Do not write the full method — just describe the formatting technique.)

2. The C# `AddNewUserName` reads input with `Console.ReadLine()`, then checks `newGamerTag.Length > 0`. After reading Python User Input, what function reads a line of text in Python? If a user types spaces and presses Enter, `Length > 0` would be non-zero in C# — but should you count that as a valid gamertag? Which string method would you use first to handle this?

3. The C# ends each screen section with:
   ```csharp
   Console.WriteLine("Press any key to continue");
   Console.ReadKey();
   ```
   `Console.ReadKey()` captures a keypress without requiring Enter. After reading Python User Input, how would you replicate a "press any key to continue" pause in Python, knowing that Python always requires Enter?

---

## 9. Error Handling

Covers handling missing files, permission errors, unexpected input, and graceful failure.

| Topic | W3Schools Link |
|---|---|
| Python Try...Except | [https://www.w3schools.com/python/python_try_except.asp](https://www.w3schools.com/python/python_try_except.asp) |
| Python Exception handling (raise) | [https://www.w3schools.com/python/python_try_except.asp](https://www.w3schools.com/python/python_try_except.asp) |
| Python Built-in Exceptions | [https://www.w3schools.com/python/python_ref_exceptions.asp](https://www.w3schools.com/python/python_ref_exceptions.asp) |

### Gamertag-Specific Challenge: Error Handling

1. In `load_gamertags()`, if `Gamertags.txt` does not exist, Python raises a specific exception. After reading Python Try...Except and Built-in Exceptions, what is the name of that exception? Write a plain-English description of what your `except` block should do when this happens — should it crash, print a message, or create an empty list?

2. In `add_new_username()`, the file write could fail (for example, the file is read-only, or the disk is full). After reading Try...Except, what exception type covers file permission errors? Write a plain-English plan for what the method should do if the write fails.

3. After reading about `try/except/finally`, explain in plain English what the `finally` block does. In the context of file handling, why might you use `finally` — and what Python shorthand (a keyword that replaces the `try/finally` pattern for files) makes this even simpler?

---

## 10. Basic Testing Mindset

Covers checking each feature one by one, edge cases, and repeated runs.

| Topic | W3Schools Link |
|---|---|
| Python `assert` statement | [https://www.w3schools.com/python/ref_keyword_assert.asp](https://www.w3schools.com/python/ref_keyword_assert.asp) |
| Python Built-in Functions (useful for testing) | [https://www.w3schools.com/python/python_ref_functions.asp](https://www.w3schools.com/python/python_ref_functions.asp) |

### Gamertag-Specific Challenge: Basic Testing Mindset

1. After reading the `assert` statement, describe in plain English what `assert` does and what happens when it fails. Without writing a full test suite, how could you use `assert` to verify that your number-ending filter returns the correct gamertags from a known list?

2. Using your Day 7 paper walkthrough results (the sample list with `DragonSlayer`, `Blaze99`, `#ShadowKing`, etc.), write three plain-English test cases for the two filter methods. For each test case, describe: the input, the expected output, and what a failure would tell you about your code.

---

## Quick Reference: All W3Schools Python Pages

- Full Python tutorial index: [https://www.w3schools.com/python/default.asp](https://www.w3schools.com/python/default.asp)
- Python built-in string methods: [https://www.w3schools.com/python/python_ref_string.asp](https://www.w3schools.com/python/python_ref_string.asp)
- Python built-in functions: [https://www.w3schools.com/python/python_ref_functions.asp](https://www.w3schools.com/python/python_ref_functions.asp)
- Python keywords: [https://www.w3schools.com/python/python_ref_keywords.asp](https://www.w3schools.com/python/python_ref_keywords.asp)
- Python exceptions: [https://www.w3schools.com/python/python_ref_exceptions.asp](https://www.w3schools.com/python/python_ref_exceptions.asp)
