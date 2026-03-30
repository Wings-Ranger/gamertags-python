# Python Classes

**W3Schools Link:** https://www.w3schools.com/python/python_classes.asp

**Homework Day(s):** Days 8–10

---

## Overview
A class is a blueprint for creating objects. Classes bundle data (attributes) and behavior (methods) together — the core idea of object-oriented programming (OOP). In Python, everything is an object, and defining your own classes lets you model real-world entities like a `Player` or `GamertagManager` in your project.

## Key Concepts
- **Class definition**: `class ClassName:` — by convention, class names use PascalCase
- **Instance**: an object created from a class — `player = Player("ShadowX")`
- **Attributes**: data stored on the object — `self.gamertag = gamertag`
- **Methods**: functions defined inside a class that operate on the object
- **`self`**: the first parameter of every instance method; refers to the current object
- **`__init__`**: the constructor method — called automatically when creating an instance
- **`__str__`**: defines the string representation of an object (`str(obj)` / `print(obj)`)

## Syntax / Example Code
```python
# Basic class definition
class Player:
    """Represents a registered player in the gamertag system."""

    # Class attribute (shared by all instances)
    platform_options = ["Xbox", "PlayStation", "PC", "Nintendo Switch"]

    def __init__(self, gamertag, platform="PC", score=0):
        """Initialize a new Player instance."""
        self.gamertag = gamertag
        self.platform = platform
        self.score = score

    def __str__(self):
        """Return a human-readable string representation."""
        return f"{self.gamertag} ({self.platform}) — Score: {self.score}"

    def __repr__(self):
        """Return a developer-friendly representation."""
        return f"Player(gamertag='{self.gamertag}', platform='{self.platform}', score={self.score})"

    def get_rank(self):
        """Return the player's rank based on score."""
        if self.score >= 5000:
            return "Diamond"
        elif self.score >= 3000:
            return "Gold"
        elif self.score >= 1000:
            return "Silver"
        else:
            return "Bronze"

    def add_score(self, points):
        """Add points to the player's score."""
        self.score += points

    def is_valid(self):
        """Return True if the gamertag meets requirements."""
        tag = self.gamertag
        return bool(tag) and 3 <= len(tag) <= 15 and tag.isalnum()


# Creating instances
p1 = Player("ShadowHunter99", "Xbox", 4250)
p2 = Player("NightOwl", "PlayStation", 3300)
p3 = Player("ProSniper")    # uses defaults: PC, score=0

# Accessing attributes and calling methods
print(p1.gamertag)      # ShadowHunter99
print(p1.score)         # 4250
print(p1.get_rank())    # Gold
print(p1)               # ShadowHunter99 (Xbox) — Score: 4250

p1.add_score(1000)
print(p1.score)         # 5250
print(p1.get_rank())    # Diamond

# Checking validity
print(p1.is_valid())    # True

# List of Player objects
players = [p1, p2, p3]
for player in players:
    print(f"{player} | Rank: {player.get_rank()}")

# Accessing class attribute
print(Player.platform_options)

# Sorting Player objects
ranked = sorted(players, key=lambda p: p.score, reverse=True)
```

## Common Use Cases
- `Player` class to encapsulate gamertag, platform, and score together
- `GamertagManager` class to handle loading, saving, and searching players
- `__str__` for clean display output
- Class methods for validation logic tied to the Player concept

## Related Days
| Day | Topic |
|-----|-------|
| Days 8-10 | Build project skeleton, data loading, display |

## See Also
- [22_python_constructors.md](22_python_constructors.md)
- [23_python_methods.md](23_python_methods.md)
- [24_python_inheritance.md](24_python_inheritance.md)

## Practice Tips
- Rewrite your gamertag project's player data as `Player` objects instead of dicts
- Implement `__str__` so `print(player)` gives useful output automatically
- Start small: just `__init__` and one method; add more methods incrementally
- Test each method individually before integrating into the full project
