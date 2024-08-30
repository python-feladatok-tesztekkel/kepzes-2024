def isinteger(s:str) -> int:
    if (len(s)==0):
        return False
    elif s.isdecimal():
        return True
    elif s[0] in '+-':
        return s[1:].isdecimal()
    else:
        return False
    
while(True):
    szam=input("Adjon meg egy egész számot: ")
    if (szam.lower()=="stop")
        break
    elif isinteger(szam):
        szam=int(szam)
        break
    else:
        print("A megadott adat nem egész szám!")

    if (type(szam)==int):
        print(f"A szám {szam} megfelelő!")