from SinglyLinkedList import SinglyLinkedList

class Queue(SinglyLinkedList):
    def __init__(self):
        self.linkedLink = SinglyLinkedList()

    def enqueue(self, currency):
        if self.linkedLink.isListEmpty():
            self.linkedLink.addCurrency(currency, self.linkedLink.count)  # Add currency object to the end of the queue
        else: 
            self.linkedLink.addCurrency(currency, self.linkedLink.count-1)

    def dequeue(self):
        if self.linkedLink.isListEmpty():  # Check if queue is empty
            print("Empty Queue")
            return None
        else:
            front_currency = self.linkedLink.getCurrency(0)  # Retrieve currency object at the front of the queue
            self.linkedLink.removeCurrency(0)  # Remove it
            return front_currency

    def peekFront(self):
        if self.linkedLink.isListEmpty():  # Check if queue is empty
            print("Queue is empty")
            return None
        else:
            return self.linkedLink.getCurrency(0)  # Return currency object at the front of the queue

    def peekRear(self):
        if self.linkedLink.isListEmpty():  # Check if queue is empty
            print("Queue is empty")
            return None
        else:
            return self.linkedLink.getCurrency(self.count - 1)  # Return currency object at the end of the queue

    def printQueue(self):
        printString = ""
        for i in range(self.linkedLink.count):  # Iterate over queue indices from front to end
            formatted_value = "%.2f" % (self.linkedLink.getCurrency(i).getNoteValue() + (self.linkedLink.getCurrency(i).getCoinValue() / 100))
            currency_name = self.linkedLink.getCurrency(i).getName()
            printString += (formatted_value + " " + currency_name + "\t")
        return printString
