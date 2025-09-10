input("Welcomd to anime recomender")
genre = input("What genre would you like?(music,action,romance) ")
length = input("Do you prefer short,medium,or long manga? ")
time = input("Publication date?(2000,2015) ")

gnr = genre
lng = length
tm = time

if gnr == "action" and tm == "2000" and lng == "long":
	print("Read Naruto \n Shingeki no Kyojin")
	
elif gnr == "action" and tm == "2015" and lng == "medium":
		print("Read Assassination classroom")

elif gnr == "action" and tm == "2015" and lng == "short":
	print("Fire force")

elif gnr == "music" and tm == "2015" and lng == "medium":
	print("BOCCHI THE ROCK,READ IT VRO ITS PEAK")

elif gnr == "romance" and tm == "2015" and lng == "medium":
	print("Kaguya-sama Love is War")

else:
	print("No manga yet...")
