from singlyLinkedList import SinglyLinkedList

class Stack(SinglyLinkedList):
    def __init__(self):
        super().__init__()
        
    def createStack(self):
        pass

    def push(self, currency):
        self.addCurrency(currency, 0) # add currency object at index 0, or the top of the stack

    def pop(self):
        if self.isListEmpty(): # check if stack is empty
            print("Empty Stack")
            return None
        else:
            popped_currency = self.getCurrency(0) # retrieve currency object at the top of the stack
            self.removeCurrency(0) # remove it
            return popped_currency

    def peek(self):
        if self.isListEmpty(): # check if stack is empty
            print("Stack is empty")
            return None
        else:
            return self.getCurrency(0) # return currency object at the top of the stack

    def printStack(self):
        printString = ""
        for i in range(self.count - 1, -1, -1): # iterate over stack indices in reverse order (top to bottom)
            formatted_value = "%.2f" % (self.getCurrency(i).getNoteValue() + (self.getCurrency(i).getCoinValue() / 100))
            currency_name = self.getCurrency(i).getName()
            printString += (formatted_value + " " + currency_name + "\t")
        return printString
    
    def destroyStack(self):
        pass
