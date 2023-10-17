class Currency:
    #Default Constructor
    def __init__() -> None:
        pass

    #Assigner
    def __init__(self,value):
        if value < 0 : raise ("invalid input: Negative Number was inputed.")

        self.noteValue,self.coinValue = value.split(".")
    
    
    def add(addend):
        if addend < 0: Currency.subtract(-addend)

        addendNoteValue,addendCoinValue = addend.split(".")

        Currency.noteValue += addendNoteValue 

        c = Currency.coinValue + addendCoinValue

        if c > 1: Currency.add(c)
        else: c = Currency.coinValue

        pass

    def subtract(subtrahend):
        if subtrahend < 0: Currency.add(-subtrahend)
        



    def isEqual(comparand) -> bool:
        if comparand == Currency.noteValue+round(Currency.coinValue/100,2): return True
        return False

    def isGreater(comparand):
        if comparand > Currency.noteValue+round(Currency.coinValue/100,2): return True
        return False

    def print():
        print(Currency.noteValue + "." + Currency.coinValue)
