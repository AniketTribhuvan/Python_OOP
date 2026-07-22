# A decorator is a function that takes another function,
# changes its behaviour, and returns a new function without
# modifying the source code of the original function.
#
# In simple words, a decorator "wraps" another function.
# A decorator itself is just a normal Python function.


# Why do we need decorators?

# Suppose we want to perform the same operation before
# executing many different functions.
#
# Instead of copying the same code into every function,
# we can write it once inside a decorator and reuse it
# wherever needed.


# Let's create a simple decorator that prints
# "Good Morning" before executing a function.

def greet(func):
    # func is the original function.

    def wrapper():
        # Code that runs before the original function.
        print("Good Morning")

        # Execute the original function.
        func()

    # Return the modified version of the function.
    return wrapper


# wrapper() is simply a new function that adds extra
# behaviour before calling the original function.


# Decorator syntax:
# Place @decorator_name above the function definition.

# Why use @decorator_name?
#
# Without it, we would have to write:
#
# function_name = decorator_name(function_name)
#
# The @ syntax is just a cleaner and more readable
# way of writing the same thing.


# Defining a function using the greet decorator.

@greet
def hello():
    print("Hello, How are you?")


hello()

# Internally, Python does:
#
# hello = greet(hello)
#
# So hello now refers to the wrapper() function.
#
# When hello() is called:
# 1. wrapper() executes.
# 2. "Good Morning" is printed.
# 3. The original hello() function is executed.

# Output:
# Good Morning
# Hello, How are you?


# Advantages of decorators:
#
# - Avoid writing the same code repeatedly.
# - Keep the original function unchanged.
# - Add or modify behaviour in a clean and reusable way.