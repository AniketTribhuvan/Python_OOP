# Custom Exceptions

We have already learned **Exception Handling** and how to **raise exceptions** in the **Python_Foundations** repository.

To study **Exception Handling** and **raising exceptions**, visit:

https://github.com/AniketTribhuvan/Python_foundations/tree/9040b4d748a952f43b8020e97a2d8417003df1fb/File_IO_Exception/Exception_handling

Now let's learn **Custom Exceptions**.

---

# What are Custom Exceptions?

Python already provides many built-in exceptions such as:

- `ValueError`
- `TypeError`
- `IndexError`
- `FileNotFoundError`

Sometimes these built-in exceptions are not descriptive enough for our program.

Sometimes we need to raise our own exceptions that better describe a specific problem.

In such cases, we create **Custom Exceptions**.

---

# Why do we need Custom Exceptions?

Suppose we are creating a bank system.

If a user tries to withdraw more money than their balance, we could write:

```python
raise ValueError("Not enough balance")
```

This works, but `ValueError` doesn't clearly describe what actually happened.

Instead, we can create our own exception.

Example:

```python
InsufficientBalanceError
```

Now the exception itself tells us exactly what went wrong.

Custom exceptions make programs easier to understand and debug.

---

# How to Create a Custom Exception?

A custom exception is simply a class that inherits from Python's `Exception` class.

Example:

```python
class InvalidAgeError(Exception):
    pass
```

Here:

- `InvalidAgeError` is our custom exception.
- It inherits from `Exception`.
- `pass` means we are not adding any extra functionality yet.

---

# Why do we inherit from `Exception`?

Python recognizes every class that inherits from `Exception` as an exception.

That means we can:

- Raise it using `raise`.
- Catch it using `except`.

Example:

```python
class InvalidAgeError(Exception):
    pass

raise InvalidAgeError("Age must be at least 18")
```

Without inheriting from `Exception`, Python will not treat the class as an exception.

---

# Real Example

```python
class InsufficientBalanceError(Exception):
    pass


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):

        if amount > self.balance:
            raise InsufficientBalanceError("Not enough balance")

        self.balance -= amount


account = BankAccount(1000)

try:
    account.withdraw(1500)

except InsufficientBalanceError as e:
    print(e)
```

Output

```text
Not enough balance
```

Explanation:

- We created a custom exception named `InsufficientBalanceError`.
- If the withdrawal amount is greater than the available balance, we raise that exception.
- The `except` block catches it and prints the error message.

---

# Summary

- Custom exceptions are user-defined exceptions.
- They are useful when built-in exceptions are not descriptive enough.
- A custom exception is created by inheriting from the `Exception` class.
- After inheriting from `Exception`, Python treats the class as a normal exception.
- Custom exceptions can be raised using `raise` and caught using `except`.
- They make code easier to read, understand and debug.