class Pound(Currency):
    def __init__(self,value):
        super().__init__(value)
        self.currency_name = "Pound"

    #additional name attribute
    def name(self):
        return self.currency_name
    
    def print(self):
        super().print()
        print(self.name(), end = " ")