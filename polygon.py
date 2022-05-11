class Polygon:

    def numOfSides(self):
        pass

class Triangle(Polygon):

    def numOfSides(self):
        print("Triangle has 3 sides")

class Pentagon(Polygon):

    def numOfSides(self):
        print("Polygon has 5 sides")

class Octagon(Polygon):

    def numOfSides(self):
        print("Octagon has 8 sides")

T = Triangle()
T.numOfSides()

O = Octagon()
O.numOfSides()

P = Pentagon()
P.numOfSides()
