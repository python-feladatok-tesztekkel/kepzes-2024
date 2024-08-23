import random


def felfedes(tipp: str, rejtett: str) -> str:
    valasz: str = ""
    for i in range(0, len(rejtett)):
        if (len(tipp) > i and tipp[i] == rejtett[i]):
            valasz += rejtett[i]
        else:
            valasz += "."
    return valasz


def felfedes2(tipp: str, rejtett: str) -> str:
    valasz: str = ""
    for t, r in zip(tipp, rejtett):
        if t == r:
            valasz += r
        else:
            valasz += "."


def felfedes3(tipp: str, rejtett: str) -> str:
    valasz: str = ""
    if (len(tipp) < len(rejtett)):
        tipp = tipp.ljust(len(rejtett)-len(tipp))
    print(f"'{tipp}'")
    for i in range(0, len(rejtett)):
        ujkar = rejtett[i] if tipp[i] == rejtett[i] else "."
        valasz += ujkar
    return valasz


def osszevon(eddigi: str, uj: str) -> str:
    valasz: str = ""
    for i in range(0, len(eddigi)):
        if len(uj) > i and uj[i] != ".":
            valasz += uj[i]
        else:
            valasz += eddigi[i]
    return valasz


szavak = ["fuvola", "csirke", "adatok", "asztal", "fogoly", "bicska", "farkas",
          "almafa", "babona", "gerinc", "dervis", "bagoly", "ecetes", "angyal", "boglya"]

tipp: str = ""
eredmeny: str = "......."
osszevonva: str = "......."
rejtett: str = random.choice(szavak)

print(rejtett)

while rejtett != eredmeny:
    tipp = input("Kérem a tippet: ")
    eredmeny = felfedes3(tipp, rejtett)
    print(f"Az eredmény:{eredmeny}")
    osszevonva = osszevon(osszevonva, eredmeny)
    print(f"Összevont eredmény: {osszevonva}")
