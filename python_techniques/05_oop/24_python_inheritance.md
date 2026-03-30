# Python Inheritance

**W3Schools Link:** https://www.w3schools.com/python/python_inheritance.asp

**Homework Day(s):** Days 8–10

---

## Overview
Inheritance allows a class (child/subclass) to acquire the attributes and methods of another class (parent/superclass). It promotes code reuse and models "is-a" relationships — a `ProPlayer` is a `Player`. Python supports single and multiple inheritance, and the `super()` function is used to call the parent class's methods.

## Key Concepts
- **Syntax**: `class Child(Parent):`
- **`super()`**: calls the parent class's method — commonly used in `__init__`
- **Method overriding**: the child redefines a method from the parent
- **`isinstance(obj, Class)`**: checks if an object is an instance of a class (or subclass)
- **`issubclass(Child, Parent)`**: checks class hierarchy
- **Multiple inheritance**: `class C(A, B):` — Python uses MRO (Method Resolution Order)
- **`__mro__`**: shows the method resolution order for a class

## Syntax / Example Code
```python
# Base (parent) class
class Player:
    """Base class for all player types."""

    def __init__(self, gamertag, platform="PC", score=0):
        self.gamertag = gamertag
        self.platform = platform
        self.score = score

    def get_rank(self):
        if self.score >= 5000: return "Diamond"
        if self.score >= 3000: return "Gold"
        if self.score >= 1000: return "Silver"
        return "Bronze"

    def __str__(self):
        return f"{self.gamertag} ({self.platform}): {self.score} pts"

    def display(self):
        print(f"  Tag   : {self.gamertag}")
        print(f"  Plat  : {self.platform}")
        print(f"  Score : {self.score}")
        print(f"  Rank  : {self.get_rank()}")


# Child class — adds competitive attributes
class ProPlayer(Player):
    """A competitive player with team and tournament data."""

    def __init__(self, gamertag, platform, score, team, tournaments_won=0):
        super().__init__(gamertag, platform, score)   # call parent __init__
        self.team = team
        self.tournaments_won = tournaments_won

    def get_rank(self):
        """Override: pro players have an extended ranking system."""
        base = super().get_rank()
        if self.tournaments_won >= 10:
            return f"Pro Legend ({base})"
        return f"Pro ({base})"

    def display(self):
        super().display()   # call parent display
        print(f"  Team  : {self.team}")
        print(f"  Wins  : {self.tournaments_won} tournaments")

    def __str__(self):
        return f"[PRO] {self.gamertag} — Team: {self.team}"


# Another child class — casual player
class CasualPlayer(Player):
    """A casual player tracked by hours played."""

    def __init__(self, gamertag, platform, hours_played=0):
        super().__init__(gamertag, platform, score=0)
        self.hours_played = hours_played

    def estimate_score(self):
        """Estimate a score based on hours played."""
        self.score = self.hours_played * 10
        return self.score


# Creating instances
regular = Player("ShadowX", "Xbox", 4250)
pro = ProPlayer("NightOwl", "PlayStation", 7200, team="TeamPhoenix", tournaments_won=12)
casual = CasualPlayer("GamerZ", "PC", hours_played=150)

print(regular)
print(pro)

pro.display()

# isinstance and issubclass
print(isinstance(pro, Player))      # True — ProPlayer IS a Player
print(isinstance(pro, ProPlayer))   # True
print(isinstance(regular, ProPlayer))  # False

print(issubclass(ProPlayer, Player))   # True
print(issubclass(Player, ProPlayer))   # False

# Polymorphism — same method call, different behavior
all_players = [regular, pro, casual]
for p in all_players:
    print(f"{p.gamertag}: {p.get_rank()}")  # calls each class's get_rank()
```

## Common Use Cases
- Extending a base `Player` class with `ProPlayer` or `CasualPlayer` subtypes
- Sharing common logic (loading, validation) in a base class
- Overriding `get_rank()` or `display()` for specialized behavior
- Using `isinstance()` to handle different player types in the same list

## Related Days
| Day | Topic |
|-----|-------|
| Days 8-10 | Build project skeleton, data loading, display |

## See Also
- [21_python_classes.md](21_python_classes.md)
- [22_python_constructors.md](22_python_constructors.md)
- [23_python_methods.md](23_python_methods.md)

## Practice Tips
- Create a `ProPlayer` subclass that adds a `team` attribute to your `Player` class
- Always call `super().__init__(...)` at the start of a child `__init__`
- Practice polymorphism: put both `Player` and `ProPlayer` in the same list and call the same method
- Use `isinstance()` instead of checking `type(obj) == ClassName` for flexibility
