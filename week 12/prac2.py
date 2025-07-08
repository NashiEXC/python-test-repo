visitorList = [] # create empty list
NoDays = int(input('Enter days of exhibition: '))
# set up the loop to repeat
for x in range( 1, NoDays+1):
    visitors = int(input(f'Day {x} visitors: '))
    visitorList.append(visitors)
# use Built-in function to find these values
print('\nLowest number of visitors:', min(visitorList))
print('Highest number visitors:', max(visitorList))
print('Total number of visitors:', sum(visitorList))
avg = sum(visitorList)/len(visitorList)
print('Average number of visitors:', avg)