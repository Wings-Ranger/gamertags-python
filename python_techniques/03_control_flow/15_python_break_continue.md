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

**C# pattern (from the gamertag project):**
```csharp
// When loading gamertags, C# skips blank/whitespace lines
foreach (string line in File.ReadAllLines("../Gamertags.txt"))
{
    if (string.IsNullOrWhiteSpace(line))
        continue;   // C# also has continue
    gamerTagList.Add(line);
}
```

**Python skeleton (fill in the blanks):**
```
# continue — skip blank or whitespace-only lines when loading
gamer_tag_list = []
raw_lines = ["ShadowX", "", "NightOwl", "  ", "ProSniper"]
for line in raw_lines:
    line = line._____(  )        # strip whitespace first
    if _____ line:               # if line is empty/falsy after stripping
        _____                    # skip this line — jump to next iteration
    gamer_tag_list._____(line)   # only valid lines reach this point

print(gamer_tag_list)            # how many items should be here?

# break — stop searching once a gamertag is found
target = "NightOwl"
for tag in gamer_tag_list:
    if tag _____ target:
        print(f"Found: {tag}")
        _____                    # stop the loop immediately
    print(f"Checking {tag}...")

# for/else — the else runs ONLY if break was never hit
for tag in gamer_tag_list:
    if tag == "GhostPlayer":
        print("Found!")
        _____
_____:                           # what keyword goes here?
    print("GhostPlayer not found in list")

# pass — placeholder for code you haven't written yet
def add_new_gamertag():
    _____    # TODO: implement this
```

**Questions:**
- `continue` behaves the same in C# and Python. What exactly does it do inside a loop body?
- `break` exits the loop entirely. When loading gamertags from a file, when might you use `break` instead of `continue`?
- What is the `for/else` pattern? When does the `else` block run — and when does it NOT run?
- What does `pass` do? When is it useful to write a function with just `pass` in the body?

**Test challenge:**
Write a `for` loop that iterates a list of raw lines (some blank). Use `continue` to skip blank lines. Then search for a specific gamertag using `break` and the `for/else` pattern to handle the "not found" case cleanly.

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

## Challenges

1. **Skip blank lines with continue:** When loading gamertags from a file, blank lines must be skipped. Fill in:
   ```
   for line in raw_lines:
       line = line._____(  )
       if _____ line:
           _____            # skip this line
       gamer_tag_list.append(line)
   ```

2. **Search with break:** Find a specific gamertag and stop as soon as you find it:
   ```
   for tag in gamer_tag_list:
       if tag == _____:
           print(f"Found: {tag}")
           _____
       print(f"Not {tag}, keep looking...")
   ```

3. **for/else pattern:** Use `for/else` to handle the "not found" case cleanly without a flag variable:
   ```
   for tag in gamer_tag_list:
       if tag == "GhostPlayer":
           print("Found!")
           _____
   _____:                    # what keyword?
       print("GhostPlayer not in list")
   ```
   When does the `else` block run? When doesn't it?

4. **pass placeholders:** Write stub functions for each method in the gamertag project using `pass` so the program structure is clear before you implement:
   ```
   def load_gamertags():
       _____
   def print_all_gamertags():
       _____
   def add_new_username():
       _____
   ```
