from linkNode import LinkNode
from dollar import Dollar
from currency import Currency

class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.start = LinkNode(None,None)
        self.end = LinkNode(None,None)

    def createList(self): pass
    def destroyList(self): pass

    def addCurrency(self, currency, index):
        new_node = LinkNode(currency, None)  # Create a new node with the given currency

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

    def removeCurrency(self, arg=None):
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

    def findCurrency(self,currency):
        indexOfCurrency = -1
        if self.isListEmpty() is False:
            for i in range(self.count):
                if self.getCurrency(i).isEqual(currency):
                    indexOfCurrency = i
                    break
        return indexOfCurrency
    

    def getNode(self,index):
        currencyAtIndex = self.start
        if index > 0 or index < self.count:
            for i in range(index):
                currencyAtIndex = currencyAtIndex.next
        
        return currencyAtIndex
    
    def getCurrency(self,index):
        return self.getNode(index).data

    def printList(self):
        printString = ""
        for i in range(self.count):
            formatted_value = "%.2f" % (self.getCurrency(i).noteValue + (self.getCurrency(i).coinValue / 100))
            currency_name = self.getCurrency(i).getName()
            printString += (str(i) + "\t" + formatted_value + " " + currency_name + "\n")
        return printString
    
    def isListEmpty(self): 
        if self.count == 0: 
            return True
        else:  
            return False
    def countCurrency(self): 
        return self.count


