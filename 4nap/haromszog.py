n = int(input("Add meg a sorok számát: "))
kozep=n-1
print(kozep)

for sor in range(n):    
    poziciok=[]
    match sor:
        case 0:
            poziciok.append(kozep)
        case sor if sor == n-1:
            poziciok=range(2*n)
        case sor if sor in range(1,n):
            poziciok.append(kozep-sor)
            poziciok.append(kozep+sor)
    for oszlop in range(2*n-1):
        if oszlop in poziciok:
            print("*",sep="",end="")
        else:
            print(".",sep="",end="")
    print("\n")
        


