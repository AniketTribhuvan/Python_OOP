"""
tensor_engine.py

A small educational tensor-processing library built to practice core
Python OOP concepts: encapsulation, inheritance (single & multiple),
polymorphism, abstraction, operator overloading, decorators, context
managers, generators, and structural typing (Protocol).
"""

from abc import ABC, abstractmethod
from typing import List, Iterator, Callable, Any, Protocol
from functools import wraps
import tracemalloc
import time
from types import TracebackType


# --------------------------------------------------------------------------
# Custom Exceptions
# --------------------------------------------------------------------------
class ShapeMismatchError(Exception):
    pass


class InvalidDataTypeError(Exception):
    pass


# --------------------------------------------------------------------------
# Structural typing (Protocol) — duck typing contract for tensor-like objects
# --------------------------------------------------------------------------
class TensorLike(Protocol):
    data: List[float]

    def __add__(self, other: 'TensorLike') -> 'TensorLike': ...
    def __mul__(self, other: 'TensorLike') -> float: ...


# --------------------------------------------------------------------------
# Dataset — encapsulation, class variables, classmethods, properties
# --------------------------------------------------------------------------
class Dataset:
    total_datasets_loaded = 0

    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size
        self.__data_source: str | None = None
        Dataset.total_datasets_loaded += 1

    @classmethod
    def from_string(cls, raw_string: str) -> 'Dataset':
        data = [item.split(":")[1].strip() for item in raw_string.split(",")]
        extracted_name = data[0]
        extracted_size = int(data[1])
        return cls(extracted_name, extracted_size)

    @property
    def data_source(self) -> str | None:
        return self.__data_source

    @data_source.setter
    def data_source(self, file_path: str) -> None:
        if isinstance(file_path, str):
            if file_path.endswith(".csv"):
                self.__data_source = file_path
                print(f"[{self.name}] Securely locked data source to: {self.__data_source}")
            else:
                raise InvalidDataTypeError("CRITICAL ERROR: Only .csv pipelines are supported.")
        else:
            raise InvalidDataTypeError("CRITICAL ERROR: Data source must be a string file path.")


# --------------------------------------------------------------------------
# DataNode family — polymorphism + composition
# --------------------------------------------------------------------------
class DataNode:
    def process(self, raw_data: Any) -> Any:
        raise NotImplementedError("Subclasses must implement this method")


class ImageNode(DataNode):
    def process(self, raw_data: List[float]) -> List[float]:
        pixels = [(pixel / 255) for pixel in raw_data]
        return pixels


class TextNode(DataNode):
    def process(self, raw_data: str) -> List[str]:
        text = raw_data.lower()
        result = text.split()
        return result


class Pipeline:
    def __init__(self, processing_node: ImageNode | TextNode) -> None:
        self.node = processing_node

    def run(self, raw_data: str | List[float]) -> List[float] | List[str]:
        result = self.node.process(raw_data)
        return result


# --------------------------------------------------------------------------
# Loader chain — single inheritance + super()
# --------------------------------------------------------------------------
# Educational implementation to demonstrate inheritance,
# method overriding, and super().
#
# These classes simulate the stages of a data-loading pipeline
# and do not perform real CSV loading. Actual file reading is
# implemented separately by PhysicalCSVStreamer.

class BaseLoader:
    def load(self) -> str:
        return "raw_bytes"


class CSVLoader(BaseLoader):
    def load(self) -> str:
        message = super().load()
        message += " -> parsed_to_csv"
        return message


class ProcessedCSVLoader(CSVLoader):
    def load(self) -> str:
        message = super().load()
        message += " -> dropped_empty_rows"
        return message


class CloudAuthenticator:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def authenticate(self) -> bool:
        print(f"Authenticating with key: {self.api_key}")
        return True


class CloudCSVLoader(CloudAuthenticator, ProcessedCSVLoader):
    def __init__(self, api_key: str) -> None:
        CloudAuthenticator.__init__(self, api_key)

    def fetch_secure_data(self) -> Any:
        if self.authenticate():
            message = self.load()
            return message


# --------------------------------------------------------------------------
# BaseTensor — abstraction
# --------------------------------------------------------------------------
class BaseTensor(ABC):
    """
    Abstract base class for all tensor types.

    Uses @abstractmethod so Python actually enforces this contract at the
    language level: any subclass that doesn't override __add__ and __mul__
    cannot be instantiated, and BaseTensor itself can never be instantiated
    directly.
    """

    @abstractmethod
    def __add__(self, other: 'TensorLike') -> None:
        raise NotImplementedError("Child Class must implement __add__ method.")

    @abstractmethod
    def __mul__(self, other: 'TensorLike') -> None:
        raise NotImplementedError("Child Class must implement __mul__ method.")


