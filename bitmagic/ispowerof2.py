def ispoweroftwo(n):
    return n and (not(n & (n-1)))

t = int(input())
while t:
    n = int(input())
    print(ispoweroftwo(n))
    t=t-1
