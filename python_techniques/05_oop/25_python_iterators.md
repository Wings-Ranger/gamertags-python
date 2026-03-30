# Python Iterators

**W3Schools Link:** https://www.w3schools.com/python/python_iterators.asp

**Homework Day(s):** Day 3, Day 8, Day 9, Day 10

---

## Overview
An iterator is an object that implements the iterator protocol: `__iter__()` and `__next__()`. Python's `for` loop works by calling these methods automatically. You can create custom iterators to define how an object is traversed, and generators provide a simpler way to build iterators using the `yield` keyword.

## Key Concepts
- **Iterable**: any object you can loop over — lists, strings, files, ranges, dicts
- **Iterator**: an iterable that tracks its current position; has `__iter__` and `__next__`
- **`iter(obj)`**: converts an iterable to an iterator
- **`next(iterator)`**: returns the next item; raises `StopIteration` when exhausted
- **Generator**: a function that uses `yield` to produce items one at a time — the simplest way to create an iterator
- **Lazy evaluation**: generators produce items on demand, saving memory for large datasets
- **`yield` vs `return`**: `yield` pauses the function and resumes on the next `next()` call

## Syntax / Example Code

```
C# pattern (from the gamertag project):
    // C# foreach uses IEnumerable — the iterator protocol under the hood
    foreach (string s in gamerTagList)
    {
        Console.WriteLine(s);
    }

Python skeleton — understand how iteration works (fill in the blanks):

    gamertags = ["ShadowX", "NightOwl", "ProSniper"]

    # The for loop uses the iterator protocol automatically:
    for _____ in gamertags:
        print(_____)

    # Under the hood, Python does this:
    it = _____(gamertags)    # what built-in creates an iterator?
    print(_____(it))         # what built-in gets the next item?
    print(_____(it))
    print(_____(it))
    # calling next() one more time raises: _____

    # Custom iterator class for Gamertags
    class GamertagIterator:
        def _____(self, tags):
            self.tags = tags
            self.index = _____       # where does iteration start?

        def _____(self):
            return _____             # what does __iter__ return for an iterator?

        def _____(self):
            if self.index < len(self.tags):
                tag = self.tags[self.index]
                self.index _____ 1   # advance the index
                return tag
            raise _____              # what stops the iteration?

    # Generator function (simpler alternative to a full iterator class)
    def active_gamertags(tags):
        for tag in tags:
            if tag:               # skip empty strings
                _____ tag         # what keyword produces one value and pauses?

    for tag in active_gamertags(gamertags):
        print(tag)

Questions:
- What two special methods make a class iterable?
- What exception signals that iteration is complete?
- What keyword turns a function into a generator?
- Why might you use a generator instead of building a full list in memory?

Test challenge:
    Write a generator function called filtered_gamertags(tags, ending_digit=True)
    that yields only tags ending with a digit. Test it with your gamertag list.
    How does it compare to the list comprehension approach?
```

## Common Use Cases
- Reading large gamertag files lazily with a generator (avoids loading all into memory)
- Building a custom `PlayerIterator` that filters as it iterates
- Using generator expressions for memory-efficient data transformations
- Implementing `__iter__` on a `GamertagManager` class so it's directly loopable

## Related Days
| Day | Topic |
|-----|-------|
| Day 3 | Loops and Program Flow (while loops, iterating lists) |
| Day 8 | Python Project Skeleton |
| Day 9 | Data Loading and Welcome Sequence |
| Day 10 | Display All Gamertags |

## See Also
- [14_python_for_loops.md](../03_control_flow/14_python_for_loops.md)
- [06_python_lists.md](../02_data_types/06_python_lists.md)
- [21_python_classes.md](21_python_classes.md)
- [27_python_file_read.md](../06_file_io/27_python_file_read.md)

## Challenges
- **Blank 1**: Implement `GamertagIterator.__next__`. It should return `self.tags[self.index]` and increment `self.index`. What exception do you raise when `self.index >= len(self.tags)`?
- **Blank 2**: Write a generator function `read_gamertag_file(filename)` that opens the file and `yield`s each non-blank line (stripped). What keyword do you use instead of `return` to produce one line at a time?
- **Blank 3**: Write a generator expression (one line) that produces only gamertags ending with a digit: `ending_digit = (_____ for s in gamertags if _____)`. What condition checks the last character?
- **Challenge**: The C# `foreach` loop and Python `for` loop look similar. What happens in Python if you call `iter()` on a plain integer like `iter(42)`? Try it. What does that error tell you about what makes something iterable?
