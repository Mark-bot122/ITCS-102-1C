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
