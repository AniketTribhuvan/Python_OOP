# Special Methods (Dunder Methods)

## What are Special Methods (Dunder Methods)?

The methods whose names **start and end with double underscores (`__`)** are called **Special Methods** or **Dunder (Double UNDERscore) Methods**.

Examples:

- `__init__`
- `__len__`
- `__getitem__`
- `__str__`
- `__repr__`
- `__add__`
- etc.

---

## Why are they called Special Methods?

Normally, we **do not call these methods directly**.

Instead, **Python automatically calls them when we use certain built-in syntax or operations.**

For example:

+-----------------------------+----------------------------------------------+
| What We Write in Python     | What Python Actually Does Behind the Scenes  |
+-----------------------------+----------------------------------------------+
| Student()                   | Calls Student.__init__() automatically       |
| len(obj)                    | Calls obj.__len__()                          |
| obj[index]                  | Calls obj.__getitem__(index)                 |
| obj1 + obj2                 | Calls obj1.__add__(obj2)                     |
| str(obj)                    | Calls obj.__str__()                          |
+-----------------------------+----------------------------------------------+

This is why they are called **special methods**.

---

# Understanding Special Methods with Examples

## 1. `__init__`

`__init__()` is automatically called whenever a new object is created.

```python
class Student:

    def __init__(self):
        print("Object Created")


obj = Student()

# Output:
# Object Created
```

Python internally does:

```python
Student.__init__(obj)
```

---

## 2. `__len__`

Suppose we have a list.

```python
numbers = [12, 13, 14]

print(len(numbers))
```

Output

```python
3
```

Internally, Python does:

```python
print(numbers.__len__())
```

The `__len__()` method returns the length of the object.

---

## 3. `__getitem__`

Suppose we access an element using indexing.

```python
numbers = [1, 2, 3]

print(numbers[0])
```

Output

```python
1
```

Internally, Python does:

```python
print(numbers.__getitem__(0))
```

The `__getitem__()` method returns the item present at the given index.

---

## Conclusion

This is how Special (Dunder) Methods work.

We usually don't call them directly.

Instead, Python automatically calls them whenever we use specific syntax like:

- Creating objects
- Using `len()`
- Indexing (`[]`)
- Using operators (`+`, `-`, `==`, etc.)

---

# Why Do We Need to Study Special Methods?

We study Special Methods because they allow **our own classes to behave like Python's built-in classes** (`list`, `tuple`, `dict`, `str`, etc.).

For example, if we create a `Library` class, Python doesn't know:

- What is the length of a Library?
- How should indexing work?

We define these behaviors by implementing Special Methods.

---

# Example: `__len__`

```python
class Library:

    def __init__(self):
        self.books = [
            "Calculus",
            "Linear Algebra",
            "Probability"
        ]


obj = Library()

# print(len(obj))
# This gives an error because Python internally calls:
#
# obj.__len__()
#
# But Library doesn't implement __len__().
```

Output

```python
TypeError: object of type 'Library' has no len()
```

Now implement `__len__()`.

```python
class Library:

    def __init__(self):
        self.books = [
            "Calculus",
            "Linear Algebra",
            "Probability"
        ]

    def __len__(self):
        return len(self.books)


obj = Library()

print(len(obj))
```

Python internally does:

```python
obj.__len__()
```

which returns

```python
len(self.books)
```

Output

```python
3
```

Now our custom object behaves just like a Python list when using `len()`.

---

# Example: `__getitem__`

Suppose we want to access books using indexing.

```python
class Library:

    def __init__(self):
        self.books = [
            "Calculus",
            "Linear Algebra",
            "Probability"
        ]

    def __getitem__(self, index):
        return self.books[index]


obj = Library()

print(obj[0])
print(obj[2])
```

Python internally does:

```python
obj.__getitem__(0)
obj.__getitem__(2)
```

Output

```python
Calculus
Probability
```

Now our custom object supports indexing just like a Python list.

---

# Summary

+-----------------+---------------------------------------------------------+
| Special Method  | Purpose                                                 |
+-----------------+---------------------------------------------------------+
| __init__()      | Initializes an object after it is created.              |
| __len__()       | Defines what len(obj) should return.                    |
| __getitem__()   | Defines how indexing (obj[index]) works.                |
| __add__()       | Defines how the + operator works.                       |
| __str__()       | Defines what print(obj) should display.                 |
+-----------------+---------------------------------------------------------+

---

## Key Takeaway

Whenever you write Python syntax like:

```python
Student()
len(obj)
obj[0]
obj1 + obj2
```

Python internally translates it into:

```python
Student.__init__()
obj.__len__()
obj.__getitem__(0)
obj1.__add__(obj2)
```

This mechanism allows us to make our own classes behave exactly like Python's built-in objects by implementing the appropriate Special (Dunder) Methods.