print("\t\t *", end="")
for x in range(1,11,1):
    for z in range(10,x,-1):
        print(" ", end=" ")
    for y in range(1,x,1):
        print("*", end=" ")
    for i in range(1,x,1):
        print("1", end= " ")
    print()

#2nd half
for x in range(1,11,1):
    for n in range(1,x,1):
        print(" ", end=" ")
    for m in range(10,x,-1):
        print("*", end=" ")
    for g in range(10,x,-1):
        print("*", end=" ")
    print("*")
