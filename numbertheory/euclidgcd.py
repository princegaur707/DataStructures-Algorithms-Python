def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
t=int(input())
while t:
    a,b = map(int,input().split())
    print(gcd(a,b))
    t=t-1