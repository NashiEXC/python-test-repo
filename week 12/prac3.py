text = 'Success is built on effort, and effort is key.'
wordList = text.split() # split words from sentence into a list

print(wordList)
numIs = wordList.count('is')
print(f'Num of is: {numIs}')

print(f'Last 2 words : { wordList[-2:]} ')