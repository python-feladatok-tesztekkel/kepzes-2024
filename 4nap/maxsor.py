fajl = open("4nap\\nora_UTF8.txt","r",encoding="UTF-8")
sorok=fajl.read().split("\n")
fajl.close()
print(sorok[:5])

hosszak=[]
for sor in sorok:
    hosszak.append(len(sor.split()))

leghosszabb=max(hosszak)

def szavak_szama(szoveg:str):
    return len(szoveg.split())

for sor in sorok:
    if (len(sor.split())==leghosszabb):
        print(f"A sor hossza {leghosszabb}:\n{sor}")


print()
print(max(sorok,key=szavak_szama))