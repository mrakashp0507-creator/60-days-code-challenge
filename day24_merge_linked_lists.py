# Day 24 - Merging Systems
# Merge Two Sorted Linked Lists

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end="")

            if current.next is not None:
                print(" -> ", end="")

            current = current.next

        print(" -> None")


def merge_sorted_lists(list1, list2):
    # Dummy node helps simplify the merging process
    dummy = Node(0)
    current = dummy

    pointer1 = list1.head
    pointer2 = list2.head

    while pointer1 is not None and pointer2 is not None:

        if pointer1.data <= pointer2.data:
            current.next = pointer1
            pointer1 = pointer1.next

        else:
            current.next = pointer2
            pointer2 = pointer2.next

        current = current.next

    # Attach remaining nodes
    if pointer1 is not None:
        current.next = pointer1

    if pointer2 is not None:
        current.next = pointer2

    # Return actual head, skipping dummy node
    return dummy.next


print("======================================")
print("       MERGING SYSTEMS")
print("======================================")

# Create first kingdom's sorted army
kingdom1 = LinkedList()

for soldier in [10, 20, 30, 40]:
    kingdom1.append(soldier)

# Create second kingdom's sorted army
kingdom2 = LinkedList()

for soldier in [15, 20, 25, 35, 40]:
    kingdom2.append(soldier)

print("\nKingdom 1:")
kingdom1.display()

print("\nKingdom 2:")
kingdom2.display()

# Merge both lists
merged_head = merge_sorted_lists(kingdom1, kingdom2)

print("\nMerged Master List:")

current = merged_head

while current is not None:
    print(current.data, end="")

    if current.next is not None:
        print(" -> ", end="")

    current = current.next

print(" -> None")

print("\nMerge completed successfully!")