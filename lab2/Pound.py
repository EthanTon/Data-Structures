from currency import Currency

class Pound(Currency):
    def __init__(self,value):
        super().__init__(value)
        self.currency_name = "Pound"

    def name(self):
        return self.currency_name