text= input("enter text: ")

print('length:', len(text))

if(text.isdigit()):
    print("digits only")
elif(text.isalpha()):
    print("alphabets only")
elif(text.alnum):
    print("alphanumeric")

if(text.islower()):
    print('All lowercase ')
if(text.isupper()):
    print('all uppercase')