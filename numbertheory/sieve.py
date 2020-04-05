#Sieve of Eratosthenes
#print all primes in range(x,y)
# T.C n*log(log(n))
from math import ceil,sqrt
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
while True:
    try:
        x,y = map(int,input("\nEnter range(x y):   ").split())
        genPrimes(x,y)
    except:
        print("Invalid input!")
        break         
