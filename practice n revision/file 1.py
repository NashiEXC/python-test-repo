# ok what am i weak in?
# while loop not that good
# string slicing, slicing in general
# List tuples n dictionaries
# Funcs and Modules
prev = 0

curr = 1

size = int(input('Enter the number: '))

print( f' {prev} {curr}', end= ' ')

for num in range(2,size):

   # store previous number

   temp = prev

   # current number becomes previous

   prev = curr

   # curr is sum of last 2 numbers

   curr = temp + curr

   print(curr, end= ' ')