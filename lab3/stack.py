from SinglyLinkedList import SinglyLinkedList

class Stack(SinglyLinkedList):
    def __init__(self):
        self.linkedList = SinglyLinkedList()
        
    def push(self, currency):
        self.linkedList.addCurrency(currency, 0) # add currency object at index 0, or the top of the stack

    def pop(self):
        if self.linkedList.isListEmpty(): # check if stack is empty
            print("Empty Stack")
            return None
        else:
            popped_currency = self.linkedList.getCurrency(0) # retrieve currency object at the top of the stack
            self.linkedList.removeCurrency(0) # remove it
            return popped_currency

    def peek(self):
        if self.linkedList.isListEmpty(): # check if stack is empty
            print("Stack is empty")
            return None
        else:
            return self.linkedList.getCurrency(0) # return currency object at the top of the stack

    def printStack(self):
        printString = self.linkedList.printList()
        return printString
    
