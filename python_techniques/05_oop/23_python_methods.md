# Python Methods

**W3Schools Link:** https://www.w3schools.com/python/python_classes.asp

---

## Overview
Methods are functions defined inside a class. They define the behavior of objects — what an object can do. Python has three types of methods: instance methods (operate on a specific object), class methods (operate on the class itself), and static methods (utility functions logically grouped in the class). Instance methods are by far the most common.

## Key Concepts
- **Instance method**: takes `self` as first parameter; accesses the specific object's attributes
- **Class method**: decorated with `@classmethod`; takes `cls` as first parameter; accesses the class
- **Static method**: decorated with `@staticmethod`; takes no special first parameter; no access to instance or class
- **Dunder (magic) methods**: special `__method__` names called by Python automatically (`__str__`, `__len__`, `__eq__`)
- **Method chaining**: returning `self` from a method enables `obj.method1().method2()`
- **`self` is explicit**: Python does not pass the instance automatically in the syntax — it's a convention, always named `self`

## Syntax / Example Code
```python
class Player:
    """Represents a gamertag entry with full behavior."""

    valid_platforms = {"Xbox", "PlayStation", "PC", "Nintendo Switch"}

    def __init__(self, gamertag, platform="PC", score=0):
        self.gamertag = gamertag
        self.platform = platform
        self.score = score

    # --- Instance methods ---

    def get_rank(self):
        """Return rank based on score."""
        if self.score >= 5000: return "Diamond"
        if self.score >= 3000: return "Gold"
        if self.score >= 1000: return "Silver"
        return "Bronze"

    def add_score(self, points):
        """Add points and return self for chaining."""
        self.score += points
        return self   # enables chaining

    def is_valid(self):
        """Return True if this player record is valid."""
        return (
            bool(self.gamertag)
            and self.gamertag.isalnum()
            and 3 <= len(self.gamertag) <= 15
            and self.platform in Player.valid_platforms
        )

    def to_csv(self):
        """Return a CSV string representation."""
        return f"{self.gamertag},{self.platform},{self.score}"

    # --- Dunder methods ---

    def __str__(self):
        return f"{self.gamertag} ({self.platform}) — {self.score} pts [{self.get_rank()}]"

    def __repr__(self):
        return f"Player({self.gamertag!r}, {self.platform!r}, {self.score})"

    def __eq__(self, other):
        """Two players are equal if they share the same gamertag (case-insensitive)."""
        if isinstance(other, Player):
            return self.gamertag.lower() == other.gamertag.lower()
        return False

    def __lt__(self, other):
        """Allow sorting players by score."""
        return self.score < other.score

    # --- Class method (alternate constructor) ---

    @classmethod
    def from_csv(cls, line):
        """Create a Player from 'gamertag,platform,score'."""
        parts = line.strip().split(",")
        return cls(parts[0], parts[1], int(parts[2]))

    # --- Static method (utility, no instance/class needed) ---

    @staticmethod
    def is_valid_gamertag(tag):
        """Check if a string is a valid gamertag format."""
        return bool(tag) and tag.isalnum() and 3 <= len(tag) <= 15


# Using instance methods
p = Player("ShadowX", "Xbox", 3500)
print(p)                # uses __str__
print(p.get_rank())     # Gold
p.add_score(500).add_score(200)   # method chaining
print(p.score)          # 4200
print(p.to_csv())       # ShadowX,Xbox,4200

# Using class method
p2 = Player.from_csv("NightOwl,PlayStation,3300")
print(p2)

# Using static method (no instance needed)
print(Player.is_valid_gamertag("GamerX"))   # True
print(Player.is_valid_gamertag("AB"))       # False

# Dunder methods enable natural Python behavior
players = [
    Player("ProSniper", "PC", 5100),
    Player("GamerZ", "Xbox", 900),
    Player("ShadowX", "Xbox", 4200),
]
players.sort()   # uses __lt__
for p in players:
    print(p)
```

## Common Use Cases
- `to_csv()` — serialize a player for file writing
- `from_csv()` (classmethod) — deserialize a line from file
- `is_valid_gamertag()` (staticmethod) — reusable format checker
- `__str__` — clean display output when printing player objects

## Related Days
| Day | Topic |
|-----|-------|
| Days 8-10 | Build project skeleton, data loading, display |

## See Also
- [21_python_classes.md](21_python_classes.md)
- [22_python_constructors.md](22_python_constructors.md)
- [24_python_inheritance.md](24_python_inheritance.md)

## Practice Tips
- Implement `to_csv()` and `from_csv()` to round-trip player data through a file
- Add `__eq__` to make duplicate detection work with `==`
- Implement `__lt__` to enable `sorted(players)` without a key argument
- Try method chaining by returning `self` from methods that modify the object
