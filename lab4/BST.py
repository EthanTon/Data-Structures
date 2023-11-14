from BSTNode import BSTNode
from dollar import Dollar
from Queue import Queue
from SinglyLinkedList import SinglyLinkedList

class BST():

    def __init__(self, root=None):
        self.root = root

    def search(self, node) -> bool:
        currNode = self.root

        while currNode is not None:
            if currNode.data.isEqual(node.data): return True
            elif currNode.data.isGreater(node.data): currNode = currNode.left
            else: currNode = currNode.right
        return False
        

    def insert(self, node):
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


    def count(self):
        count = 0
        queue = Queue()
        queue.enqueue(self.root)

        while queue.peekFront is not None:
            node = queue.peekFront()
            queue.dequeue()
            while node is not None:
                count += 1
                queue.enqueue(node.left)
                queue.enqueue(node.right)
        return count

    def getRoot(self):
        return self.root

    def isEmpty(self):
        if  self.root is None:
            return True
        else: return False

    def empty(self):
        self.root = None

# Test the BST
def test_bst():
    bst = BST()

    # Create nodes
    node1 = BSTNode(5)
    node2 = BSTNode(3)
    node3 = BSTNode(7)
    node4 = BSTNode(12)

    # Insert nodes into the BST
    bst.insert(node1)
    bst.insert(node2)
    bst.insert(node3)
    bst.insert(node4)

    # Search for existing and non-existing nodes
    assert bst.search(node1) == True
    assert bst.search(node4) == True
    assert bst.search(BSTNode(10)) == False

    print(bst.count())

    print("BST test passed!")

# Run the test function
test_bst()