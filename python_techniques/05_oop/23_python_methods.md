# Python Methods

**W3Schools Link:** https://www.w3schools.com/python/python_classes.asp

**Homework Day(s):** Days 8–10

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

```
C# pattern (from the gamertag project):
    internal class Gamertags
    {
        private string[] gamerTagList = { };

        public void LoadGamertags() { ... }
        public void PrintAllGamertags() { ... }
        public void PrintGamertagsEndingWithNumber() { ... }
        public void PrintGamertagsNotStartingWithNumberorLetter() { ... }
        public void ShowWelcomeMessage() { ... }
        public void AddNewUserName() { ... }
    }

Python skeleton — translate each method (fill in the blanks):

    class Gamertags:

        def _____(self):
            self.gamer_tag_list = _____

        # Instance method — translates LoadGamertags()
        def load_gamertags(_____, filename):
            # open the file, read lines into self.gamer_tag_list
            _____

        # Instance method — translates PrintAllGamertags()
        def print_all_gamertags(_____):
            for _____ in self.gamer_tag_list:
                print(_____)

        # Instance method — translates PrintGamertagsEndingWithNumber()
        def print_gamertags_ending_with_number(_____):
            for s in self._____:
                if s[_____]._____(  ):   # check last character
                    print(s)

        # Static method — a utility that doesn't need self
        @_____
        def is_valid_gamertag(tag):
            return _____ and tag._____(  ) and 3 <= len(tag) <= _____

Questions:
- Every instance method has what as its first parameter?
- C# uses `public void` and `private void`. How does Python mark a method's
  visibility? (Hint: check the W3Schools link — Python doesn't use keywords)
- What decorator turns a method into a static method?
- C# uses `foreach (string s in gamerTagList)`. What is the Python equivalent loop?

Test challenge:
    Implement print_all_gamertags(self). Then call it on an instance where
    gamer_tag_list is empty. What gets printed? How would you add a message
    like "No gamertags found" when the list is empty?
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

## Challenges
- **Blank 1**: Write the `print_all_gamertags(self)` method body. It should loop over `self.gamer_tag_list` and print each tag. What loop syntax do you use?
- **Blank 2**: Write `print_gamertags_ending_with_number(self)`. You need to check the last character of each string `s`. In C# that's `s[s.Length - 1]`. What is the Python equivalent index for the last character?
- **Blank 3**: Write `add_new_user_name(self)`. It should call `input(_____)`  to get a gamertag, then append it to `self.gamer_tag_list`. What list method adds an item to the end?
- **Challenge**: The C# `AddNewUserName()` also writes to the file with `File.AppendAllText`. Where should your Python method do the file write — inside `add_new_user_name` or in a separate method? What are the trade-offs of each approach?
