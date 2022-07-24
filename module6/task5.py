"""
### Task 6.5

A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance. 
Implement singleton logic inside your custom class using a method to initialize class instance.

Example:

```python
 p = Sun()
 f = Sun()
 p is f
True
```"""


class Sun:
    __instance = None

    def __new__(cls):
        if Sun.__instance is None:
            Sun.__instance = super().__new__(cls)
        return Sun.__instance


if __name__ == "__main__":
    p = Sun()
    f = Sun()
    assert p is f

    print("Passed")
