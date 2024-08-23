szotar = {"szia": "hello", "alma": "apple", "ablak": "window", "ajtó": "door"}

szotar["lemez"] = "disk"

szo = input("Adjon meg egy szót")
if szo in szotar:
    print(szotar[szo])
else:
    print("Nincs ez a szó!")

hossz = {}
for szo in szotar:
    hossz[szo] = len(szo)

gyakorisag = {}
for szo in szotar:
    if (szo in gyakorisag):
        gyakorisag[szo] += 1
    else:
        gyakorisag[szo] = 1

print(gyakorisag)

for kulcs, ertek in gyakorisag.items():
    print(f'{kulcs} {ertek}')
