# TypeVar, Callable, Union & Protocol

These are some useful types provided by Python's **typing** module.

They help us write more readable code and make type checkers (like **mypy**) understand our code better.

> **Note:**
> These are only **type hints**.
> Python does **not** enforce them while running the program.

---

# 1. TypeVar

## What is TypeVar?

A **TypeVar** represents an unknown type.

Instead of fixing a type like `int` or `str`, we create a placeholder type.

Later, the type checker replaces that placeholder with the actual type based on how the function is used.

---

## Why do we need TypeVar?

Suppose we want to write a function that works for **any datatype**.

Example:

```python
print(identity(10))
print(identity("Hello"))
print(identity([1, 2, 3]))
```

The input type should be the same as the return type.

Using `Any` loses this relationship.

TypeVar preserves it.

---

## Syntax

```python
from typing import TypeVar

T = TypeVar("T")
```

`T` is just a placeholder.

You can give it any name.

```python
Item = TypeVar("Item")
```

---

## Example

```python
from typing import TypeVar

T = TypeVar("T")

def identity(value: T) -> T:
    return value

print(identity(10))
print(identity("Hello"))
print(identity([1, 2, 3]))
```

Output

```text
10
Hello
[1, 2, 3]
```

Explanation:

When we call:

```python
identity(10)
```

the type checker treats `T` as:

```python
int
```

When we call:

```python
identity("Hello")
```

it treats `T` as:

```python
str
```

The input type and return type always remain the same.

---

## Intuition

TypeVar is a placeholder that has no fixed type by itself. When you call the function, Python looks at what you passed in and says "okay, T = int for this call." Every place that same T appears in that function's signature must match that call's type.

---

## TypeVar vs Any

Using `Any`

```python
from typing import Any

def identity(value: Any) -> Any:
    return value
```

Using `TypeVar`

```python
from typing import TypeVar

T = TypeVar("T")

def identity(value: T) -> T:
    return value
```

The second version is better because the type checker understands that:

- If the input is `int`, the output is also `int`.
- If the input is `str`, the output is also `str`.

---

# 2. Callable

## What is Callable?

A **Callable** represents anything that can be called like a function.

Examples:

- Functions
- Methods
- Objects implementing `__call__()`

---

## Why do we need Callable?

Sometimes we pass functions as arguments.

Example:

```python
def execute(func):
    func()
```

Here, `func` is not an integer or a string.

It is a callable object.

---

## Syntax

```python
from typing import Callable

Callable[[parameter_types], return_type]
```

---

## Example

```python
from typing import Callable

def greet():
    print("Good Morning")

def execute(func: Callable[[], None]) -> None:
    func()

execute(greet)
```

Output

```text
Good Morning
```

Explanation:

```python
Callable[[], None]
```

means:

- Takes no arguments.
- Returns `None`.

---

## Example with Parameters

```python
from typing import Callable

def add(a: int, b: int) -> int:
    return a + b

def calculate(func: Callable[[int, int], int]) -> None:
    print(func(10, 20))

calculate(add)
```

Output

```text
30
```

Here,

```python
Callable[[int, int], int]
```

means:

- Accepts two integers.
- Returns an integer.

---

## Intuition

Callable means "this thing can be called like a function." When used as a type hint, it tells you two things: what argument types the function accepts, and what type it returns.

---

# 3. Union

## What is Union?

A **Union** means a value can be one of multiple types.

Sometimes a parameter or variable is valid for more than one datatype.

Instead of choosing only one type, we use **Union**.

---

## Why do we need Union?

Suppose a function should accept both integers and floats.

Without Union:

```python
def square(x: int):
    return x * x
```

Passing a float is also valid, but the type hint only allows integers.

Union solves this problem.

---

## Syntax

```python
from typing import Union

Union[type1, type2]
```

---

## Example

```python
from typing import Union

def square(x: Union[int, float]) -> float:
    return x * x

print(square(5))
print(square(2.5))
```

Output

```text
25
6.25
```

Both `int` and `float` are accepted.

---

## Python 3.10+

Instead of writing:

```python
Union[int, float]
```

we can simply write:

```python
int | float
```

Example:

```python
def square(x: int | float) -> float:
    return x * x
```

This is the modern and recommended syntax.

---

## Intuition

Union means the value can be one type out of several allowed types — but only one at a time, not all together.

---

# 4. Protocol

## What is a Protocol?

A **Protocol** defines a set of methods or attributes that a class should have.

Think of it as a contract.

If a class follows that contract, it can be used wherever that protocol is expected.

---

## Why do we need Protocol?

Suppose we have a function that only needs an object with a `speak()` method.

It doesn't care which class the object belongs to.

Without Protocol:

```python
def make_sound(animal):
    animal.speak()
```

Readers don't know what kind of object is expected.

Protocol solves this problem.

---

## Syntax

```python
from typing import Protocol

class ProtocolName(Protocol):
    ...
```

---

## Example

```python
from typing import Protocol

class Speaker(Protocol):

    def speak(self) -> None:
        ...

class Dog:

    def speak(self) -> None:
        print("Bark")

class Cat:

    def speak(self) -> None:
        print("Meow")

def make_sound(animal: Speaker) -> None:
    animal.speak()

make_sound(Dog())
make_sound(Cat())
```

Output

```text
Bark
Meow
```

Notice something interesting.

Neither `Dog` nor `Cat` inherits from `Speaker`.

Yet both satisfy the protocol because they implement:

```python
def speak(self):
```

This is called **structural typing**.

Python checks **what a class can do**, not **what it inherits from**.

---

## Intuition

Protocol defines a contract: a set of methods/attributes a class must have. Any class that has those methods automatically satisfies the Protocol — it doesn't need to inherit from it. If it has the right shape, it qualifies.

---

## Protocol vs Abstract Class

| Protocol | Abstract Class |
|----------|----------------|
| Defines a contract | Defines a contract |
| Classes do not need to inherit from it | Classes must inherit from it |
| Based on available methods and attributes | Based on inheritance |
| Mainly used for static type checking | Used during both design and runtime |

---

# When should we use these?

## Use TypeVar

When the input type and return type should always remain the same.

Example:

```python
identity(value)
```

---

## Use Callable

When passing functions or callable objects.

Example:

```python
Callable[[int], str]
```

---

## Use Union

When a value can have multiple valid types.

Example:

```python
int | float
```

---

## Use Protocol

When you care about what an object can do instead of which class it belongs to.

---

# Summary

| Type | Purpose |
|------|---------|
| `TypeVar` | Represents a placeholder type that stays consistent |
| `Callable` | Represents functions or callable objects |
| `Union` | A value can have multiple possible types |
| `Protocol` | Defines a contract based on methods and attributes instead of inheritance |

---

# Final Notes

- All four are provided by Python's **typing** module.
- They improve code readability.
- They help IDEs provide better suggestions.
- They help static type checkers like **mypy** detect mistakes.
- Python itself ignores these type hints while executing the program.