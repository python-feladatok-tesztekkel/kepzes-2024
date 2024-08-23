for szam in range(1, 100):
    if (szam % 3 == 0):
        print("s", end=" ")
    else:
        print(szam, end=" ")

print()
print()

for szam in range(1, 100):
    if (szam % 3 == 0) or (szam % 5 == 0):
        print("s", end=" ")
    else:
        print(szam, end=" ")

print()
print()

for szam in range(1, 110):
    adat = str(szam)
    if (szam % 3 == 0 or adat.find("3") >= 0):
        print("s", end=" ")
    else:
        print(szam, end=" ")

print()
print()

for szam in range(1, 110):
    adat = str(szam)
    if (szam % 3 == 0 or "3" in adat):
        print("s", end=" ")
    else:
        print(szam, end=" ")


# rekurziv algoritmus osztás vagy osztási maradék (utolsó számjegy, többi számjegy)
