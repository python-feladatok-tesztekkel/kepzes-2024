def fibonnaci(n:int) -> int:
    if (n==1):
        return 0
    elif (n==2 or n ==3):
        return 1
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)
    

def fibonnaci2(n:int) -> int:
    fib=[]
    if (n<=0):
        return fib
    elif (n==1 ):
        return [0]
    elif (n==2):
        return [0,1]
    fib=[0,1]
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
    return fib
   
    


print(fibonnaci2(8))