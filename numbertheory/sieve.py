#print all primes smaller than or equal to n
# T.C n*log(log(n))
def genprime(n):
    prime=[True]*(n+1)
    prime[0]=False
    prime[1]=False
    p=2
    for i in range(p*p,n+1,1):
        if(prime[i]==True):
            for i in range(p*p,n+1,p):
                prime[i]=False
    for i in range(len(prime)):
        if(prime[i]==True):
            print(i,end=" ")
while True:
    try:
        n=int(input("\nEnter number:   "))
        genprime(n)
    except:
        print("Invalid input!")
        break


