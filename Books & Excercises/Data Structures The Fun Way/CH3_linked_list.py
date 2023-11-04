from __future__ import annotations
import random


class LinkedListNode:
    """ A single node from a Linked List """

    # This forward declaration only works from Python 3.7 forward
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.previous = None


class LinkedList:
    """ A custom implementation of Linked Lists """

    def __init__(self, first_value=None):
        self.head = LinkedListNode(first_value)
        self.current = self.head
        self.length = 1

    def linked_list_lookup_by_index(self, element_index: int):
        count = 0
        self.current = self.head
        # We haven't arrived at index AND current is not None
        while count < element_index and self.current:
            self.current = self.current.next
            count += 1
        return self.current

    def insert_after_by_index(self, inserted_node: LinkedListNode, index: int):
        # We find the existing node by index, then use that node to insert
        index_node = self.linked_list_lookup_by_index(index)
        self.insert_after_by_node(inserted_node, index_node)

    def insert_after_by_node(self, inserted_node: LinkedListNode, index_node: LinkedListNode):
        left_node = index_node
        right_node = left_node.next

        # Set two-way links on new node
        inserted_node.previous = left_node
        inserted_node.next = right_node

        # Edit links on outer nodes
        left_node.next = inserted_node
        if right_node:  # Only do this isn't already the last node
            right_node.previous = inserted_node
        self.length += 1

    def delete_node_by_index(self, index):
        self.delete_node(self.linked_list_lookup_by_index(index))

    def delete_node(self, node: LinkedListNode):
        # Make new head if it's the first node in Linked List
        if not node.previous:
            self.head = node.next
            # Delete previous from new HEAD
            self.head.previous = None

        else:
            # Link previous node to node after deleted node
            node.previous.next = node.next

        # Don't try to change TAIL if we are deleting tail
        if node.next:
            node.next.previous = node.previous
        self.length -= 1


if __name__ == '__main__':
    # Test node insertion
    linked_list = LinkedList('HEAD')
    middle_node = LinkedListNode('MID')
    last_node = LinkedListNode('TAIL')

    linked_list.insert_after_by_index(last_node, 0)
    linked_list.insert_after_by_index(middle_node, 0)

    current = linked_list.head
    print("Following the links of the list")
    while current:
        print(current.value)
        current = current.next

    # Insert some more links
    for value in range(25):
        node = LinkedListNode(value)
        linked_list.insert_after_by_index(node, random.choice(range(linked_list.length)))

    # Print them out
    current = linked_list.head
    print("\nFollowing the links of the longer list")
    while current:
        print(current.value)
        current = current.next

    # Check if first node is still HEAD
    print(f"\nFirst node should have value HEAD. "
          f": {linked_list.linked_list_lookup_by_index(0).value}")

    # Delete first and last node
    print(f"First node value: {linked_list.linked_list_lookup_by_index(0).value}")
    linked_list.delete_node_by_index(0)
    print(f"First node value after delete: {linked_list.linked_list_lookup_by_index(0).value}\n")

    last_index = linked_list.length - 1
    print(f"Linked List Length: {last_index}")
    print(f"Last node value: {linked_list.linked_list_lookup_by_index(last_index).value}")
    linked_list.delete_node_by_index(last_index)
    last_index = linked_list.length - 1
    print(
        f"Last node value after delete: {linked_list.linked_list_lookup_by_index(last_index).value}\n")
