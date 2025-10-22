myDict = {'Year': 1 , 'Sem':1, 'Code':"IT1x14" }
print(f'(a) { myDict }')

print(f'(b) No. of items in dict = {len(myDict)}')

myDict['Credit'] = 4 #add a key Credit with value 4
print(f'(c) {myDict}')

#2 methods of getting value
print(f'(d)\tCode is { myDict.get('Code') }')
print(f'\tSem is { myDict['Sem'] }')

#remove item
del(myDict['Sem'])
print(f'(e) {myDict}')

myDict['Code'] = 'IT1x54' #change value of item
print(f'(f) {myDict}')

if('Code' in myDict): #check whether key in Dictionary
    print(f'(g) Found Code in key, value = {myDict['Code']}')

print('(h)')
for x in myDict: # x gets the key
    print(f'\t{x} - {len(x)}')

print('(i)')
for x, y in myDict.items(): # x gets the key, y gets value
    print(f'\tKey={x} , value = {y}')
    
myDict.clear() # or myDict = {}
print(f'(j) {myDict}')