"""
#### Task 6.2
Implement custom dictionary that will memorize 10 latest changed keys.
Using method "get_history" return this keys.


Example:
```python
 d = HistoryDict({"foo": 42})
 d.set_value("bar", 43)
 d.set_value("foo", 1)
 d.get_history()

["bar", "foo"]
```
"""


class HistoryDict:
    def __init__(self, dict=None):
        if dict == None:
            self.dict = {}
        else:
            self.dict = dict
        self.history = []

    def set_value(self, key, value):
        self.dict[key] = value
        self.history.append(key)

    def get_history(self):
        return self.history


if __name__ == "__main__":
    d = HistoryDict({"foo": 42})
    d.set_value("bar", 43)
    d.set_value("foo", 1)
    assert d.get_history() == ["bar", "foo"]
    assert d.dict == {"foo": 1, "bar": 43}

    d = HistoryDict({"foo": 42})
    d.set_value("bar", 43)
    assert d.get_history() == ["bar"]
    assert d.dict == {"foo": 42, "bar": 43}

    d = HistoryDict()
    d.set_value("bar", 43)
    d.set_value("foo", 1)
    assert d.get_history() == ["bar", "foo"]
    assert d.dict == {"foo": 1, "bar": 43}
