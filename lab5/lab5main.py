"""
Lab Number: 5
Name: Ethan Ton, Alex Cho
Purpose: This program demonstrates 
"""

from dollar import Dollar
from HashTable import HashTable

def main():
    ht = Hashtable(29)
    
    #start up sequence
    dollar_values = [
    57.12, 23.44, 87.43, 68.99, 111.22,
    44.55, 77.77, 18.36, 543.21, 20.21,
    345.67, 36.18, 48.48, 101.00, 11.00,
    21.00, 51.00, 1.00, 251.00, 151.00
    ]
    
    # Creating 20 Dollar objects
    for value in dollar_values:
        ht.HashInsert(Dollar(value))
        
    print(ht.getCollisions)

    
    