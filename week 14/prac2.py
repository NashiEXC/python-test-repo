def areaCircle( r ):
    area = 3.142 * r ** 2
    return (area)

radius1 = 10
radius2 = 20

print("Area of Circle")
print(f'\tradius {radius1} = {areaCircle(radius1):.2f}')
print(f'\tradius {radius2} = {areaCircle(radius2):.2f}')