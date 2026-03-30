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

```
C# context:
    // The gamertag project uses a single Gamertags class — no inheritance.
    // Inheritance is a general OOP concept you may apply when extending the project.

    // C# inheritance syntax:
    class ProPlayer : Player   // ProPlayer inherits from Player
    {
        public string Team { get; set; }

        public ProPlayer(string gamertag, string team) : base(gamertag)
        {
            this.Team = team;
        }
    }

Python skeleton — translate inheritance (fill in the blanks):

    class Player:
        def _____(self, gamertag, platform="PC"):
            self.gamertag = _____
            self.platform = _____

        def display(self):
            print(f"Tag: {self._____}")

    # Child class inherits from Player
    class ProPlayer(_____):   # what goes in the parentheses?

        def _____(self, gamertag, platform, team):
            _____.__init__(_____, gamertag, platform)  # call parent constructor
            self.team = _____

        def display(self):        # overrides parent display()
            _____._____()         # call parent version first
            print(f"Team: {self._____}")

    # Using isinstance() — Python equivalent of C#'s 'is' keyword
    pro = ProPlayer("ShadowX", "Xbox", "TeamPhoenix")
    print(isinstance(pro, Player))    # _____ (True or False?)
    print(isinstance(pro, ProPlayer)) # _____ (True or False?)

Questions:
- How do you specify a parent class in Python? Where does it go in the class definition?
- What function calls the parent class's method? (C# uses `: base(...)`)
- What is method overriding? When would you override `display()` in `ProPlayer`?
- What does `isinstance(obj, Class)` return when `obj` is a subclass instance?

Test challenge:
    Create a list containing both a `Player` and a `ProPlayer` instance. Loop over
    the list and call `display()` on each. Notice that each prints differently —
    that is called polymorphism. What determines which `display()` gets called?
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

## Challenges
- **Blank 1**: Write the `ProPlayer.__init__` so it calls the parent constructor with `super().__init__(_____, _____)`. What arguments does `Player.__init__` expect?
- **Blank 2**: Override `display()` in `ProPlayer`. First call `super().display()`, then print the team. Why do you call `super().display()` rather than duplicating the code?
- **Blank 3**: Write `isinstance(pro, _____)` to check if `pro` is a `Player`. What class name goes in the blank?
- **Challenge**: C# uses `: base(...)` in a constructor to call the parent. Python uses `super().__init__(...)`. Write both side-by-side in comments in your Python file. What are the key differences in syntax? What happens if you forget to call `super().__init__()` in a child class?
