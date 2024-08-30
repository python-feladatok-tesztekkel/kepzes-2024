def szamjegyek_osszege(szamjegy:str)->int:
    osszeg=0
    for jegy in szamjegy:
        if (jegy.isdigit()):
            osszeg+=int(jegy)
    return osszeg

def eletszam(datum) ->str:
    while(len(datum) >1 ):
        datum = str(int(sum(int(szamjegy) for szamjegy in datum)))
    return datum


szuletesnap=input("Adja meg a születésnapját szám formátumban: ")
szuletesnap_jegyosszeg=szamjegyek_osszege(szuletesnap)

#eletszam=szamjegyek_osszege(str(szuletesnap_jegyosszeg))
print("Életszam: "+eletszam(szuletesnap))

