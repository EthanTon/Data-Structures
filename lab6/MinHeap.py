"""
Lab Number: 6
Name: Ethan Ton
Purpose: Implement a minHeap to store data, perform search, insert and delete nodes, perform BFS/DFS traversals.
"""
from BST import BST
from BSTNode import BSTNode
from Queue import Queue
from dollar import Dollar

class MinHeap(BST):
    def __init__(self, root=None):
        """
        Initializes a heap with an optional root node using BST.

        Pre: root (BSTNode): The root node of the heap. Default is None.

        Post: Initializes a heap with an optional root node.

        Returns: None
        """
        super().__init__(root)
    def search(self, key) -> bool:
        """
        Searches for a key in the heap.

        Pre: key (Object): The key to search for in the heap.

        Post: Returns True if the key is found in the heap, otherwise False.

        Returns: bool
        """
        if self.root is not None:
            result = self.breadthFirstTraversal(None)

            j = self.count()

            for i in range(j):
                if result.dequeue().isEqual(key):
                    return True
        return False

    def insert(self,node):
        """
        Inserts a node into the heap.

        Pre: node (BSTNode): The node to be inserted into the heap.

        Post: Inserts a node into the heap.

        Returns: 0 if empty
        """
        #Empty case
        if self.isEmpty():
            self.root = node
            return 0
        root = self.root
        if self.search(node.data) is False:
            if node.data.isGreater(root.data):
                if root.left is None:
                    root.left = node
                elif root.right is None:
                    root.right = node
                elif root.left is not None and root.right is not None:
                    leftCount = self.count(root.left,self.root)
                    rightCount = self.count(root.right,self.root)
    
                    if leftCount > (rightCount+1):
                        self.root = root.right
                    else: 
                        self.root = root.left
                    self.insert(node)
                self.root = root
            else:
                temp = root.data
                self.root.data = node.data
                node.data = temp
                root.data=self.root.data
                self.insert(node)
        else: raise ValueError("Value found for node")
    
    def remove(self, node):
        """
        Removes a parent node from a heap.

        Pre: key (Object): The key of the node to be removed.

        Post: Removes a parent node with the specific key from the Heap.

        Returns: Node if failed
        """
        if self.isEmpty(): return node
        if self.search(node.data) is False: return node
        root = self.root
        if node.data.isEqual(self.root.data):
            removed = self.root
            current = self.root
            parent = current
            if self.root.right is None: next = self.root.left
            else: next = self.root.right
            while next is not None:
                if current.right is None and current.left is not None:
                    parent = current
                    current = current.left
                    break
                else:
                    parent = current
                    current = current.right
                    if current.right is None: next = current.left
                    else: next = current.right
            self.root.data = current.data
            if parent.right is not None and parent.right.data.isEqual(current.data):
                parent.right = None
            else:
                parent.left = None
        else:
            self.root = self.root.left
            self.remove(node)
            self.root = root
            self.root = self.root.right
            self.remove(node)
            self.root = root
        
        while True:
            if self.root.left is not None and self.root.right is not None:
                if self.root.data.isGreater(self.root.left.data):
                    temp = self.root.data
                    self.root.data = self.root.left.data
                    self.root.left.data = temp
                    self.root = self.root.left
                if self.root.data.isGreater(self.root.right.data):
                    temp = self.root.data
                    self.root.data = self.root.right.data
                    self.root.right.data = temp
                    self.root = self.root.right
                else:
                    break
            else:
                break
        self.root = root