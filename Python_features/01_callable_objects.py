# __call__() is a special dunder method that allows an object
# to be called like a function using parentheses ().

# Normal function

def info(name):
    print(f"My name is {name}")


info("Aniket")      # Calling a normal function.


# Normally, only functions can be called like this.
# But if a class implements __call__(), then its objects
# can also be called like functions.


# Can objects be called like functions?

class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Aniket")

# s1()
#
# This raises a TypeError because Student does not define
# the __call__() method.

# When an object is called like:
#
# object()
#
# Python internally does something similar to:
#
# object.__call__()
#
# Since Student doesn't define __call__(), calling s1()
# results in an error.


# Defining __call__() and using an object like a function.

class StudentCallable:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"My name is {self.name}")


s2 = StudentCallable("John")

s2()

# Output :
# My name is John

# Python internally calls:
#
# s2.__call__()


# __call__() can also accept arguments.

class Calculator:

    def __call__(self, a, b):
        return a + b


c1 = Calculator()

print(c1(10, 20))

# Output :
# 30


# Why not create a normal method?

# We could write:
#
# calculator.add(10, 20)
#
# instead of:
#
# calculator(10, 20)
#
# Both are correct.

# __call__() is useful when an object represents one main action.
# Calling the object directly feels more natural than calling
# a separate method.


# Function Instances (Callable Objects)

# An object that implements __call__() is called a
# callable object (or callable instance) because it behaves
# like a function.


# Why is this useful?

# Suppose a class has only one primary job.
# Instead of writing:
#
# object.do_work()
#
# writing:
#
# object()
#
# is cleaner and more natural.

# Another advantage is that the object remembers its state
# (instance variables).
#
# A normal function doesn't automatically remember values
# between calls unless you explicitly store them elsewhere.


# callable() function

# callable() checks whether an object can be called
# using parentheses ().

print(callable(c1))

# Output :
# True