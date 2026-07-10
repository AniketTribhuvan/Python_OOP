# Difference Between Composition & Inheritance

We have studied **Inheritance**, which represents an **"Is-A" relationship**, and **Composition**, which represents a **"Has-A" relationship**.

Although both are OOP concepts used to reuse code, they solve different types of problems.

## Inheritance (Is-A Relationship)

In inheritance, a child class extends a parent class.

The child class can directly access the public and protected members of the parent class.

The child class is simply a more specialized version of the parent class.

**Examples:**
- Dog is an Animal
- Car is a Vehicle
- Student is a Person

---

## Composition (Has-A Relationship)

In composition, one class contains an object of another class.

The composite class accesses the component class through that object instead of directly inheriting from it.

The component class has its own attributes and methods because it represents a separate object.

For example:

- A **Car** has an **Engine**.
- The **Engine** is a separate object with its own attributes (horsepower, fuel type) and methods (start()).
- The **Car** simply uses the Engine object.

---

# When to use Composition & Inheritance?

Never mix them. They represent different relationships.

The easiest way to decide is to identify the relationship in the problem.

- If the relationship is **"Is-A"**, use **Inheritance**.
- If the relationship is **"Has-A"**, use **Composition**.

## Examples

| Relationship | Use |
|-------------|-----|
| Dog is an Animal | Inheritance |
| Car is a Vehicle | Inheritance |
| Student is a Person | Inheritance |
| Car has an Engine | Composition |
| Computer has a CPU | Composition |
| ChatBot has an LLM | Composition |