# FixedArrayList

## Introduction

The reason for why I put **FixedArrayList** instead of only **Array** is because the behavior and the methods are not the same. There are methods implemented here that are not allowed in a traditional low-level array abstraction. This structure behaves like a restricted list built on top of a fixed-size array, not like a primitive array itself.

This implementation is designed for academic purposes, following strict data structure rules: fixed capacity, manual shifting of elements, explicit size tracking, and controlled access operations.

---

## 1. Conceptual Difference: Array vs FixedArrayList

### 1.1 Traditional Array (Conceptual Model)

A traditional array:

- Has fixed capacity
- Allows direct index access
- Does not provide high-level methods like:
  - `insert_before`
  - `insert_after`
  - `remove_value`
  - `binary_search` (as a built-in behavior)
- Does not track logical size separately from capacity in low-level models

In many programming languages, arrays:

- Do not shift elements automatically
- Do not prevent overwriting
- Do not enforce abstraction boundaries

They are raw storage structures.

---

### 1.2 FixedArrayList (This Implementation)

This structure:

- Has fixed capacity
- Tracks logical size separately from physical capacity
- Prevents insertion when full
- Prevents access when empty
- Automatically shifts elements when inserting or removing
- Provides high-level operations similar to a list
- Enforces error handling using custom exceptions

This makes it closer to a controlled list implementation built on top of a static array.

---

## 2. Core Structural Design

### 2.1 Internal State

The class maintains three core attributes:

- `__capacity__` → maximum number of elements
- `__size__` → current number of valid elements
- `__A__` → underlying fixed storage (`list[Optional[T]]`)

Important distinction:

- **Capacity** = physical limit
- **Size** = logical number of stored elements
- Only indices `[0, size)` are considered valid

Elements beyond `size - 1` are ignored by design.

---

## 3. Step-by-Step Design Decisions

### Step 1: Capacity Validation

At initialization:

```python
if capacity <= 0:
    raise CapacityError(...)
```

This enforces structural correctness from the beginning. A raw array might allow invalid states. This implementation does not.

---

### Step 2: State Validation Methods

Private helpers were introduced:

- `__is__full`
- `__is__empty`
- `__validate_access__index`
- `__validate_insert_index`

Why separate access and insert validation?

- **Access** requires: `0 <= index < size`
- **Insert** requires: `0 <= index <= size`

These are not the same rule. A traditional array does not differentiate these cases because it does not enforce logical size abstraction.

---

### Step 3: Shifting Mechanisms

Two private methods control structural integrity:

- `__shift__right`
- `__shift_left`

These ensure:

- No gaps inside `[0, size)`
- Elements remain contiguous
- Logical ordering is preserved

In a raw array, shifting is not automatic. Here, it is part of the abstraction.

---

### Step 4: Controlled Insertion

Supported insertion operations:

- `append`
- `insert`
- `insert_at_start`
- `insert_after`
- `insert_before`

These are higher-level behaviors not typically associated with a raw array.

The renaming from simpler names (like `remove_start`) to `remove_at_start` / `remove_at_end` was intentional. The naming now reflects the operation type, position-based removal, and consistency with `remove_at(index)`, improving semantic clarity and matching list-like conventions.

---

### Step 5: Controlled Removal

Removal operations:

- `remove_at_start`
- `remove_at_end`
- `pop(index)`
- `remove_value`

These all:

1. Validate state
2. Shift elements left when necessary
3. Decrease logical size

No `None` values are manually inserted into logical positions because the academic rule requires left shifting and structural compactness. A real dynamic structure might nullify references — this implementation prioritizes academic behavioral correctness.

---

### Step 6: Encapsulation of Search

Two search mechanisms exist:

**Sequential Search**
- `index_of`
- `contains`

**Binary Search**
- `binary_search`
- Requires sorted structure
- Validates sortedness before execution

Unlike a primitive array, this structure enforces safety by checking sorted state before performing binary search.

---

### Step 7: Generic and Comparable Constraint

The structure uses:

```python
T = TypeVar("T", bound=Comparable)
```

This ensures:

- Only comparable types can be stored
- Sorting and binary search are type-safe

A basic array does not enforce comparison constraints at the type level. This is a design improvement over a naive implementation.

---

## 4. Why Method Names Were Changed

The method names were refined for clarity and correctness:

| Old Style | New Style |
|-----------|-----------|
| `remove_start` | `remove_at_start` |
| `remove_end` | `remove_at_end` |
| `remove_at` | `pop(index)` / `remove_value` |

Reasons:

1. To clearly distinguish between position-based and value-based operations.
2. To match common list conventions.
3. To reflect precise behavior.
4. To improve readability and maintainability.
5. To reduce ambiguity in academic evaluation.

For example:
- `remove_value` clearly removes by value.
- `pop(index)` returns the removed value.
- `remove_at_end` explicitly indicates position-based removal.

---

## 5. Behavioral Guarantees

This FixedArrayList guarantees:

- No overflow beyond capacity
- No underflow when empty
- No invalid index access
- No structural gaps
- Logical size always accurate
- Explicit error reporting
- Deterministic shifting behavior

A traditional array does not guarantee these at the abstraction level.

---

## 6. Academic vs Practical Perspective

This implementation prioritizes:

- Structural correctness
- Strict boundary enforcement
- Manual element shifting
- Explicit state validation
- Custom exception semantics

In a production dynamic list, capacity may grow automatically, sorted state might be tracked with a flag, and memory references might be cleared. Those optimizations were intentionally not included to preserve academic structural rules.

---

## 7. Conclusion

**FixedArrayList** is not just an array. It is:

- A controlled abstraction
- A fixed-capacity list implementation
- A structure enforcing academic data structure principles
- A generic, type-safe, comparable-based container

The renaming of methods, separation of validation logic, strict shifting mechanics, and controlled search operations distinguish it clearly from a raw array implementation. This design reflects a deliberate evolution from a basic array-based model into a structured, academically correct fixed list abstraction.