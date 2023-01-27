# class Vehicle:
#     def __init__(self, manufacturer, year, km):
#         self.manufacturer = manufacturer
#         self.year = year
#         self.km = km

#     def drive(self, km):
#         if km <= 0: raise ValueError('Distance could not be negative or equal to Zero')
#         self.km += km



# bmw = Vehicle('BMW', 2022, 0)
# bmw.drive(2)
# bmw.drive(12)


# class GMVehicle(Vehicle):
#     color = 'White'
#     def __init__(self, year, km, manufacturer = "GM"):
#         Vehicle.__init__(self, manufacturer, year, km)

#     def breakk(self):
#         print('I am broken')

# matiz = GMVehicle(2006,99999)
# matiz.drive(1)
# print(matiz.km)
# matiz.breakk()
# print(matiz.manufacturer)


# class Animal:
#     def __init__(self, color, voice,type, eating, legs):
#         self.color = color
#         self.voice = voice
#         self.type = type
#         self.eating = eating
#         self.legs = legs


# class Mammals(Animal):
#     color =  "oq"
#     def __init__(self, color, voice, type, eating, legs):
#         super().__init__(color, voice, type, eating, legs)


# cat = Animal('oq','miyov', 'mushuksimonlar & sut emizuvchi  ', 'sut & non & go\'sht', '4 oyoqli')
# print(cat.color)
# print(cat.type)
# print(cat.legs)

# Homo = Mammals('oq tanli','hello','inson & sut emizuvchi',"Tirik jonzotlar va o'simliklar", '2 oyoqli')
# print(Homo.type)
# print(Homo.eating)
# print(Homo.legs)

class Polygon:
    sides = []
    def __init__(self, n):
        self.n = n
        self.inputSides()

    def  inputSides(self):
        self.sides = [float(input("Enter side" + str(i + 1)+ " : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side", i + 1 , "is", self.sides[i])

triangle = Polygon(3)
print(triangle.sides)
triangle.inputSides()
print(triangle.sides)
triangle.dispSides(0)