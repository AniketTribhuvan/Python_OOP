# Type Hints & Linting

Python is a **dynamically typed language**.

```python
name = "Hello"
age = 17
score = 92.88
```

Here, we never specify the data types.

Python automatically determines the type of each variable while the program runs.

---

# Why can this become a problem?

Consider this function:

```python
def add(num1, num2):
    return num1 + num2

print(add("Hello", "Hi"))
```

**Output**

```python
HelloHi
```

Python doesn't report any error because adding two strings is a valid operation.

But imagine this function was intended to add only numbers.

Python won't warn us before running the program.

This is where **type hints** become useful.

---

# What are Type Hints?

A **type hint** tells readers and development tools what type of data is expected.

Example:

```python
def square(x: int) -> int:
    return x * x
```

Here:

- `x: int` means `x` is expected to be an integer.
- `-> int` means the function is expected to return an integer.

---

# Important Point

Python **does not enforce type hints**.

They are only hints.

For example:

```python
def square(x: int) -> int:
    return x * x

print(square("Hello"))
```

Python will still run this code until it encounters an operation that is invalid for the supplied value.

Type hints themselves do **not** prevent incorrect values from being passed.

Instead, they help:

- Developers understand the code.
- IDEs provide better suggestions and warnings.
- Type checkers (like **mypy**) detect type-related mistakes before running the program.

---

# Why should we use Type Hints?

Type hints make code:

- Easier to read.
- Easier to maintain.
- Easier for IDEs to understand.
- Easier for static type checkers like **mypy** to analyse.

---

# Common Type Hints

## Integer

```python
age: int = 17
```

---

## Float

```python
price: float = 99.99
```

---

## String

```python
name: str = "Aniket"
```

---

## Boolean

```python
is_student: bool = True
```

---

## List

```python
numbers: list[int] = [1, 2, 3]
```

Meaning:

- A list
- Every element should be an integer

---

## Dictionary

```python
marks: dict[str, int] = {
    "Math": 95,
    "Science": 91,
}
```

Meaning:

- Keys are strings.
- Values are integers.

---

## Tuple

```python
point: tuple[int, int] = (5, 8)
```

---

## Set

```python
unique: set[str] = {"Python", "AI"}
```

---

# Type Hints in Functions

Without type hints:

```python
def greet(name):
    return "Hello " + name
```

With type hints:

```python
def greet(name: str) -> str:
    return "Hello " + name
```

Here:

- `name: str` means the parameter is expected to be a string.
- `-> str` means the function is expected to return a string.

---

# Multiple Parameters

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

# Union Types (`|`)

Sometimes a value can have more than one valid type.

Example:

```python
def greet(name: str | None) -> None:
    if isinstance(name, str):
        print(f"Good Morning {name}")
    else:
        print("Good Morning")
```

Here:

```python
str | None
```

means:

- `name` can be a string
- OR it can be `None`

Another example:

```python
def double(x: int | float) -> float:
    return x * 2
```

Here, `x` can be either an integer or a float.

---

# Any

Sometimes we don't care about the type.

```python
from typing import Any

def print_value(value: Any) -> None:
    print(value)
```

`Any` means the value can be of any type.

It is imported from the `typing` module.

---

# Type Hints with Classes

Type hints can also be used inside classes.

```python
class Student:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
```

---

# Part 2: Linting

# What is a Linter?

A **linter** is a tool that analyses your code and reports problems such as:

- Mistakes
- Bad coding style
- Unused variables
- Possible bugs
- Inconsistent formatting

Think of it as a grammar checker for your code.

---

## Example

```python
x = 10
y = 20

print(x)
```

A linter may report:

```text
Unused variable: y
```

---

# Ruff

**Ruff** is one of the most popular Python linters.

It is fast and can detect many common issues in Python code.

---

# Type Checker vs Linter

| Type Checker | Linter |
|--------------|---------|
| Checks whether type hints are used correctly | Checks overall code quality |
| Focuses on type-related errors | Focuses on code style, possible bugs and best practices |
| Example: **mypy** | Example: **Ruff** |

---

# Summary

- Python is dynamically typed.
- Type hints improve readability and help development tools.
- Python ignores type hints while executing code.
- **mypy** checks whether type hints are correct.
- **Ruff** checks overall code quality and coding style.
- Both tools help write cleaner and more reliable Python code.