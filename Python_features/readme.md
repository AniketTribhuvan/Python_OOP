# Data Streams

## Overview

This folder focuses on building memory-efficient data pipelines using advanced Python features.

## Topics Covered

- callable objects (`__call__`)
- decorators
- decorators with arguments
- `functools.wraps`
- generators
- generator expressions
- lazy evaluation

## Skills Developed

- Creating callable objects using `__call__`
- Building reusable decorators
- Preserving function metadata using `functools.wraps`
- Writing memory-efficient generators
- Processing large datasets using lazy evaluation

## Key Takeaways

- `__call__` allows objects to behave like functions.
- Decorators modify or extend function behavior without changing the original function.
- `functools.wraps` preserves the metadata of decorated functions.
- Generators produce values one at a time instead of storing everything in memory.
- Lazy evaluation improves memory efficiency when working with large datasets.

## 🗂️ Project Structure

```text
Python_features/
  README.md                                   # Folder overview of data streaming concepts
  NOTES.md                                    # Notes and concepts related to callable objects, decorators, and generators
  
  01_callable_objects.py                      # Understanding __call__()

  02_decorators/
    01_decorators.py                            # Understanding Python decorators
    02_decorators_with_arguments.py             # Building decorators with arguments
    03_wraps.py                                 # Preserving function metadata using functools.wraps
```