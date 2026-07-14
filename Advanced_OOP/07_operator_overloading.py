# Operator Overloading means giving a special meaning to operators
# (+, -, *, etc.) for objects of our own class.
#
# It is implemented using special methods (dunder methods).

# You already use operator overloading every day.
# For example, integers know how to perform addition because the int class
# has an __add__() method.

print(5 + 3)

# Internally, Python performs something similar to:
# print((5).__add__(3))
#
# (This is only to understand the concept. Python internally performs
# the operation using the special method.)

# Output :
# 8


# Without operator overloading

class Student:
    # Stores marks of a student.
    def __init__(self, marks):
        self.marks = marks


s1 = Student(70)
s2 = Student(65)

# We want to add marks of two Student objects.

# print(s1 + s2)
#
# This raises a TypeError because Python doesn't know
# how to add two Student objects.


# With operator overloading

class Student:
    def __init__(self, marks):
        self.marks = marks

    # Overload the + operator.
    def __add__(self, other):
        return self.marks + other.marks


s1 = Student(70)
s2 = Student(65)

# __add__() is called automatically when we use:
# object1 + object2
#
# Here:
# self  -> s1
# other -> s2

print(s1 + s2)

# Output :
# 135


# Difference between Dunder Methods & Operator Overloading
#
# Dunder methods are special methods defined by Python.
# They are automatically called when we use certain syntax.
#
# Operator overloading is the process of changing the behavior of
# operators for objects of our own class by implementing these dunder methods.
#
# It is called "operator overloading" because we give an existing
# operator (+, -, *, etc.) a new meaning for our custom objects.


# Some common operator methods:
#
# +   -> __add__()
# -   -> __sub__()
# *   -> __mul__()
# /   -> __truediv__()
# ==  -> __eq__()
# !=  -> __ne__()
# <   -> __lt__()
# >   -> __gt__()
# <=  -> __le__()
# >=  -> __ge__()