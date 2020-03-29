# T.C O(n*log(logn))
from math import floor,ceil,sqrt
def genPrimes(x,y):
    n = y
    primes = [True]*(n+1)
    primes[0]=primes[1]=False
    for p in range(2,ceil(sqrt(n))):
        if primes[p] == True:
            for i in range(p*p,n+1,p):
                primes[i]=False
    
    for i in range(x,y+1):
        if primes[i]==True:
            print(i,end=" ")
t = int(input())
while t:
    x,y = map(int,input().split())
    genPrimes(x,y)
    t=t-1            
