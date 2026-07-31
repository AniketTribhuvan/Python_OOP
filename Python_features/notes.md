# Executable Objects (__call__)

## What is __call__()?

Normally, we call functions using parentheses.

```python
greet()
```

Python also allows objects themselves to be called like functions.

This is done by implementing the `__call__()` magic method.

Whenever an object is called using parentheses, Python automatically executes the `__call__()` method.

---

## Example

```python
class Greeter:

    def __call__(self):
        print("Hello!")

greet = Greeter()

greet()
```

Output:

```python
Hello!
```

Although `greet` is an object, it behaves like a function.

---

## Why Use __call__()?

`__call__()` is useful when an object needs to maintain state while behaving like a function.

It is commonly used in:

- Data processing pipelines
- Machine learning preprocessing
- Neural network layers
- Custom callable classes

Example:

```python
class TensorProcessor:

    def __call__(self, values):
        return [value * 2 for value in values]

processor = TensorProcessor()

print(processor([1, 2, 3]))
```

Output:

```python
[2, 4, 6]
```
---

# Decorators

## What is a Decorator?

A decorator is a function that modifies or extends the behavior of another function without changing its original code.

Decorators are created using the `@` symbol.

Syntax:

```python
@decorator
def function():
    pass
```

---

## Why Use Decorators?

Decorators help add common functionality such as:

- Logging
- Timing
- Authentication
- Validation
- Caching

without modifying the original function.

---

## Example

```python
def decorator(function):

    def wrapper():
        print("Before Function")

        function()

        print("After Function")

    return wrapper

@decorator
def greet():
    print("Hello")

greet()
```

Output:

```python
Before Function
Hello
After Function
```

The original function remains unchanged, but its behavior is extended.

---

# functools.wraps

## Why Use wraps?

When a function is decorated, Python replaces the original function with the wrapper function.

As a result, important information like the function's name and documentation is lost.

Example:

```python
def decorator(function):

    def wrapper():
        function()

    return wrapper

@decorator
def greet():
    pass

print(greet.__name__)
```

Output:

```python
wrapper
```

Instead of `"greet"`, Python displays `"wrapper"`.

---

## Using functools.wraps

The `wraps` decorator preserves the original function's metadata.

Example:

```python
from functools import wraps

def decorator(function):

    @wraps(function)
    def wrapper():
        function()

    return wrapper

@decorator
def greet():
    pass

print(greet.__name__)
```

Output:

```python
greet
```

---

# Generators

## What is a Generator?

A generator is a special type of function that produces values one at a time using the `yield` keyword.

Unlike a normal function, a generator does not return all values at once.

Instead, it pauses after each `yield` and resumes when requested.

---

## Example

```python
def numbers():

    yield 1
    yield 2
    yield 3

generator = numbers()

print(next(generator))
print(next(generator))
print(next(generator))
```

Output:

```python
1
2
3
```

---

## yield vs return

| yield | return |
|--------|---------|
| Produces one value at a time | Returns everything at once |
| Pauses function execution | Ends function execution |
| Memory efficient | Stores complete result in memory |

---

# Generator Expressions

Generator expressions provide a shorter syntax for creating generators.

Syntax:

```python
generator = (expression for item in iterable)
```

Example:

```python
squares = (number * number for number in range(5))

for value in squares:
    print(value)
```

Output:

```python
0
1
4
9
16
```

Generator expressions look similar to list comprehensions but use parentheses instead of square brackets.

---

# Lazy Evaluation

## What is Lazy Evaluation?

Lazy evaluation means values are created only when they are needed.

Instead of computing everything immediately, computation happens one step at a time.

Generators use lazy evaluation.

Example:

```python
def numbers():

    for number in range(1000000):
        yield number
```

Even though the generator can produce one million numbers, only one number exists in memory at any given time.

This makes generators extremely memory efficient.

---

# Python Static Typing

Python is a dynamically typed language, which means variables can store values of different types during runtime.

Example:

```python
x = 10
x = "Hello"
```

Although this flexibility is useful, it can also introduce bugs that are only discovered when the program is executed.

Static typing helps solve this problem by allowing us to specify the expected types of variables, functions, and objects before execution.

This section covers:

- Type Hints
- mypy
- TypeVar
- Callable
- Union
- Protocol

These concepts are widely used in enterprise applications to improve code quality, readability, and maintainability.

---

# Type Hints

## What are Type Hints?

Type hints allow us to specify the expected data types of variables, function parameters, and return values.

Python itself does not enforce these types during runtime, but type checkers like `mypy` can verify them before execution.

Example:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"

