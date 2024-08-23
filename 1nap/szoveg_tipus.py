nev = "Gipsz Jakab"
print(nev)
print(nev[2])
print(nev[2:7])
print(nev[:3])
print(nev[3:])
print(nev[:-3])
print(nev[-3:])
print(nev[2:8:2])
print(nev[:])
print(nev[::2])
print(nev[::-1])

# nev[0] = M
mipsz = "M"+nev[1:]
print(mipsz)

nagynev = mipsz.upper()
print(nagynev)

kisnev = mipsz.lower()
print(kisnev)

csere = nev.replace("a", "e")
print(csere)

pozicio = nev.find(" ")
print(pozicio)
pozicio = nev.find("a")
print(pozicio)
pozicio = nev.find("g")
print(pozicio)

print(nev.split())
print(nev.split("a"))

print("Gipsz"+" "+"Jakab")
