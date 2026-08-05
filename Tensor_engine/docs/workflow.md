# Workflow — End-to-End Walkthrough

This document walks through a realistic use of the Tensor Engine from
start to finish, tracing exactly what happens at each step.

## Scenario

We want to: describe a dataset, validate its source file, load it through
an authenticated cloud loader, stream a CSV file in batches, process a
batch through a pipeline node, convert it into a tensor, and run tensor
math on it — all while logging performance and memory usage.

## Step 1 — Describe the dataset

```python
from tensor_engine import Dataset

d1 = Dataset.from_string("name: sensor_readings, size: 6")
d1.data_source = "datasets/sample_dataset.csv"
```

`from_string` parses a formatted string into a new `Dataset` instance.
Setting `data_source` triggers the property setter, which validates the
path is a string ending in `.csv` before storing it — an invalid path
(e.g. `.json`) raises `InvalidDataTypeError` immediately, rather than
failing later during loading.

## Step 2 — Authenticate and load

```python
from tensor_engine import CloudCSVLoader

loader = CloudCSVLoader(api_key="sk-demo-12345")
result = loader.fetch_secure_data()
# -> "Authenticating with key: sk-demo-12345"
# -> "raw_bytes -> parsed_to_csv -> dropped_empty_rows"
```

`fetch_secure_data()` authenticates first (from `CloudAuthenticator`),
then calls `load()`, which runs through the full inheritance chain
(`BaseLoader → CSVLoader → ProcessedCSVLoader`), each layer appending its
own processing step to the message.

## Step 3 — Stream the CSV in batches

```python
from tensor_engine import PhysicalCSVStreamer

streamer = PhysicalCSVStreamer("datasets/sample_dataset.csv", batch_size=2)
for batch_A, batch_B in streamer.stream():
    print(batch_A, batch_B)
```

The streamer reads the file line by line rather than loading it entirely
into memory, yielding a batch as soon as `batch_size` rows have
accumulated. See `streaming.md` for the full mechanics.

## Step 4 — Process a batch through a pipeline

```python
from tensor_engine import Pipeline, ImageNode

pipeline = Pipeline(ImageNode())
normalized = pipeline.run([0, 128, 255])
# -> [0.0, 0.5019607843137255, 1.0]
```

`Pipeline` delegates to whichever node it was given — swapping in
`TextNode()` instead would tokenize text rather than normalize pixels,
with no change to `Pipeline` itself.

## Step 5 — Convert to a tensor

```python
from tensor_engine import TensorProcessor

processor = TensorProcessor()
tensor = processor(normalized)
# -> Tensor1D([0.0, 0.5019607843137255, 1.0])
```

## Step 6 — Tensor math

```python
from tensor_engine import Tensor1D

t1 = Tensor1D([1.0, 2.0, 3.0])
t2 = Tensor1D([4.0, 5.0, 6.0])

t3 = t1 + t2   # element-wise -> Tensor1D([5.0, 7.0, 9.0])
dot = t1 * t2   # dot product -> 32.0
```

Both `__add__` and `__mul__` are wrapped with `@time_execution`, so every
call automatically prints how long it took:

```
[Telemetry] __add__ executed in 0.0062 ms
[Telemetry] __mul__ executed in 0.0205 ms
```

## Step 7 — Track memory usage

```python
from tensor_engine import MemoryMonitor

with MemoryMonitor():
    big = Tensor1D([1.0] * 1_000_000)
    _ = big + Tensor1D([1.0] * 1_000_000)
```

```
--- Starting Memory Monitor ---
[Telemetry] __add__ executed in 1168.6680 ms
--- Memory Monitor Closed | Peak Usage: 46.2052 MB ---
```

## Error handling along the way

Two custom exceptions guard the system at multiple points:

- `InvalidDataTypeError` — raised by `Dataset.data_source` for non-`.csv`
  paths, and by `TensorProcessor` for non-list input.
- `ShapeMismatchError` — raised by `Tensor1D.__add__` / `__mul__` when two
  tensors have different lengths.

```python
try:
    Tensor1D([1.0, 2.0, 3.0]) + Tensor1D([1.0, 2.0])
except ShapeMismatchError as e:
    print(e)
    # -> Cannot operate on tensors of different lengths: 3 vs 2
```

See `outputs/engine_telemetry_output.txt` for a full sample run combining
every step above.