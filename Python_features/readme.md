# Data Streams

## Overview

This folder focuses on building memory-efficient data pipelines using advanced Python features & writing type-safe Python code using static typing.

These concepts are commonly used in modern software systems to process large amounts of data efficiently. By combining callable objects, decorators, and generators, we can build reusable and scalable data processing pipelines while monitoring their execution.
Static typing helps detect type-related errors before the program runs, making code more reliable, easier to maintain, and better suited for large-scale applications. These concepts are widely used in professional Python projects to improve code quality and reduce runtime bugs.

## Topics Covered

- callable objects (`__call__`)
- decorators
- decorators with arguments
- `functools.wraps`
- generators
- generator expressions
- lazy evaluation
- type hints
- mypy
- strict type checking

## Skills Developed

- Creating callable objects using `__call__`
- Building reusable decorators
- Preserving function metadata using `functools.wraps`
- Writing memory-efficient generators
- Processing large datasets using lazy evaluation
- Measuring function execution time using decorators
- Writing type-safe Python code
- Adding type hints to functions, variables, and classes

## Key Takeaways

- `__call__` allows objects to behave like functions.
- Decorators modify or extend function behavior without changing the original function.
- `functools.wraps` preserves the metadata of decorated functions.
- Generators produce values one at a time instead of storing everything in memory.
- Lazy evaluation improves memory efficiency when working with large datasets.
- Type hints improve code readability and maintainability.
- Static typing helps detect errors before runtime.

## 🗂️ Project Structure

```text
Python_features/
  README.md                                   # Folder overview of data streaming concepts
  NOTES.md                                    # Notes related to callable objects, decorators, generators & type hinting
  
  01_callable_objects.py                      # Understanding __call__()

  02_decorators/
    01_decorators.py                            # Understanding Python decorators
    02_decorators_with_arguments.py             # Building decorators with arguments
    03_wraps.py                                 # Preserving function metadata using functools.wraps
  
  03_generator.md                               # Understanding generators, generator expressions & lazy data streaming

  04_type_hints.py                              # Understanding basic type hints

  05_advanced_typing.md                         # Understanding TypeVar, Callable, Union & Protocol
```