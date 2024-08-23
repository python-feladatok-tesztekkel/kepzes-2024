with open("2nap\\nora_UTF8.txt", "r", encoding="utf-8") as fajl:
    szavak = fajl.read().split()

print(szavak)

hossz = {}
for szo in szavak:
    hossz[szo] = len(szo)

gyakorisag = {}
for szo in szavak:
    if (szo in gyakorisag):
        gyakorisag[szo] += 1
    else:
        gyakorisag[szo] = 1

# for kulcs, ertek in gyakorisag.items():
#    print(f'{kulcs} {ertek}')


leggyakoribb_szo = max(gyakorisag, key=gyakorisag.get)
leggyakoribb_szo = max(gyakorisag.values())
print(leggyakoribb_szo)
print(gyakorisag["a"])
