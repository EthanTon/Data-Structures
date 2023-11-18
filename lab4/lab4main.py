"""
Lab Number: 4
Name: Ethan Ton, Alex Cho
Purpose: This program demonstrates the BST operations using Dollar currency objects, dollar_values.
"""

from BSTNode import BSTNode
from BST import BST
from dollar import Dollar

def main():

    bst = BST()
    file = open('output.txt', 'w')

    #start up sequence
    dollar_values = [
    57.12, 23.44, 87.43, 68.99, 111.22,
    44.55, 77.77, 18.36, 543.21, 20.21,
    345.67, 36.18, 48.48, 101.00, 11.00,
    21.00, 51.00, 1.00, 251.00, 151.00
    ]

    # Creating 20 Dollar objects
    for value in dollar_values:
        bst.insert(BSTNode(Dollar(value)))
    
    output = bst.print()
    print(output)
    file.write(output + "\n")

    while True:
        print("\nOptions:")
        print("[a] Add Node")
        print("[d] Delete Node")
        print("[s] Show/Display Tree")
        print("[q] Quit")

        option = input("Enter your option: ").lower()

        if option == 'a':
            value = input("Enter value for new node:")
            try:
                bst.insert(BSTNode(Dollar(float(value))))
            except:
                print("Invalid Input: "+value+" was rejected")
        elif option == 'd':
            value = input("Enter value for removal:")
            try:
                bst.remove((Dollar(float(value))))
            except:
                print("Invalid Input: "+value+" was rejected")
        elif option == 's': #rewrite
            
            output = bst.print()
            print(output)
            file.write(output + "\n")
            
        elif option == 'q':
            output = bst.print()
            print(output)
            file.write(output + "\n")
            break
        else:
            print("Invalid option. Please try again.")
    file.close()
    
if __name__ == '__main__':
    main()