# Python Break and Continue

**W3Schools Link:** https://www.w3schools.com/python/python_for_loops.asp

**Homework Day(s):** Day 3

---

## Overview
`break` and `continue` are loop control statements that alter the normal flow of `for` and `while` loops. `break` immediately exits the loop entirely, while `continue` skips the remainder of the current iteration and proceeds to the next one. Used carefully, they make loops cleaner and more expressive.

## Key Concepts
- **`break`**: exits the innermost loop immediately; execution resumes after the loop
- **`continue`**: skips the rest of the current iteration; loop condition is re-checked (while) or next item fetched (for)
- **`pass`**: a no-op placeholder; does nothing but satisfies a syntax requirement
- **Loop `else`**: the `else` clause of a loop runs only if the loop finished without hitting `break`
- Only affects the **innermost** loop in nested loops
- Overusing `break`/`continue` can reduce readability — use with clear intent

## Syntax / Example Code
```python
# break — stop when target found
gamertags = ["ShadowX", "NightOwl", "ProSniper", "GamerZ"]

for tag in gamertags:
    if tag == "ProSniper":
        print("Found ProSniper!")
        break
    print(f"Checking {tag}...")
# Output:
# Checking ShadowX...
# Checking NightOwl...
# Found ProSniper!

# for/else with break — search pattern
target = "GhostPlayer"
for tag in gamertags:
    if tag == target:
        print(f"Found: {tag}")
        break
else:
    print(f"{target} not found in the list")

# continue — skip invalid entries while loading
raw_lines = ["ShadowX,Xbox,4250", "", "NightOwl,PS,3300", "  ", "ProSniper,PC,5100"]

players = []
for line in raw_lines:
    line = line.strip()
    if not line:
        continue   # skip blank lines
    parts = line.split(",")
    if len(parts) != 3:
        continue   # skip malformed lines
    players.append({"gamertag": parts[0], "platform": parts[1], "score": int(parts[2])})

print(f"Loaded {len(players)} valid players")

# continue in a while loop — skip zeros
numbers = [5, 0, 3, 0, 8, 0, 2]
total = 0
for n in numbers:
    if n == 0:
        continue
    total += n
print(f"Sum (excluding zeros): {total}")  # 18

# pass — placeholder in a block you haven't written yet
def display_leaderboard():
    pass   # TODO: implement

# break in a while loop — menu exit
while True:
    choice = input("Enter 'q' to quit or press Enter: ").strip()
    if choice == "q":
        print("Exiting...")
        break
    print("Continuing...")

# Nested loops — break only exits innermost
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
found = False
for row in matrix:
    for val in row:
        if val == 5:
            found = True
            break   # exits inner loop only
    if found:
        break       # exits outer loop
print(f"Found 5: {found}")
```

## Common Use Cases
- Using `continue` to skip blank or malformed lines when reading a file
- Using `break` to stop searching once a gamertag is found
- Using `for/else` to handle "not found" cleanly without a flag variable
- Using `pass` as a placeholder in functions you plan to implement later

## Related Days
| Day | Topic |
|-----|-------|
| Day 3 | Loops and Program Flow (while loops, iterating lists) |

## See Also
- [13_python_while_loops.md](13_python_while_loops.md)
- [14_python_for_loops.md](14_python_for_loops.md)
- [12_python_if_else.md](12_python_if_else.md)

## Practice Tips
- Practice the `for/else` search pattern — it's very Pythonic
- Use `continue` when loading data to cleanly skip bad records
- Avoid `break` inside deeply nested loops — consider refactoring to a function with `return`
- Replace a boolean flag variable with `for/else` wherever possible
