# Python File Write

**W3Schools Link:** https://www.w3schools.com/python/python_file_write.asp

**Homework Day(s):** Day 5, Day 13

---

## Overview
Writing to files in Python uses the `open()` function with mode `"w"` (write/overwrite) or `"a"` (append). The `"w"` mode creates the file if it doesn't exist and overwrites it if it does. The `"a"` mode adds content to the end without touching existing content. Both are essential for a gamertag manager that persists player data.

## Key Concepts
- **`"w"` mode**: creates or overwrites the file entirely — use with caution
- **`"a"` mode**: appends to the end of the file; creates if not exists
- **`f.write(string)`**: writes a string to the file; does NOT add a newline automatically
- **`f.writelines(list)`**: writes each string in the list; no newlines added automatically
- **Always add `"\n"`**: ensure each record ends with a newline for proper line separation
- **`with` statement**: ensures the file is closed (and flushed) after writing
- **`csv.writer`**: use for robust CSV writing, handles quoting automatically

## Syntax / Example Code
```python
import csv

# --- Write mode ("w") — creates or overwrites ---
players = [
    {"gamertag": "ShadowX",   "platform": "Xbox",         "score": 4250},
    {"gamertag": "NightOwl",  "platform": "PlayStation",  "score": 3300},
    {"gamertag": "ProSniper", "platform": "PC",           "score": 5100},
]

def save_players(filename, players):
    """Save all players to a CSV file (overwrites)."""
    with open(filename, "w", encoding="utf-8") as f:
        for player in players:
            line = f"{player['gamertag']},{player['platform']},{player['score']}\n"
            f.write(line)
    print(f"Saved {len(players)} players to {filename}")

save_players("gamertags.txt", players)

# --- Append mode ("a") — adds to end, does not overwrite ---
def add_player_to_file(filename, player):
    """Append a single player record to the file."""
    with open(filename, "a", encoding="utf-8") as f:
        line = f"{player['gamertag']},{player['platform']},{player['score']}\n"
        f.write(line)
    print(f"Added {player['gamertag']} to {filename}")

new_player = {"gamertag": "GamerZ", "platform": "Nintendo Switch", "score": 900}
add_player_to_file("gamertags.txt", new_player)

# --- writelines() — write a list of strings ---
lines = ["IronFox,Xbox,2100\n", "BlazeMaster,PC,3800\n"]
with open("gamertags.txt", "a", encoding="utf-8") as f:
    f.writelines(lines)

# --- Using csv.writer for robust output ---
def save_players_csv(filename, players):
    """Save players using csv.writer (handles edge cases automatically)."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for player in players:
            writer.writerow([player["gamertag"], player["platform"], player["score"]])

save_players_csv("gamertags.csv", players)

# --- Write with a header row ---
def save_with_header(filename, players):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["gamertag", "platform", "score"])   # header
        for p in players:
            writer.writerow([p["gamertag"], p["platform"], p["score"]])

# --- Full load-modify-save pattern ---
def add_new_gamertag(filename, gamertag, platform, score):
    """Load existing records, add new player, save all back."""
    # Load existing
    existing = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    existing.append(line)
    except FileNotFoundError:
        pass

    # Add new record
    new_line = f"{gamertag},{platform},{score}"
    existing.append(new_line)

    # Save all back
    with open(filename, "w", encoding="utf-8") as f:
        for line in existing:
            f.write(line + "\n")

    print(f"Added {gamertag} to {filename}")
```

## Common Use Cases
- `save_players("gamertags.txt", players)` — persist the full player list after any change
- `add_player_to_file("gamertags.txt", player)` — quick append for a new gamertag
- Overwriting the file with updated data after editing a record
- Using `csv.writer` to avoid issues with commas inside field values

## Related Days
| Day | Topic |
|-----|-------|
| Day 5 | File Handling (reading, appending, file paths) |
| Day 13 | Add new gamertag + run-again loop |

## See Also
- [26_python_file_handling.md](26_python_file_handling.md)
- [27_python_file_read.md](27_python_file_read.md)
- [05_python_strings.md](../02_data_types/05_python_strings.md)
- [35_python_string_formatting.md](../07_strings/35_python_string_formatting.md)

## Practice Tips
- Practice the full cycle: write a file with `"w"`, then read it back with `"r"`
- Add a gamertag with `"a"` mode and verify the file was not overwritten
- Always end each written line with `"\n"`
- Use `csv.writer` instead of manual string formatting for production-quality output
