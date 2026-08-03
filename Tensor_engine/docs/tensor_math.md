# Tensor Math

This document explains exactly how `Tensor1D`'s math operations work,
including a design decision that's easy to misread if you're expecting
NumPy-like behavior.

## Addition (`+`) — element-wise

```python
t1 = Tensor1D([1.0, 2.0, 3.0])
t2 = Tensor1D([4.0, 5.0, 6.0])
t3 = t1 + t2
```

Internally:

```python
zip(t1.data, t2.data)              # (1,4), (2,5), (3,6)
result = [a + b for a, b in ...]    # [5.0, 7.0, 9.0]
return Tensor1D(result)
```

`t1 + t2` returns a **new `Tensor1D`** — `Tensor1D([5.0, 7.0, 9.0])`.

## Multiplication (`*`) — dot product, not element-wise

This is the detail most worth understanding and explaining clearly:
`Tensor1D.__mul__` does **not** multiply element-by-element. It computes
a dot product and returns a single `float`.

```python
dot = t1 * t2
```

Internally:

```python
zip(t1.data, t2.data)                    # (1,4), (2,5), (3,6)
result = sum(a * b for a, b in ...)       # 4 + 10 + 18 = 32.0
return result
```

`t1 * t2` returns `32.0` — a plain number, not a tensor.

### Why document this explicitly?

Because `*` on vector-like objects often implies element-wise
multiplication (that's what NumPy arrays do by default). Here it was
implemented as a dot product on purpose, since a dot product is one of
the most common operations tensors are used for. It's called out here so
that anyone using — or reviewing — this code isn't surprised by the
return type.

## Shape validation

Both `__add__` and `__mul__` check that both tensors have equal length
before doing any math:

```python
if len(self.data) == len(other.data):
    ...
else:
    raise ShapeMismatchError(
        f"Cannot operate on tensors of different lengths: {len(self.data)} vs {len(other.data)}"
    )
```

This fails fast with a clear, specific error rather than letting `zip()`
silently truncate to the shorter length (which is what would happen if
this check weren't there — a subtle bug that would only surface later
with wrong-looking results, not a crash).

## Supporting dunder methods

```python
len(t1)     # -> 3           (via __len__)
t1[1]       # -> 2.0         (via __getitem__)
print(t1)   # -> Tensor1D([1.0, 2.0, 3.0])   (via __str__ / __repr__)
```

These make `Tensor1D` behave like a native Python sequence in day-to-day
use, even though it's a custom class.

## Performance telemetry

Both operations are decorated with `@time_execution` (see
`architecture.md`), so every call automatically prints its execution time
in milliseconds — useful for spotting slow operations on large tensors
without adding manual timing code at every call site.

## Memory layout

`Tensor1D` uses `__slots__ = ['data']`, which prevents Python from
creating a per-instance `__dict__`. This matters once you're creating many
tensors (e.g. one per streamed batch) — it reduces the memory overhead per
object.