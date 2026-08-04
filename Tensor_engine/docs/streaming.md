# Streaming

This document explains how the Tensor Engine handles datasets too large to
comfortably fit in memory, using Python generators.

## Why generators?

A normal function that returns a full list has to build the entire list in
memory before returning anything. A **generator function** (any function
using `yield`) instead pauses after producing one value, and only resumes
when the next value is requested. This means a dataset of any size can be
processed one batch at a time, using a small, constant amount of memory —
regardless of how large the full dataset is.

## `LargeDatasetStreamer` — synthetic batches

```python
streamer = LargeDatasetStreamer(total_rows=3000, batch_size=1000)
for batch in streamer.stream():
    print(len(batch))
```

```python
def stream(self):
    for i in range(0, self.total_rows, self.batch_size):
        batch = [2.0] * self.batch_size
        print(f"Yielding batch of {self.batch_size} floats...")
        yield batch
```

Each call to `stream()` produces one batch of `batch_size` floats at a
time. With `total_rows=3000` and `batch_size=1000`, this yields exactly 3
batches, and at no point are more than 1000 floats held in memory at once.

This class uses synthetic placeholder data (`[2.0] * batch_size`) — it
exists to demonstrate the batching *mechanism* in isolation, before
introducing the complexity of reading a real file.

## `PhysicalCSVStreamer` — real file batches

```python
streamer = PhysicalCSVStreamer("datasets/sample_dataset.csv", batch_size=2)
for batch_A, batch_B in streamer.stream():
    print(batch_A, batch_B)
```

```python
def stream(self):
    batch_A, batch_B = [], []
    with open(self.file_path, "r") as file:
        next(file, None)  # skip header row
        for line in file:
            columns = line.strip().split(",")
            val_A = float(columns[0])
            val_B = float(columns[1])
            batch_A.append(val_A)
            batch_B.append(val_B)
            if len(batch_A) == self.batch_size:
                yield batch_A, batch_B
                batch_A, batch_B = [], []
```

This reads the CSV file **line by line** rather than loading it all with
`.readlines()`. The file handle only ever has one line "in flight" at a
time, and only `batch_size` rows accumulate in memory before being
yielded and reset.

### Walkthrough with `datasets/sample_dataset.csv`

Given a file with 6 data rows and `batch_size=2`, the stream yields 3
batches, each containing 2 rows worth of data from columns A and B.

### A known edge case

If the total number of data rows isn't evenly divisible by `batch_size`,
the leftover rows accumulated in `batch_A` / `batch_B` are **never
yielded**, because the `yield` only happens inside the `if` check within
the loop — once the file ends, any partial batch still sitting in memory
is silently discarded.

This is a real, currently-unfixed limitation of the streamer — documented
here on purpose rather than hidden, and tracked as an improvement in
`future_work.md`.

## When to use which streamer

- Use `LargeDatasetStreamer` when you need placeholder/synthetic data to
  test a pipeline's batching behavior without needing a real file.
- Use `PhysicalCSVStreamer` when reading actual tabular data from disk in
  a memory-safe way.