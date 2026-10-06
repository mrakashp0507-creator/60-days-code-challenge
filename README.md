# Day 24 - Merging Systems

## Merge Two Sorted Linked Lists

## Problem

Two kingdoms maintain their soldier records as sorted linked lists.

The goal is to merge both lists into one sorted master list without losing
the existing order.

Duplicate values must also be preserved.

---

## Example

### Kingdom 1

    10 -> 20 -> 30 -> 40

### Kingdom 2

    15 -> 20 -> 25 -> 35 -> 40

### Merged Result

    10 -> 15 -> 20 -> 20 -> 25 -> 30 -> 35 -> 40 -> 40

---

## Merge Strategy

The algorithm uses two pointers.

- Pointer 1 points to the current node in List 1.
- Pointer 2 points to the current node in List 2.
- Compare both values.
- Attach the smaller value to the result.
- Move that pointer forward.
- Continue until one list is exhausted.
- Attach the remaining nodes from the other list.

---

## Duplicate Values

Duplicates are preserved.

For example:

    List 1: 20
    List 2: 20

Result:

    20 -> 20

No values are removed.

---

## Dummy Node

A temporary dummy node is used to make the merge logic easier.

The actual merged list starts from:

    dummy.next

The dummy node itself is not part of the result.

---

## Complexity

If List 1 contains n nodes and List 2 contains m nodes:

Time Complexity:

    O(n + m)

Extra Space:

    O(1)

The existing linked-list nodes are reused.

---

## Real-World Applications

Merge operations are useful in:

- Databases
- Distributed systems
- Search engines
- Data processing
- File systems
- External sorting systems

---

## How to Run

Open the VS Code terminal and run:

    python day24_merge_linked_lists.py

---

## Learning Outcomes

- Created sorted linked lists.
- Used multiple pointers.
- Merged two sorted lists.
- Preserved duplicate values.
- Reused existing nodes.
- Understood O(n + m) merging.
