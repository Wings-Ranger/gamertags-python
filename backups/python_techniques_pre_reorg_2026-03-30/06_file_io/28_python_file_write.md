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

```
C# pattern (from the gamertag project):
    // Appending a new gamertag to the file
    File.AppendAllText("../Gamertags.txt", "\n" + newGamerTag);

Python skeleton — write and append to files (fill in the blanks):

    # Append mode — adds to the end without overwriting (like File.AppendAllText)
    new_tag = "ShadowX99"
    with open("Gamertags.txt", _____) as f:   # what mode letter appends?
        f._____("\n" + _____)                  # what method writes a string?

    # Write mode — creates or OVERWRITES the entire file
    gamer_tag_list = ["ShadowX", "NightOwl", "ProSniper"]
    with open("Gamertags.txt", _____) as f:   # what mode letter overwrites?
        for tag in gamer_tag_list:
            f.write(_____ + "\n")             # write each tag + newline

    # Save all gamertags back to file (full overwrite pattern)
    def save_gamertags(filename, gamer_tag_list):
        with open(_____, _____) as f:
            for tag in _____:
                f._____(tag + _____)          # each line needs a newline character

    # Add a new gamertag — matching C#'s AddNewUserName() + File.AppendAllText()
    def add_new_user_name(self):
        new_tag = input(_____)._____(  )      # prompt user, then strip whitespace
        self.gamer_tag_list._____(new_tag)    # add to in-memory list
        with open(self.filename, _____) as f: # append to file
            f.write(_____ + new_tag)          # what prefix did the C# code use?

Questions:
- What is the difference between `"w"` mode and `"a"` mode?
- Why does `f.write()` NOT add a newline automatically? What do you have to add?
- The C# code writes `"\n" + newGamerTag`. Why does the newline come first?
- After appending, how can you verify the file was updated correctly?

Test challenge:
    Write a function that appends a gamertag to "Gamertags.txt". Then read the file
    back and confirm the last line matches what you appended. What happens if you
    call your append function twice with the same gamertag — does Python stop you?
    Should it?
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

## Challenges
- **Blank 1**: Fill in `with open("Gamertags.txt", _____) as f:` for appending. Then write `f.write("\n" + new_tag)`. What does the `"\n"` do, and why does it come before the tag?
- **Blank 2**: Write `save_gamertags(filename, gamer_tag_list)` using `"w"` mode. Loop over the list and write each tag followed by `"\n"`. What method on `f` writes a string?
- **Blank 3**: In `add_new_user_name(self)`, after appending to the file, also append to `self.gamer_tag_list`. What list method appends a single item?
- **Challenge**: The C# code uses `File.AppendAllText` which opens, writes, and closes in one call. Your Python version uses `with open(..., "a")`. What would happen if you opened the file in `"w"` mode instead of `"a"` mode each time you add a gamertag? Test it with two additions and observe.
