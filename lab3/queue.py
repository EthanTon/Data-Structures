from singlyLinkedList import SinglyLinkedList

class Queue(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def createQueue(self):
        pass

    def enqueue(self, currency):
        self.addCurrency(currency, self.count-1)  # Add currency object to the end of the queue

    def dequeue(self):
        if self.isListEmpty():  # Check if queue is empty
            print("Empty Queue")
            return None
        else:
            front_currency = self.getCurrency(0)  # Retrieve currency object at the front of the queue
            self.removeCurrency(0)  # Remove it
            return front_currency

    def peekFront(self):
        if self.isListEmpty():  # Check if queue is empty
            print("Queue is empty")
            return None
        else:
            return self.getCurrency(0)  # Return currency object at the front of the queue

    def peekRear(self):
        if self.isListEmpty():  # Check if queue is empty
            print("Queue is empty")
            return None
        else:
            return self.getCurrency(self.count - 1)  # Return currency object at the end of the queue

    def printQueue(self):
        printString = ""
        for i in range(self.count):  # Iterate over queue indices from front to end
            formatted_value = "%.2f" % (self.getCurrency(i).getNoteValue() + (self.getCurrency(i).getCoinValue() / 100))
            currency_name = self.getCurrency(i).getName()
            printString += (formatted_value + " " + currency_name + "\t")
        return printString

    def destroyQueue(self):
        pass
