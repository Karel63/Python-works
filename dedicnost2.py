import os
import math

class Bod:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def nastavSouradnice(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"[{self.x},{self.y}]"

    def get_y(self):
        print(self.y)    

    def get_x(self):
        print(self.x) 

class Usecka:

    def __init__(self, u=0, v=0, x=0, y=0):
        self.__a = Bod(u, v)
        self.__b = Bod(x, y)
    
    def nastavSouradnice(self, u, v, x, y):
        self.__a.nastavSouradnice(u, v)
        self.__b.nastavSouradnice(x, y)

    def __str__(self):
        return  f"[{self.__a.x},{self.__a.y}][{self.__b.x},{self.__b.y}]"

    def delkaUsecky(self):
        return math.sqrt(math.pow(self.__a.x - self.__b.x, 2) + math.pow(self.__a.y - self.__b.y, 2))

    def get_A(self):
        print(self.__a)

    def get_B(self):
        print(self.__b)

B = Bod()
B.nastavSouradnice(1, -2)
print(B)

U = Usecka(1, 3, 4, -1)
print(U)
print(f"{U.delkaUsecky():.2f}")

B.get_y()
B.get_x()
U.get_A()
U.get_B()
