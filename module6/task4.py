"""
### Task 6.4
Create hierarchy out of birds. 
Implement 4 classes:
* class `Bird` with an attribute `name` and methods `fly` and `walk`.
* class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value. 
Implement the method `eat` which will describe its typical ration.
* class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
Add same "eat" method but with other implementation regarding the swimming bird tastes.
* class `SuperBird` which can do all of it: walk, fly, swim and eat.
But be careful which "eat" method you inherit.
"""
import string


class Bird:
    def __init__(self, name):
        self.name = name

    def walk(self) -> string:
        return f"{self.name} can walk"

    def __repr__(self):
        return f"{self.name} can walk and fly"


class FlyingBird(Bird):
    def __init__(self, name, ration="plants"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        return f"{self.name} eats mostly {self.ration}"

    def fly(self):
        return f"{self.name} can fly"

    def __repr__(self):
        return f"{self.name} can walk and fly"


class NonFlyingBird(Bird):
    def eat(self):
        return f"{self.name} eats fish"

    def swim(self):
        return f"{self.name} can swim"

    def __repr__(self):
        return f"{self.name} can walk and swim"


class SuperBird(NonFlyingBird, FlyingBird):
    def __repr__(self):
        return f"{self.name} can fly, walk and swim"

    def eat(self):
        return super().eat()


if __name__ == "__main__":
    bird = Bird("Any")
    penguin = NonFlyingBird("Penguin")
    canary = FlyingBird("Canary", "flowers")
    gull = SuperBird("Gull")

    assert str(bird) == "Any can walk and fly"
    assert bird.walk() == "Any can walk"

    assert str(penguin) == "Penguin can walk and swim"
    assert penguin.swim() == "Penguin can swim"
    # penguin.fly() throws error
    assert penguin.walk() == "Penguin can walk"
    assert penguin.eat() == "Penguin eats fish"

    assert str(canary) == "Canary can walk and fly"
    # canary.swim() throws error
    assert canary.fly() == "Canary can fly"
    assert canary.walk() == "Canary can walk"
    assert canary.eat() == "Canary eats mostly flowers"

    assert str(gull) == "Gull can fly, walk and swim"
    assert gull.swim() == "Gull can swim"
    assert gull.fly() == "Gull can fly"
    assert gull.walk() == "Gull can walk"
    assert gull.eat() == "Gull eats fish"

    assert SuperBird.__mro__ == (SuperBird, NonFlyingBird, FlyingBird, Bird, object)

    print("Passed")

"""
Implement str() function call for each class.

Example:
```python
 b = Bird("Any")
 b.walk()
"Any bird can walk"

p = NonFlyingBird("Penguin", "fish")
>> p.swim()
"Penguin bird can swim"
 p.fly()
AttributeError: 'Penguin' object has no attribute 'fly'
 p.eat()
"It eats mostly fish"

c = FlyingBird("Canary")
 str(c)
"Canary can walk and fly"
 c.eat()
"It eats mostly grains"

s = SuperBird("Gull")
 str(s)
"Gull bird can walk, swim and fly"
 s.eat()
"It eats fish"
```

Have a look at __mro__ method of your last class."""
