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

```
C# pattern (from the gamertag project):
    internal class Gamertags
    {
        private string[] gamerTagList = { };
        // methods like LoadGamertags(), PrintAllGamertags(), etc.
    }

Python skeleton — define a Gamertags class (fill in the blanks):

    _____ Gamertags:
        """Manages a collection of gamertags loaded from a file."""

        _____ _____(self):
            self.gamer_tag_list = _____   # empty list, like string[] gamerTagList = { }

        _____ load_gamertags(self):
            pass  # you'll implement file reading here

        _____ print_all_gamertags(self):
            pass  # you'll implement display here

    # Creating an instance (like: Gamertags gt = new Gamertags(); in C#)
    gt = _____()
    gt._____(   )

Questions:
- What Python keyword starts a class definition? (Hint: it is NOT "internal class")
- How do you define a method that belongs to a specific instance? What is the
  mandatory first parameter called?
- What is the Python equivalent of C#'s constructor? What special name does it have?
- How do you call a method on your instance `gt`? What syntax do you use?

Test challenge:
    Create an instance of your Gamertags class, call load_gamertags() on it, then
    call print_all_gamertags(). What happens if load_gamertags() hasn't been
    implemented yet? What should print_all_gamertags() print when the list is empty?
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

## Challenges
- **Blank 1**: Define a `Gamertags` class with an `__init__` that sets `self.gamer_tag_list = _____`. What value makes an empty list in Python?
- **Blank 2**: Add a `show_welcome_message(self)` method. What should it print? How does it match the C# `ShowWelcomeMessage()` method?
- **Blank 3**: Add a `__str__` method that returns `f"Gamertags: _____ entries"`. What attribute gives you the count?
- **Challenge**: C# uses `Console.WriteLine()` to print. What Python function do you call inside your methods? Write the `show_welcome_message` method body using only that function.
