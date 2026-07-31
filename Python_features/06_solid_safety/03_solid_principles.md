# Single Responsibility Principle (SRP) & Interface Segregation Principle (ISP)

These are two of the five **SOLID Principles**.

SOLID principles help us write code that is:

- Easy to understand
- Easy to maintain
- Easy to extend
- Easy to test

In this file, we will learn:

1. Single Responsibility Principle (SRP)
2. Interface Segregation Principle (ISP)

---

# 1. Single Responsibility Principle (SRP)

## What is SRP?

**A class should have only one responsibility (one job).**

In other words,

> A class should have only one reason to change.

---

## Why do we need SRP?

Suppose we create one class that:

- Stores student data
- Saves data to a file
- Prints student details

Now this class has three different jobs.

If tomorrow:

- The file format changes
- The printing format changes
- The student data changes

We have to modify the same class again and again.

This makes the class difficult to maintain.

Instead, each class should do only one job.

---

## Without SRP

```python
class Student:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

    def save_to_file(self):
        print("Saving student data...")
```

Here the `Student` class has multiple responsibilities.

- Store student data
- Display student data
- Save student data

This violates the Single Responsibility Principle.

---

## With SRP

```python
class Student:

    def __init__(self, name):
        self.name = name


class StudentPrinter:

    def display(self, student):
        print(student.name)


class StudentStorage:

    def save_to_file(self, student):
        print("Saving student data...")
```

Now every class has only one responsibility.

- `Student` stores data.
- `StudentPrinter` displays data.
- `StudentStorage` saves data.

Each class has only one reason to change.

---

## Advantages of SRP

- Smaller classes
- Easier to understand
- Easier to maintain
- Easier to test
- Changes affect fewer parts of the program

---

# Real Example

Think about a printer.

Its job is:

```text
Print documents.
```

Imagine if the same printer also had to:

- Browse the internet
- Play music
- Edit videos

It would become unnecessarily complicated.

Similarly, every class should focus on only one job.

---

# 2. Interface Segregation Principle (ISP)

## What is ISP?

**A class should not be forced to implement methods that it does not need.**

Instead of creating one large interface, create multiple smaller interfaces.

---

## Why do we need ISP?

Suppose we create one interface for every animal.

```python
class Animal:

    def walk(self):
        ...

    def swim(self):
        ...

    def fly(self):
        ...
```

Now consider a dog.

A dog can walk.

But it cannot fly.

Still, it is forced to implement `fly()`.

This violates the Interface Segregation Principle.

---

## Without ISP

```python
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class Dog(Animal):

    def walk(self):
        print("Dog walks")

    def fly(self):
        raise NotImplementedError("Dogs cannot fly")
```

Here, `Dog` is forced to implement `fly()` even though it doesn't make sense.

This violates ISP.

---

## With ISP

Instead of one large interface, divide it into smaller interfaces.

```python
from abc import ABC, abstractmethod


class Walkable(ABC):

    @abstractmethod
    def walk(self):
        pass


class Flyable(ABC):

    @abstractmethod
    def fly(self):
        pass


class Dog(Walkable):

    def walk(self):
        print("Dog walks")


class Bird(Walkable, Flyable):

    def walk(self):
        print("Bird walks")

    def fly(self):
        print("Bird flies")
```

Now:

- `Dog` only implements `Walkable`.
- `Bird` implements both `Walkable` and `Flyable`.

No class is forced to implement unnecessary methods.

---

## Advantages of ISP

- Smaller interfaces
- Less unnecessary code
- Easier to maintain
- More flexible design
- Classes only implement what they actually need

---

# Real Example

Think about a remote control.

A TV remote has buttons like:

- Power
- Volume
- Channel

A fan remote only needs:

- Power
- Speed

Imagine forcing the fan remote to include:

- Channel buttons
- Netflix button
- HDMI button

Those buttons would never be used.

Instead, each remote should only contain the buttons it actually needs.

This is the idea behind the Interface Segregation Principle.

---

# SRP vs ISP

| Single Responsibility Principle | Interface Segregation Principle |
|---------------------------------|---------------------------------|
| Focuses on classes | Focuses on interfaces (or abstract classes/protocols) |
| One class should have one responsibility | One interface should contain only related methods |
| Prevents classes from becoming too large | Prevents classes from implementing unnecessary methods |
| One reason to change | Only implement what is needed |

---

# Summary

## Single Responsibility Principle (SRP)

- A class should have only one responsibility.
- A class should have only one reason to change.
- Separate different responsibilities into different classes.
- Makes code easier to maintain and understand.

---

## Interface Segregation Principle (ISP)

- A class should not be forced to implement methods it does not need.
- Prefer multiple small interfaces over one large interface.
- Classes should only implement the functionality they actually use.
- Makes code more flexible and maintainable.