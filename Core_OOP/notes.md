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

---

# Instance Variables

Instance variables belong to individual objects.

Every object has its own separate copy.

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

Changing one object's instance variable does not affect another object.

---

# Class Variables

Class variables are shared by all objects of a class.

Example:

```python
class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name

student1 = Student("Aniket")
student2 = Student("Rahul")

print(student1.school)
print(student2.school)
```

Output:

```python
ABC School
ABC School
```

If the class variable changes, every object sees the updated value.

---

## Instance Variables vs Class Variables

| Instance Variable | Class Variable |
|-------------------|----------------|
| Belongs to object | Belongs to class |
| Separate copy for every object | Shared by every object |
| Defined using `self` | Defined directly inside class |
| Stores object-specific data | Stores common data |

---

# Encapsulation

## What is Encapsulation?

Encapsulation means wrapping data and methods together inside a class while restricting direct access to important data.

Instead of allowing users to modify internal variables directly, we provide controlled access.

Benefits:

- Data protection
- Better validation
- Prevent accidental modification
- Cleaner design

---

# Access Modifiers

Python mainly provides three types of access levels.

## Public Members

Public members can be accessed from anywhere.

Example:

```python
class Student:

    def __init__(self):
        self.name = "Aniket"

student = Student()

print(student.name)
```

---

## Protected Members

Protected members use a single underscore `_`.

They indicate that the variable should only be used inside the class or its child classes.

Example:

```python
class Student:

    def __init__(self):
        self._marks = 95
```

Protected members can still be accessed outside the class, but it is discouraged.

---

## Private Members

Private members use double underscores `__`.

Python performs name mangling to reduce accidental external access.

Example:

```python
class Student:

    def __init__(self):
        self.__marks = 95
```

Trying to access it directly:

```python
student = Student()

print(student.__marks)
```

Output:

```python
AttributeError
```

---

# Getters and Setters

## Why Use Getters and Setters?

Sometimes we don't want users to access or modify an object's data directly.

Instead, we control access through getter and setter methods.

- A **getter** returns the value of a private attribute.
- A **setter** updates the value after performing validation.

This helps protect the object's data and prevents invalid values from being stored.

Example:

```python
class Student:

    def __init__(self):
        self.__marks = 0

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):

        if marks >= 0:
            self.__marks = marks

student = Student()

student.set_marks(95)

print(student.get_marks())
```

Output:

```python
95
```

Validation helps prevent invalid data from entering the object.

---

## The Problem with Traditional Getters and Setters

Although traditional getters and setters provide data protection, they make code less readable.

Instead of accessing an attribute directly, we must call methods.

Example:

```python
student.set_marks(95)

print(student.get_marks())
```

This looks similar to languages like Java or C++, but it is not considered the Pythonic way.

Python provides a cleaner solution using **properties**.

---

## @property

### What is @property?

`@property` is a built-in decorator that allows a method to be accessed like an attribute.

It acts as a getter without requiring parentheses.

Example:

```python
class Student:

    def __init__(self):
        self.__marks = 0

    @property
    def marks(self):
        return self.__marks

student = Student()

print(student.marks)
```

Output:

```python
0
```

Although `marks` is actually a method, it behaves like a normal attribute.

---

## @property.setter

### What is @property.setter?

`@property.setter` defines the setter method for a property.

It allows us to update an attribute while still performing validation.

Example:

```python
class Student:

    def __init__(self):
        self.__marks = 0

    @property
    def marks(self):
        return self.__marks

    @marks.setter
    def marks(self, value):

        if value >= 0:
            self.__marks = value

student = Student()

student.marks = 95

print(student.marks)
```

Output:

```python
95
```

Now the object looks like it has a normal public attribute, but the getter and setter methods are executed automatically.

---

# Traditional Getters & Setters vs @property

| Traditional Getters & Setters | @property |
|-------------------------------|-----------|
| Uses methods like `get_marks()` and `set_marks()` | Uses normal attribute syntax |
| Requires parentheses | No parentheses required |
| Less readable | More readable |
| Similar to Java/C++ | Pythonic approach |

---

## Why is @property Better?

`@property` provides the benefits of getters and setters while keeping the syntax simple.

Advantages:

- Cleaner code
- More readable
- Supports validation
- Protects private data
- Allows implementation changes without changing how the attribute is used

For these reasons, `@property` is the preferred way to implement getters and setters in Python.

# Inheritance

## What is Inheritance?

Inheritance allows one class to acquire the properties and methods of another class.

The existing class is called the parent class.

The new class is called the child class.

Syntax:

```python
class Parent:
    pass

class Child(Parent):
    pass
```

---

## Why Use Inheritance?

Inheritance helps:

- Reuse code
- Reduce duplication
- Build class hierarchies
- Extend existing functionality

Example:

```python
class Animal:

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

dog = Dog()

dog.speak()
```

Output:

```python
Animal speaks
```

---

# Method Overriding

Method overriding allows a child class to provide its own implementation of a parent class method.

Example:

```python
class Animal:

    def speak(self):
        print("Animal speaks")

class Dog(Animal):

    def speak(self):
        print("Dog barks")

dog = Dog()

dog.speak()
```

Output:

```python
Dog barks
```

The child method replaces the parent implementation.

---

# Composition

## What is Composition?

Composition represents a **Has-A** relationship.

Instead of inheriting from another class, one object contains another object.

Example:

```python
class Engine:

    def start(self):
        print("Engine Started")

class Car:

    def __init__(self):
        self.engine = Engine()

    def start(self):
        self.engine.start()

car = Car()

car.start()
```

Output:

```python
Engine Started
```

Here:

- A Car **has an** Engine.
- Car does not inherit from Engine.

---

## Composition vs Inheritance

| Composition | Inheritance |
|-------------|-------------|
| Has-A relationship | Is-A relationship |
| Uses one object inside another | Child extends parent |
| More flexible | Can create rigid hierarchies |
| Preferred in many enterprise applications | Useful when true parent-child relationship exists |

---

# Important Revision Points

Classes are blueprints for creating objects.

Objects are instances of classes.

`__init__()` is the constructor and runs automatically when an object is created.

`self` refers to the current object.

Instance variables belong to individual objects.

Class variables are shared among all objects.

Encapsulation protects internal data from direct modification.

Private members use double underscores (`__`).

Getters retrieve data, while setters update data after validation.

Inheritance allows child classes to reuse parent functionality.

Method overriding lets child classes provide specialized behavior.

Composition represents a **Has-A** relationship and promotes flexible object design.