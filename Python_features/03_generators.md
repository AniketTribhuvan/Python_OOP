# Generators

A **generator** is an object that produces values **one at a time**, only when they are requested, instead of storing all values in memory.

Generators are **iterators**, so they can be used with `next()` and `for` loops.

---

# Why do generators exist?

Suppose we want to print numbers from **1 to 1,000,000**.

One approach is to create a list.

```python
my_list = [i for i in range(1, 1_000_001)]

print(my_list)
```

This creates a list containing **all one million numbers at once**.

The problem is that all those numbers are stored in memory, which consumes a large amount of memory.

This is called **eager evaluation** because every value is created immediately.

---

Instead, imagine this process:

1. Create one number.
2. Use (print/process) that number.
3. Remove it from memory.
4. Create the next number.

This way, only **one value** is kept in memory at a time.

This is the main idea behind generators.

> **Create one value only when it is needed.**

This is called **lazy evaluation**.

---

# Ways to create generators

There are two ways to create generators.

1. Generator Function
2. Generator Expression

---

# Generator Function

A **generator function** is simply a normal function that contains the `yield` keyword.

The presence of `yield` automatically turns a normal function into a generator function.

---

# What does `yield` do?

`yield`:

- Returns a value to the caller.
- Pauses the function immediately after returning the value.
- Preserves the function's state.
- Continues execution from the same place when called again.

Example:

```python
def func():
    yield 1
    yield 2
    yield 3
```

---

# Creating a Generator Object

```python
gen = func()

print(gen)
```

**Output**

```python
<generator object func at 0x...>
```

Notice that the function did **not execute**.

Calling a generator function only creates a **generator object**.

The code inside the function starts executing only when values are requested.

---

# Using `next()`

`next()` fetches the next value from an iterator.

```python
print(next(gen))
```

**Output**

```python
1
```

Here:

- The generator starts executing.
- `yield 1` returns `1`.
- Execution pauses at that point.

Calling `next()` again:

```python
print(next(gen))
```

**Output**

```python
2
```

The generator continues from where it was paused instead of starting from the beginning.

---

# Iterating with a `for` loop

Instead of calling `next()` repeatedly, we usually use a `for` loop.

```python
def func():
    yield 1
    yield 2
    yield 3

gen = func()

for value in gen:
    print(value)
```

**Output**

```python
1
2
3
```

Internally, the `for` loop repeatedly calls:

```python
next(gen)
```

until a `StopIteration` exception is raised.

---

# Generator Expression

A **generator expression** is similar to a list comprehension.

The only difference is:

- List comprehension uses `[]`
- Generator expression uses `()`

Example:

```python
squares = (x * x for x in range(5))

print(squares)
```

**Output**

```python
<generator object <genexpr> at 0x...>
```

Iterating over it:

```python
for value in squares:
    print(value)
```

**Output**

```python
0
1
4
9
16
```

---

# Example: Printing many numbers

```python
def gen_nums(limit):
    i = 0

    while i < limit:
        yield i
        i += 1


gen_obj = gen_nums(1000)

for number in gen_obj:
    print(number)
```

Even though this prints **1000 numbers**, the generator keeps only **one number** in memory at a time.

---

# Lazy Evaluation vs Eager Evaluation

| Lists | Generators |
|--------|------------|
| Eager evaluation | Lazy evaluation |
| Creates all values immediately | Creates values only when needed |
| Stores all values in memory | Stores only one value at a time |
| Uses more memory | Memory efficient |

---

# When should you use generators?

Generators are useful when:

- Working with very large datasets.
- Reading large files.
- Processing data one item at a time.
- Memory efficiency is important.

---

# Important Note

Generators are **not better than every data structure**.

They solve a different problem.

Use a generator when:

- You don't need all values at once.
- You want to process values one by one.
- You want to reduce memory usage.

If you need random indexing (`numbers[5]`), modifying elements, or accessing the same data multiple times, a **list** is usually a better choice.