"""
Lab Number: 5
Name: Ethan Ton, Alex Cho
Purpose: Implement a hash table with quadratic probing collision resolution, specifically designed for storing and managing Dollar objects based on their hash values in a given size.
"""

from dollar import Dollar

class HashTable:
    def __init__(self, size=None):
        if size is not None:
            self.size = size
            self.map = [None] * size
            self.collisions = 0
            self.length = 0
        else: raise ValueError

    def getLoadFactor(self) -> float:
        """
        Gets hash table load factor.
    
        Pre: None
        Post: Gets the load factor
    
        Returns: load factor
        """
        return float(self.collisions/self.size)
    
    def getCollisions(self) -> int:
        """
        Gets the collision count
    
        Pre: None
        Post: Gets the number of collision
    
        Returns: collision
        """
        return self.collisions

    def HashingFunction(self,item=None) -> int:
        """
        Gets the name of the currency.
    
        Pre: dollar object named item
        Post: returns the index of currency or raises ValueError if item is none.
    
        Returns: index
        """
        if item is not None:
            m = 2
            n = 3
            return int((m*item.getNoteValue() + n*item.getCoinValue())%self.size)
        else: raise ValueError

    def HashInsert(self, item):
        """
        Inserts an element into hash table
    
        Pre: dollar object named item
        Post: Adds an element to the hash table
            If the index is equal to original index a value error is raised.
    
        Returns: None
        """
        index = self.HashingFunction(item)
        originalIndex = index
        i = 1  # Quadratic probing increment

        while self.map[index] is not None:
            index = (originalIndex + i**2) % self.size
            i += 1
            self.collisions += 1
            if index == originalIndex:
                raise ValueError("HashTable is full")

        self.map[index] = item
        self.length += 1

    def HashRemove(self, item):
        """
        Removes items from hash table
    
        Pre: dollar object named item
        Post: Removes item wherever it is located from the hash table.
    
        Returns: None
        """
        index = self.HashingFunction(item)
        originalIndex = index

        while self.map[index] is not None:
            if item.isEqual(self.map[index]):
                self.map[index] = None
                return
            index = (index + 1) % self.size
            if index == originalIndex:
                break  # Item not found

    def HashSearch(self, item):
        """
        Searches for items in hash table
    
        Pre: dollar object named item
        Post: index of item
    
        Returns: index if item is found or None if item is not found
        """
        index = self.HashingFunction(item)
        originalIndex = index

        while self.map[index] is not None:
            if item.isEqual(self.map[index]):
                return index
            index = (index + 1) % self.size
            if index == originalIndex:
                break  # Item not found

        return None