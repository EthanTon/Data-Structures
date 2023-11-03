from SinglyLinkedList import SinglyLinkedList

class Queue(SinglyLinkedList):
    def __init__(self):
        self.linkedList = SinglyLinkedList()

    def enqueue(self, currency):
        self.linkedList.addCurrency(currency, self.linkedList.countCurrency())  # Add currency object to the end of the queue

    def dequeue(self):
        if self.linkedList.isListEmpty():  # Check if queue is empty
            print("Empty Queue")
            return None
        else:
            front_currency = self.linkedList.getCurrency(0)  # Retrieve currency object at the front of the queue
            self.linkedList.removeCurrency(0)  # Remove it
            return front_currency

    def peekFront(self):
        if self.linkedList.isListEmpty():  # Check if queue is empty
            print("Queue is empty")
            return None
        else:
            return self.linkedList.getCurrency(0)  # Return currency object at the front of the queue

    def peekRear(self):
        if self.linkedList.isListEmpty():  # Check if queue is empty
            print("Queue is empty")
            return None
        else:
            return self.linkedList.getCurrency(self.linkedList.countCurrency() - 1)  # Return currency object at the end of the queue

    def printQueue(self):
        return self.linkedList.printList()
