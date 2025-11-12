ame = input("Hi,what is your name? ")

print("********************")
print("\nODD NUMBER SELECTOR,PRESS 0 TO STOP")
print("\n********************")


oddnm = True
odd = " "
sum = 0

while oddnm == True:
   num = eval(input("enter a random number"))

   if num % 2 == 1:
      print("ODD NUMBER  DETECTED")
      sum += num
      odd += str(num) + " "
      continue
   elif num == 0:
