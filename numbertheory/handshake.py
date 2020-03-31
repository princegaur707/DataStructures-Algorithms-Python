def handshake(n,k):
    cnt=0
    for i in range(n):
        if(i<k):
            cnt+=(n-(i+1)-1)
        else:
            cnt+=(n-(i+1))
    return cnt
while True:
    try:
        a,b=map(int,input("Enter n & k:   ").split())
        print(handshake(a,b))
    except:
        print("That was invalid input!")
        break