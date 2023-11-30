"""
Lab Number: 5
Name: Ethan Ton, Alex Cho
Purpose: This program demonstrates the Hash Table operations using Dollar currency objects, dollar_values.
"""

from dollar import Dollar
from HashTable import HashTable

def main():
    dollar_values = [
        57.12, 23.44, 87.43, 68.99, 111.22,
        44.55, 77.77, 18.36, 543.21, 20.21,
        345.67, 36.18, 48.48, 101.00, 11.00,
        21.00, 51.00, 1.00, 251.00, 151.00
    ]

    ht = HashTable(29)

    # Inserting data into the hash table
    for value in dollar_values:
        ht.HashInsert(Dollar(value))

    print("Data items loaded:", ht.length)
    print("Load factor:", ht.getLoadFactor())
    print("Number of collisions:", ht.getCollisions())

    while True:
        option = input("\nEnter a Dollar value to search (Press 'q' to quit): ")
        if option.lower() == 'q':
            break

        try:
            option = float(option)
            result = ht.HashSearch(Dollar(option))
            if result is not None:
                print(f"Dollar found at index {result}.")
            else:
                print("Invalid Data")
        except ValueError:
            print("Invalid input. Please enter a valid Dollar value.")

if __name__ == '__main__':
    main()
