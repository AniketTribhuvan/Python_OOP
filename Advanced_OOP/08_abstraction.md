# 🎭 Abstraction in Python

## What is Abstraction?

**Abstraction** is the process of **hiding implementation details** and exposing only the **essential functionality** to the user.

> **Remember:**
>
> - **Abstraction** hides **how something works**.
> - **Encapsulation** hides **the data**.

---

## Real-Life Example

Think about driving a car.

To drive it, we only use:

- Steering
- Accelerator
- Brake
- Gear

We don't need to know:

- How fuel is injected
- How pistons move
- How the engine works internally

The car hides all these complex details and only exposes the controls we actually need.

That's **Abstraction**.

---

## Python Example

```python
numbers = [10, 20, 30]
numbers.append(40)
```

When we call `append()`:

- We don't know how Python resizes memory.
- We don't know how it stores the new element.
- We don't need to know.

Python hides the implementation and only exposes the `append()` method.

This is **Abstraction**.

---

# How is Abstraction achieved in Python?

Python provides the **`abc` (Abstract Base Class)** module.

It contains:

- `ABC` class
- `@abstractmethod` decorator

---

# Before Abstract Classes...

Let's first understand **Protocol**.

## Protocol

A **Protocol** is simply a **set of rules (or a contract)** that classes must follow.

Example:

If a payment system says,

> "Every payment class must have a `pay()` method."

Then every payment class must follow that rule.

---

# Abstract Class

An **Abstract Class** is a class that:

- Inherits from `ABC`
- Contains one or more `@abstractmethod`s

It acts like a **blueprint (contract)**.

Instead of telling **how** something should work, it tells **what every subclass must implement**.

Everything a normal class can have, an abstract class can also have.

**Note** : An abstract class is still a class. The only difference is that it has at least one abstract method, so it cannot be instantiated directly.

---

# `@abstractmethod`

`@abstractmethod` marks a method as **abstract**.

It tells Python:

> "Every concrete subclass **must override this method** before its object can be created."

So it **enforces the contract** defined by the Abstract Class.

---

# Example

```python
from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):

    def pay(self):
        print("Processing UPI payment")


class CreditCard(Payment):

    def pay(self):
        print("Processing Card payment")


def checkout(payment):
    payment.pay()


checkout(UPI())
checkout(CreditCard())
```

### Output

```text
Processing UPI payment
Processing Card payment
```

---

# 1. How Abstraction Works

The `Payment` class only says:

> Every payment method must provide a `pay()` method.

It **doesn't tell how** the payment should happen.

The implementation is hidden inside:

- `UPI`
- `CreditCard`

The user simply calls:

```python
payment.pay()
```

without caring how the payment is actually processed.

That's **Abstraction**.

---

# 2. How Abstract Class Works

```python
class Payment(ABC):
```

By inheriting `ABC`, `Payment` becomes an **Abstract Base Class**.

Its job is to define a **contract**.

In this example, the contract is:

> Every payment class must implement `pay()`.

It doesn't process any payment itself.

Instead, subclasses like `UPI` and `CreditCard` provide their own implementation.

---

# 3. How `@abstractmethod` Enforces the Contract

```python
@abstractmethod
def pay(self):
    pass
```

This tells Python:

> Every concrete subclass **must override `pay()`**.

Example:

```python
class Cash(Payment):
    pass

Cash()
```

Result:

```text
TypeError:
Can't instantiate abstract class Cash
with abstract method pay
```

Python refuses to create the object because the contract wasn't followed.

---

# 4. How Everything is Connected

```text
abc module
│
├── ABC
│     │
│     └── Makes Payment an Abstract Class
│
└── @abstractmethod
      │
      └── Makes pay() mandatory

Payment (Abstract Class)
│
├── Defines the contract
│      "Every payment class must implement pay()"
│
├───────────────┐
│               │
UPI        CreditCard
│               │
└──── Both implement pay()
        │
        ▼
checkout(payment)
        │
   payment.pay()
        │
Python automatically calls
the correct implementation.
```

Here,

- **Abstraction** hides implementation details.
- **Inheritance** allows subclasses to inherit the contract.
- **Polymorphism** lets `checkout()` work with any payment object.
- **`@abstractmethod`** ensures every subclass follows the contract.

All four work together.

---

# 5. What Happens if Something is Missing?

## A) Without `ABC`

```python
class Payment:
```

Python treats it like a normal class.

No abstract behavior.

No enforcement.

---

## B) Without `@abstractmethod`

```python
class Payment(ABC):

    def pay(self):
        pass
```

Subclasses are **not forced** to override `pay()`.

Even incomplete subclasses can be instantiated.

---

## C) Without Inheriting `Payment`

```python
class UPI:

    def pay(self):
        ...
```

The program can still work because `checkout()` only calls `pay()`.

This is called **Duck Typing**.

But now there's:

- No common contract
- No protocol enforcement
- No guarantee every payment class follows the same interface

---

## D) Without Overriding `pay()`

```python
class UPI(Payment):
    pass
```

```python
UPI()
```

Result:

```text
TypeError
```

Python refuses to create the object because the contract wasn't followed.

---

## E) Without `checkout()`

You would manually write:

```python
UPI().pay()
CreditCard().pay()
```

`checkout()` is just a common function that works with **any payment object** following the same contract.

---

# Complete Flow

```text
abc module
      │
      ▼
ABC + @abstractmethod
      │
      ▼
Payment becomes an Abstract Class
      │
      ▼
Defines a contract
      │
      ▼
Every subclass must implement pay()
      │
      ▼
UPI and CreditCard implement pay()
      │
      ▼
checkout() calls payment.pay()
      │
      ▼
Python runs the correct pay() method
```

---

# 6. Why Use Abstraction?

Abstraction is used to define a **common contract** while hiding implementation details.

### Benefits

- ✅ Enforces consistency by making every subclass implement required methods.
- ✅ Hides internal implementation from the user.
- ✅ Prevents incomplete implementations using `@abstractmethod`.
- ✅ Makes code easier to extend by adding new subclasses.
- ✅ Enables polymorphism, allowing the same code to work with different objects.

---

## Short Definition

> **Abstraction defines a common contract, hides implementation details, enforces mandatory methods, and enables polymorphism, making code cleaner, more consistent, and easier to maintain.**