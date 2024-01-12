"""Binary Tree sort function."""

import time
import sys


sort_name = "BINARY TREE SORT"
# sys.setrecursionlimit(2000)


def sort_list(list_to_sort, display_update):
    """Sort list using Binary Tree Sort.

    Args:
        list_to_sort (list of numbers): The list to sort
            will not be modified during the sort
        display_update (function): Call this to update the display

    Returns:
        process time elapsed
        sorted list
    """
    start_time = time.process_time()

    # Create the binary tree from all the values in the list
    btree_root = BNode(list_to_sort[0])
    for x in list_to_sort[1:]:
        btree_root.search_and_add(x)

    # Traverse the binary tree to collect all the values sorted in order
    result = []
    btree_root.traverse(result)

    elapsed_time = time.process_time() - start_time

    return elapsed_time, result


class BNode:
    """A binary search tree node."""

    def __init__(self, val):
        """Initialize the node with a value."""
        self.val = val
        self.left = None
        self.right = None

    def insert_left(self, val):
        """Insert a new node to the immediate left of this one."""
        self.left = BNode(val)

    def insert_right(self, val):
        """Insert a new node to the immediate right of this one."""
        self.right = BNode(val)

    def search_and_add(self, val):
        """Insert a new value somewhere below this node."""
        if val <= self.val:
            if self.left is None:
                self.insert_left(val)
            else:
                self.left.search_and_add(val)
        else:
            if self.right is None:
                self.insert_right(val)
            else:
                self.right.search_and_add(val)

    def traverse(self, result):
        """Append this node and its children to the result list."""
        """ INFIX order - first the children on the left, then this node, then
            the children on the right
        """
        if self.left is not None:
            self.left.traverse(result)
        result.append(self.val)
        if self.right is not None:
            self.right.traverse(result)
