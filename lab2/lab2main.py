from currency import Currency
from dollar import Dollar
from pound import Pound

def main():


    # Declaring currency 
    currencies = [Pound(0.00),Dollar(0.00)]


    operation = "r" #default state
    while operation != "q":
        
        for currency in currencies: currency.print()   
        print()

        Input = []
        inputLength = 0

        for i in input().split(" "):
            Input.append(i)
            inputLength += 1



        affectedCurrency = ""
        operandValue = 0.0
        effectCurrency = ""

        if(inputLength == 4):
            affectedCurrency = Input[1]

            operandValue = float(Input[2])

            effectCurrency = Input[3]
        elif(inputLength == 1): pass
        else: print("Invalid input")
        
        try:

            if effectCurrency == "pound": operand = Pound(operandValue)
            elif effectCurrency == "dollar": operand = Dollar(operandValue)
            else: operation = "r"
        except ValueError: 
            operand = Currency(0.00)
            operation = "r"

        #operator block
        operation = Input[0]

        if operation == "a":
            if affectedCurrency == "p": currencies[0].add(operand)
            elif affectedCurrency == "d": currencies[1].add(operand)
            else: print("Invalid Input")
        elif operation == "s":
            if affectedCurrency == "p": currencies[0].subtract(operand)
            elif affectedCurrency == "d": currencies[1].subtract(operand)
            else: print("Invalid Input")
        elif operation == "q":  break
        else: print("Invalid Input")


if __name__ == "__main__":
    main()

