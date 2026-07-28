# `__enter__()` & `__exit__()` Dunder Methods (Context Managers)

`__enter__()` and `__exit__()` are special dunder methods that implement the **Context Manager Protocol**.

They are used for **resource management**, allowing Python to automatically acquire and release resources.

Common resources include:

- Files
- Database connections
- Network connections
- Locks

These methods are used with the **`with` statement**.

---

# Why do we need them?

Resources should always be released after they are no longer needed.

Suppose we manually open a file.

```python
file = open("data.txt", "r")

print(file.read())

file.close()
```

This works correctly.

But if an exception occurs before `close()` executes:

```python
file = open("data.txt", "r")

print(file.read())

10 / 0

file.close()
```

The program stops before reaching:

```python
file.close()
```

The file remains open.

This is called a **resource leak**.

---

# The Solution

Python provides the `with` statement.

```python
with open("data.txt", "r") as file:
    print(file.read())
```

When execution leaves the `with` block, Python automatically cleans up the resource.

Even if an exception occurs, the resource is still released.

---

# How does `with` work?

The `with` statement internally uses two dunder methods:

- `__enter__()`
- `__exit__()`

### If no exception occurs

Internally, Python behaves approximately like this:

```python
manager = ContextManager()

value = manager.__enter__()

try:
    # Code inside with block

finally:
    manager.__exit__(None, None, None)
```

---

### If an exception occurs

```python
manager = ContextManager()

manager.__enter__()

try:
    # Code inside with block

except Exception as e:
    manager.__exit__(
        type(e),
        e,
        e.__traceback__
    )
    raise
```

Python automatically calls both methods.

We never call them directly.

---

# `__enter__()`

## What is `__enter__()`?

`__enter__()` is called when entering the `with` block.

It is usually used to:

- Open a file
- Connect to a database
- Acquire a lock
- Allocate resources

It returns the object assigned after the `as` keyword.

---

## Syntax

```python
def __enter__(self):
    ...
    return object
```

---

## Common Structure

```python
def __enter__(self):

    # Acquire resource

    return resource
```

---

# `__exit__()`

## What is `__exit__()`?

`__exit__()` is called whenever the `with` block finishes.

It is always executed, even if an exception occurs.

It is usually used to:

- Close files
- Close database connections
- Release locks
- Clean up resources

---

## Syntax

```python
def __exit__(self, exc_type, exc_value, traceback):
    ...
```

---

# Why does `__exit__()` receive these parameters?

Python always passes three extra arguments to `__exit__()`.

```python
exc_type
exc_value
traceback
```

These tell the context manager whether an exception occurred.

If no exception occurs:

```python
exc_type = None
exc_value = None
traceback = None
```

If an exception occurs:

- `exc_type` → Type of exception (e.g. `ZeroDivisionError`)
- `exc_value` → Exception object (e.g. `"division by zero"`)
- `traceback` → Information about where the exception occurred

These parameters allow the context manager to perform different actions depending on whether execution succeeded or failed.

---

# Do we always use these parameters?

No.

Most context managers simply clean up resources and ignore them.

Example:

```python
def __exit__(self, exc_type, exc_value, traceback):

    self.file.close()

    return False
```

Even if you do not use these parameters, they **must still be present** because Python always passes them when calling `__exit__()`.

---

# When do we use these parameters?

Use them when cleanup depends on whether an exception occurred.

Examples:

- Commit or rollback a database transaction.
- Log exceptions.
- Handle specific exceptions differently.

Example:

```python
def __exit__(self, exc_type, exc_value, traceback):

    if exc_type is None:
        commit()

    else:
        rollback()

    return False
```

---

# Return Value of `__exit__()`

`__exit__()` can return either:

- `False` (or `None`)
- `True`

---

## Returning `False` (Default)

```python
def __exit__(self, exc_type, exc_value, traceback):

    self.file.close()

    return False
```

or simply:

```python
def __exit__(self, exc_type, exc_value, traceback):

    self.file.close()
```

Python performs the cleanup and then **re-raises the exception** if one occurred.

This is the default behaviour.

---

## Returning `True`

```python
def __exit__(self, exc_type, exc_value, traceback):

    print("Exception handled")

    return True
```

Returning `True` tells Python:

> "I have handled this exception."

Python will **not** re-raise the exception.

Use this only when you intentionally want to suppress an exception.

---

# Common Structures

## 1. Resource Cleanup Only (Most Common)

Use this when exceptions do not affect the cleanup process.

```python
class Resource:

    def __enter__(self):

        # Acquire resource

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        # Release resource

        return False
```

Examples:

- Files
- Locks
- Network connections

---

## 2. Exception-Aware Cleanup

Use this when cleanup depends on whether an exception occurred.

```python
class Resource:

    def __enter__(self):

        # Acquire resource

        return self

    def __exit__(self, exc_type, exc_value, traceback):

        if exc_type is None:

            # Success

            ...

        else:

            # Exception occurred

            ...

        return False
```

Examples:

- Database transactions
- Logging
- Conditional cleanup

---

# Real Example

```python
class FileManager:

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, "r")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        print("File closed")
        return False


with FileManager("data.txt") as file:
    print(file.read())
```

Even if an exception occurs while reading the file, `__exit__()` still closes it.

---

# Summary

- `__enter__()` and `__exit__()` implement the Context Manager Protocol.
- They are automatically used by the `with` statement.
- `__enter__()` is called when entering the `with` block.
- `__enter__()` usually acquires resources and returns an object.
- `__exit__()` is called whenever the `with` block finishes.
- `__exit__()` is always executed, even if an exception occurs.
- Python always passes `exc_type`, `exc_value`, and `traceback` to `__exit__()`.
- These parameters can be ignored if only resource cleanup is required.
- They are useful when cleanup depends on whether an exception occurred.
- Returning `False` (or `None`) lets Python re-raise the exception.
- Returning `True` suppresses the exception.
- Context managers make resource management automatic, safer, and easier.