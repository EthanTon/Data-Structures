from currency import Currency
from dollar import Dollar
from pound import Pound

def main():

    # Declaring currency
    currencies = [Pound(1.00),Dollar(0.00)]
    for currency in currencies: 
        currency.print()
    print()

if __name__ == "__main__":
    main()

