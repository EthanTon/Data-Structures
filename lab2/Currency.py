class Currency:
    #Default Constructor
    def __init__() -> None:
        pass

    #Assigner
    def __init__(self,value):
        if value < 0 : raise ("invalid input: Negative Number was inputted.")
        
        self.noteValue = int(value)
        self.coinValue = int(round(value*100)%100)

    def add(addend):
        addendNoteValue = int(addend)
        addendCoinValue = int(round(addend*100)%100)
        Currency.coinValue = Currency.coinValue + addendCoinValue
        Currency.noteValue += addendNoteValue + int(Currency.coinValue/100)
        Currency.coinValue = int(Currency.coinValue%100)
    
    def subtract(subtrahend):
        pass
        



    def isEqual(comparand) -> bool:
        if int(100*comparand) == 100*Currency.noteValue +  Currency.coinValue: return True
        return False

    def isGreater(comparand):
        if int(100*comparand) > 100*Currency.noteValue +  Currency.coinValue: return True
        return False

    def print():
        print(Currency.noteValue + "." + Currency.coinValue)
