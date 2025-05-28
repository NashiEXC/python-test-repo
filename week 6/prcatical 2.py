i=int(input("enter a number:"))
sum=0

while (i>0):
    sum += i
    i = int(input("enter a number:"))

if i <= 0:
    print(f"sum is {sum}")
