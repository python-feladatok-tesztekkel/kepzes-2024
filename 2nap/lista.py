diakok = ["Anna", "Barna", "Cili", "Dani", "Eleonóra"]
print(diakok)
print(diakok[3])

for diak in diakok:
    print(diak, end=" ")

print()
print(diakok[2:4])
print(diakok[:4])
print(diakok[2:])

diakok.append("Ferenc")
diakok.insert(2, "Bea")
diakok.remove("Barna")

while "Barna" in diakok:
    diakok.remove("Barna")
valaki = diakok.pop()

del diakok[4]

rendezett = sorted(diakok)
rendezett = sorted(diakok, reverse=True)

diakok.sort()

diakok.sort(reverse=True)