# --------------------------------------------------------------------------
# time_execution — decorator
# --------------------------------------------------------------------------
def time_execution(func: Callable[..., Any]) -> Callable[..., Any]:
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = (end_time - start_time) * 1000
        print(f"[Telemetry] {func.__name__} executed in {elapsed_time:.4f} ms")
        return result
    return wrapper


# --------------------------------------------------------------------------
# MemoryMonitor — context manager
# --------------------------------------------------------------------------
class MemoryMonitor:
    def __enter__(self) -> object:
        print("--- Starting Memory Monitor ---")
        tracemalloc.start()
        return self

    def __exit__(self, exc_type: type[BaseException] | None, exc: BaseException | None,
                 tb: TracebackType | None) -> None:
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        peak_mb = peak / (1024 * 1024)
        print(f"--- Memory Monitor Closed | Peak Usage: {peak_mb:.4f} MB ---")


# --------------------------------------------------------------------------
# Tensor1D — operator overloading, __slots__
# --------------------------------------------------------------------------
class Tensor1D(BaseTensor):
    __slots__ = ['data']

    def __init__(self, input_data: List[float]) -> None:
        self.data = input_data

    @time_execution
    def __add__(self, other: 'TensorLike') -> 'Tensor1D':
        if len(self.data) == len(other.data):
            iterables = zip(self.data, other.data)
            result = [(a + b) for a, b in iterables]
            new_instance_obj = Tensor1D(result)
            return new_instance_obj
        else:
            raise ShapeMismatchError(
                f"Cannot operate on tensors of different lengths: {len(self.data)} vs {len(other.data)}"
            )

    @time_execution
    def __mul__(self, other: 'TensorLike') -> float:
        if len(self.data) == len(other.data):
            iterables = zip(self.data, other.data)
            result = sum((a * b) for a, b in iterables)
            return result
        else:
            raise ShapeMismatchError(
                f"Cannot operate on tensors of different lengths: {len(self.data)} vs {len(other.data)}"
            )

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, key: int) -> float:
        return self.data[key]

    def __str__(self) -> str:
        return f"Tensor1D({self.data})"

    def __repr__(self) -> str:
        return self.__str__()


# --------------------------------------------------------------------------
# TensorProcessor — callable object
# --------------------------------------------------------------------------
class TensorProcessor:
    def __call__(self, raw_data: List[float]) -> 'Tensor1D':
        if isinstance(raw_data, list):
            tensor_obj = Tensor1D(raw_data)
            return tensor_obj
        else:
            raise InvalidDataTypeError("CRITICAL ERROR: TensorProcessor requires a list of floats.")


# --------------------------------------------------------------------------
# Streamers — generators for memory-efficient batching
# --------------------------------------------------------------------------
class LargeDatasetStreamer:
    def __init__(self, total_rows: int = 10000, batch_size: int = 1024) -> None:
        self.total_rows = total_rows
        self.batch_size = batch_size

    def stream(self) -> Iterator[List[float]]:
        for i in range(0, self.total_rows, self.batch_size):
            batch = [2.0] * self.batch_size
            print(f"Yielding batch of {self.batch_size} floats...")
            yield batch


class PhysicalCSVStreamer:
    def __init__(self, file_path: str, batch_size: int = 1024):
        self.file_path = file_path
        self.batch_size = batch_size

    def stream(self) -> Iterator[tuple[List[float], List[float]]]:
        batch_A = []
        batch_B = []
        with open(self.file_path, "r") as file:
            next(file, None)
            for line in file:
                columns = line.strip().split(",")
                val_A = float(columns[0])
                val_B = float(columns[1])
                batch_A.append(val_A)
                batch_B.append(val_B)
                if len(batch_A) == self.batch_size:
                    yield batch_A, batch_B
                    batch_A = []
                    batch_B = []

            # FIX: without this, any leftover rows that don't fill a full
            # batch (e.g. 5 rows with batch_size=2 -> last row alone) would
            # never be yielded and would be silently lost. This flushes
            # whatever remains once the file has been fully read.
            if batch_A:
                yield batch_A, batch_B