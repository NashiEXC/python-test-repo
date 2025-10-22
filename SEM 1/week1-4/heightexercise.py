import random as r
heighttotalcm = r.randint(1, 199)
hmeter = heighttotalcm // 100
hCm = heighttotalcm % 100

print(f"height {heighttotalcm} is " ,end='')
print(f"{hmeter}m and {hCm}cm")