import os
import math

class Bod:
    
    def __init__(self, B: dict):
        self.souradnice = B

    def nastavSouradnice(self, x, y):
        self.souradnice["x"] = x
        self.souradnice["y"] = y

    def __str__(self):
        return "[{},{}]".format(self.souradnice["x"], self.souradnice["y"])
        
    def get_y(self):
        print(self.souradnice["x"])  

    def get_x(self):
        print(self.souradnice["y"])

class Usecka:

    def __init__(self, A: Bod, B: Bod):
        self.__a = A
        self.__b = B
    
    def nastavSouradnice(self, A: dict, B: dict):
        self.__a.nastavSouradnice(A["x"], A["y"])
        self.__b.nastavSouradnice(B["x"], B["y"])

    def __str__(self):
        return  "[{},{}][{},{}]".format(self.__a.souradnice["x"], self.__a.souradnice["y"], self.__b.souradnice["x"], self.__b.souradnice["y"])

    def delkaUsecky(self):
        return math.sqrt(math.pow(self.__a.souradnice["x"] - self.__b.souradnice["x"], 2) + math.pow(self.__a.souradnice["y"] - self.__b.souradnice["y"], 2))

    def get_A(self):
        print(self.__a)

    def get_B(self):
        print(self.__b)

B = Bod({"x": 1, "y": -2})
print(B)

D = Bod({"x": 1, "y": 3})
E = Bod({"x": 4, "y": -1})
U = Usecka(D, E)
print(U)
print(f"{U.delkaUsecky():.2f}")

B.get_y()
B.get_x()
U.get_A()
U.get_B()
