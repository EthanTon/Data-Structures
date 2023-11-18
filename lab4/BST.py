from BSTNode import BSTNode
from dollar import Dollar
from Queue import Queue
from SinglyLinkedList import SinglyLinkedList
import os
import contextlib

class BST():

    def __init__(self, root=None):
        self.root = root

    def search(self,key) -> bool:
        currNode = self.root

        while currNode is not None:
            if currNode.data.isEqual(key): return True
            elif currNode.data.isGreater(key): currNode = currNode.left
            else: currNode = currNode.right
        return False    
    
    def insert(self, node):
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
            return  # Key not found
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
        if head is None:
            return self.count(self.root,self.root)
        if root is None:
            return 0
        else: return 1+self.count(root.left,self.root)+self.count(root.right,self.root)

    def getRoot(self):
        return self.root

    def isEmpty(self):
        if  self.root is None:
            return True
        else: return False
    
    def inorderTraversal(self, root):
        result = Queue()
        if root:
            result = self.inorderTraversal(root.left)
            result.enqueue(root.data)
            right = self.inorderTraversal(root.right)
            j = self.count(root.right,self.root)
            for i in range(j):
                result.enqueue(right.dequeue())
        return result
    
    def preorderTraversal(self, root):
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
        return self.breadthFirstTraversal(self.root).printQueue() + "\n" + self.inorderTraversal(self.root).printQueue() + "\n" + self.preorderTraversal(self.root).printQueue() + "\n" + self.postorderTraversal(self.root).printQueue() + "\n"

    def empty(self):
        self.root = None

