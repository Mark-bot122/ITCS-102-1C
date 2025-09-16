nmb = eval(input("Enter a number--> "))

sagot = 1

for i in range (nmb,1,-1):
    sagot *= i
print("The factotrial of", nmb, "is " , sagot)
