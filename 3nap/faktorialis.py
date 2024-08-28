def fakt(n:int) -> int:
    """Faktoriális számítás

    Args:
        n (int): Ennek a számnak a faktiriálisát számítjuk_

    Returns:
        int: _A kiszámolt faktoriális
    """    ''''''
    if (n==1):
        return 1
    else:
        return n*fakt(n-1)

print(fakt(5))


def fakt2(n:int) -> int:
    szorzat = 1
    for szam in range(1,n+1):
        szorzat *=szam
    return szorzat

print(fakt2(5))
