gyumolcsok = ["alma", "eper", "banán",
              "sárgadinnye", "narancs", "feketeribizli", "dió"]

print(sorted(gyumolcsok))
print(sorted(gyumolcsok, key=len))
print(sorted(gyumolcsok, key=len, reverse=True))

szamok = [4, 3, 8, 6, 2]
print(min(szamok))
print(min(szamok))
print(min(gyumolcsok))
print(max(gyumolcsok))

print(min(gyumolcsok, key=len))
print(max(gyumolcsok, key=len))