print(greet("Aniket"))
```

Output:

```python
Hello, Aniket
```

---

## Type Hinting Variables

Variables can also be annotated with their expected type.

Example:

```python
age: int = 17
name: str = "Aniket"
height: float = 5.8
is_student: bool = True
```

These annotations improve code readability and editor support.

---

## Type Hinting Collections

Python allows type hints for collections.

Example:

```python
numbers: list[int] = [1, 2, 3]

names: list[str] = ["Aniket", "Rahul"]

marks: dict[str, int] = {
    "Math": 95,
    "Science": 92
}
```

---

# mypy

## What is mypy?

`mypy` is a static type checker for Python.

It analyzes your code and reports type-related errors before the program runs.

Example:

```python
def square(number: int) -> int:
    return number * number

square("10")
```

Running `mypy` reports that a string is passed where an integer is expected.

---

## Installing mypy

```bash
pip install mypy
```

Checking a file:

```bash
mypy program.py
```

Strict mode:

```bash
mypy --strict program.py
```

Strict mode performs more comprehensive type checking.

---

# TypeVar

## What is TypeVar?

Sometimes we want to write reusable functions that work with different data types while maintaining type safety.

`TypeVar` allows us to create generic types.

Example:

```python
from typing import TypeVar

T = TypeVar("T")
```

---

## Example

```python
from typing import TypeVar

T = TypeVar("T")

def first_item(items: list[T]) -> T:
    return items[0]

print(first_item([1, 2, 3]))
print(first_item(["A", "B", "C"]))
```

Output:

```python
1
A
```

The same function works with multiple data types while preserving type information.

---

# Callable

## What is Callable?

`Callable` represents functions or callable objects.

It specifies:

- Parameter types
- Return type

Syntax:

```python
Callable[[parameter_types], return_type]
```

---

## Example

```python
from typing import Callable

def add(a: int, b: int) -> int:
    return a + b

operation: Callable[[int, int], int] = add

print(operation(10, 20))
```

Output:

```python
30
```

`Callable` is commonly used when passing functions as arguments.

---

# Union

## What is Union?

Sometimes a variable or parameter can accept more than one data type.

`Union` allows multiple possible types.

Example:

```python
from typing import Union

def display(value: Union[int, str]):

    print(value)

display(10)
display("Hello")
```

Output:

```python
10
Hello
```

---

## Union Using |

In Python 3.10+, the `|` operator can also be used.

Example:

```python
def display(value: int | str):

    print(value)
```

Both approaches are equivalent.

---

# Protocol

## What is Protocol?

`Protocol` defines a set of required methods or attributes that an object must provide.

Unlike inheritance, a class does not need to explicitly inherit from a protocol.

If it satisfies the required structure, it is considered compatible.

This concept is known as **structural typing**.

---

## Example

```python
from typing import Protocol

class Drawable(Protocol):

    def draw(self) -> None:
        ...

class Circle:

    def draw(self) -> None:
        print("Drawing Circle")

def render(shape: Drawable):

    shape.draw()

circle = Circle()

render(circle)
```

Output:

```python
Drawing Circle
```

Even though `Circle` does not inherit from `Drawable`, it satisfies the protocol because it implements the required method.

---

# Why Use Protocol?

Protocols help:

- Reduce tight coupling
- Improve flexibility
- Support structural typing
- Build reusable interfaces

They are widely used in large Python libraries.

---

# Static Typing Benefits

Static typing provides several advantages:

- Detects type errors before execution
- Improves code readability
- Enhances editor auto-completion
- Simplifies debugging
- Makes large codebases easier to maintain
- Encourages writing cleaner APIs

---

# Dynamic Typing vs Static Typing

| Dynamic Typing | Static Typing |
|----------------|---------------|
| Types are checked during runtime | Types are checked before execution |
| More flexible | More predictable |
| Errors may appear during execution | Many errors are detected early |
| No type annotations required | Uses type hints |

---

# Context Managers

## What is a Context Manager?

A context manager is an object that automatically manages resources before and after a block of code executes.

It is commonly used with the `with` statement.

Instead of manually opening and closing resources, a context manager ensures they are properly cleaned up, even if an error occurs.

Syntax:

```python
with resource:
    # Code
```

---

## Why Use Context Managers?

Context managers help:

- Automatically release resources
- Prevent resource leaks
- Make code cleaner
- Handle exceptions safely

Common use cases include:

- File handling
- Database connections
- Memory monitoring
- Network connections

---

# __enter__()

The `__enter__()` method executes when entering the `with` block.

It prepares the resource and optionally returns an object.

Example:

```python
class Demo:

    def __enter__(self):
        print("Entering Context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting Context")

with Demo():
    print("Inside Block")
