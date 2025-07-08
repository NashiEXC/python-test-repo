#list storing name, age, height (m)
myList=[ ['mick',18,1.7],
        ['jade',22,1.55],
        ['sota',16,1.77] ]

myDict = {'mick': { 'age':18, 'height': 1.7},
        'jade': { 'age':22, 'height': 1.55},
        'Sota': { 'age':16, 'height': 1.77}}

print('Getting values from nested List in a loop')
for rec in myList:
    print(f'name = {rec[0]}, age = {rec[1]}, height = {rec[2]}')

print(f'\nGetting an age using [] in nested List : {myList[1][1]}')

print('\nGetting value from nested Dict in a loop')
for key,value in myDict.items():
    print(f'name = {key}, age = {value['age']}, height = {value['height']}')
    
print(f'\nGetting an age using [] in nested Dict : {myDict['jade']['age']}')