# Advanced Object-Oriented Programming (OOP)

Advanced OOP builds upon the core OOP concepts by introducing Python-specific features that make code more reusable, maintainable, and easier to understand.

These concepts are widely used in large applications and frameworks where classes interact with one another in more complex ways.

This section covers:

- Class Methods
- Static Methods
- Alternative Constructors
- Advanced Inheritance
- Method Resolution Order (MRO)
- Object Introspection

---

# Class Methods

## What is a Class Method?

A class method is a method that operates on the class itself instead of a particular object.

It receives the class as its first argument using `cls`.

To create a class method, we use the `@classmethod` decorator.

Syntax:

```python
class Student:

    @classmethod
    def method_name(cls):
        pass
```

---

## Why Use Class Methods?

Class methods are useful when we need to:

- Access or modify class variables
- Create alternative constructors
- Perform operations related to the class instead of individual objects

Example:

```python
class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()
```

Output:

```python
ABC School
```

---

# Alternative Constructors

## What are Alternative Constructors?

Normally, objects are created using `__init__()`.

Sometimes, data is available in another format, and we want another way to create an object.

Class methods are commonly used for this purpose.

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data):

        name, age = data.split(",")

        return cls(name, int(age))

student = Student.from_string("Aniket,17")

print(student.name)
print(student.age)
```

Output:

```python
Aniket
17
```

Here, `from_string()` acts as an alternative constructor.

---

# Static Methods

## What is a Static Method?

A static method belongs to a class but does not access either:

- Instance variables
- Class variables

It behaves like a normal function that is placed inside a class because it is logically related to that class.

We create static methods using the `@staticmethod` decorator.

Syntax:

```python
class Student:

    @staticmethod
    def greet():
        print("Welcome")
```

---

## Why Use Static Methods?

Static methods are useful for:

- Utility functions
- Validation functions
- Mathematical calculations
- Helper methods

Example:

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

print(Calculator.add(10, 20))
```

Output:

```python
30
```

---

## Class Method vs Static Method

| Class Method | Static Method |
|--------------|---------------|
| Uses `cls` | Uses no special first parameter |
| Can access class variables | Cannot access class or instance variables directly |
| Can modify class state | Mainly used for helper functions |
| Often used as alternative constructors | Used for utility operations |

---

# Multiple Inheritance

## What is Multiple Inheritance?

Multiple inheritance allows a child class to inherit from more than one parent class.

Syntax:

```python
class Parent1:
    pass

class Parent2:
    pass

class Child(Parent1, Parent2):
    pass
```

Example:

```python
class Camera:

    def capture(self):
        print("Capturing Photo")

class MusicPlayer:

    def play(self):
        print("Playing Music")

class Phone(Camera, MusicPlayer):
    pass

phone = Phone()

phone.capture()
phone.play()
```

Output:

```python
Capturing Photo
Playing Music
```

---

# Multilevel Inheritance

## What is Multilevel Inheritance?

Multilevel inheritance forms a chain where one child becomes the parent of another class.

Example:

```python
class Animal:

    def eat(self):
        print("Eating")

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

dog = Dog()

dog.eat()
```

Output:

```python
Eating
```

---

# Hierarchical Inheritance

## What is Hierarchical Inheritance?

Hierarchical inheritance occurs when multiple child classes inherit from the same parent class.

Example:

```python
class Animal:

    def speak(self):
        print("Animal Sound")

class Dog(Animal):
    pass

class Cat(Animal):
    pass
```

Both `Dog` and `Cat` inherit from `Animal`.

---

# Hybrid Inheritance

## What is Hybrid Inheritance?

Hybrid inheritance combines two or more inheritance types within the same program.

It commonly combines:

- Multiple inheritance
- Multilevel inheritance
- Hierarchical inheritance

Example:

```python
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass
```

Hybrid inheritance is powerful but can become difficult to manage if not designed carefully.

---

# Method Resolution Order (MRO)

## What is MRO?

When a class inherits from multiple parent classes, Python must decide where to search for methods.

The order Python follows is called the Method Resolution Order (MRO).

Python follows the C3 Linearization algorithm to compute this order.

---

## Example

```python
class A:

    def show(self):
        print("Class A")

class B(A):

    def show(self):
        print("Class B")

class C(A):

    def show(self):
        print("Class C")

class D(B, C):
    pass

obj = D()

obj.show()
```

Output:

```python
Class B
```

Python checks classes according to the MRO and executes the first matching method.

---

## Viewing the MRO

We can view the MRO using:

```python
print(D.mro())
```

or

```python
print(D.__mro__)
```

This helps understand how Python searches for methods.

---

# Object Introspection

## What is Introspection?

Introspection is the ability to examine an object during runtime.

Python provides built-in utilities that allow us to inspect:

- Attributes
- Methods
- Documentation
- Internal object information

---

# dir()

The `dir()` function lists the available attributes and methods of an object.

Example:

```python
class Student:

    def __init__(self):
        self.name = "Aniket"

student = Student()

print(dir(student))
```

This is useful when exploring unfamiliar objects.

---

# __dict__

The `__dict__` attribute stores an object's writable attributes as a dictionary.

Example:

```python
class Student:

    def __init__(self):
        self.name = "Aniket"
        self.age = 17

student = Student()

print(student.__dict__)
```

Output:

```python
{'name': 'Aniket', 'age': 17}
```

This helps inspect an object's current state.

---

# help()

The `help()` function displays documentation about objects, functions, classes, or modules.

