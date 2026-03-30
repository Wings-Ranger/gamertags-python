# Python File Read

**W3Schools Link:** https://www.w3schools.com/python/python_file_read.asp

**Homework Day(s):** Day 5, Days 9–10

---

## Overview
Reading files in Python is done with the `open()` function in read mode (`"r"`). Python provides multiple ways to read file content: all at once, one line at a time, or all lines as a list. For a gamertag project, reading a CSV or text file line by line and parsing each record is a fundamental skill.

## Key Concepts
- **`f.read()`**: reads the entire file as a single string
- **`f.readline()`**: reads one line at a time (including the newline character)
- **`f.readlines()`**: reads all lines into a list of strings
- **`for line in f:`**: most memory-efficient way to iterate lines — preferred for large files
- **`.strip()`**: removes leading/trailing whitespace and newlines from each line — always apply
- **Empty line handling**: skip blank lines with `if not line.strip(): continue`
- **`encoding="utf-8"`**: specify encoding to handle international characters correctly

## Syntax / Example Code
```python
# --- Method 1: read all at once ---
with open("gamertags.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

# --- Method 2: readlines() — list of all lines ---
with open("gamertags.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
# lines = ["ShadowX,Xbox,4250\n", "NightOwl,PlayStation,3300\n", ...]
for line in lines:
    print(line.strip())

# --- Method 3: for loop (most Pythonic, memory efficient) ---
with open("gamertags.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue   # skip blank lines
        print(line)

# --- Parsing CSV lines into player dicts ---
def load_players(filename):
    """Load players from a CSV file (gamertag,platform,score)."""
    players = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split(",")
                if len(parts) != 3:
                    print(f"Skipping malformed line: {line}")
                    continue
                try:
                    player = {
                        "gamertag": parts[0].strip(),
                        "platform": parts[1].strip(),
                        "score": int(parts[2].strip())
                    }
                    players.append(player)
                except ValueError:
                    print(f"Skipping line with invalid score: {line}")
    except FileNotFoundError:
        print(f"File not found: {filename}")
    return players

players = load_players("gamertags.txt")
print(f"Loaded {len(players)} players")
for p in players:
    print(f"  {p['gamertag']} ({p['platform']}): {p['score']}")

# --- Reading a specific line by number ---
with open("gamertags.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    if lines:
        first_line = lines[0].strip()
        print(f"First entry: {first_line}")

# --- Counting lines in a file ---
with open("gamertags.txt", "r", encoding="utf-8") as f:
    count = sum(1 for line in f if line.strip())
print(f"Total records: {count}")

# --- Using csv module for robust CSV reading ---
import csv

def load_players_csv(filename):
    players = []
    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) == 3:
                    players.append({
                        "gamertag": row[0],
                        "platform": row[1],
                        "score": int(row[2])
                    })
    except FileNotFoundError:
        pass
    return players
```

## Common Use Cases
- Loading all gamertag records at startup into a list of dicts
- Counting how many records are in the file
- Parsing CSV-formatted player data with `.split(",")`
- Using `csv.reader` for more robust CSV parsing

## Related Days
| Day | Topic |
|-----|-------|
| Day 5 | File Handling (reading, appending, file paths) |
| Days 9-10 | Data loading, display |

## See Also
- [26_python_file_handling.md](26_python_file_handling.md)
- [28_python_file_write.md](28_python_file_write.md)
- [09_python_dictionaries.md](../02_data_types/09_python_dictionaries.md)
- [36_python_try_except.md](../08_error_handling/36_python_try_except.md)

## Practice Tips
- Always call `.strip()` on every line you read from a file
- Skip blank lines with `if not line: continue` after stripping
- Wrap file reading in `try/except FileNotFoundError` to handle missing files gracefully
- Use `csv.reader` when your data may contain commas inside quoted fields
