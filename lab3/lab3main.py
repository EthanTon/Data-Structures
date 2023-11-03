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

    queueList.enqueue(currency[1])

    print(queueList.printQueue())

if __name__ == '__main__':
    main()