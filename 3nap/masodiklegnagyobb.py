def masodiklegnagyobb(lista:list)->int:
    legnagyobb=max(lista)
    lista.remove(legnagyobb)
    return max(lista)

lista=[3,5,2,7,3]
masolat=list(lista)

print(masodiklegnagyobb(lista))
print(masolat)
