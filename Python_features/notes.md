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