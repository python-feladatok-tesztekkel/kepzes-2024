szavak=[]
with open("3nap\\nora_UTF8.txt","r",encoding="UTF-8") as befajl:
    szavak.append([sor.split() for sor in befajl])

print(szavak[:20])