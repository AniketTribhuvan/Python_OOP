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