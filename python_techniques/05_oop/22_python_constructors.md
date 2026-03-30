# Python Constructors (`__init__`)

**W3Schools Link:** https://www.w3schools.com/python/python_classes.asp

**Homework Day(s):** Days 8–10

---

## Overview
The `__init__` method is Python's constructor — a special method automatically called when a new object is created from a class. It initializes the object's attributes with the values passed at creation time. Every class that needs to set up initial state should define `__init__`. Its name is surrounded by double underscores, making it a "dunder" (magic) method.

## Key Concepts
- **Called automatically**: runs immediately when you write `Player("ShadowX")`
- **`self` is the instance**: always the first parameter; Python passes it automatically
- **Sets instance attributes**: `self.attribute = value` inside `__init__`
- **Can accept any parameters**: with or without defaults
- **Does not return a value**: any `return` in `__init__` must be bare `return` or return `None`
- **Validation in `__init__`**: you can validate inputs and raise exceptions if invalid
- **`__new__` vs `__init__`**: `__new__` creates the object; `__init__` initializes it — you'll almost always only need `__init__`

## Syntax / Example Code
```python
class Player:
    """Represents a gamertag entry."""

    def __init__(self, gamertag, platform="PC", score=0):
        """
        Initialize a Player.

        Args:
            gamertag (str): The player's unique gamertag.
            platform (str): Gaming platform. Defaults to 'PC'.
            score (int): Initial score. Defaults to 0.
        """
        # Validate before storing
        if not gamertag or not gamertag.isalnum():
            raise ValueError(f"Invalid gamertag: '{gamertag}'")
        if len(gamertag) < 3 or len(gamertag) > 15:
            raise ValueError(f"Gamertag length must be 3–15 characters")

        self.gamertag = gamertag
        self.platform = platform
        self.score = int(score)   # ensure correct type
        self.active = True        # default attribute not in parameters

    def __str__(self):
        return f"{self.gamertag} ({self.platform}): {self.score} pts"


# Creating instances — __init__ called automatically
p1 = Player("ShadowX", "Xbox", 4250)
p2 = Player("NightOwl")                # uses defaults: PC, 0
p3 = Player("ProSniper", score=5100)   # keyword argument

print(p1)   # ShadowX (Xbox): 4250 pts
print(p2)   # NightOwl (PC): 0 pts

# Accessing attributes set in __init__
print(p1.gamertag)   # ShadowX
print(p1.platform)   # Xbox
print(p1.score)      # 4250
print(p1.active)     # True

# Validation in __init__ raises exceptions
try:
    bad = Player("AB")   # too short
except ValueError as e:
    print(f"Error: {e}")

try:
    bad = Player("Shadow Hunter")  # spaces not allowed
except ValueError as e:
    print(f"Error: {e}")

# Creating from a CSV line (factory pattern)
class PlayerFromCSV(Player):
    @classmethod
    def from_csv(cls, line):
        """Create a Player from a CSV string 'gamertag,platform,score'."""
        parts = line.strip().split(",")
        if len(parts) != 3:
            raise ValueError(f"Invalid CSV line: {line}")
        return cls(parts[0], parts[1], int(parts[2]))

p4 = PlayerFromCSV.from_csv("GamerZ,Xbox,2100")
print(p4)
```

## Common Use Cases
- Setting all player attributes (`gamertag`, `platform`, `score`) in one place
- Validating input data immediately when a `Player` object is created
- Providing sensible defaults for optional fields like `platform` and `score`
- Using `@classmethod` factory methods like `from_csv()` for alternate constructors

## Related Days
| Day | Topic |
|-----|-------|
| Days 8-10 | Build project skeleton, data loading, display |

## See Also
- [21_python_classes.md](21_python_classes.md)
- [23_python_methods.md](23_python_methods.md)
- [37_python_exceptions.md](../08_error_handling/37_python_exceptions.md)
- [38_python_raising_exceptions.md](../08_error_handling/38_python_raising_exceptions.md)

## Practice Tips
- Always validate input in `__init__` and raise `ValueError` for bad data
- Set every attribute your class needs in `__init__` — don't create attributes elsewhere
- Use default parameter values for optional fields
- Test construction with both valid and invalid data to verify your validation works
