def cipher(file = " ", keyword = " "):
    with open(file) as main:
        text = main.read()
        print(text)
        text2 = ""
        alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n = 0
        n2 = 1
        for char in text.upper():
            if char != " ":
                if n >= len(keyword):
                    n = 0
                for letter in alph:
                    if letter == keyword[n].upper():
                        number1 = n2
                    if letter == char:
                        number2 = n2
                    n2 += 1
                number = number1 + number2
                if (number1 + number2) >= len(alph):
                    number = (number1 + number2) - len(alph)
                text2 += alph[number - 1]
                n += 1
                n2 = 1
        main.close()
    
    with open("cipher/ciphered.txt", "a") as c:
        c.write(text2)
        c.close()

def decipher(file = " ", keyword = " "):
    with open(file) as main:
        text = main.read()
        text2 = ""
        alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n = 0
        n2 = 1
        for char in text.upper():
            if char != " ":
                if n >= len(keyword):
                    n = 0
                for letter in alph:
                    if letter == keyword[n].upper():
                        number1 = n2
                    if letter == char:
                        number2 = n2
                    n2 += 1
                number = number2 - number1
                if (number2 - number1) < 0:
                    number = (number2 - number1) + len(alph)
                text2 += alph[number - 1]
                n += 1
                n2 = 1
        print(text2)
    main.close()

    with open("cipher/deciphered.txt", "a") as d:
        d.write(text2)
        d.close()

cipher("cipher/text.txt", "abcdz")
decipher("cipher/ciphered.txt", "abcdz")