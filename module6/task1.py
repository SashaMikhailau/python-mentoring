"""
### Task 6.1
Implement a Counter class which optionally accepts the start value and the counter stop value.
If the start value is not specified the counter should begin with 0.
If the stop value is not specified it should be counting up infinitely.
If the counter reaches the stop value, print "Maximal value is reached."

Implement two methods: "increment" and "get"

* <em>If you are familiar with Exception rising use it to display the "Maximal value is reached." message.</em>

Example:
```python
c = Counter(start=42)
 c.increment()
 c.get()
43

 c = Counter()
 c.increment()
 c.get()
1
 c.increment()
 c.get()
2

 c = Counter(start=42, stop=43)
 c.increment()
 c.get()
43
 c.increment()
Maximal value is reached.
 c.get()
43
"""


class Counter:
    def __init__(self, start=0, stop=None):
        self.current = start
        self.stop = stop

    def increment(self):
        if self.stop == None or self.stop > self.current:
            self.current += 1
        else:
            raise AttributeError("Maximal value is reached.")

    def get(self):
        return self.current


if __name__ == "__main__":
    c = Counter(start=42)
    c.increment()
    assert c.get() == 43

    c = Counter()
    c.increment()
    assert c.get() == 1
    c.increment()
    assert c.get() == 2

    c = Counter(start=42, stop=43)
    c.increment()
    assert c.get() == 43
    try:
        c.increment()
    except AttributeError:
        pass
    assert c.get() == 43
