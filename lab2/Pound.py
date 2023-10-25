from currency import Currency

class Pound(Currency):
    def __init__(self,value=None):
        super().__init__(value)
        self.currency_name = "Pound"

    """
        Gets the name of the currency.
    
        Pre: None
        Post: Gets the currency name
    
        Returns: None
        """
    def getName(self):
        return self.currency_name