---
name: "Batch MD Answer Review"
description: "Validate answers across multiple markdown homework files and produce one consolidated score report with per-file breakdown."
argument-hint: "Provide markdown file paths and your answers for each file."
agent: "MD Answer Verifier"
tools: [read, search]
---
Review my answers across multiple markdown homework files and return a single consolidated report.

## Inputs I Will Provide
- A list of markdown file paths
- My answers for each file

## What To Do
1. Read each file and match my answers to the relevant questions/blanks.
2. Grade each answer using the verifier rubric.
3. Produce one combined report with:
- Overall score: `correct / total` and percentage
- Per-file score: `correct / total` and percentage
- Incorrect items grouped by file
- Top 3 weak concepts across all files
- A short study plan (5 to 10 minutes per weak concept)

## Scoring Rules
- Count each distinct answer as one graded item.
- Accept equivalent wording when conceptually correct.
- If an answer is missing, mark it incorrect and list it as missing.

## Output Format
Use this exact section order:

1. Overall Score
2. Per-File Breakdown
3. Incorrect Answers by File
4. Weak Concepts
5. Quick Study Plan

Keep explanations concise and practical.
