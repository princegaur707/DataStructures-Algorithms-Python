def gcd(a,b):
    if(b==0):
        return a
    return gcd(b,a%b)
t=int(input("Enter no. of test cases: "))
while t:
    a,b=(map(int,input().split()))
    print(gcd(a,b))
    t-=1
