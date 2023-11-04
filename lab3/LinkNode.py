"""
Lab Number: 3
Name: Ethan Ton, Alex Cho
Purpose: Implement a LinkNode class to be used in a Singly Linked List.
"""

class LinkNode:
    def __init__(self,currency,n):
        """
        Initializes a node for a singly linked list.

        Pre: currency (Object): A 'Currency' object to be stored in the node.
             n (LinkNode or None): The next node in the linked list, or None if it's the last node.
        Post: Initializes a node with the provided currency self.data and a reference to the next node, self.next

        Returns: None
        """
        self.data = currency
        self.next = n