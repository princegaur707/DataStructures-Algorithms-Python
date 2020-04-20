# T.C logn
# Implementation of Brian Kernighan’s Algorithm:
def cntsetbit(n):
    cnt = 0
    while n:
        n = n & (n-1)
        cnt = cnt + 1
    return cnt

while True:
    try:
        n = int(input("\nEnter number:   "))
        print(cntsetbit(n))
    except:
        print("Invalid input!")
        break