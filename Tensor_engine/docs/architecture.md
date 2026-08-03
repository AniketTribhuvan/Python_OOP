# Architecture

This document explains how the classes in `tensor_engine.py` fit together,
and why they're organized the way they are.

## High-level layers

The engine is organized into four loose layers, each building on the one
below it:

```
┌─────────────────────────────────────────────┐
│  Tensor Math Layer                           │
│  Tensor1D, TensorProcessor, TensorLike       │
├─────────────────────────────────────────────┤
│  Processing Layer                            │
│  DataNode, ImageNode, TextNode, Pipeline     │
├─────────────────────────────────────────────┤
│  Loading Layer                               │
│  BaseLoader → CSVLoader → ProcessedCSVLoader │
│  CloudAuthenticator, CloudCSVLoader           │
├─────────────────────────────────────────────┤
│  Data & Streaming Layer                      │
│  Dataset, LargeDatasetStreamer,              │
│  PhysicalCSVStreamer                         │
└─────────────────────────────────────────────┘
```

Cross-cutting tools (`time_execution`, `MemoryMonitor`, custom exceptions)
support every layer rather than belonging to one.

## Data & Streaming Layer

`Dataset` represents metadata about a dataset — its name, size, and a
validated `.csv` data source. The `data_source` property setter enforces
that only string paths ending in `.csv` are accepted, raising
`InvalidDataTypeError` otherwise. This keeps invalid state out of the
object entirely, rather than discovering it later during processing.

`LargeDatasetStreamer` and `PhysicalCSVStreamer` are generators that
produce data in fixed-size batches instead of loading everything into
memory at once. See `streaming.md` for details.

## Loading Layer

Loaders form a single-inheritance chain:

```
BaseLoader.load()        -> "raw_bytes"
CSVLoader.load()         -> "raw_bytes -> parsed_to_csv"
ProcessedCSVLoader.load() -> "raw_bytes -> parsed_to_csv -> dropped_empty_rows"
```

Each subclass calls `super().load()` and appends its own step, so the
final message documents the full processing history.

`CloudCSVLoader` combines two unrelated class families through **multiple
inheritance**: `CloudAuthenticator` (login logic) and `ProcessedCSVLoader`
(the loading chain above). `fetch_secure_data()` authenticates first, then
reuses the inherited `load()` chain — showing how multiple inheritance can
compose unrelated capabilities into a single class.

## Processing Layer

`DataNode` is a base class with a `process()` method that subclasses must
override. `ImageNode` and `TextNode` implement it differently (pixel
normalization vs. text tokenization) — the same interface, different
behavior, i.e. **polymorphism**.

`Pipeline` doesn't inherit from `DataNode` — it holds one via composition
(`self.node = processing_node`) and delegates to it. This was a deliberate
choice: a `Pipeline` isn't a *type* of node, it just *uses* one.

## Tensor Math Layer

`BaseTensor` is an abstract base class defining the contract
(`__add__`, `__mul__`) that `Tensor1D` must fulfill. `Tensor1D` overloads
Python's built-in operators so tensor objects behave like numeric types:

- `+` → element-wise addition, returns a new `Tensor1D`
- `*` → dot product, returns a single `float`
- `len()`, `[]`, `str()` are also overloaded for natural usage

`TensorLike` is a `Protocol` (structural typing) — any object with a
`.data` list, `__add__`, and `__mul__` satisfies it without needing to
inherit from anything. This is what allows `Tensor1D.__add__` to type-hint
its `other` parameter without hard-coupling to a specific class.

`TensorProcessor` is a callable class (`__call__`) that validates raw
input and wraps it into a `Tensor1D` — used as a clean entry point into
the tensor system.

## Cross-cutting concerns

- **`time_execution`** — a decorator applied to `Tensor1D.__add__` and
  `__mul__` that logs how long each operation takes, without touching the
  math logic itself.
- **`MemoryMonitor`** — a context manager (`__enter__`/`__exit__`) that
  tracks peak memory usage of any code block wrapped in `with MemoryMonitor():`.
- **`ShapeMismatchError`, `InvalidDataTypeError`** — custom exceptions used
  throughout instead of generic `Exception`, so calling code can catch
  specific failure modes.

## Design decisions worth knowing

- `Tensor1D` uses `__slots__` to avoid a per-instance `__dict__`, since
  tensors may be created in large numbers.
- `*` was implemented as a dot product rather than element-wise
  multiplication — a deliberate choice, documented in `tensor_math.md`.
- `BaseTensor` doesn't use `@abstractmethod`, so Python doesn't currently
  block direct instantiation of it — noted as a known gap in
  `future_work.md`.