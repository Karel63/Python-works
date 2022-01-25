t = input()
print ("Zadejte kolik čísel:", int(t))
print("Zadejte jakých", int(t), "čísel: ")
Cisla = [4, 8, 7, 3, 2]
Cislo = len(Cisla)
for x in range(Cislo - 1):
    for y in range(Cislo - 1 - x):
        if Cisla[y] > Cisla[y + 1]:
            Cisla[y], Cisla[y + 1] = Cisla[y + 1], Cisla[y]
print(Cisla)
