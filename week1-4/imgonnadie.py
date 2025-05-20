totalsec = int(input("enter seconds: "))

hr = totalsec // 3600
min= (totalsec//60) % 60 #or minute = (totalsec - (hr*3600)) // 60
sec = totalsec % 60

print(f"{totalsec} is {hr} hours, {min} minutes and {sec} secpnds")