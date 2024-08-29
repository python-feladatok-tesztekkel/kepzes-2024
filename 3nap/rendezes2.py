def maradek(szam: int)->int:
    return szam%5

szamok=[24,17,30,41,14]

print(sorted(szamok))
print(sorted(szamok,key=maradek))


def valodi_osztok(szam:int) -> int:
    darab=0
    for i in range(2,szam):
        if (szam % i == 0):
            darab+=1
    return darab

szamok=[9,28,23,96,5]
print(sorted(szamok,key=valodi_osztok))

szamok=[24,17,30,41,14]
print(sorted(szamok,key=lambda szam: szam % 5))


szavak = ['sárgarépa','alma','Gesztenye']

print(sorted(szavak))

print(sorted(szavak,key = lambda szó: szó.lower()))