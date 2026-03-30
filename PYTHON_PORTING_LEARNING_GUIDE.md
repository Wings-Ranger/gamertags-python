# Python Learning Guide for Porting This Project

## Goal
Move the current C# console gamertag program into Python while keeping the same behavior:
- Load gamertags from a text file
- Display all gamertags
- Filter gamertags by specific character rules
- Add a new gamertag to the file
- Ask whether to run again

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
Use this mapping as your mental translation guide.
- C# class and methods: Python class and methods
- C# array of strings: Python list of strings
- foreach loop: Python iteration over a list
- if statements with character helpers: Python string methods and character checks
- Console read/write: Python text input and printing
- File.ReadAllLines and append: Python file read and append workflow
- Main loop with bool flag: Python while loop with boolean state

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
