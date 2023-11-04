from SinglyLinkedList import SinglyLinkedList
    
class Stack(SinglyLinkedList):
    def __init__(self):
        """
        Initializes a stack using a singly linked list.

        Pre: None
        Post: Initializes a stack with singly linked list.

        Returns: None
        """
        self.linkedList = SinglyLinkedList()

    def push(self, currency):
        """
        Adds a currency object to the top of the stack.

        Pre: currency (Object): A 'Currency' object to be added to the stack.
        Post: Adds the currency object to the top of the stack.

        Returns: None
        """
        self.linkedList.addCurrency(currency, 0)  # add currency object at index 0, or the top of the stack

    def pop(self):
        """
        Removes and returns the currency object at the top of the stack.

        Pre: None
        Post: Removes and returns the currency object at the top of the stack.
              Returns None and prints a message if the stack is empty.

        Returns: 'Currency' object or None if stack is empty.
        """
        if self.linkedList.isListEmpty(): # check if stack is empty
            print("Empty Stack")
            return None
        else:
            popped_currency = self.linkedList.getCurrency(0) # retrieve currency object at the top of the stack
            self.linkedList.removeCurrency(0) # remove it
            return popped_currency

    def peek(self):
        """
        Returns the currency object at the top of the stack without removing it.

        Pre: None
        Post: Returns the currency object at the top of the stack without removing it.
              Returns None and prints a message if the stack is empty.

        Returns: 'Currency' object or None if stack is empty.
        """
        if self.linkedList.isListEmpty(): # check if stack is empty
            print("Stack is empty")
            return None
        else:
            return self.linkedList.getCurrency(0) # return currency object at the top of the stack

    def printStack(self):
        """
        Prints the list of currencies in the stack.

        Pre: None
        Post: Constructs a formatted string containing currency values and names in the stack.

        Returns: str -> printString
        """
        printString = self.linkedList.printList()
        return printString