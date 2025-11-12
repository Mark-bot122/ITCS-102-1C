def greetwithname(name):
    print(f"HI {name}, I Hope you're having a good day!!")

def greetperson(name,loc,age):
    print(f"Hi {name}, from {loc} and {age} year\'s old")

def functionwithreturn(number):
    print(f"This function calculates the summation from 1 - {number}")
    sum = 0
    for x in range(1, number+1, 1):
        sum += x
    return sum

def factorialwithreturn(number):
    print(f"This function calculates the factorial from 1 - {number}")
    fac = 1
    for z in range(number,0, -1):
        fac *= z
    return fac
    
