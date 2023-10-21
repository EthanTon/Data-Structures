class Currency:
    #Default Constructor
    def __init__() -> None:
        pass

    #Assigner
    def __init__(self,value):
        try:
            if value < 0 : raise ValueError
        
            self.noteValue = int(value)
            self.coinValue = int(round(value*100)%100)
        except ValueError: 
            (print("Invalid value"))
            raise ValueError


    def add(self,addend):
        self.noteValue += addend.noteValue
        coinValueTemp = self.coinValue + addend.coinValue
        if(coinValueTemp > 100): 
            self.noteValue = self.noteValue + 1
            self.coinValue = coinValueTemp - 100
        else:  self.coinValue = coinValueTemp

    
    def subtract(self,subtrahend):
        try:
            self.noteValue = self.noteValue - subtrahend.noteValue

            coinTempValue = self.coinValue - subtrahend.coinValue

            if(coinTempValue < 0): 
                self.noteValue = self.noteValue - 1
                self.coinValue = 100+coinTempValue
                if self.noteValue < 0: 
                    raise ValueError
            else: self.coinValue = coinTempValue
            if self.noteValue < 0 or self.coinValue < 0: raise ValueError
        except ValueError: 
            (print("Invalid subtraction"))
            self.add(subtrahend)
        
            
        
    def isEqual(self,comparand) -> bool:
        if comparand.noteValue == self.noteValue and comparand.coinValue == self.coinValue: return True
        return False

    def isGreater(self,comparand) -> bool:
        if comparand.noteValue > self.noteValue: return False
        if comparand.coinValue == self.noteValue:
            if comparand.coinValue > self.coinValue: return False
        return True

    def print(self):
        print("%.2f" % (self.noteValue + (self.coinValue/100)), end = " ")
