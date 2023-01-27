class  Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age * 7

class BritishCat:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        self.breed = 'British Shorthair'


pet1 = Dog("Tuzik", 2)
pet2 = Dog("Bobik", 5)
pet3 = BritishCat("Marusya", 2)
print(pet1.name)
print(pet2.age)
print(pet3.breed)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point1 = Point(4, 4)
point2 = Point(6, 2)

class Line:
    def __init__(self, p1, p2):
        self.x1 = p1.x
        self.x1 = p2.x
        self.y1 = p1.y
        self.y2 = p2.y
        self.lenght = ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


    def shift_x(self, add):
        self.x1 += add
        self.x2 += add
    

line = Line(point1,point2)
print(line.x1, line.x2)
line.shift_x(-1)
print(line.x1, line.x2)