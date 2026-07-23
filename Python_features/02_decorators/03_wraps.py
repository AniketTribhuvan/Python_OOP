# As we know, when we call a decorated function,
# Python actually calls the wrapper() function returned
# by the decorator.

# Because of this, the original function is replaced by
# wrapper(). So if we try to access information about the
# function (its metadata), we get information about wrapper()
# instead of the original function.


# Example:

def decorator(func):

    def wrapper():
        func()

    return wrapper


@decorator
def greet():
    """Greets the user."""
    print("Hello")


print(greet.__name__)

# Output :
# wrapper


help(greet)

# Output (simplified):
#
# Help on function wrapper in module __main__:
#
# wrapper()

# greet now points to wrapper(), so Python thinks
# the function's name is "wrapper" instead of "greet".

# This causes a metadata problem.


# Python provides the functools module,
# which contains the wraps decorator.

# wraps is used to copy the metadata of the original
# function to the wrapper function.

# Metadata includes:
# - Function name (__name__)
# - Docstring (__doc__)
# - Annotations (__annotations__)
# - Module (__module__)
# and some other function information.

# Syntax:
#
# @wraps(original_function)

from functools import wraps


def decorator(func):

    @wraps(func)
    def wrapper():
        func()

    return wrapper


@decorator
def greet():
    """Greets the user."""
    print("Hello")


print(greet.__name__)

# Output :
# greet

print(greet.__doc__)

# Output :
# Greets the user.

# Now greet still points to wrapper(),
# but wrapper has copied the metadata of greet.
# So the decorated function behaves as if it
# still has the original function's information.