"""
Lab Number: 3
Name: Ethan Ton, Alex Cho
Purpose: This program demonstrates the implementation of a singly linked list, stack, and queue, allowing users to perform various operations on each data structure using currency objects.
"""

from SinglyLinkedList import SinglyLinkedList
from dollar import Dollar
from Stack import Stack
from Queue import Queue


def main():
    print("Ethan Ton/Alex Cho: Starting ADT demonstration...")

    # 20 Dollar objects in a list

    currency = (
        Dollar(57.12),
        Dollar(23.44),
        Dollar(87.43),
        Dollar(68.99),
        Dollar(111.22),
        Dollar(44.55),
        Dollar(77.77),
        Dollar(18.36),
        Dollar(543.21),
        Dollar(20.21),
        Dollar(345.67),
        Dollar(36.18),
        Dollar(48.48),
        Dollar(101.00),
        Dollar(11.00),
        Dollar(21.00),
        Dollar(51.00),
        Dollar(1.00),
        Dollar(251.00),
        Dollar(151.00)
    )

    linkedList = SinglyLinkedList()
    stackList = Stack()
    queueList = Queue()

    # #LinkedList Module

    for i in range(7):
        linkedList.addCurrency(currency[i], 0)

    print(linkedList.findCurrency(Dollar(87.43)))
    print(linkedList.findCurrency(Dollar(44.56)))

    linkedList.removeCurrency(Dollar(111.22))
    linkedList.removeCurrency(2)

    print(linkedList.printList())

    for i in range(8, 12):
        linkedList.addCurrency(currency[i], i % 5)

    linkedList.removeCurrency(linkedList.countCurrency() % 6)
    linkedList.removeCurrency(int(linkedList.countCurrency() / 7))

    print(linkedList.printList())

    # Stack Module

    for i in range(13, 20):
        stackList.push(currency[i])

    stackList.peek().print()
    print()

    for i in range(3):
        stackList.pop()

    print(stackList.printStack())

    for i in range(5):
        stackList.push(currency[i])

    for i in range(2):
        stackList.pop()

    print(stackList.printStack())

    # Queue Module

    counter = 0
    for i in range(5, len(currency), 2):
        queueList.enqueue(currency[i])
        counter += 1
        if counter == 7:
            break

    queueList.peekFront().print()
    print()
    queueList.peekRear().print()
    print()

    queueList.dequeue()
    queueList.dequeue()

    print(queueList.printQueue())

    for i in range(10, 15):
        queueList.enqueue(currency[i])

    for i in range(3):
        queueList.dequeue()

    print(queueList.printQueue())

    # End Message

    print("...The ADT demonstration has ended")


if __name__ == '__main__':
    main()