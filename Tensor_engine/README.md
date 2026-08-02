# Tensor Engine

A small educational tensor-processing library built while studying Python
Object-Oriented Programming as part of my MSBTE AI/ML diploma (K Scheme).

It simulates — in miniature — the pieces real ML frameworks like PyTorch
use internally: dataset loading and validation, batching, tensor math,
telemetry, and memory profiling. The goal wasn't to build a production ML
library — it was to deliberately practice and demonstrate as many core
Python OOP concepts as possible in one coherent, working system.

## Why this project exists

Most OOP tutorials teach concepts in isolation — one lesson on inheritance,
another on decorators, another on generators. I wanted a single project
where all of these ideas had to work *together* to produce something
functional, the way they do in real codebases. Tensor Engine is that
project.

## Concepts demonstrated

| Concept | Where |
|---|---|
| Encapsulation | `Dataset` — private attributes + validated property setters |
| Single & multiple inheritance | `BaseLoader → CSVLoader → ProcessedCSVLoader`, `CloudCSVLoader` |
| Polymorphism | `DataNode` subclasses (`ImageNode`, `TextNode`) |
| Abstraction | `BaseTensor`, `DataNode` |
| Operator overloading | `Tensor1D.__add__`, `__mul__`, `__len__`, `__getitem__`, `__str__` |
| Decorators | `time_execution` — automatic performance telemetry |
| Context managers | `MemoryMonitor` — peak memory tracking |
| Generators | `LargeDatasetStreamer`, `PhysicalCSVStreamer` — memory-safe batching |
| Structural typing (Protocol) | `TensorLike` — duck typing contract |
| Custom exceptions | `ShapeMismatchError`, `InvalidDataTypeError` |

## Project structure

```
Tensor_engine/

  README.md                 # Project overview, setup instructions, concepts demonstrated, and documentation

  requirements.txt          # Project dependencies and future development tools (mypy, ruff, etc.)

  tensor_engine.py          # Educational tensor-processing library demonstrating core Python OOP concepts

  main.py                   # Entry point for running and testing the Tensor Engine

  datasets/                 # Sample datasets used by PhysicalCSVStreamer
    sensor_readings.csv     # Sample sensor dataset used by main.py

  docs/                     # Project documentation and implementation details
    architecture.md         # System architecture and class relationships
    workflow.md             # End-to-end project execution workflow
    tensor_math.md          # Tensor operations and mathematical implementation
    streaming.md            # Dataset streaming, generators, and batching
    future_work.md          # Current limitations and future improvements
```

## Getting started

```bash
git clone <your-repo-url>
cd Tensor_Engine
pip install -r requirements.txt
python tensor_engine.py
```

No external dependencies are required to run the core engine — the
standard library (`typing`, `functools`, `tracemalloc`, `time`, `abc`) is
enough. `requirements.txt` is kept for future tooling (linting, testing).

## Quick usage example

```python
from tensor_engine import Tensor1D

t1 = Tensor1D([1.0, 2.0, 3.0])
t2 = Tensor1D([4.0, 5.0, 6.0])

t3 = t1 + t2          # element-wise addition -> Tensor1D([5.0, 7.0, 9.0])
dot = t1 * t2          # dot product -> 32.0
```

See `docs/workflow.md` for a full end-to-end walkthrough and
`docs/tensor_math.md` for details on how the math operations work.

## Documentation index

- [`docs/architecture.md`](docs/architecture.md) — how the classes fit together
- [`docs/workflow.md`](docs/workflow.md) — a full walkthrough from dataset to tensor math
- [`docs/tensor_math.md`](docs/tensor_math.md) — addition vs. dot product, shape checking
- [`docs/streaming.md`](docs/streaming.md) — how large datasets are streamed in batches
- [`docs/future_work.md`](docs/future_work.md) — known limitations and next steps

## About me

I'm Aniket, a second-year MSBTE AI/ML diploma student. This project is
part of my portfolio while I work toward an AI/ML role in Bangalore after
graduation. Feedback and suggestions are welcome.