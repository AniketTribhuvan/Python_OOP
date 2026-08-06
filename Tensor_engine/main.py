"""
main.py

A real, connected use of the Tensor Engine: two vibration sensors (A and
B) mounted on the same machine, streamed from a CSV file, cleaned,
converted into tensors, and analyzed with actual tensor math.

This is NOT a feature-by-feature tour of every class in isolation --
every class here is used for the job it was actually built for, in the
order a real pipeline would use it:

    Dataset             -> describe & validate the data source
    CloudCSVLoader      -> simulate authenticated fetch of the raw file
    PhysicalCSVStreamer -> stream the (large) CSV in memory-safe batches
    SensorNode/Pipeline -> normalize each batch before it becomes a tensor
    TensorProcessor     -> convert clean batches into Tensor1D objects
    Tensor1D            -> the actual math: addition + dot product
    MemoryMonitor       -> track memory while the whole thing runs

Run this file directly:
    python main.py
"""

import time

from tensor_engine import (
    Dataset,
    DataNode,
    Pipeline,
    CloudCSVLoader,
    PhysicalCSVStreamer,
    TensorProcessor,
    Tensor1D,
    MemoryMonitor,
    ShapeMismatchError,
    InvalidDataTypeError,
)


DATASET_PATH = "datasets/sensor_readings.csv"
BATCH_SIZE = 20_000


class SensorNode(DataNode):
    """
    A custom DataNode, written here in main.py rather than inside
    tensor_engine.py, to show the engine's design is actually extensible:
    Pipeline doesn't care which DataNode subclass it's holding, so new
    data types can be supported without touching the core library at all.

    Real sensors drift and have outlier spikes. This node clips extreme
    values into a sane range before the data becomes a tensor -- a
    simplified stand-in for real sensor-data cleaning.
    """

    def process(self, raw_data: list) -> list:
        cleaned = []
        for value in raw_data:
            # Clip anything outside a sane vibration range.
            # A real project would base this on the sensor's spec sheet;
            # here it's just a simple, explainable rule.
            if value > 10.0:
                value = 10.0
            elif value < -10.0:
                value = -10.0
            cleaned.append(value)
        return cleaned


def section(title: str) -> None:
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)


def describe_dataset() -> Dataset:
    section("1. Dataset — describe and validate the data source")

    dataset = Dataset.from_string("name: vibration_sensors, size: 200000")
    print(f"Dataset: {dataset.name} ({dataset.size} rows)")

    dataset.data_source = DATASET_PATH  # validated: must be a real .csv path
    print(f"Validated data source: {dataset.data_source}")

    # Show the validation actually doing its job
    try:
        dataset.data_source = "sensor_readings.json"
    except InvalidDataTypeError as e:
        print(f"Rejected bad source as expected: {e}")

    return dataset


def authenticate_and_fetch() -> None:
    section("2. CloudCSVLoader — simulated authenticated fetch")

    loader = CloudCSVLoader(api_key="sk-sensor-demo-key")
    status = loader.fetch_secure_data()
    print(f"Fetch pipeline status: {status}")
    print("(This models the auth + raw-parsing step that would happen")
    print(" before a real cloud file becomes available to stream.)")


def stream_and_analyze() -> None:
    section("3-6. Stream, clean, tensorize, and analyze the sensor data")

    sensor_pipeline = Pipeline(SensorNode())
    processor = TensorProcessor()

    total_rows = 0
    total_batches = 0
    similarity_scores = []       # dot product per batch
    combined_signal_peak = 0.0    # tracks the largest combined reading seen

    start_time = time.time()

    try:
        streamer = PhysicalCSVStreamer(DATASET_PATH, batch_size=BATCH_SIZE)

        for batch_a, batch_b in streamer.stream():
            total_batches += 1
            total_rows += len(batch_a)

            # Clean each sensor's batch through the pipeline
            clean_a = sensor_pipeline.run(batch_a)
            clean_b = sensor_pipeline.run(batch_b)

            # Convert clean batches into real tensors
            tensor_a = processor(clean_a)
            tensor_b = processor(clean_b)

            # --- Actual tensor math ---
            try:
                combined = tensor_a + tensor_b          # element-wise addition
                similarity = tensor_a * tensor_b        # dot product
            except ShapeMismatchError as e:
                # Would only happen if a batch got corrupted mid-stream
                print(f"Skipping malformed batch {total_batches}: {e}")
                continue

            similarity_scores.append(similarity)
            batch_peak = max(combined.data)
            if batch_peak > combined_signal_peak:
                combined_signal_peak = batch_peak

            if total_batches % 3 == 0:
                print(f"  Batch {total_batches}: {len(batch_a)} rows | "
                      f"similarity (dot product) = {similarity:.2f}")

    except FileNotFoundError:
        print(f"(Could not find {DATASET_PATH}. Run generate_sensor_data.py first.)")
        return

    elapsed = time.time() - start_time

    section("Results")
    print(f"Total rows processed        : {total_rows:,}")
    print(f"Total batches                : {total_batches}")
    print(f"Average similarity (A · B)   : {sum(similarity_scores)/len(similarity_scores):.2f}")
    print(f"Peak combined signal (A + B) : {combined_signal_peak:.4f}")
    print(f"Time taken                   : {elapsed:.2f} seconds")


def demo_invalid_tensor_input() -> None:
    section("7. TensorProcessor — guarding against bad input")

    processor = TensorProcessor()
    try:
        processor("this is not a list of floats")
    except InvalidDataTypeError as e:
        print(f"Rejected as expected: {e}")


def main() -> None:
    describe_dataset()
    authenticate_and_fetch()

    with MemoryMonitor():
        stream_and_analyze()

    demo_invalid_tensor_input()

    section("Workflow complete")
    print("Dataset -> CloudCSVLoader -> PhysicalCSVStreamer -> Pipeline ->")
    print("TensorProcessor -> Tensor1D math. Every class did the one job")
    print("it was actually built for.")


if __name__ == "__main__":
    main()