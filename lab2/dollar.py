"""
Lab Number: 2
Name: Ethan Ton, Alex Cho
Purpose: Define a Dollar class that represents currency objects for Dollars and provides currency-specific operations.
"""
from currency import Currency

class Dollar(Currency):
    def __init__(self,value=None):
        super().__init__(value)
        self.currency_name = "Dollar"
    """
        Gets the name of the currency.
    
        Pre: None
        Post: Gets the currency name
    
        Returns: None
        """
    def getName(self):
        return self.currency_name
