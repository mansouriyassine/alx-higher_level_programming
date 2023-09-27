#!/usr/bin/python3

class Node:
    """Define a node of a singly linked list."""
    def __init__(self, data, next_node=None):
        """
        Initialize a new Node instance with data and optional next_node.
        """
        self.data = data
        self.next_node = next_node


class SinglyLinkedList:
    """Define a singly linked list."""
    def __init__(self):
        """Initialize an empty singly linked list."""
        self.head = None

    def __str__(self):
        """Return a string representation of the list."""
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next_node
        return '\n'.join(nodes)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list (increasing order)."""
        new_node = Node(value, None)
        if self.head is None:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node and value >= current.next_node.data:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node


if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.sorted_insert(2)
    sll.sorted_insert(5)
    sll.sorted_insert(3)
    sll.sorted_insert(10)
    sll.sorted_insert(1)
    sll.sorted_insert(-4)
    sll.sorted_insert(-3)
    sll.sorted_insert(4)
    sll.sorted_insert(5)
    sll.sorted_insert(12)
    sll.sorted_insert(3)
    print(sll)
