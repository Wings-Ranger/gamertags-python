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

```
C# pattern (from the gamertag project):
    internal class Gamertags
    {
        private string[] gamerTagList = { };
        // C# fields are initialized at declaration — no explicit constructor needed
        // for simple defaults. Python always uses __init__.
    }

Python skeleton — define the constructor (fill in the blanks):

    class Gamertags:

        def _____(self):
            # equivalent to: private string[] gamerTagList = { };
            self._____ = _____   # what Python type replaces string[]?

        def _____(self, gamertag, platform="PC"):
            # extra constructor with parameters — what name does this method have?
            self.gamertag = _____
            self.platform = _____

    # Calling the constructor — Python does NOT use the "new" keyword
    gt = _____()          # no arguments
    p  = _____(_____, _____)  # with arguments

Questions:
- What is the name of Python's constructor method? (It starts and ends with __)
- What is the first parameter of __init__ always called, and why?
- How do you set an instance attribute inside __init__? What prefix do you use?
- In C# you write `new Gamertags()`. What is the Python equivalent? (no keyword needed)

Test challenge:
    Create a Gamertags instance with no arguments, then print its gamer_tag_list
    attribute. What do you expect to see? Now try adding a value to gamer_tag_list
    from outside the class — can you do it? Should you?
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

## Challenges
- **Blank 1**: Write `__init__` for `Gamertags` so it sets `self.gamer_tag_list = _____`. What is the empty-list literal in Python?
- **Blank 2**: Add a second parameter `filename` to `__init__` with a default value of `_____`. What filename does the C# project use? (Hint: `"../Gamertags.txt"`)
- **Blank 3**: Inside `__init__`, write `self.filename = _____`. What value goes on the right side?
- **Challenge**: In C#, `private string[] gamerTagList = { }` is declared at class level. In Python, where does attribute initialization belong? Try declaring `gamer_tag_list = []` at class level instead of in `__init__` — what surprising behavior might that cause when you have multiple instances?
