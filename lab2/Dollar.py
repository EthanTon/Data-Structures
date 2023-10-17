class Dollar(Currency):
    def __init__(self, noteValue, coinValue):
        super().__init__(noteValue, coinValue)
        self.currency_name = "Dollar"

    def name(self):
        return self.currency_name
