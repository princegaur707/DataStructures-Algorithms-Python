# T.C logn
# Implementation of Brian Kernighan’s Algorithm:
def cntsetbit(n):
    cnt = 0
    while n:
        n = n & (n-1)
        cnt = cnt + 1
    return cnt
t = int(input())
while t:
    n = int(input())
    print(cntsetbit(n))
    t=t-1
    