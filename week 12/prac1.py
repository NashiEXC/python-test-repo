myList = ['Mon','Tue','Wed','Thur','Fri']
print(f'(a) {myList}')

print(f'(b) No. of items in list = {len(myList)}')

myList.append('Sat')
myList.append('Sun')
print(f'(c) {myList}')

print(f'(d) 5th item: {myList[4]}')

myList.pop(4) #remove 5th item, index 4
print(f'(e) {myList}')

myList.remove('Tue') #Remove 1st ‘Tue’ found
print(f'(f) {myList}')

myList[1]='NewValue' #change value of 2nd item
print(f'(g) {myList}')

if 'Sun' in myList: #check item in list?
    print(f'(h) Found Sun in the list')

print('(i)')
for x in myList:
    print(f'\t{x} - {len(x)}')
    
myList.clear() # or myList = []
print(f'(j) {myList}')