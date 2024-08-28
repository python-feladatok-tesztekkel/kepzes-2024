def minmax(adatok:list) -> tuple:
    if (not isinstance(adatok,list)):
        return None
    else:
        return (max(adatok),min(adatok))
    
print(minmax([3,1,6,9,3,2]))
print(minmax(["c","b","s","a"]))    