file = open("4nap\\nora_UTF8.txt","r",encoding="utf-8")
szavak=file.read().split()
rendezett_szavak=sorted(szavak)
file.close()

file_out=open("4nap\\rendezett.txt","w",encoding="utf-8")
for szo in rendezett_szavak:
    file_out.write(szo+"\n")
file_out.close()

szavak2=[]
for szo in szavak:
    if len(szo)>1:
        szavak2.append(szo)



utolso_elotti_rendezett_szavak=sorted(szavak2,key=lambda szo: szo[-2])

file_out=open("4nap\\utolsoelotti.txt","w",encoding="utf-8")
for szo in utolso_elotti_rendezett_szavak:
    file_out.write(szo+"\n")
file_out.close()