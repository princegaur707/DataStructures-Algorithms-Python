# check if kth bit is set from right
t = int(input())
while t:
    n,k = map(int,input().split())
    print(str(bin(n))[2:])
    if(n & (1 << (k-1))):    #How this & operation is performed
        print("SET")
    else:
        print("NOT SET")
    t=t-1
