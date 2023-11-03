from SinglyLinkedList import SinglyLinkedList

class Stack(SinglyLinkedList):
    def __init__(self):
        self.linkedLink = SinglyLinkedList()
        
    def push(self, currency):
        self.linkedLink.addCurrency(currency, 0) # add currency object at index 0, or the top of the stack

    def pop(self):
        if self.linkedLink.isListEmpty(): # check if stack is empty
            print("Empty Stack")
            return None
        else:
            popped_currency = self.linkedLink.getCurrency(0) # retrieve currency object at the top of the stack
            self.linkedLink.removeCurrency(0) # remove it
            return popped_currency

    def peek(self):
        if self.linkedLink.isListEmpty(): # check if stack is empty
            print("Stack is empty")
            return None
        else:
            return self.linkedLink.getCurrency(0) # return currency object at the top of the stack

    def printStack(self):
        printString = ""
        for i in range(self.linkedLink.count - 1, -1, -1): # iterate over stack indices in reverse order (top to bottom)
            formatted_value = "%.2f" % (self.linkedLink.getCurrency(i).getNoteValue() + (self.linkedLink.getCurrency(i).getCoinValue() / 100))
            currency_name = self.linkedLink.getCurrency(i).getName()
            printString += (formatted_value + " " + currency_name + "\t")
        return printString
    
