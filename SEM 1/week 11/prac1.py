string= input("Enter String: ")

print(f"length: {len(string)}")

if(string[-1] == '.'):
    print("It ends in a full stop")
else:
    print("it does not end in a full stop")

index=0
for char in string:
    print('position', index, ':',char)
    index += 1

