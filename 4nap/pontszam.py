pontszam = int(input("Adja meg a dolgozat pontszámát: "))

elegtelen = range(0,50)
elegseges = range(50,60)
kozepes = range(60,70)
jo = range(70,85)
jeles = range(85,101)

match pontszam:
    case pontszam if pontszam in elegtelen:
        print("Elégtelen")
    case pontszam if pontszam in elegseges:
        print("Elégséges")
    case pontszam if pontszam in kozepes:
        print("Közepes")
    case pontszam if pontszam in jo:
        print("jó")
    case pontszam if pontszam in jeles:
        print("Jeles")
    case _:
        print("Ennyi pontra nem értékelhető")