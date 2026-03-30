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
