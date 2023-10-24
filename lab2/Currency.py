class Currency:
    #Assigner
    def __init__(self,value=None):
            
            if value is None:
                self.noteValue = 0.00
                self.coinValue = 0.00
        
            self.noteValue = int(value)
            self.coinValue = int(round(value*100)%100)
        
    def getname(): print("in child class")


    def add(self,addend):
        try:
            if(addend.getName()!=self.getName()): raise ValueError
            self.noteValue += addend.noteValue
            coinValueTemp = self.coinValue + addend.coinValue
            if(coinValueTemp > 100): 
                self.noteValue = self.noteValue + 1
                self.coinValue = coinValueTemp - 100
            else:  self.coinValue = coinValueTemp
        except ValueError: ("Invalid addition")

        

    
    
    def subtract(self,subtrahend):
        try:
            if(subtrahend.getName()!=self.getName()): raise ValueError("InvalidSubtrahend")
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
            print("Invalid subtraction")
            self.add(subtrahend)
        except ValueError("InvalidSubtrahend"): print("Invalid subtraction")
            
        
            
        
    def isEqual(self,comparand) -> bool:
        try:
            if(comparand.getName()!=self.getName()): raise ValueError
            if comparand.noteValue == self.noteValue and comparand.coinValue == self.coinValue: return True
        except ValueError: 
            print("Invalid operation")
        return False

    def isGreater(self,comparand) -> bool:
        try:
            if(comparand.getName()!=self.getName()): raise ValueError
            if comparand.noteValue > self.noteValue: return False
            if comparand.noteValue == self.noteValue:
                if comparand.coinValue > self.coinValue: return False
            return True
        except ValueError: 
            print("Invalid operation")
            return False

    def print(self):
        print("%.2f" % (self.noteValue + (self.coinValue/100)),self.getName(), end=" ")
