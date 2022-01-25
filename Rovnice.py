a = float(input())
b = float(input())
c = float(input())

#Zde se vypíše žablona
print("Kvardratická rovnice ve tvaru: ax**2 + bx + c = 0")

#Zde se Vypíšou zadané hodnoty
print("Zadané hodnoty: A =", float(a),", B =", float(b),", C =", float(c))

#Pokud bude discriminant menší než 0, napíše to že rovnice nemá řešení
if a < 0:
    print("Řešení: Nemá řešení")


#Zde se vypočítá discriminant
D = b**2 - 4 * a * c

#Pokud bude discriminant menší než 0, napíše to že rovnice nemá řešení
if D < 0:
    print("Řešení: Nemá řešení")

#Pokud se bude disriminant rovnat 0, vypočítá se x
elif D == 0:
    X = -b / (2 * a)
    print("Řešení: X =", float(X))

#Pokud bude discriminant větší než 0, vypočítá se X1 a X2
else:
    Xa = (-b - D**0.5) / 2 * a
    Xb = (-b + D**0.5) / 2 * a
    print("Řešení: X1 =", float(Xa),", X2 =", float(Xb))
