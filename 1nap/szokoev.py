ev = int(input("Adjon meg egy évszámot: "))

if (ev % 4 == 0 and ev % 100 != 0) or (ev % 400 == 0):
    print("Szököév.")
else:
    print("Nem szökőév.")

if ev % 400 == 0:
    print("Szökőév.")
elif (ev % 4 == 0):
    if (ev % 100 == 0):
        print("Nem szököév.")
    else:
        print("Szökőév.")
else:
    print("Nem szökőév.")
