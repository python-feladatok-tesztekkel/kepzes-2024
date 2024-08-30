honap = int (input("Add meg a hónap számát: "))

match honap:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f"A {honap}. honap 31 napos")
    case 4 | 6 | 9 | 11:
        print(f"A {honap}. honap 30 napos")
    case 2:
        print(f"A {honap}. honap 28 napos (szökőévben 29)")
    case _:
        print(f"{honap} számmal nem létezik hónap.")