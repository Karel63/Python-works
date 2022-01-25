"""dělitelný 4, nedělitelný 100 = přestupný
dělitelný 4 a 100, nedělitelný 400 = není přestupný
dělitelný 4, 100 a 400 = přestupný"""

year = int(input("Zadejte rok: "))
print(year, "\n\n")

if year % 4 == 0 and year % 100 > 0:
    print("Tento rok je přestupný")
elif year % 100 == 0 and year % 400 == 0:
    print("Tento rok je přestupný")
else:
    print("Tento rok není je přestupný")
