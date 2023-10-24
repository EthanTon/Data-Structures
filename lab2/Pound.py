from currency import Currency

class Pound(Currency):
    def __init__(self,value=None):
        super().__init__(value)
        self.currency_name = "Pound"

    def getName(self):
        return self.currency_name