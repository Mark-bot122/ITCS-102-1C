import os
from activities import *

print("Welcome to Neji's Compiler")
print("Here is the overall of what I have learned on Python")
print("1.Functions\n2.Lessons\n3.Terminate the program")
uno = input("Please select a option: ")
os.system("cls")



while True:


    if uno == "1":
        print("---------------------------------------------")
        print("Great! You are now in the Basic Functions")
        print("1.Print\n2.Input\n3.Calc\n4.For loop\n5.While loop\n6.Go to previous page")
        print("--------------------------------------------")
        basic = input("Please select a option: ")


        while True:
            if basic == "1":
                os.system("cls")
                print("PRINT\n\nPrint is a Basic Python command/function that prints what the programmer wants the computer or the program to say")
                print("Instructions:\nPut 'print' fuction at the line of code\nType a close and open parenthesis\nInside the close and open parenthesis,type a quote and type 'Hello world' inside")
                una = input(" ").lower()
                os.system("cls")
                if una == "print(\"Hello world\")".lower():
                    print("Good job,you are now exiting the print function...")
                else:
                    print("Wrong!Try again")
                    continue
                break
                
            

            elif basic == "2":
                print("INPUT\n\nInput function is like the same command as Print but Input is asking or waiting rather for another command for the user")
                print("\nFor instance, you need to navigate on your program, then the function you will use is Input")
                print("Instruction:\nPut a variable 'name' then = sign and input('what is your name?: ') then print the command")
                dalawa = input(" ").lower()
                os.system("cls")
                if dalawa == "name = input('what is your name?: ')".lower():
                    sagot = input("what is your name?: ")
                    os.system("cls")
                    print(f"Hello{sagot}, welcome to my program ")
                else:
                    print("Wrong!Try again")
                    continue
                break

            elif basic == "3":
                print("Calculations\n\n Python can also calculate simple mathematical problems like...")
                # for z in range(1,5,1):
                #     print(z)
                math = ["addition", "subtraction", "multiplication", "division"]
                for i in range(len(math)):
                    print("-", math[i])
                tatlo = input("What would you like to try?(Type 'exit' to exit): ").lower()
                
                if tatlo == "addition".lower():
                    os.system("cls")
                    total = 0
                    print("Great, You are trying Addition")
                    add1 = eval(input("Put a number: "))
                    add2 = eval(input("Put a number: "))
                    total = add1 + add2

                    print(f"The sum of {add1} and {add2} is {total}")
                    ulit = input("Would you like to try again?( Y / N ): ").lower()
                    if ulit == "Y".lower():
                        os.system("cls")
                        continue
                    elif ulit == "N".lower():
                        os.system("cls")
                        print("Exiting addition...")
                        break
                
                elif tatlo == "subtraction".lower():
                    os.system("cls")
                    print("Great! You are trying subtraction")
                    sub1 = eval(input("Put a number: "))
                    sub2 = eval(input("Put a number: "))
                    total = sub1 - sub2
                    print(f"The difference of {sub1} and {sub2} is {total}.")
                    ulit = input("Would you like to try again?( Y / N ): ").lower()
                    if ulit == "Y".lower():
                        os.system("cls")
                        continue
                    elif ulit == "N".lower():
                        os.system("cls")
                        print("Exiting subtraction...")
                        break

                elif tatlo == "multiplication".lower():
                    os.system("cls")
                    print("Great! You are trying multiplication")
                    mul1 = eval(input("Put a number: "))
                    mul2 = eval(input("Put a number: "))
                    total = mul1 * mul2
                    print(f"The product of {mul1} and {mul2} is {total}.")
                    ulit = input("Would you like to try again?( Y / N ): ").lower()
                    if ulit == "Y".lower():
                        os.system("cls")
                        continue
                    elif ulit == "N".lower():
                        os.system("cls")
                        print("Exiting multiplication...")
                        break

                elif tatlo == "division".lower():
                    os.system("cls")
                    print("Great! You are trying division")
                    div1 = eval(input("Put a number: "))
                    div2 = eval(input("Put a number: "))
                    total = div1 / div2
                    print(f"The quotient of {div1} and {div2} is {total}.")
                    ulit = input("Would you like to try again?( Y / N ): ").lower()
                    if ulit == "Y".lower():
                        os.system("cls")
                        continue
                    elif ulit == "N".lower():
                        os.system("cls")
                        print("Exiting division...")
                        break
                elif tatlo == "exit".lower():
                    os.system("cls")
                    print("You are now exiting calc...")
                    break

            elif basic == "4":
                print("Great! You are now in the for loop")
                print("\n\nIn For loop, this is quite a tricky part. This function Iterates a sequence")
                print("In order to use this function, you need to start with 'for' *insert variable* in range(#,#,#)[hastags represents number]")
                pg2 = input("Next page?( Y / N): ").lower()
                
                if pg2 == "Y" or "y".lower():
                    os.system("cls")
                    print("PAGE 2")
                    print("for *variable* in range(#,#,#) the 1st hastag represent for 'start'\nThat is where your loop will start")
                    print("The number starts in 0 - infinity")
                    print("The 2nd hastag represents 'stop' of your loop, that means it declares when or where your loop will stop")
                    print("The number starts from 0 - infinity")
                    print("Lastly, the 3rd hashtag represents steps")
                    print("The number starts from 0 - infinity")

                apat = input("Would you like to try?( Y / N ): ").lower()
                if apat == "Y" or "y".lower():
                    print("Great! Now try it ")
                    x = eval(input("Start: "))
                    y = eval(input("Stop: "))
                    z = eval(input("Step: "))
                    for i in range(x, y, z):
                        print(i)
                    break 
            
            elif basic == "5":
                os.system("cls")
                print("You have entered on while loop")
                print("\n\nIn while Loop, you can use this for conditionals statements.")
                print("This function is similar to for loop but instead if Integers, we can use text or so called conditions")
                lima = input("Do you want to try while loop?( Y / N ): ").lower()
                if lima == "Y".lower():
                    os.system("cls")
                    print("Great! Read Carefully")
                    print("In order to do a while loop, you will start on typing 'while' and assigning a variable(optional) 'True' then using a colon(:) to create a code block")
                    pg2 = input("\nNext page?(2): ").lower()
                else:
                    break
                

                if pg2 == '2'.lower():
                    os.system("cls")
                    print("After inserting it in a code block, you can now create your simple conditions like this program")
                    print("This Program runs entirely on while loop and basic conditions")

                    pg3 = input("Page 3?(3): ").lower()
                    if pg3 == "3".lower():
                        os.system("cls")
                        print("This is how it will look like")
                        print("while True: \n\twash_again = input('do you want to was again?( Y \ N ): )")
                        print("\n\n if wash_again == 'Y':\n\tcontinue\nelse:\n\tprint('washing stops..)\n\tbreak")
                        lup = input("Press 1 to try: ")
                        if lup == "1":
                            washing()
                            break
                        else:
                            break
            elif basic == "6":
                os.system("cls")
                print("You are now in the Main Menu")
            break
        break

    elif uno == "2":
        print("You have entered Lessons")
        print("Here is the overall activities that we have done")
        act = ["Activity 1", "activity 2", "activity 3","activity 4", "activity 5", "Next Page","Terminate Lesson"]
        x = 0
        for i in act:
            x += 1
            print(f"{x} - {i}")
        una = input("PIck one from the option to run: ")
        if una == "1":
            activity_1()
        elif una == "2":
            activity_2()
        elif una == "3":
            activity_3()
        elif una == "4":
            activity_4()
        elif una == "5":
            activity_5()
        elif una == "6":
            os.system("cls")
            print("Lessons(Page 2)")
            print("Here is the overall activities that we have done")
            act = ["Activity 6", "activity 7", "activity 8","activity 9", "activity 10", "Next Page"]
            x = 0
            for i in act:
                x += 1
                print(f"{x} - {i}")
            una = input("PIck one from the option to run: ")
            if una == "1":
                activity_6()
            elif una == "2":
                activity_7()
            elif una == "3":
                activity_8()
            elif una == "4":
                activity_9()
            elif una == "5":
                activity_10()
            elif una == "6":
                os.system("cls")
                print("Lessons(Page 3)")
                print("Here is the overall activities that we have done")
                act = ["Activity 11", "activity 12", "activity 13","activity 14", "activity 15", "Next Page"]
                x = 0
                for i in act:
                    x += 1
                    print(f"{x} - {i}")
                una = input("PIck one from the option to run: ")
                if una == "1":
                    activity_11()
                elif una == "2":
                    activity_12()
                elif una == "3":
                    activity_13()
                elif una == "4":
                    activity_14()
                elif una == "5":
                    activity_15()
                elif una == "6":
                    os.system("cls")
                    print("Lessons(Page 4)")
                    print("Here is the overall activities that we have done")
                    act = ["Activity 16", "activity 17", "activity 18","activity 19", "activity 20", "Terminate the Program"]
                    x = 0
                    for i in act:
                        x += 1
                        print(f"{x} - {i}")
                    una = input("PIck one from the option to run: ")
                    if una == "1":
                        activity_16()
                    elif una == "2":
                        activity_17()
                    elif una == "3":
                        activity_18()
                    elif una == "4":
                        activity_19()
                    elif una == "5":
                        activity_20()
                    elif una == "6":
                        print("Terminating Program...")
                        print("Termination Complete\n\nThank you.")
                        break
    

    if uno == "3":
        print("Thank you for using my Program")
        print("Terminating Program")
        break
