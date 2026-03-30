# Python Function Arguments

**W3Schools Link:** https://www.w3schools.com/python/python_functions.asp

**Homework Day(s):** Day 4

---

## Overview
Function arguments allow you to pass data into functions, making them flexible and reusable. Python supports positional arguments, keyword arguments, default parameter values, and variable-length argument lists (`*args`, `**kwargs`). Understanding how to design function signatures is key to writing clean, flexible code.

## Key Concepts
- **Positional arguments**: passed in order — `func(a, b, c)`
- **Keyword arguments**: passed by name — `func(name="GamerX", score=4250)`
- **Default parameter values**: used when an argument is not provided — `def func(platform="PC")`
- **`*args`**: collects extra positional arguments into a tuple
- **`**kwargs`**: collects extra keyword arguments into a dictionary
- **Argument order**: positional → `*args` → keyword with defaults → `**kwargs`
- **Immutable defaults**: avoid mutable defaults like `[]` or `{}` — use `None` instead

## Syntax / Example Code

**C# pattern (from the gamertag project):**
```csharp
// C# methods in the Gamertags class access fields directly —
// no parameters needed because data lives on the object.
public void PrintAllGamertags()
{
    foreach (string s in gamerTagList)  // accesses class field
        Console.WriteLine(s);
}
// In Python we pass data explicitly as arguments instead.
```

**Python skeleton (fill in the blanks):**
```
# Positional argument — data passed in order by position
def display_gamertag(_____, _____):    # name the two parameters
    print(f"{_____} | {_____}")

display_gamertag(_____, _____)         # pass values in order

# Keyword arguments — pass by name (order doesn't matter)
display_gamertag(_____ = "Xbox", _____ = "ShadowHunter99")

# Default parameter values — optional arguments
def create_player(gamertag, platform=_____, score=_____):
    return {
        "gamertag": _____,
        "platform": _____,
        "score": _____
    }

p1 = create_player("ShadowX")                   # uses all defaults
p2 = create_player("NightOwl", _____, _____)     # overrides platform and score
p3 = create_player("ProSniper", score=_____)     # keyword override only

# *args — accept ANY number of positional arguments as a tuple
def print_tags(*_____):
    for i, tag in _____(_____, 1):
        print(f"  {_____}. {_____}")

print_tags(_____, _____, _____)        # pass as many as you want

# AVOID mutable defaults — use None instead
def add_gamertag(tag, player_list=_____):    # NOT player_list=[]
    if player_list _____ _____:
        player_list = []
    player_list._____(tag)
    _____ player_list
```

**Questions:**
- C# methods in the `Gamertags` class use class fields for data. In Python functions, how do you give a function access to the gamertag list?
- What is the difference between a positional argument and a keyword argument?
- What does a default parameter value do? When would you use `platform="PC"` as a default?
- Why should you use `player_list=None` instead of `player_list=[]` as a default? What subtle bug does the mutable default cause?

**Test challenge:**
Write a `create_player` function with `gamertag` required and `platform`, `score` optional with defaults. Call it three ways: with only `gamertag`, with all three positional, and with `gamertag` plus `score` as a keyword argument skipping `platform`.

## Common Use Cases
- `create_player(tag, platform="PC")` — sensible defaults for optional fields
- `display_player(*player_tuple)` — unpacking stored tuples into function calls
- `filter_players(players, platform=None, min_score=0)` — optional filters
- `*args` for functions that accept variable numbers of gamertags

## Related Days
| Day | Topic |
|-----|-------|
| Day 4 | Functions (decomposition, inputs/outputs, naming) |

## See Also
- [17_python_functions.md](17_python_functions.md)
- [19_python_return_values.md](19_python_return_values.md)
- [07_python_tuples.md](../02_data_types/07_python_tuples.md)
- [09_python_dictionaries.md](../02_data_types/09_python_dictionaries.md)

## Challenges

1. **Positional vs keyword:** Call `display_player` both ways — positional then keyword:
   ```
   def display_player(gamertag, platform, score):
       print(f"{gamertag} | {platform} | {score}")

   display_player(_____, _____, _____)                          # positional
   display_player(score=_____, gamertag=_____, platform=_____)  # keyword
   ```

2. **Default arguments:** Add defaults so `platform` and `score` are optional:
   ```
   def create_player(gamertag, platform=_____, score=_____):
       return {"gamertag": gamertag, "platform": platform, "score": score}

   p = create_player("GhostPlayer")    # uses defaults
   print(p)                            # what does p look like?
   ```

3. **Mutable default trap:** What goes wrong with this function? Fix it:
   ```
   def add_gamertag(tag, player_list=[]):    # ← what is the problem?
       player_list.append(tag)
       return player_list

   # Fix:
   def add_gamertag(tag, player_list=_____):
       if player_list _____ _____:
           player_list = _____
       player_list.append(tag)
       return player_list
   ```

4. **\*args:** Write a function that accepts any number of gamertags and prints them numbered:
   ```
   def print_tags(*_____):
       for i, tag in enumerate(_____, 1):
           print(f"{_____}. {_____}")

   print_tags("ShadowX", "NightOwl", "ProSniper")
   ```
