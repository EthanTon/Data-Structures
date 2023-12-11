"""
Lab Number: 4
Name: Ethan Ton, Alex Cho
Purpose: This program demonstrates the heap operations using Dollar currency objects, dollar_values.
"""
from BSTNode import BSTNode
from MinHeap import MinHeap
from dollar import Dollar

def main():
    heap = MinHeap()
    

    #start up sequence
    dollar_values = [
    57.12, 23.44, 87.43, 68.99, 111.22,
    44.55, 77.77, 18.36, 543.21, 20.21,
    345.67, 36.18, 48.48, 101.00, 11.00,
    21.00, 51.00, 1.00, 251.00, 151.00
    ]

    # Creating 20 Dollar objects
    i = 0
    for value in dollar_values:
        heap.insert(BSTNode(Dollar(value)))
        i+=1
        if i == 10:
            print(heap.print())
    print(heap.print())

if __name__ == '__main__':
    main()


    