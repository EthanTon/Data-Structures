from BST import BST

class MinHeap(BST):
    def search(self, key) -> bool:
        return super().search(key)
    
    def insert(self, node):
        return super().insert(node)
    
    def remove(self, key):
        return super().remove(key)
    
    def _remove(self, key, root=None):
        return super()._remove(key, root)
        