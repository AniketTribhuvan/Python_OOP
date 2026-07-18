# Advanced OOP

## Overview

This folder focuses on advanced Object-Oriented Programming concepts in Python.

These concepts extend the core OOP principles by introducing Python-specific features, advanced inheritance structures, and object introspection techniques. Mastering them helps in writing cleaner, more maintainable, and more Pythonic code.

Also transform ordinary Python objects into mathematical objects by implementing magic methods, operator overloading, object representation, memory optimization, and abstraction. These concepts are essential for designing scalable data structures used in AI, machine learning, and scientific computing.

## Topics Covered

- class methods
- static methods
- alternative constructors
- multiple inheritance
- multilevel inheritance
- hybrid inheritance
- hierarchical inheritance
- method resolution order (MRO)
- object introspection
- `dir()`, `__dict__` & `help()`
- magic methods (dunder methods)
- `__init__`, `__len__` & `__getitem__`
- operator overloading

## Skills Developed

- Creating alternative constructors using class methods
- Writing utility methods using static methods
- Understanding complex inheritance structures
- Predicting method lookup using MRO
- Avoiding common inheritance issues
- Inspecting objects dynamically at runtime
- Exploring object attributes and methods using introspection tools
- Building custom Python objects
- Overloading operators for mathematical operations

## Key Takeaways

- Class methods work with the class itself and can be used as alternative constructors.
- Static methods belong logically to a class but do not access class or instance data.
- Multiple inheritance allows a class to inherit from more than one parent class.
- Multilevel inheritance creates inheritance chains across multiple generations.
- Hybrid and hierarchical inheritance combine different inheritance structures.
- Python follows Method Resolution Order (MRO) to determine which method should be executed.
- Introspection utilities help inspect an object's attributes, methods, and documentation during runtime.
- Magic methods allow Python objects to behave like built-in data types.
- Operator overloading enables mathematical operations on custom objects.

## 🗂️ Project Structure

```text
Advanced_OOP/
  readme.md                                   # Folder overview of advanced OOP concepts
  notes.md                                    # Notes and concepts related to advanced OOP

  01_class_methods.py                            # Understanding @classmethod
  02_static_methods.py                           # Understanding @staticmethod
  03_alternative_constructor.py                  # Creating objects using alternative constructors

  04_inheritance/
    01_multiple_inheritance.py                          # Understanding multiple inheritance
    02_multilevel_inheritance.py                        # Understanding multilevel inheritance
    03_hierarchical_and_hybrid_inheritance.py           # Understanding hybrid inheritance & hierarchical inheritance
  
  05_introspection.py                                   # Understand using dir(), __dict__ & help()

  06_dunder_methods/
    01_dunder_methods.md                                # Understanding __init__, __len__ & __getitem__
    02_str_repr_and_slots.md                            # Understanding __str__, __repr__ & __slots__
  
  07_operator_overloading.py                            # Understand operator overloading deeply

  08_abstraction.md                                     # Understand abstraction, protocol & @abstractmethod