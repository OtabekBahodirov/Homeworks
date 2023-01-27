# class Polygon:
#     # Initializing the number of sides
#     def __init__(self, no_of_sides):
#         self.n = no_of_sides
#         self.sides = [0 for i in range(no_of_sides)]

#     def inputSides(self):
#         self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

#     # method to display the length of each side of the polygon
#     def dispSides(self):
#         for i in range(self.n):
#             print("Side",i+1,"is",self.sides[i])

# class Triangle(Polygon):
#     # Initializing the number of sides of the triangle to 3 by 
#     # calling the __init__ method of the Polygon class
#     def __init__(self):
#         Polygon.__init__(self,3)

#     def findArea(self):
#         a, b, c = self.sides

#         # calculate the semi-perimeter
#         s = (a + b + c) / 2

#         # Using Heron's formula to calculate the area of the triangle
#         area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
#         print('The area of the triangle is %0.2f' %area)

        

# class RightTriangle(Triangle):
#     def __init__(self, a, b):
#         self.sides = [a, b, (a*a + b*b)**0.5]
    
#     def find_area(self):
#         a, b, _ = self.sides
#         area = (a*b)/2
#         print('The area of the right triangle is %0.2f' %area)
    
#     def find_hypotenuse(self):
#         c = self.sides[2]
#         print('The hypotenuse of the right triangle is %0.2f' %c)

# # Creating an instance of the RightTriangle class
# rt = RightTriangle(3, 4)

# # Printing the area of the right triangle
# rt.find_area()

# # Printing the hypotenuse of the right triangle
# rt.find_hypotenuse()


class Shape:
    def area(self):
        pass
    
    
# class Circumference(Shape):
#     def __init__(self, radius):
#         self.r = radius
        
#     def area(self):
#         from math import pi
#         return pi * self.r ** 2
    
#     def length(self):
#         from math import pi
#         return 2 * pi * self.r

# class Square(Shape):
#     def area(self, side):
#        return side * side
   
#     def length(self, side):
#         return 4 * side

# class Rectangle(Shape):
#     def __init__(self, a, b):
#         super().__init__()
#         return a * b

# class Triangle(Shape):
#      def __init__(self, a, b, c):
#         super().__init__()
#         from math import sqrt
#         P = a + b + c
#         p = P / 2
#         return sqrt(p*(p-a)*(p-b)*(p-c))
    
    
# t = Triangle()
# print(t.area(3, 4, 5))

# r = Rectangle()
# print(r.area(5, 10))

# c = Circumference(5)
# print(c.area())
# print(c.length())



# class Paralelogram(Shape):
#     def __init__(self, a , b):
#         self.a, self.b = a, b
#         self.angle = 0

#     def area(self):
#         from math import sin, radians
#         if self.angle == 0:
#           self.angle = int(input('Enter angle between a and b sides'))

#         return self.a * self.b * sin(radians(self.angle))
        

# class Rectangle(Paralelogram):
#     def  __init__(self, a, b):
#         super().__init__(a, b)

# class Rhombus(Paralelogram):
#     def __init__(self, a,):
#         super().__init__(a, a)


# class Square(Rhombus):
#     def __init__(self, a):
#         super().__init__(a)
#         self.angle = 90


# Mohirdev Darslari

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self, ism, familya, pasport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familya
        self.pasport = pasport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida Ma'lumot"""
        info = f"{self.ism} {self.familiya}. "
        info += f"Pasport: {self.pasport}, {self.tyil}"
        return info
    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil

class Talaba(Shaxs):
    """Talaba klasi"""
    def __init__(self, ism, familya, pasport, tyil, idraqam, manzil):
        super().__init__(ism, familya, pasport, tyil)
        self.idraqam = idraqam 
        self.bosqich = 1
        self.manzil = manzil

    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida Ma'lumot    bu uslub polimorfizim deyiladi"""
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.get_bosqich()}-bosqich. ID raqami: {self.idraqam}"
        return info


class Manzil:
    """Manzil saqlash uchun klass"""
    def __init__(self, uy, kocha, tuman, viloyat):
        """Manzil xususiyatlari"""
        self.uy = uy 
        self.kocha = kocha 
        self.tuman = tuman
        self.viloyat = viloyat


    def get_manzil(self):
        """Manzilni  ko'rish"""
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani,"
        manzil += f"{self.kocha} ko'chasi, {self.uy} - uy"
        return manzil


talaba1_manzil = Manzil(12,"Olmazor", "Romitan", "Buxoro")
talaba1 = Talaba("Muslim", "Ergashov","AF2004477", 2005, "N0005641",talaba1_manzil)
print(talaba1.manzil.get_manzil())
print(talaba1.get_info())
print(talaba1.get_age(2023))

print(talaba1_manzil)
inson = Shaxs("Otabek", "Bahodirov", "AC1234567", 2004)
print(inson.get_info())
print(inson.get_age(2023))

# class Talaba(Shaxs)