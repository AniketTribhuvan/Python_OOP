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