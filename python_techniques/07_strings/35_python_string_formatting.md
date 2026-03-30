# Python String Formatting

**W3Schools Link:** https://www.w3schools.com/python/python_string_formatting.asp

**Homework Day(s):** Day 1, Days 8–10

---

## Overview
Python offers multiple ways to format strings: f-strings (Python 3.6+), `.format()`, and the older `%` operator. F-strings are the modern standard — they are readable, fast, and support format specifications directly inside the curly braces. Format specifiers control alignment, padding, decimal places, and number formatting.

## Key Concepts
- **f-strings**: `f"Name: {variable}"` — embed expressions directly
- **Format specifiers**: `{value:format_spec}` inside f-strings or `.format()`
- **Alignment**: `<` left, `>` right, `^` center, with optional width `{x:<15}`
- **Number formatting**: `,` for thousands separator, `.2f` for 2 decimal places
- **Padding character**: `{x:=^20}` pads with `=` centered in 20 chars
- **`.format()`**: `"Name: {}".format(name)` — older style, still valid
- **`%` formatting**: `"Name: %s" % name` — legacy style, avoid in new code

## Syntax / Example Code
```python
gamertag = "ShadowHunter99"
platform = "Xbox"
score = 4250
accuracy = 87.523

# --- f-string basics ---
print(f"Player: {gamertag}")
print(f"Platform: {platform}")
print(f"Score: {score}")

# --- Expressions inside f-strings ---
tags = ["ShadowX", "NightOwl", "ProSniper"]
print(f"Total players: {len(tags)}")
print(f"Uppercase: {gamertag.upper()}")
print(f"Score doubled: {score * 2}")

# --- Number formatting ---
print(f"Score: {score:,}")            # 4,250  (thousands separator)
print(f"Score: {score:>10,}")         # right-aligned in 10 chars: "     4,250"
print(f"Accuracy: {accuracy:.1f}%")   # 87.5%  (1 decimal place)
print(f"Accuracy: {accuracy:.2f}%")   # 87.52%
print(f"Hex score: {score:#x}")       # 0x109a

# --- String alignment ---
print(f"{'Gamertag':<16} {'Platform':<14} {'Score':>8}")
print(f"{'ShadowX':<16} {'Xbox':<14} {4250:>8,}")
print(f"{'NightOwl':<16} {'PlayStation':<14} {3300:>8,}")
print(f"{'ProSniper':<16} {'PC':<14} {5100:>8,}")

# --- Padding with a fill character ---
print(f"{'LEADERBOARD':=^40}")   # ===============LEADERBOARD===============
print(f"{'ShadowX':*<20}")       # ShadowX************

# --- Multi-line formatted output ---
def display_player(player):
    tag   = player['gamertag']
    plat  = player['platform']
    sc    = player['score']
    print(f"  {'Gamertag':<10}: {tag}")
    print(f"  {'Platform':<10}: {plat}")
    print(f"  {'Score':<10}: {sc:,}")

players = [
    {"gamertag": "ShadowX",   "platform": "Xbox",        "score": 4250},
    {"gamertag": "NightOwl",  "platform": "PlayStation", "score": 3300},
]
for p in players:
    display_player(p)
    print()

# --- .format() style (older) ---
msg = "Player: {}, Score: {:,}".format(gamertag, score)
print(msg)

msg = "Player: {gamertag}, Score: {score:,}".format(gamertag=gamertag, score=score)
print(msg)

# --- Multiline f-string ---
summary = (
    f"{'=' * 35}\n"
    f"  Gamertag : {gamertag}\n"
    f"  Platform : {platform}\n"
    f"  Score    : {score:,}\n"
    f"{'=' * 35}"
)
print(summary)

# --- Debug: variable name = value (Python 3.8+) ---
x = 42
print(f"{x=}")         # x=42
print(f"{score=}")     # score=4250
```

## Common Use Cases
- Building aligned, fixed-width leaderboard tables with `:<15` and `:>8`
- Displaying scores with thousands separators: `f"{score:,}"`
- Printing section headers: `f"{'LEADERBOARD':=^40}"`
- Generating CSV-compatible output: `f"{tag},{platform},{score}"`

## Related Days
| Day | Topic |
|-----|-------|
| Day 1 | Python Foundations (variables, data types, strings, lists) |
| Days 8-10 | Build project skeleton, data loading, display |

## See Also
- [05_python_strings.md](../02_data_types/05_python_strings.md)
- [31_python_print.md](../06_file_io/31_python_print.md)
- [32_python_string_methods.md](32_python_string_methods.md)

## Practice Tips
- Build a `display_player_table(players)` function using aligned f-string format specifiers
- Practice all three alignment specs: `<` (left), `>` (right), `^` (center)
- Use `{score:,}` for all score displays to make large numbers readable
- Try `f"{'Title':=^40}"` to create styled section headers in your console UI
