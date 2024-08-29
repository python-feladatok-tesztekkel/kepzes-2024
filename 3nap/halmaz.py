halmaz = {1,2,3,4,4,5}
ureshalmaz = set()

print(halmaz)
print(ureshalmaz)

a="az elso mondat"
b="ez a masodik szoveg"

metszet = set(a).intersection(set(b))
print(f"A közös betűk {metszet}")

csaka=set(a).difference(set(b))
csakb=set(b).difference(set(a))

print(f"Az első szövegben különböző betűk: {csaka}")
print(f"Az első szövegben különböző betűk: {csakb}")

mondat=input("Kérek egy szöveget: ")
print(len(set(mondat)))
print(len(mondat))
