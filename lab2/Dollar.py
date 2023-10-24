from currency import Currency

class Dollar(Currency):
    def __init__(self,value=None):
        super().__init__(value)
        self.currency_name = "Dollar"
    
    def getName(self):
        return self.currency_name