Example:

```python
help(str)
```

or

```python
help(Student)
```

It provides useful information about available methods and their descriptions.

---

# Why is Introspection Useful?

Introspection helps developers:

- Explore unknown objects
- Understand available methods
- Debug programs
- Learn third-party libraries
- Inspect object state during runtime

It is especially useful when working with large Python libraries.

---

# Python Magic Methods & Math Engine

Python provides special methods, also known as **magic methods** or **dunder (double underscore) methods**, that allow custom objects to behave like Python's built-in data types.

These methods are automatically called by Python when certain operations are performed on an object.

For example:

- Creating an object calls `__init__()`
- Using `len()` calls `__len__()`
- Accessing an index calls `__getitem__()`
- Printing an object calls `__str__()`
- Using `+` calls `__add__()`

Magic methods make custom classes feel natural and Pythonic.

This section covers:

- Magic Methods
- Operator Overloading
- Object Representation
- Memory Optimization
- Abstract Base Classes (ABC)
- Abstraction

---

# Magic Methods (Dunder Methods)

## What are Magic Methods?

Magic methods are special methods whose names begin and end with double underscores (`__`).

Python automatically invokes these methods when corresponding operations are performed on an object.

Example:

```python
class Student:

    def __init__(self):
        print("Object Created")

student = Student()
```

Output:

```python
Object Created
```

The constructor is automatically called when an object is created.

---

# __init__()

## What is __init__()?

`__init__()` is the constructor of a class.

It initializes an object's attributes immediately after the object is created.

Example:

```python
class Tensor1D:

    def __init__(self, values):
        self.values = values

tensor = Tensor1D([1, 2, 3])

print(tensor.values)
```

Output:

```python
[1, 2, 3]
```

---

# __len__()

## What is __len__()?

`__len__()` defines what should happen when the `len()` function is used on an object.

Example:

```python
class Tensor1D:

    def __init__(self, values):
        self.values = values

    def __len__(self):
        return len(self.values)

tensor = Tensor1D([10, 20, 30])

print(len(tensor))
```

Output:

```python
3
```

---

# __getitem__()

## What is __getitem__()?

`__getitem__()` makes an object subscriptable.

It is automatically called when square brackets (`[]`) are used.

Example:

```python
class Tensor1D:

    def __init__(self, values):
        self.values = values

    def __getitem__(self, index):
        return self.values[index]

tensor = Tensor1D([5, 10, 15])

print(tensor[1])
```

Output:

```python
10
```

After implementing `__getitem__()`, custom objects behave like lists.

---

# Operator Overloading

## What is Operator Overloading?

Operator overloading allows Python operators to work with custom objects.

Instead of using built-in behavior, Python calls specific magic methods.

Some common operator overloads are:

| Operator | Magic Method |
|-----------|--------------|
| `+` | `__add__()` |
| `-` | `__sub__()` |
| `*` | `__mul__()` |
| `/` | `__truediv__()` |
| `==` | `__eq__()` |

---

# __add__()

`__add__()` defines how two objects should behave when the `+` operator is used.

Example:

```python
class Student:
    def __init__(self, marks):
        # Initialize the marks attribute
        self.marks = marks

    def __add__(self, other):
        # Overload the '+' operator.
        # When 's1 + s2' is executed, Python internally calls:
        # s1.__add__(s2)
        return self.marks + other.marks


# Create two Student objects
s1 = Student(80)
s2 = Student(90)

# Internally executes: s1.__add__(s2)
print(s1 + s2)  # Output: 170
```

---

# Object Representation

Sometimes we print an object directly.

Without defining representation methods, Python displays something like:

```python
<__main__.Student object at 0x000001A2>
```

This is difficult to understand.

Python provides two magic methods to customize object representation.

---

# __str__()

`__str__()` returns a user-friendly representation of an object.

It is automatically called when using `print()`.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"

student = Student("Aniket")

print(student)
```

Output:

```python
Student: Aniket
```

---

# __repr__()

`__repr__()` returns a detailed representation mainly intended for developers and debugging.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Student(name='{self.name}')"

student = Student("Aniket")

print(repr(student))
```

Output:

```python
Student(name='Aniket')
```

---

## __str__() vs __repr__()

| __str__() | __repr__() |
|------------|------------|
| User-friendly output | Developer-friendly output |
| Used by `print()` | Used by `repr()` and debugging |
| Easy to read | More detailed representation |

---

# __slots__()

## What is __slots__()?

Normally, Python stores object attributes inside a dictionary (`__dict__`).

This provides flexibility but consumes additional memory.

`__slots__` tells Python exactly which attributes an object can have.

This reduces memory usage and prevents adding new attributes dynamically.

Example:

```python
class Student:

    __slots__ = ["name", "age"]

    def __init__(self, name, age):
        self.name = name
        self.age = age
```

Now only the `name` and `age` attributes can exist inside the object.

---

## Advantages of __slots__()

- Reduces memory usage
- Faster attribute access
- Prevents accidental creation of new attributes

---

# Abstract Base Classes (ABC)

## What is an Abstract Base Class?

An Abstract Base Class (ABC) defines a common blueprint for child classes.

It cannot be instantiated directly.

Instead, child classes must implement the abstract methods.

Python provides the `abc` module for creating abstract classes.

---

## Example

```python
from abc import ABC, abstractmethod

class Student(ABC):

    @abstractmethod
    def display(self):
        pass
```

Any class inheriting from `Student` must implement the `display()` method.