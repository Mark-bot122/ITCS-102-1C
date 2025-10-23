print("ODD NUMBER ACCUMULATOR")
print("Enter 10 numbers. We'll sum only the odd ones!\n")

odd_sum = 0

for i in range(1, 11):
    num = int(input(f"Enter number {i}: "))
    if num % 2 != 0:
        odd_sum += num

print(f"\n Sum of all odd numbers: {odd_sum}")
