file = open("3nap\\nora_UTF8.txt","r",encoding="UTF-8")

#szavak=set()
#for sor in file:
#    osszesszavak=sor.strip().split()
#    for szo in osszesszavak:
#        szavak.add(szo.lower())

szavak=set(file.read().split())

file.close()

print(f"{len(szavak)} különböző szó fordul elő!")

rendezett_szavak=sorted(szavak)
print(rendezett_szavak[:10])

file_ki=open("3nap\\szavak.txt","w",encoding="UTF-8")
for szo in rendezett_szavak:
    file_ki.write(szo+"\n")