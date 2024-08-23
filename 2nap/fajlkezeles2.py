szavak = []
szohosszak = []
with open("2nap\\szavak_sms.txt") as fajl:
    for sor in fajl:
        szavak.append(sor.strip())
        szohosszak.append(len(sor.strip()))

print(min(szavak, key=len))
print(max(szavak, key=len))
print(min(szohosszak))
print(max(szohosszak))

print(len(min(szavak, key=len)))
print(len(max(szavak, key=len)))

avg = sum(szohosszak)/len(szohosszak)
print(avg)

avg = 0
for szo in szavak:
    avg += len(szo)
avg /= len(szavak)
print(avg)


avg = sum(len(szo) for szo in szavak) / len(szavak)
print(avg)
