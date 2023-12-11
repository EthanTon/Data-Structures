
"""
Lab Number: 4
Name: Ethan Ton, Alex Cho
Purpose: Implement a Binary Search Tree (BST) to store data, perform search, insert and delete nodes, perform BFS/DFS traversals.
"""

from BSTNode import BSTNode
from dollar import Dollar
from Queue import Queue

class BST():

    def __init__(self, root=None):
        """
        Initializes a Binary Search Tree (BST) with an optional root node.

        Pre: root (BSTNode): The root node of the BST. Default is None.

        Post: Initializes a BST with an optional root node.

        Returns: None
        """
        self.root = root

    def search(self,key) -> bool:
        """
        Searches for a key in the BST.

        Pre: key (Object): The key to search for in the BST.

        Post: Returns True if the key is found in the BST, otherwise False.

        Returns: bool
        """
        currNode = self.root

        while currNode is not None:
            if currNode.data.isEqual(key): return True
            elif currNode.data.isGreater(key): currNode = currNode.left
            else: currNode = currNode.right
        return False    
    
    def insert(self, node):
        """
        Inserts a node into the BST.

        Pre: node (BSTNode): The node to be inserted into the BST.

        Post: Inserts a node into the BST.

        Returns: None
        """
        if node is None: pass
        elif self.search(node.data) is False:
            root = self.root
            if self.isEmpty():
                root = node
            elif(node.data.isGreater(self.root.data)):
                if(self.root.right is None):
                    self.root.right = node
                else: 
                    self.root = self.root.right
                    self.insert(node)
            else:
                if(self.root.left is None):
                    self.root.left = node
                else: 
                    self.root = self.root.left
                    self.insert(node)
            self.root = root
        else: raise ValueError("Value found for node")

    def remove(self, key):
        """
        Removes a node with a specific key from the BST.

        Pre: key (Object): The key of the node to be removed.

        Post: Removes a node with the specific key from the BST.

        Returns: None
        """
        self._remove(key, self.root)

    def _remove(self, key, root=None):

        if root is None:
            return

        parent = None
        current = root

        while current is not None:
            if key.isEqual(current.data):
                break
            parent = current
            if key.isGreater(current.data) is False:
                current = current.left
            else:
                current = current.right

        if current is None:
            raise ValueError("Not Found")  # Key not found
        # Node with one child or no child
        if current.left is None:
            if parent is None:
                self.root = current.right
            elif key.isGreater(parent.data) is False:
                parent.left = current.right
            else:
                parent.right = current.right
        elif current.right is None:
            if parent is None:
                self.root = current.left
            elif key.isGreater(parent.data) is False:
                parent.left = current.left
            else:
                parent.right = current.left
        else:
            # Node with two children
            successorParent = current
            successor = current.right

            while successor.left is not None:
                successorParent = successor
                successor = successor.left

            current.data = successor.data

            if successorParent.left == successor:
                successorParent.left = successor.right
            else:
                successorParent.right = successor.right

    def count(self,root=None,head=None):
        """
        Counts the number of nodes in the BST.

        Pre: root (BSTNode): The root node of the subtree to count. Default is None.
             head (BSTNode): The head/root of the entire BST. Default is None.

        Post: Counts the number of nodes in the BST.

        Returns: int
        """
        if head is None:
            return self.count(self.root,self.root)
        if root is None:
            return 0
        else: return 1+self.count(root.left,self.root)+self.count(root.right,self.root)

    def getRoot(self):
        """
        Retrieves the root node of the BST.

        Pre: None

        Post: Returns the root node of the BST.

        Returns: BSTNode
        """
        return self.root

    def isEmpty(self):
        """
        Checks if the BST is empty.

        Pre: None

        Post: Returns True if the BST is empty, otherwise False.

        Returns: bool
        """
        if  self.root is None:
            return True
        else: return False
    
    def inorderTraversal(self, root):
        """
        Performs an inorder traversal of the BST.

        Pre: root (BSTNode): The root node of the BST.

        Post: Returns a queue containing data of nodes in inorder traversal sequence.

        Returns: Queue
        """
        result = Queue()
        if root:
            result = self.inorderTraversal(root.left) #recursively traverse the left subtree
            result.enqueue(root.data) #enqueue the current node's data
            right = self.inorderTraversal(root.right) #recursively traverse the right subtree
            j = self.count(root.right,self.root) #get the count of the nodes in the right subtree
            for i in range(j): #iterate through the right subtree nodes
                result.enqueue(right.dequeue()) #enqueue
        return result
    
    def preorderTraversal(self, root):
        """
        Performs a preorder traversal of the BST.

        Pre: root (BSTNode): The root node of the BST.

        Post: Returns a queue containing data of nodes in preorder traversal sequence.

        Returns: Queue
        """
        result = Queue()
        if root:
            result.enqueue(root.data)
            left = self.inorderTraversal(root.left)
            j = self.count(root.left,self.root)
            for i in range(j):
                result.enqueue(left.dequeue())
            right = self.inorderTraversal(root.right)
            j = self.count(root.right,self.root)
            for i in range(j):
                result.enqueue(right.dequeue())
        return result

    def postorderTraversal(self, root):
        """
        Performs a postorder traversal of the BST.

        Pre: root (BSTNode): The root node of the BST.

        Post: Returns a queue containing data of nodes in postorder traversal sequence.

        Returns: Queue
        """
        result = Queue()
        if root:
            left = self.inorderTraversal(root.left)
            j = self.count(root.left,self.root)
            for i in range(j):
                result.enqueue(left.dequeue())
            right = self.inorderTraversal(root.right)
            j = self.count(root.right,self.root)
            for i in range(j):
                result.enqueue(right.dequeue())
            result.enqueue(root.data)
        return result
    
    def breadthFirstTraversal(self, root):
        """
        Performs a breadth-first traversal of the BST.

        Pre: root (BSTNode): The root node of the BST.

        Post: Returns a queue containing data of nodes in breadth-first traversal sequence.

        Returns: Queue
        """
        result = Queue()
        if self.isEmpty(): #check if the BST is empty
            return result #return an empty list

        queue = Queue() #create a queue
        queue.enqueue(self.root) #enqueue the root node of the BST

        j = self.count()
        for i in range(j): #loop until the queue is empty
            node = queue.dequeue() #dequeue the node
            result.enqueue(node.data) #add that node's data to the result list

            if node.left is not None: #enqueue the left child if it exists
                queue.enqueue(node.left)
            if node.right is not None: #enqueue the right child if it exists
                queue.enqueue(node.right)

        return result
    
    def print(self) -> str:
        """
        Prints the BST data in different traversal orders.

        Pre: None

        Post: Returns a string containing BST data in different traversal orders.

        Returns: str
        """
        return self.breadthFirstTraversal(self.root).printQueue() + "\n" + self.inorderTraversal(self.root).printQueue() + "\n" + self.preorderTraversal(self.root).printQueue() + "\n" + self.postorderTraversal(self.root).printQueue() + "\n"

    def empty(self):
        """
        Empties the BST.

        Pre: None

        Post: Sets the root node of the BST to None.

        Returns: None
        """
        self.root = None