class Currency:
    #Assigner
    
    def __init__(self,value=None):
    """
    Initializes an instance of the Currency class.

    Pre: value (int, optional) represents the initial value. 
    Post: If None, both noteValue and coinValue is set to 0.00. 
        otherwise, noteValue will be set to the integer part of the value and 
        coinValue will be set to the remainder after converting the value to cents.

    Returns: None
    """
        if value is None:
            self.noteValue = 0.00
            self.coinValue = 0.00
        else:
            self.noteValue = int(value)
            self.coinValue = int(round(value*100)%100)
        
    def getName():
    '''
    Gets the name of the currency.
    
    Pre: None
    Post: Gets the currency name
    
    Returns: None
    '''
        print("in child class")
    

    def add(self,addend):     
    """
    This method adds the values of two currency objects and updates the attributes noteValue and coinValue accordingly.

    Pre: addend (Object): This is the currency object to be added. It has a 'getName()'
        method and has the attributes 'noteValue' and 'coinValue'.
    Post: self.coinValue and self.noteValue are updated accordingly to account for the addition.

    Returns: None
    """
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
    """
    This method subtracts the values of two currency objects and updates the attributes noteValue and coinValue accordingly.

    Pre: subtrahend (Object): This is the currency object to be subtracted.
    Post: self.coinValue and self.noteValue are updated accordingly to account for the subtraction.

    Returns: None
    """
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
    """
    This method checks if two currency objects are equal to eachother.

    Pre: comparand (Object): The currency object to be compared.
    Post: 
    
    Returns:
        bool: True if the noteValue and coinValue of both objects are equal, otherwise False.
    """
        try:
            if(comparand.getName()!=self.getName()): raise ValueError
            if comparand.noteValue == self.noteValue and comparand.coinValue == self.coinValue: return True
        except ValueError: 
            print("Invalid operation")
        return False

    
    def isGreater(self,comparand) -> bool:
    """
    This method checks if the current currency object is greater than the comparand.

    Pre:comparand (Object): The currency object to be compared. 
    Post:

    Returns:
        bool: True if the current currency object is greater than the comparand currency object, otherwise False.

    """
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
    """
    Prints the combined value of noteValue and coinValue as a two digit decimal along with the name of the currency.

    Pre: None
    Post: Currency values followed by the name are printed.
    """
        print("%.2f" % (self.noteValue + (self.coinValue/100)),self.getName(), end=" ")