numS = 2 #number of small room
numB = 3 #number of Big room
sTables = int(input('Enter number of tables in small room: '))
bTables = int(input('Enter number of tables in big room: '))

totalSmall , totalBig = numS * sTables , numB * bTables
totalTable = totalSmall + totalBig


print(f"Total Tables = {totalTable}" )