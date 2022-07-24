"""### Task 6.6
Implement a class Money to represent value and currency.
You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication, addition and subtraction).
Tip: use class attribute exchange rate which is dictionary and stores information about exchange rates to your default currency:
```python
exchange_rate = {
    "EUR": 0.93,
    "BYN": 2.1,
    "JOY": 130.84,
    ...
}
```

Example:
```python
x = Money(10, "BYN")
y = Money(11) # define your own default value, e.g. “USD”
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8) # result in “EUR”
>>34.29 EUR

lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)
print(s) #result in “BYN”
>>33.29 BYN
```

<em>Have a look at @functools.total_ordering</em>"""


class Money:
    exchange_rate = {
        "EUR": 0.93,
        "BYN": 2.1,
        "JPY": 130.84
    }

    default_currency = "USD"

    def __init__(self, amount, currency=default_currency):
        rate = self.exchange_rate.get(currency, 1)
        self.total = amount / rate

    def __add__(self, other):
        return Money(self.total + other.total)

    def __radd__(self, other):
        return Money(self.total + other)

    def __sub__(self, other):
        return Money(self.total - other.total)

    def __mul__(self, other):
        return Money(self.total * other)

    def __truediv__(self, other):
        return Money(self.total / other)

    def __eq__(self, other):
        return self.total == other.total

    def __repr__(self):
        return f"{self.total} {self.default_currency}"


if __name__ == "__main__":
    x = Money(10, "BYN")
    y = Money(11)
    z = Money(12.34, "EUR")

    assert str(z + x * 3.11 + y * 0.8) == "36.87834101382488 USD"

    lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")]
    assert str(sum(lst)) == "15.853696262974772 USD"

    print("Passed")
