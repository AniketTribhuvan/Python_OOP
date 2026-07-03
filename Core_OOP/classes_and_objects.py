# Object orientated programming organizes code into objects. It combines attributes (variables) & methods.
# Programs become organized, reusable & easy to maintain.

# class : A class is a blueprint. It defines how an object created will look.

class student:      # student is a class. Currently this class contains nothing.
    pass

# object : Objects are instances of a class. Each object has its own data.
s1 = student()      # s1 is an object of class student.

# attributes & methods : Attributes store data. Methods define what an object can do.
class student:
    def __init__(self, name):       # Currently ignore this function. We will learn it properly later.
        self.name = name

    def show_name(self):
        print(f"Name of student : {self.name}")

s1 = student("Aniket")      # Object created.
s1.show_name()              # s1 calls show_name().
# Output :
# Name of student : Aniket

# self : self refers to the current object.
# When we call a method using an object, Python automatically passes that object as self.
# Example:
# s1.show_name()
# Internally Python does:
# student.show_name(s1)

# Constructors : Constructors are methods that are called automatically when Python creates an object.
# __init__ : __init__ is a constructor mainly used to initialize instance variables.

class student:
    def __init__(self, name):   # Called immediately when Python creates an object.
        self.name = name

    def show_name(self):
        print(f"Name of student : {self.name}")

s2 = student("Aniket")  # Python creates s2 and immediately calls __init__("Aniket").
s2.show_name()
# Output :
# Name of student : Aniket

# practice :

# 1. Employee Details
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Employee name : {self.name}\nSalary : {self.salary}")

emp1 = Employee("Aniket", 35000)
emp1.show_details()

# Output :
# Employee name : Aniket
# Salary : 35000

# 2. Rectangle Area
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Area : {self.length * self.width} sq.m")

    def perimeter(self):
        print(f"Perimeter : {(2 * self.length) + (2 * self.width)} m")

rect1 = Rectangle(10, 2.5)
rect1.area()
rect1.perimeter()

# Output :
# Area : 25.0 sq.m
# Perimeter : 25.0 m