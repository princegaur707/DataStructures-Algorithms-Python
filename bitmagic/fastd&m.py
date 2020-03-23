# x >> y , x divide by 2^y
# x << y , x multiply by 2^y
t = int(input())
while t:
    n = int(input())
    print(n>>1,n<<1)
    t=t-1
