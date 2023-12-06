"""
Lab Number: 4
Name: Ethan Ton, Alex Cho
Purpose: Implement a Binary Search Tree (BST) node to store data.
"""

from dollar import Dollar

class BSTNode:
    def __init__(self, data, left=None, right=None):
        """
        Initializes a node for a Binary Search Tree (BST).

        Pre: data (Object): Data to be stored in the node.
             left (BSTNode or None): The left child node, or None if there's no left child.
             right (BSTNode or None): The right child node, or None if there's no right child.
        Post: Initializes a node with the provided data self.data, 
              a reference to the left child node self.left, and a reference to the right child node self.right.

        Returns: None
        """
        self.data = data
        self.left = left
        self.right = right
