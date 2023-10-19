class Currency:
    #Default Constructor
    def __init__() -> None:
        pass

    #Assigner
    def __init__(self,value):
        if value < 0 : raise ("invalid input: Negative Number was inputted.")
        
        self.noteValue = int(value)
        self.coinValue = int(round(value*100)%100)

    def add(self,addend):
        self.noteValue += addend.noteValue
        coinValueTemp = self.coinValue + addend.coinValue
        if(coinValueTemp > 100): 
            self.noteValue += 100
            self.coinValue = coinValueTemp-100
        else:  self.coinValue = coinValueTemp

    
    def subtract(subtrahend):
        pass
        



    def isEqual(self,comparand) -> bool:
        if comparand.noteValue == self.noteValue and comparand.coinValue == self.coinValue: return True
        return False

    def isGreater(self,comparand) -> bool:
        if comparand.noteValue > self.noteValue: return False
        if comparand.coinValue > self.coinValue: return False
        return True

    def print(self):
        print("%.2f" % (self.noteValue + (self.coinValue/100)), end = " ")
