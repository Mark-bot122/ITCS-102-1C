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
