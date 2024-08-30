with open("4nap\\nora.txt","r",encoding="utf-8") as f:
    szavak = f.read().split()

print(szavak)
print(szavak[1])

with open("4nap\\nora.txt","r",encoding="utf-8") as f:
    for sor in f:
        print(sor)

sorok=[]
with open("4nap\\nora.txt","r",encoding="utf-8") as f:
    for sor in f:
        sorok.append(sor.split())

print(sorok)
print(sorok[1])

sorok=[]
with open("4nap\\nora.txt","r",encoding="utf-8") as f:
    for sor in f:
        sorok+=sor.split()

print(sorok)
print(sorok[1])

sorok=[]
with open("4nap\\nora.txt","r",encoding="utf-8") as f:
    for sor in f:
        sorok+=[sor.split()]

print(sorok)
print(sorok[1])