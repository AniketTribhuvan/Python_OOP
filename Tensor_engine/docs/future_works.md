# Future Work & Known Limitations

Documenting known gaps honestly is part of good engineering practice.
This file tracks current limitations of the Tensor Engine and possible
next steps.

## 1. `Tensor1D.__mul__` only supports dot product

Currently `*` always computes a dot product, returning a single float.
There's no way to get element-wise multiplication (a Hadamard product)
through the same operator.

**Possible fix:** add a separate method, e.g. `elementwise_mul()`, or
introduce a wrapper type to disambiguate intent, similar to how NumPy
distinguishes `@` (matrix multiply) from `*` (element-wise).

## 4. No support for multi-dimensional tensors

`Tensor1D` only handles flat 1-D lists of floats. Real tensor libraries
support arbitrary dimensions (matrices, batches of matrices, etc).

**Possible next step:** a `TensorND` class built on nested lists or a
flat buffer with shape metadata, once the 1-D case is fully solid.

## 5. No unit tests yet

The project currently relies on manual/demo runs (see
`outputs/engine_telemetry_output.txt`) rather than an automated test
suite.

**Next step:** add a `tests/` directory with `pytest` covering:
- shape mismatch errors for both `__add__` and `__mul__`
- `Dataset.data_source` validation (valid `.csv`, invalid extension,
  non-string input)
- `TensorProcessor` validation for non-list input
- streaming output correctness for both streamer classes

## 6. No CLI or script entry point yet

Currently every component has to be imported and used from a Python
shell or another script. A small `if __name__ == "__main__":` demo block,
or a proper CLI, would make the project easier for others to try quickly.

## 7. Type hints could be tightened further

Some `Any` type hints (e.g. in `DataNode.process`) are broader than they
need to be now that concrete subclasses exist. These could be narrowed
using generics or overloads as the project matures.

---

None of the above are urgent bugs — the engine works correctly for its
current intended use. They're listed here as the natural next steps for
anyone (including future me) picking this project back up.