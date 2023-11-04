from SinglyLinkedList import SinglyLinkedList

class Queue(SinglyLinkedList):
    def __init__(self):
        """
        Initializes a queue using a singly linked list.

        Pre: None
        Post: Initializes a queue with singly linked list.

        Returns: None
        """
        self.linkedList = SinglyLinkedList()

    def enqueue(self, currency):
        """
        Adds a currency object to the end of the queue.

        Pre: currency (Object): A 'Currency' object to be added to the queue.
        Post: Adds the currency object to the end of the queue.

        Returns: None
        """
        self.linkedList.addCurrency(currency, self.linkedList.countCurrency())  # Add currency object to the end of the queue

    def dequeue(self):
        """
        Removes and returns the currency object at the front of the queue.

        Pre: None
        Post: Removes and returns the currency object at the front of the queue.
              Returns None and prints a message if the queue is empty.

        Returns: 'Currency' object or None if queue is empty.
        """
        if self.linkedList.isListEmpty():  # Check if queue is empty
            print("Empty Queue")
            return None
        else:
            front_currency = self.linkedList.getCurrency(0)  # Retrieve currency object at the front of the queue
            self.linkedList.removeCurrency(0)  # Remove it
            return front_currency

    def peekFront(self):
        """
        Returns the currency object at the front of the queue without removing it.

        Pre: None
        Post: Returns the currency object at the front of the queue without removing it.
              Returns None and prints a message if the queue is empty.

        Returns: 'Currency' object or None if queue is empty.
        """
        if self.linkedList.isListEmpty():  # Check if queue is empty
            print("Queue is empty")
            return None
        else:
            return self.linkedList.getCurrency(0)  # Return currency object at the front of the queue

    def peekRear(self):
        """
        Returns the currency object at the end of the queue without removing it.

        Pre: None
        Post: Returns the currency object at the end of the queue without removing it.
              Returns None and prints a message if the queue is empty.

        Returns: 'Currency' object or None if queue is empty.
        """
        if self.linkedList.isListEmpty():  # Check if queue is empty
            print("Queue is empty")
            return None
        else:
            return self.linkedList.getCurrency(self.linkedList.countCurrency() - 1)  # Return currency object at the end of the queue

    def printQueue(self):
        """
        Prints the list of currencies in the queue.

        Pre: None
        Post: Constructs a formatted string containing currency values and names in the queue.

        Returns: str
        """
        return self.linkedList.printList()
