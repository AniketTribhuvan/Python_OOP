# Python Object-Oriented Programming (OOP)

Object-Oriented Programming (OOP) is a way of programming where code is organized into objects.

An object contains both:

- Data (Attributes)
- Behavior (Methods)

Instead of writing everything inside functions, OOP groups related data and functions together inside classes.

This makes programs:

- Organized
- Reusable
- Easy to maintain
- Easy to scale

Python is a multi-paradigm language, but OOP is widely used for building large applications.

---

# Classes and Objects

## What is a Class?

A class is a blueprint or template used to create objects.

It defines:

- Attributes (variables)
- Methods (functions)

A class itself does not store actual data.

It simply describes what an object should contain.

Syntax:

```python
class Student:
    pass
```

---

## What is an Object?

An object is an instance of a class.

When an object is created, memory is allocated for it, and it receives its own copy of instance variables.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

student1 = Student("Aniket")
student2 = Student("Rahul")

print(student1.name)
print(student2.name)
```

Output:

```python
Aniket
Rahul
```

Here:

- `Student` is the class.
- `student1` and `student2` are objects.
- Both objects are created from the same blueprint but store different data.

---

## Why Use Classes?

Without classes, we would have to create separate variables for every entity.

Example:

```python
student1_name = "Aniket"
student1_marks = 95

student2_name = "Rahul"
student2_marks = 90
```

As the program grows, this becomes difficult to manage.

Classes group related data together and make programs much cleaner.

---

# Constructors (__init__)

## What is a Constructor?

A constructor is a special method that automatically executes whenever an object is created.

In Python, the constructor is written using the `__init__()` method.

Syntax:

```python
class Student:

    def __init__(self):
        print("Object Created")
```

Example:

```python
class Student:

    def __init__(self):
        print("Constructor Called")

student = Student()
```

Output:

```python
Constructor Called
```

---

## Why is __init__() Used?

The main purpose of `__init__()` is to initialize object attributes.

Example:

```python
class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age

student = Student("Aniket", 17)

print(student.name)
print(student.age)
```

Output:

```python
Aniket
17
```

Each object stores its own values.

---

# self Keyword

`self` refers to the current object.

Whenever a method is called, Python automatically passes the current object as the first argument.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

student = Student("Aniket")

print(student.name)
```

Here,

`self.name` belongs to the current object.