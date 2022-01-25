import random
random.seed()
treasure = random.choice(range(10))
y = 3
x = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
print("Najděte poklad!\n")
while y != 0:
	print(x)
	print("Životy:", y)
	cislo = int(input("Zadejte číslo: "))
	print(cislo)
	if x[cislo] == "_":
		print("Toto číslo už jste zadali\n")
		continue
	if cislo == treasure:
		x[cislo] = "*"
		print("\n")
		print(x)
		print("Životy:", y)
		print("Našli jste poklad!")
		break
	else:
		print("Nic jste nenašli...\n")
		x[cislo] = "_"
		y = y - 1
if y == 0:
	x[cislo] = "_"
	print(x)
	print("Životy:", y)
	print("Prohráli jste!")
	print("Poklad byl na pozici:", treasure)
