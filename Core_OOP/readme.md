# Core OOP

## Overview

This folder focuses on the core concepts of Object-Oriented Programming (OOP) in Python.

These concepts form the foundation of writing organized, reusable, and scalable programs. Understanding them is essential before moving towards advanced OOP concepts and building larger software systems.

## Topics Covered

- classes & objects
- constructors (`__init__`)
- instance variables
- class variables
- encapsulation
- access modifiers
- getters & setters
- inheritance
- method overriding
- Types of inheritance
- composition

## Skills Developed

- Creating classes and objects
- Initializing object state using constructors
- Differentiating between instance and class variables
- Protecting data using encapsulation
- Controlling attribute access with getters and setters
- Reusing code through inheritance
- Customizing inherited behavior using method overriding
- Building flexible object relationships using composition

## Mini Projects / Practice

- library_membership_system

## Key Takeaways

- Classes act as blueprints for creating objects.
- Constructors initialize object data when an object is created.
- Instance variables belong to individual objects, while class variables are shared across all objects.
- Encapsulation helps protect internal object data.
- Getters and setters provide controlled access to private attributes.
- Inheritance allows child classes to reuse and extend parent class functionality.
- Method overriding enables child classes to provide their own implementation of inherited methods.


## 🗂️ Project Structure

```text
Core_OOP/
  README.md                                  # Folder overview of core OOP concepts
  NOTES.md                                   # Notes and concepts related to core OOP

  classes_and_objects.py                     # Creating classes,objects & constructors (__init)
  instance_vs_class_variables.py             # Instance variables and class variables

  encapsulation/
    access_modifiers.py                      # Public, protected, and private members
    getters_and_setter.py                    # Data validation using getters and setters
  
  inheritance/
    inheritance.py                           # Basic inheritance
    method_overriding.py                     # Overriding inherited methods
    composition.py                           # Understanding the has-a relationship
    inheritance_vs_composition.md            # Difference between Is-A & Has-A Relationship
  
  Practice/
    library_membership_system.py             # Mini project
```