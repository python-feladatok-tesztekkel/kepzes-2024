
def to_decimal(hexa:str)->tuple:
    red=hexa[1:3]
    green=hexa[3:5]
    blue=hexa[5:7]
    redDec=int(red,base=16)
    greenDec=int(green,base=16)
    blueDec=int(blue,base=16)
    return redDec,greenDec,blueDec


hexa="#abcd12"

print(to_decimal(hexa))

