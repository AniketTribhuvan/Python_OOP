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