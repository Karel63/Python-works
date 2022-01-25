lives = 5
slovo1 = "_"
slovo2 = "_"
slovo3 = "_"
slovo4 = "_"
slovo5 = "_"
x = 0
while lives > 0:
    if x == 5:
        print("\n", slovo1, slovo2, slovo3, slovo4, slovo5, "\n")
        print("Zivoty =", lives)
        print("Vyhrali jste")
        break
    print("\n", slovo1, slovo2, slovo3, slovo4, slovo5, "\n")
    print("Zivoty =", lives)
    print("Zadejte pismeno: ")
    pismeno = str(input())
    if pismeno == "p":
        slovo1 = "p"
        x = x + 1
    elif pismeno == "r":
        slovo2 = "r"
        x = x + 1
    elif pismeno == "a":
        slovo3 = "a"
        x = x + 1
    elif pismeno == "s":
        slovo4 = "s"
        x = x + 1
    elif pismeno == "e":
        slovo5 = "e"
        x = x + 1
    else:
        print("Nope")
        lives = lives - 1
if lives == 0:
    print("\n", slovo1, slovo2, slovo3, slovo4, slovo5, "\n")
    print("Zivoty =", lives)
    print("Prohrali jste")
