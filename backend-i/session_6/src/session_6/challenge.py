def factorial(a):
    assert isinstance(a, (int, float))

    if a < 0:
        raise Exception("Sorry, no numbers below zero")
    if a == 0:
        return 1
    
    def calc(a):
        if(a == 1):
            return a
        else:
            return a*factorial(a-1)
    
    return calc(a)
        
    
    