```

Output:

```python
Entering Context
Inside Block
Exiting Context
```

---

# __exit__()

The `__exit__()` method executes when leaving the `with` block.

It performs cleanup operations, regardless of whether an exception occurred.

Its parameters are:

- `exc_type`
- `exc_value`
- `traceback`

These provide information about any exception raised inside the `with` block.

---

# Exception Handling

## What is an Exception?

An exception is an error that occurs while a program is running.

If an exception is not handled, the program terminates.

Example:

```python
number = 10 / 0
```

Output:

```python
ZeroDivisionError
```

---

## Handling Exceptions

Python provides the `try` and `except` statements to handle exceptions.

Example:

```python
try:

    number = 10 / 0

except ZeroDivisionError:

    print("Cannot divide by zero.")
```

Output:

```python
Cannot divide by zero.
```

Handling exceptions prevents unexpected program crashes.

---

# Custom Exceptions

## Why Create Custom Exceptions?

Built-in exceptions are useful, but applications often require more meaningful errors.

Custom exceptions allow developers to define application-specific error types.

Example:

```python
class ShapeMismatchError(Exception):
    pass
```

Now this exception can be raised whenever tensor shapes do not match.

---

## Raising a Custom Exception

Example:

```python
class ShapeMismatchError(Exception):
    pass

raise ShapeMismatchError("Tensor sizes must match.")
```

Output:

```python
ShapeMismatchError: Tensor sizes must match.
```

---

## Another Example

```python
class InvalidDataTypeError(Exception):
    pass

def process(value):

    if not isinstance(value, (int, float)):
        raise InvalidDataTypeError("Only numeric values are allowed.")

process("Hello")
```

Output:

```python
InvalidDataTypeError: Only numeric values are allowed.
```

Custom exceptions make debugging much easier.

---

# SOLID Principles

## What are SOLID Principles?

SOLID is a collection of software design principles that help create clean, maintainable, and scalable applications.

The five principles are:

- Single Responsibility Principle (SRP)
- Open/Closed Principle (OCP)
- Liskov Substitution Principle (LSP)
- Interface Segregation Principle (ISP)
- Dependency Inversion Principle (DIP)

In this roadmap, the primary focus is on SRP and ISP.

---

# Single Responsibility Principle (SRP)

## What is SRP?

A class should have only one responsibility.

It should have only one reason to change.

Bad Example:

```python
class Report:

    def generate(self):
        pass

    def save(self):
        pass

    def email(self):
        pass
```

This class has multiple responsibilities.

Better Example:

```python
class ReportGenerator:

    def generate(self):
        pass

class ReportSaver:

    def save(self):
        pass

class ReportEmailer:

    def email(self):
        pass
```

Each class now has a single responsibility.

---

# Interface Segregation Principle (ISP)

## What is ISP?

Clients should not be forced to depend on methods they do not use.

Instead of creating one large interface, create multiple smaller interfaces.

Bad Example:

```python
class Worker:

    def work(self):
        pass

    def eat(self):
        pass
```

Not every worker may require both methods.

Better design separates unrelated behaviors into different interfaces.

This results in cleaner and more flexible code.

---

# Why Follow SOLID Principles?

SOLID principles help developers:

- Reduce code duplication
- Improve maintainability
- Increase flexibility
- Simplify testing
- Build scalable applications

They are widely used in enterprise software development.

---

# Important Revision Points

Type hints specify the expected types of variables, parameters, and return values.

Python does not enforce type hints during runtime.

`mypy` checks type correctness before execution.

`mypy --strict` performs more comprehensive type checking.

`TypeVar` is used to write generic, reusable functions.

`Callable` represents functions or callable objects with specific parameter and return types.

`Union` allows a value to have multiple possible data types.

The `|` operator provides a shorter syntax for `Union` in Python 3.10+.

`Protocol` enables structural typing by defining required methods or attributes.

Static typing improves code quality, readability, and maintainability while reducing runtime errors.

Context managers automatically manage resources using the `with` statement.

`__enter__()` executes when entering the context.

`__exit__()` executes when leaving the context and performs cleanup.

`tracemalloc` tracks memory allocations during program execution.

Memory monitoring helps identify memory leaks and optimize applications.

Exceptions are runtime errors that can interrupt program execution.

`try` and `except` allow programs to handle exceptions safely.

Custom exceptions represent application-specific error conditions.

The Single Responsibility Principle (SRP) states that a class should have only one responsibility.

The Interface Segregation Principle (ISP) encourages creating small, focused interfaces instead of large, general-purpose ones.

Applying SOLID principles results in cleaner, more maintainable, and scalable software.