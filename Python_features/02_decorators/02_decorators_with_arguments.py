# Previously, we created decorators for functions
# that didn't have any parameters.

# But what if the function has parameters?
# Let's understand this with an example.

def process(func):

    def wrapper():
        print("Adding")
        func()

    return wrapper


@process
def add(a, b):
    print(a + b)


# add(10, 15)

# This raises a TypeError because wrapper()
# accepts 0 arguments, but we passed 2.


# Why does wrapper() get called?

# When Python sees:

# @process
# def add(...):

# it internally does:

# add = process(add)

# Notice that process() receives only the function object,
# not its arguments.

# process() creates wrapper() and returns it.

# So after decoration:

# add = wrapper

# Therefore, when we call:

# add(10, 15)

# Python is actually calling:

# wrapper(10, 15)

# Since wrapper() accepts no arguments,
# a TypeError is raised.

# The problem is NOT with the decorator.
# The problem is that wrapper() cannot receive
# the arguments meant for the original function.


# The solution is to use *args and **kwargs.

# *args collects all positional arguments.
# **kwargs collects all keyword arguments.

# This allows wrapper() to accept any number
# of arguments and pass them to the original function.


def process(func):

    def wrapper(*args, **kwargs):
        print("Adding")

        # Forward all received arguments
        # to the original function.
        func(*args, **kwargs)

    return wrapper


@process
def add(a, b):
    print(a + b)


add(10, 15)

# Output:
# Adding
# 25


# What if the original function returns a value?

def process(func):

    def wrapper(*args, **kwargs):
        print("Adding")

        # The return value of func() is ignored.
        func(*args, **kwargs)

    return wrapper


@process
def add(a, b):
    return a + b


print(add(10, 15))

# Output:
# Adding
# None

# add() returns 25, but wrapper() doesn't return it.
# Since every Python function returns None by default
# if no return statement is present, add() finally returns None.


# A better way to write decorators

# Most decorators are written like this because they work
# whether the original function returns a value or not.

def process(func):

    def wrapper(*args, **kwargs):
        print("Adding")

        # Execute the original function and store its return value.
        result = func(*args, **kwargs)

        # Return the same value back to the caller.
        return result

    return wrapper


@process
def add(a, b):
    return a + b


print(add(10, 15))

# Output:
# Adding
# 25

# Even if the original function doesn't return anything,
# this structure still works correctly because result
# will simply be None.