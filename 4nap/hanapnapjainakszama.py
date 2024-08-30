harmincas = {4, 6, 9, 11}
harmineegyes = {1,3,5,7,8,10,12}

honap = int(input("Kérek egy hónapt:"))

match honap:
    case x if x in harmincas:
        print(f"A {honap}. hónap harminc napos!")
    case x if x in harmineegyes:
        print(f"A {honap}. hónap harmincegy napos!")
    case 2:
        print(f"A {honap}. 28 vagy 29 napos!")
    case _:
        print("Nem hónap számot adott meg!")
        