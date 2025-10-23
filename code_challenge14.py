anime_list = [ ]

anime = True
while anime == True:
    list = input("Enter an anime (or type \"exit\" to stop): ")

    if list == "Exit":
        print("You have exited the anime entry program")
        break
    else:
        anime_list.append(list)
        continue
print("Here is the list of animes you typed: ")
for a in anime_list:
    print(f"-{a}")
