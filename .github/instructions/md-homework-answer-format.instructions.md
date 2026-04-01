---
name: "Markdown Homework Answer Format"
description: "Use when answering or validating markdown homework questions in python_techniques files. Enforce a consistent answer format before grading."
applyTo: "python_techniques/**/*.md"
---
# Markdown Homework Answer Format

Use this format before validation so grading is accurate and fast.

## Required Format
For each question, provide exactly these lines:

Question ID: <Q1, Q2, Blank 1, Challenge 3, etc.>
Answer: <your answer>
Reason: <one short sentence>
Confidence: <High | Medium | Low>

## Rules
- Keep one answer block per question.
- Do not combine multiple questions in one block.
- For code blanks, include only the value or token that fills the blank.
- For True or False style checks, still include a one-line reason.
- If unsure, write your best answer and set Confidence to Low.

## Validation Prep
Before grading, the assistant should:
1. Confirm each answer block maps to a real question in the file.
2. Flag missing Question IDs.
3. Flag duplicate Question IDs.
4. Ask for missing blocks if needed.

## Example
Question ID: Blank 1
Answer: -1
Reason: Python negative indexing uses -1 for the last character.
Confidence: High
