x = int(input("enter number: "))
sum= 0

for x in range (1, x+1, 2):
    print(f"{x}")
    sum += x

print(f"sum is {sum}")