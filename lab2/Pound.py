from currency import Currency

class Pound(Currency):
    def __init__(self,value):
        super().__init__(value)
        self.currency_name = "Pound"

    #additional name attribute
    def name(self):
        return self.currency_name
    
    def isSameCurrency(self, comparand):
        if self.currency_name == comparand.currency_name:
            return True
        else:
            return False
    
    def add(self, addend):
        if self.isSameCurrency(addend):
            super().add(addend)
        else:
            print("Invalid addition")
    
    def subtract(self, subtrahend):
        if self.isSameCurrency(subtrahend):
            super().subtract(subtrahend)
        else:   
            print("Invalid subtraction")
        
    def isEqual(self, comparison):
        if self.isSameCurrency(comparison):
            super().isEqual(comparison)
        else:    
            print("Invalid comparison")
        
    def isGreater(self, compare):
        if self.isSameCurrency(compare):
            super().isGreater(compare)
        else:
            print("Invalid comparison")
    
    def print(self):
        super().print()
        print(self.name(), end = " ")