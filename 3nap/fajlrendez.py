with open("3nap\\nora_UTF8.txt","r",encoding="utf-8") as befajl:
    szavak=befajl.read().split()

rendezett = sorted(szavak)

with open("3nap\\rendezett.txt","w",encoding="utf-8") as kifajl:
    #kifajl.write(str(rendezett))
    for szo in rendezett:
        kifajl.write(szo+"\n")

