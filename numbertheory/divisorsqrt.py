import math
from math import sqrt,ceil
def sqrtdivisors(n):
    ls=[]
    ls1=[]
    for i in range(1,ceil(sqrt(n))):
        if(n%i==0):
            if(n%i==i):
                ls1.append(i)
            else:
                ls1.append(i)
                ls.append(n/i)
    ls1+=ls[::-1]
    return(ls1)
while True:
    try:
        n=int(input("Enter number:    "))
        print(sqrtdivisors(n))
    except:
        print("Invalid input!")
        break