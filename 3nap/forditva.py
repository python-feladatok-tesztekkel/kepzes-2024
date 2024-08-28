def fordit(szo:str)->str:
    """_summary_

    Args:
        szo (str): _description_

    Returns:
        str: _description_
    """    
    if (type(szo)==str):
        ujszo=""
        for betu in szo[::-1]:
            if betu.isalpha():
                ujszo+=betu
            else:
                break;
        if (len(ujszo)==len(szo)):
            return ujszo
    return "Nem szöveget kaptam!"


def fordit2(szo:str)->str:
    """_summary_

    Args:
        szo (str): _description_

    Returns:
        str: _description_
    """    
    if (isinstance(szo,str)):
        ujszo=""
        for betu in szo[::-1]:
            if betu.isalpha():
                ujszo+=betu
            else:
                break;
        if (len(ujszo)==len(szo)):
            return ujszo
    return "Nem szöveget kaptam!"


print(fordit("hello"))