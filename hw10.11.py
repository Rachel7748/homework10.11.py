import math
class Radius:

    def __init__(self, radius, hekef, area):
        self.radius = radius
        self.hekef = hekef
        self.area = area

    def __str__(self):
        return f'radius:{self.radius}, hekef:{self.hekef}, area:{self.area}'

radius =(5)
hekef = int(2 * math.pi * radius)
area = int(math.pi * radius ** 2 )

print('radius:', radius)
print('hekef: ',hekef)
print('area:', area)




