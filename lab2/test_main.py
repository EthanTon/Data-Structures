if __name__ == '__main__':
    #Declare a primitive array of 2 Currency references, first pound object second dollar object, both zero value
    currencies = [Pound(0.00), Dollar(0.00)]
    
    currencies[0].add(Pound(5.75))
    currencies[1].add(Dollar(6.25))
    
    currencies[0].subtract(Pound(2.50))
    currencies[1].subtract(Dollar(4.50))
    
    currencies[0].print()
    currencies[1].print()

    print(currencies[0].isEqual(Pound(3.25)))
    print(currencies[1].isGreater(Dollar(4.0)))