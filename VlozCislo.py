vstup = int(input("Vlož číslo: \n"))
print("vložené číslo:", vstup, "\n")

def funkce(x):
    return x % 2 == 0 or x % 3 == 0 or x % 5 == 0

if funkce(vstup):
    print("Číslo je násobkem alespoň jednoho z čísel 2, 3, 5.")
else:
    print("Číslo není násobkem žádného z čísel 2, 3, 5.")
