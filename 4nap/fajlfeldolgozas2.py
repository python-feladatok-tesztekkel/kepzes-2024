fajl = open("4nap\\nora_UTF8.txt","r",encoding="UTF-8")
#sorok = fajl.readlines()
sorok = fajl.read().split("\n")
fajl.close()

rendezett = sorted(sorok,key=len)
fajl_out=open("4nap\\hossz.txt","w",encoding="UTF-8")
for sor in rendezett:
    fajl_out.write(sor+"\n")
fajl_out.close()