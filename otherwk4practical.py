ip = input('enter a number: ')
try:
    ipf = float(ip)
except ValueError:
    print("%s is not a valid number" % (ip))
else:
    print("%s is not a valid number" % (ip))
    print("program exit with no exceptions raised")