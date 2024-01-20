from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, value,
                 parent: Optional[TreeNode, None] = None,
                 left: Optional[TreeNode, None] = None,
                 right: Optional[TreeNode, None] = None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def find_value(self, value) -> Optional[TreeNode, None]:
        """
        Find a value in the tree.
        Will go through nodes recursively to find the correct node.
        Either returns the node with the value or None if not found.
        :param value:
        :return:
        """
        if self.value == value:
            return self
        elif value < self.value and self.left:
            return self.left.find_value(value)
        elif value > self.value and self.right:
            return self.right.find_value(value)
        else:
            return None

    def insert_node(self, new_node: TreeNode):
        if new_node.value < self.value:
            if self.left is None:
                new_node.parent = self
                self.left = new_node
            else:
                self.left.insert_node(new_node)
        elif new_node.value > self.value:
            if self.right is None:
                new_node.parent = self
                self.right = new_node
            else:
                self.right.insert_node(new_node)
        else:
            print("Value already in tree!")


class BinarySearchTree:
    def __init__(self, root: Optional[TreeNode, None] = None):
        self.root = root

    def find_tree_node(self, value) -> Optional[TreeNode, None]:
        if self.root:
            return self.root.find_value(value)
        else:
            return None

    def insert_tree_node(self, value):
        """
        Insert a new node into the tree.
        :param value:
        :return:
        """
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
        else:
            self.root.insert_node(new_node)

    def remove_tree_node(self, value):
        """
        Delete a node from the tree.
        :param value:
        :return:
        """
        node_to_delete = self.find_tree_node(value)
        if node_to_delete is None:
            print("Node not found!")
            return
        else:
            # Case 1: Node has no children
            if node_to_delete.left is None and node_to_delete.right is None:
                if node_to_delete.parent.left == node_to_delete:
                    node_to_delete.parent.left = None
                else:
                    node_to_delete.parent.right = None
                del node_to_delete
                return
            # Case 2: Node has one child
            elif node_to_delete.left is None or node_to_delete.right is None:
                if node_to_delete.left:
                    child = node_to_delete.left
                else:
                    child = node_to_delete.right
                if node_to_delete.parent.left == node_to_delete:
                    node_to_delete.parent.left = child
                else:
                    node_to_delete.parent.right = child
                del node_to_delete
                return
            # Case 3: Node has two children
            else:
                # Find the smallest node in the right subtree
                smallest_node = node_to_delete.right
                while smallest_node.left:
                    smallest_node = smallest_node.left
                # Copy the smallest node's value into the node to delete
                node_to_delete.value = smallest_node.value
                # Delete the smallest node
                if smallest_node.parent.left == smallest_node:
                    smallest_node.parent.left = None
                else:
                    smallest_node.parent.right = None
                del smallest_node
                return