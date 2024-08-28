def to_list(list:list) -> list:
    new_list = [ lista[i] for i in range(0,len(lista),2) ]
    return new_list


def to_list2(list:list) -> list:
    new_list = [ x for x in lista[::2] ]
    return new_list

def to_list3(list:list) -> list:
    new_list = lista[::2]    
    return new_list

def to_list4(list:list) -> list:
    return lista[::2]    

lista = [1,2,3,4,5,6,7,8,9,10]
print(to_list3(lista))
