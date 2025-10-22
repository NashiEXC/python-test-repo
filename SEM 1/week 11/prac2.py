text= input("enter text: ")
filter= input("enter text to filter: ")
newtext= ""

for char in text:
    if not(char in filter):
        newtext += char

print(newtext)