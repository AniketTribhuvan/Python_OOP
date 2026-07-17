# `__str__()`, `__repr__()` & `__slots__`

These are all **dunder (double underscore) methods**, but they solve completely different problems.

- `__str__()` → Human-readable representation
- `__repr__()` → Developer/debug representation
- `__slots__` → Memory optimization

---

# 1. `__str__()`

`__str__()` is a dunder method used to define a **human-readable representation** of an object.

Whenever we do any of the following:

```python
print(obj)
```

```python
str(obj)
```

```python
f"{obj}"
```

Python internally calls:

```python
obj.__str__()
```

Developers implement `__str__()` to display a clean and user-friendly representation of an object.

It is mainly meant for **end users**.

---

## Without `__str__()`

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


s = Student("Aniket", 17)

print(s)
```

**Output**

```python
<__main__.Student object at 0x000001E93A6F1C10>
```

By default, Python prints:

- Class name
- Memory address of the object

This is not very useful for users.

---

## Implementing `__str__()`

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(Name={self.name}, Age={self.age})"


s = Student("Aniket", 17)

print(s)
```

**Output**

```python
Student(Name=Aniket, Age=17)
```

Now Python executes our custom `__str__()` method instead of the default representation.

---

# 2. `__repr__()`

`__repr__()` is a dunder method used to define the **official representation** of an object.

Whenever we execute:

```python
repr(obj)
```

Python internally calls:

```python
obj.__repr__()
```

Unlike `__str__()`, `__repr__()` is mainly meant for **developers**.

It should return a representation that is as clear and unambiguous as possible.

---

## Without `__repr__()`

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


s = Student("Aniket", 17)

print(repr(s))
```

**Output**

```python
<__main__.Student object at 0x000001E93A6F1C10>
```

By default, `__repr__()` also prints the class name and memory address.

So until we define our own methods, both `__str__()` and `__repr__()` behave similarly.

---

## Implementing `__repr__()`

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student('{self.name}', {self.age})"


s = Student("Aniket", 17)

print(repr(s))
```

**Output**

```python
Student('Aniket', 17)
```

Now Python executes our custom `__repr__()` method.

---

# Difference between `__str__()` & `__repr__()`

| `__str__()` | `__repr__()` |
|-------------|--------------|
| Human-readable representation | Developer/debug representation |
| Used by `print()`, `str()` and f-strings | Used by `repr()` |
| User-friendly | More precise and unambiguous |
| Mainly for end users | Mainly for developers |

---

# 3. `__slots__`

`__slots__` is completely different from `__str__()` and `__repr__()`.

It is used for **memory optimization**.

---

## First understand `__dict__`

Normally, every Python object stores its instance variables inside a dictionary called `__dict__`.

Example:

```python
class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


s = Student("Aniket", 17)

print(s.__dict__)
```

**Output**

```python
{
    "name": "Aniket",
    "age": 17
}
```

So every instance variable is stored inside this dictionary.

---

## Why does Python use a dictionary?

Because dictionaries are flexible.

We can add new attributes anytime.

Example:

```python
s.city = "Nashik"
```

Python simply stores this new attribute inside `s.__dict__`.

---

## The problem

Every object gets its own dictionary.

For example:

- 10 objects → 10 dictionaries
- 1,000 objects → 1,000 dictionaries
- 10 million objects → 10 million dictionaries

When millions of objects are created, these dictionaries consume a lot of memory.

---

## How `__slots__` solves this

Using `__slots__`, we tell Python:

> "Don't create a `__dict__` for every object. Only reserve memory for these specific attributes."

As a result:

- Less memory is used
- Attribute access can be slightly faster
- New attributes cannot be added accidentally

---

## Using `__slots__`

```python
class Student:

    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


s = Student("Aniket", 17)

# print(s.__dict__)
# AttributeError

# s.city = "Nashik"
# AttributeError
```

Notice that `__slots__` is defined **inside the class**, not inside `__init__()`.

Since Python only reserves memory for `"name"` and `"age"`:

- There is no `__dict__` for the object.
- New attributes like `city` cannot be created.

---

# When should you use `__slots__`?

Use `__slots__` only when:

- You are creating a very large number of objects.
- Memory usage matters.
- The object's attributes are fixed and won't change.

For normal Python programs, using `__slots__` is usually **not necessary**.