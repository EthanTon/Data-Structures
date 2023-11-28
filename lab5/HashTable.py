from dollar import Dollar

class HashTable:
    def __init__(self, size=None):
        if size is not None:
            self.size = size
            self.map = [None] * size
            self.collisions = 0
        else: raise ValueError

    def getLoadFactor(self) -> float:
        return float(self.size/self.collisions)

    def HashingFunction(self,item=None) -> int:
        if item is not None:
            m = 2
            n = 3
            return int((m*item.getNoteValue() + n*item.getCoinValue())%self.size)
        else: raise ValueError

    def HashInsert(self, item):
        if self.HashSearch(item) is None:
            index = self.HashingFunction(item)
            if map[index] is not None:
                map[index] = item
            else: pass

    def HashRemove(self,item):
        index = self.HashSearch(item)
        if index is not None:
            map[index] = None

    def HashSearch(self, item):
        index = self.HashingFunction(item)

        if item.isEqual(self.map[index]):
            return index
        else: return None

    

        
    

    