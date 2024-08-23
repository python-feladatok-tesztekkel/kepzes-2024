fajl = open("2nap\szavak_sms.txt")
for sor in fajl:
    print(sor, end="")

fajl.close()


with open("2nap\szavak_sms.txt") as fajl:
    for sor in fajl:
        print(sor, end="")

sorok = []
with open("2nap\szavak_sms.txt") as fajl:
    for sor in fajl:
        sorok.append(sor.strip())
print(sorok)


keresett = "teker"
sorok = []
with open("2nap\szavak_sms.txt") as fajl:
    for sor in fajl:
        sorok.append(sor.strip())

if keresett in sorok:
    print("A szó benne a van a fájlba.")
else:
    print("A szó nincs a fájlban.")
