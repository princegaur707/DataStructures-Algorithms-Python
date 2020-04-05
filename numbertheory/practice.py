from math import ceil,sqrt
def genprime(x,y):
    primes=[True]*(y+1)
    primes[0]=primes[1]=False
    for p in range(2,ceil(sqrt(y))):
        if primes[p]==True:
            for i in range(p*p,y+1,p):
                primes[i]=False
    for i in range(x,y+1):
        if primes[i]==True:
            print(i,end =' ')
while True:
    x,y=map(int,input().split())
    genprime(x,y)