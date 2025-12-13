def washing():

    while True:
        wash_again = input("Continue washing the clothes ( yes / no )").lower()
        if wash_again == "yes":
            print("washing again...")
            continue
        else:
            print("washing stops...")
            break
    # First block
def activity_1():
    print("Hello world") 

def activity_2():
    name = input("What is your name? ")
    print("Hello", name, "welcome to the matrix!!")

def activity_3():
    print("Magandang Hapon, \n\t\t\tBSIT 1C")

def activity_4():
    name = input("What is your name--> ")
    print("Welcome to my program ", name)
    print("your name has ",len(name) , "characters")

def activity_5():
    something = eval(input("Put something ..."))
    print("The value of something is " , type(something))
   # Second block     
def activity_6():
    n1 = eval(input("enter first number:"))
    n2 = eval(input("enter second number:"))
    s = n1 + n2
    d= n1 - n2
    p = n1 * n2
    q = n1 / n2

    print("the sum of",n1,"and",n2, "is equal to",s)
    print("the difference of",n1,"and",n1,"is equal to",d)
    print("the product of",n1,"and",n2,"isequal to",p)
    print("the quotient of",n1,"and",n2,"is equal to",q)

def activity_7():
    a = 5
    print("The amount of chromosomes the you had", a)

    a += 5
    print("The amount that you want is", a)

    a += 60
    a *= 2
    print("Your current money right now", a)

def activity_8():
    a = 10
    b = 20

    print( a < b )

    name1 = "Neji"
    name2 = "neji"

    print( name1 != name2 )

def activity_9():
    username = 'Neji'
    password = 'mark123'

    print("USER LOGIN")
    print( (username == 'Neji') and ( password == 'mark123' ) )

def activity_10():
    username = 'mark'
    password = 'neji'

    u = input("USERNAME --> ")
    p = input("PASSWORD --> ")

    if (u == username) and (p == password):
        print("Access granted")
    else:
        print("Acces Denied")
    # Third block
def activity_11():
    temp = eval(input("Enter imong temp --> "))

    if temp >= 1 and temp <= 20:
        print("Temperature is considered cold ")

    elif temp >= 21 and temp <= 30:
        print("Temperature is moderately cold")

    elif temp >= 31 and temp <= 37:
        print("Temperature is Lukewarm")

    elif temp >= 38 and temp <= 45:
        print("Temperature is Hot")

    elif temp >= 46 and temp <= 50:
        print("Temperature is Boiling Hot")

    elif temp >= 51:
        print("Temperature is considered dangerous")

    elif temp <= 1:
        print("Freezing temp")

    else:
        print("Invalid temperature")

def activity_12():
    for cycle in range(1,101,1):
        print(cycle, "I LOVE BOCCHI THE ROCK")
        print("nuh uh", cycle )

def activity_13():
    sum = 0

    for x in range(1,11,1):
        nmb = eval(input("Enter any number --> "))
        sum += nmb
    print("The sum of all the numbers is", sum)

def activity_14():
    for nmb in range(20,0,-1):
        print(nmb)

def activity_15():
    print("lol")

def activity_16():
    for x in range(1,11,1):
        for i in range(1,x,1):
            print(i,end=" ")
        print()

def activity_17():
    for x in range(1,11,1):
        for n in range(10,x,-1):
            print("*", end= " ")
        print()

def activity_18():
    print("no")

def activity_19():
    print("\t\t *", end= " ")
    for x in range(1,11,1):
        for y in range(10,x,-1):
            print(" ", end= " ")
        for z in range(1,x,1):
            print("*", end= " ")
        for m in range(1,x,1):
            print("*", end= " ")
        print()

    for l in range(1,11,1):
        for o in range(1,l,-1):
            print(" ", end= " ")
        for q in range(11,l,-1):
            print("*", end= " ")
        for t in range():
            print()
        print()

def activity_20():
    isDirty = True

    while isDirty == True:
        wash_again = input("Continue washing the clothes ( yes / no ): ").lower()

        if wash_again == 'yes':
            print("Washing the clothes again... ")
            continue
        else:
            print("washing stops now...")
            break

def activity_21():
    import random

    print("NUMBER GUESSING GAME")

    random_value = random.randint(1,5) #generate random integer from 1-5
    tries = 0
    Tuloy = True


    name = input("Enter your name: ")

    while Tuloy == True:
        num = eval(input("Enter a number: "))
        tries += 1
        if num == random_value:
            print("WINNNNEEERRR!!!!!!!!!!!!")
            break
        else:
            print("Incorrect guess\nTry again :<")
            continue

    print(f"HI {name} your guess is correct\nNumber of tries {tries}")



