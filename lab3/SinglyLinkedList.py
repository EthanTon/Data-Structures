from LinkNode import LinkNode
from dollar import Dollar
from currency import Currency


class SinglyLinkedList:
    def __init__(self):
        """
        Initializes a singly linked list.

        Pre: None
        Post: Initializes an empty singly linked list with count set to 0.
              The start and end nodes are created with 'LinkNode' objects.

        Returns: None
        """
        self.count = 0
        self.start = LinkNode(None, None)
        self.end = LinkNode(None, None)

    def createList(self):
        """
        Creates an empty linked list.

        Pre: None
        Post: Creates an empty linked list with count set to 0.
              The start and end nodes are initialized with 'LinkNode' objects.

        Returns: None
        """
        pass

    def destroyList(self):
        """
        Destroys the linked list.

        Pre: None
        Post: Clears the linked list, setting count to 0 and start/end nodes to None.

        Returns: None
        """
        pass

    def addCurrency(self, currency, index):
        """
        Adds a currency node to the linked list at a specified index.

        Pre: currency (Object): A 'Currency' object to be added to the linked list.
             index (int): The index where the currency node will be added.
        Post: Adds the currency node to the linked list at the specified index.
              Updates 'self.count' and adjusts start and end nodes if necessary.

        Returns: None
        """
        new_node = LinkNode(currency, None)  # Create a new node with the given currency

        try:
            if self.isListEmpty():  # If the list is empty, set both start and end to the new node
                self.start = new_node
                self.end = new_node
            elif index == 0:  # If index is 0, update the start
                new_node.next = self.start
                self.start = new_node
            else:
                prev_node = self.getNode(index - 1)  # Get the previous node
                if prev_node:
                    new_node.next = prev_node.next
                    prev_node.next = new_node
                if new_node.next is None:
                    self.end = new_node
            self.count += 1
        except:
            pass

    def removeCurrency(self, arg=None):
        """
        Removes a currency node from the linked list.

        Pre: arg (Object or int): Either a 'Currency' object to be removed or the index of the node to be removed.
        Post: Removes the currency node from the linked list based on the provided argument.
              Updates 'self.count' and adjusts start and end nodes if necessary.

        Returns: None
        """
        if isinstance(arg, Currency):
            # Remove currency by object
            index = self.findCurrency(arg)
        elif isinstance(arg, int):
            # Remove currency by index
            index = arg

        if not self.isListEmpty() and 0 <= index < self.count:
            revNode = self.getNode(index)
            sucNode = revNode.next

            if revNode == self.start:
                self.start = sucNode

            if index > 0:
                prevNode = self.getNode(index - 1)
                prevNode.next = sucNode

                if revNode == self.end:
                    self.end = prevNode

            self.count -= 1

    def findCurrency(self, currency):
        """
        Finds the index of a specific currency in the linked list.

        Pre: currency (Object): A 'Currency' object to be searched for in the linked list.
        Post: If the linked list is not empty, it returns the index of the currency node if found, otherwise returns -1.

        Returns: int
        """
        indexOfCurrency = -1
        if self.isListEmpty() is False:
            for i in range(self.count):
                if self.getCurrency(i).isEqual(currency):
                    indexOfCurrency = i
                    break
        return indexOfCurrency

    def getNode(self, index):
        """
        Retrieves the node at a specified index.

        Pre: index (int): The index of the node to retrieve.
        Post: Returns the node at the specified index.

        Returns: 'LinkNode' object at the specified index or -1 if index is out of bounds.
        """
        currencyAtIndex = self.start
        try:
            if index > 0 or index < self.count:
                for i in range(index):
                    currencyAtIndex = currencyAtIndex.next

        except:
            return -1
        return currencyAtIndex

    def getCurrency(self, index):
        """
        Retrieves the currency object at a specified index.

        Pre: index (int): The index of the currency to retrieve.
        Post: Returns the 'Currency' object at the specified index.

        Returns: 'Currency' object or None if index is out of bounds.
        """
        try:
            currency = self.getNode(index).data
        except:
            return None
        return currency

    def printList(self):
        """
        Prints the list of currencies in a formatted string.

        Pre: None
        Post: Creates a formatted string containing currency values and names.

        Returns: str: printString
        """
        try:
            printString = ""
            for i in range(self.count):
                formatted_value = "%.2f" % (self.getCurrency(i).noteValue + (self.getCurrency(i).coinValue / 100))
                currency_name = self.getCurrency(i).getName()
                printString += (formatted_value + " " + currency_name + "\t")
        except:
            printString = "Error"

        return printString

    def isListEmpty(self):
        """
        Checks if the linked list is empty.

        Pre: None
        Post: Returns True if the linked list is empty, otherwise False.

        Returns: bool
        """
        if self.count == 0:
            return True
        else:
            return False

    def countCurrency(self):
        """
        Returns the count of currencies in the linked list.

        Pre: None
        Post: Returns the current count of currencies in the linked list.

        Returns: int
        """
        return self.count