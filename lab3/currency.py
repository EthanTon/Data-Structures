"""
THERE WAS A CHANGE IN THE CURRENCY CLASS

We added the following methods to the class:

getNoteValue() 
getCoinValue()

These will act as a way for others to get the note and value values. In the original code, these methods were not present which prevented us from getting the note and value values to use in the singlylinkedlist class.
"""

"""
Lab Number: 2
Name: Ethan Ton, Alex Cho
Purpose: Implement a Currency class to perform various currency operations, such as addition, subtraction, comparison, and printing.
"""
class Currency: 
    def __init__(self,value=None):
        if value is None:
            self.noteValue = 0.00
            self.coinValue = 0.00
        else:
            self.noteValue = int(value)
            self.coinValue = int(round(value*100)%100)

    def getNoteValue(self):
        """
        Gets the note value.
    
        Pre: None
        Post: Gets the note value
    
        Returns: self.noteValue
        """
        return self.noteValue
    def getCoinValue(self):
        """
        Gets the coin value.
    
        Pre: None
        Post: Gets the coin value.
    
        Returns: self.coinValue
        """
        return self.coinValue

    def getName(self):
        """
        Gets the name of the currency.
    
        Pre: None
        Post: Gets the currency name
    
        Returns: None
        """
        pass
    
        """
        This method adds the values of two currency objects and updates the attributes noteValue and coinValue accordingly.

        Pre: addend (Object): This is the currency object to be added. It has a 'getName()'
            method and has the attributes 'noteValue' and 'coinValue'.
        Post: self.coinValue and self.noteValue are updated accordingly to account for the addition.

        Returns: None
        """
    def add(self,addend):     
    
        try:
            if(addend.getName()!=self.getName()):
                raise ValueError
            self.noteValue += addend.noteValue
            coinValueTemp = self.coinValue + addend.coinValue
            if(coinValueTemp > 100): 
                self.noteValue = self.noteValue + 1
                self.coinValue = coinValueTemp - 100
            else:
                self.coinValue = coinValueTemp
        except ValueError:
            print("Invalid addition")

    def subtract(self,subtrahend):   
        """
        This method subtracts the values of two currency objects and updates the attributes noteValue and coinValue accordingly.

        Pre: subtrahend (Object): This is the currency object to be subtracted.
        Post: self.coinValue and self.noteValue are updated accordingly to account for the subtraction.

        Returns: None
        """
        try:
            if subtrahend.getName() != self.getName():
                raise ValueError("InvalidSubtrahend")
            self.noteValue = self.noteValue - subtrahend.noteValue

            coinTempValue = self.coinValue - subtrahend.coinValue

            if coinTempValue < 0:
                self.noteValue = self.noteValue - 1
                self.coinValue = 100+coinTempValue
                if self.noteValue < 0: 
                    raise ValueError
            else:
                self.coinValue = coinTempValue
            if self.noteValue < 0 or self.coinValue < 0:
                raise ValueError
        except ValueError:
            print("Invalid subtraction")
            if self.noteValue < 0:
                self.add(subtrahend)

    def isEqual(self,comparand) -> bool:
        """
        This method checks if two currency objects are equal to eachother.

        Pre: comparand (Object): The currency object to be compared.
        Post: if ValueError print "Invalid Operation"
    
        Returns:
            bool: True if the noteValue and coinValue of both objects are equal, otherwise False.
        """
        try:
            if comparand.getName() != self.getName(): raise ValueError
            if comparand.noteValue == self.noteValue and comparand.coinValue == self.coinValue: return True
        except ValueError: 
            print("Invalid operation")
        return False

    
    def isGreater(self,comparand) -> bool:
        """
        This method checks if the current currency object is greater than the comparand.

        Pre: comparand (Object) with 'GetName()', 'noteValue', and 'coinValue' attributes
        Post: Invalid operation if there is a ValueError
        Return: True if the current currency object is greater than the comparand currency object, otherwise False
        """
        try:
            if comparand.getName()!= self.getName():
                raise ValueError
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
        Post: Prints the combined value of noteValue and coinValue as a two-digit decimal along with the name of the currency
        Return: None
        Function Print()
            PrintFormatted(self.noteValue + (self.coinValue / 100), self.GetName())
        End
        """
        print("%.2f" % (self.noteValue + (self.coinValue/100)),self.getName(), end=" ")
