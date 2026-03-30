# Gamertags Python Homework Hub

Quick-glance home page for your holiday homework. This README combines all 3 planning documents so you can check progress quickly on GitHub while out and about.

## Table of Contents
- [Daily Status](#daily-status)
- [Quick Start](#quick-start)
- [Quick Links](#quick-links)
- [Phone Update (60 Seconds)](#phone-update-60-seconds)
- [At-a-Glance Dashboard](#at-a-glance-dashboard)
- [Full Document 1: Python Porting Learning Guide](#full-document-1-python-porting-learning-guide)
- [Full Document 2: Two-Week Homework Plan](#full-document-2-two-week-homework-plan)
- [Full Document 3: Progress Tracker](#full-document-3-progress-tracker)
- [Source Files (Kept Intact)](#source-files-kept-intact)

## Daily Status
![Day](https://img.shields.io/badge/Day-0%2F14-lightgrey)
![Confidence](https://img.shields.io/badge/Confidence-0%2F5-lightgrey)
![Focus](https://img.shields.io/badge/Focus-Not%20set-lightgrey)

Quick update line:
- Current day: Day 0 of 14
- Confidence: 0 of 5
- Focus today: Not set

## Quick Start
1. Open [Python Homework Progress Tracker](PYTHON_HOMEWORK_PROGRESS_TRACKER.md).
2. Tick off today's checklist items and write one blocker and one win.
3. Update Day, Confidence, and Focus in the Daily Status section above.

## Quick Links
- [Python Porting Learning Guide](PYTHON_PORTING_LEARNING_GUIDE.md)
- [Two-Week Python Homework Plan](TWO_WEEK_PYTHON_HOMEWORK_PLAN.md)
- [Python Homework Progress Tracker](PYTHON_HOMEWORK_PROGRESS_TRACKER.md)

## Phone Update (60 Seconds)
1. Open this repository in the GitHub mobile app.
2. Go to [Python Homework Progress Tracker](PYTHON_HOMEWORK_PROGRESS_TRACKER.md) and tap Edit.
3. Change checklist items from `[ ]` to `[x]` for tasks you completed.
4. Open [README.md](README.md) and update Day, Confidence, and Focus.
5. Commit with a short message like `Day 3 progress update`.

## At-a-Glance Dashboard

### Mission
Port the C# gamertag console app into Python with the same behavior and safe input/file handling.

### Timeline
- Duration: 14 days
- Study target: 60 to 90 minutes per day
- End goal: feature-complete Python version plus reflection notes

### Core Features to Match
- Load gamertags from a text file
- Display all gamertags with numbering
- Filter names ending with a number
- Filter names not starting with a letter or number
- Add a new gamertag and save it
- Ask user whether to run again

### Today Checklist
- [ ] Read today's day plan
- [ ] Do implementation or theory task
- [ ] Run a quick self-check
- [ ] Write one blocker and one win

---

## Full Document 1: Python Porting Learning Guide
<details>
<summary>Open/close full guide</summary>

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

</details>

---

## Full Document 2: Two-Week Homework Plan
<details>
<summary>Open/close full 14-day plan</summary>

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

Checkpoint:
- You can describe the full app flow from start to finish without looking at C#

### Day 4: Functions
Focus:
- Function purpose and decomposition
- Inputs and outputs
- Naming and single responsibility

Homework tasks:
- Break your app into small function-sized responsibilities
- Write a function list for each app behavior

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

Checkpoint:
- You can confidently explain all filter rules and edge cases

### Day 7: Mini Review Day
Focus:
- Consolidation and weak spots

Homework tasks:
- Review your notes from days 1 to 6
- Rewrite confusing notes in simpler words
- Attempt a paper walkthrough of the full app behavior

Checkpoint:
- You can teach the project logic to someone else without showing code

## Week 2: Build, Verify, and Improve

### Day 8: Python Project Skeleton
Focus:
- Project organization
- Planning class and method structure

Homework tasks:
- Create your Python project folder structure
- Plan where each responsibility lives
- Confirm naming consistency

Checkpoint:
- Your project structure is clear and maintainable

### Day 9: Data Loading and Welcome Sequence
Focus:
- Initial startup behavior

Homework tasks:
- Implement and verify startup sequence behavior
- Confirm data loads correctly before processing

Checkpoint:
- Program starts cleanly and loads data every run

### Day 10: Display All Gamertags
Focus:
- Iteration and numbering output

Homework tasks:
- Implement full listing behavior
- Verify numbering and output readability

Checkpoint:
- All gamertags display in expected order with expected numbering

### Day 11: Filter 1 (Ending with Number)
Focus:
- Character-based filtering logic

Homework tasks:
- Implement number-ending filter
- Test with multiple valid and invalid examples

Checkpoint:
- Only correct gamertags are shown for this rule

### Day 12: Filter 2 (Not Starting with Letter or Number)
Focus:
- Start-character classification

Homework tasks:
- Implement second filter
- Test symbol-leading and edge cases

Checkpoint:
- Filter output exactly matches rule definition

### Day 13: Add New Gamertag + Run-Again Loop
Focus:
- User input and persistence

Homework tasks:
- Implement add-new behavior
- Verify write-to-file and reload behavior
- Confirm run-again prompt loops correctly

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

Checkpoint:
- Your Python version is feature-complete and reliable

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

</details>

---

## Full Document 3: Progress Tracker
<details>
<summary>Open/close full tracker</summary>

# Python Homework Progress Tracker (14 Days)

## How to Use
- Mark each task when complete
- Circle confidence score each day (1 = low, 5 = high)
- Write one blocker and one win every day
- Keep this file updated as your holiday homework log

## Weekly Overview

### Week 1 Goal
Build Python foundations and understand how your C# app logic maps to Python.

### Week 2 Goal
Build, test, and polish the Python version of your gamertag app.

## Daily Tracker

| Day | Focus | Main Task Done | Revision Done | Confidence (1-5) | Biggest Blocker | Biggest Win |
|---|---|---|---|---|---|---|
| 1 | Python foundations | [ ] | [ ] | [ ] |  |  |
| 2 | Conditions and decisions | [ ] | [ ] | [ ] |  |  |
| 3 | Loops and program flow | [ ] | [ ] | [ ] |  |  |
| 4 | Functions | [ ] | [ ] | [ ] |  |  |
| 5 | File handling | [ ] | [ ] | [ ] |  |  |
| 6 | String/character validation | [ ] | [ ] | [ ] |  |  |
| 7 | Review and consolidate | [ ] | [ ] | [ ] |  |  |
| 8 | Project skeleton | [ ] | [ ] | [ ] |  |  |
| 9 | Startup + data loading | [ ] | [ ] | [ ] |  |  |
| 10 | Display all gamertags | [ ] | [ ] | [ ] |  |  |
| 11 | Filter: ending with number | [ ] | [ ] | [ ] |  |  |
| 12 | Filter: not starting letter/number | [ ] | [ ] | [ ] |  |  |
| 13 | Add new gamertag + loop | [ ] | [ ] | [ ] |  |  |
| 14 | Final testing + submission prep | [ ] | [ ] | [ ] |  |  |

## Feature Completion Checklist
- [ ] Can load gamertags from file reliably
- [ ] Can display all gamertags with numbering
- [ ] Can filter gamertags ending with a number
- [ ] Can filter gamertags not starting with a letter or number
- [ ] Can add a new gamertag and save it
- [ ] Can run again based on user choice
- [ ] Handles empty and unusual input safely
- [ ] Handles missing file scenario safely

## Quality Checklist
- [ ] Program is easy to read and organised
- [ ] Names are clear and consistent
- [ ] No unnecessary duplication of logic
- [ ] Output is user-friendly and readable
- [ ] End-to-end behavior matches your original C# project

## Final Reflection (Complete on Day 14)
- What I learned most:
- Hardest concept and how I improved:
- What I am most proud of:
- What I would improve next:
- Final confidence score (1-5):

</details>

---

## Source Files (Kept Intact)
- [PYTHON_PORTING_LEARNING_GUIDE.md](PYTHON_PORTING_LEARNING_GUIDE.md)
- [TWO_WEEK_PYTHON_HOMEWORK_PLAN.md](TWO_WEEK_PYTHON_HOMEWORK_PLAN.md)
- [PYTHON_HOMEWORK_PROGRESS_TRACKER.md](PYTHON_HOMEWORK_PROGRESS_TRACKER.md)
