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
        return float(self.size/self.collisions)
    
    def getCollisions(self) -> int:
        return self.collisions

    def HashingFunction(self,item=None) -> int:
        if item is not None:
            m = 2
            n = 3
            return int((m*item.getNoteValue() + n*item.getCoinValue())%self.size)
        else: raise ValueError

    def HashInsert(self, item):
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
        index = self.HashingFunction(item)
        originalIndex = index

        while self.map[index] is not None:
            if item.isEqual(self.map[index]):
                return index
            index = (index + 1) % self.size
            if index == originalIndex:
                break  # Item not found

        return None
