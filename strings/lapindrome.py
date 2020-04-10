from collections import Counter
t=int(input())
while t:
    str1=input()
    l=len(str1)
    c=0
    if l%2==0:
        if Counter(str1[:l//2])==Counter(str1[l//2:]):
            c=1
            print("YES")
        if(c==0):
            print("NO")
    else:
        if Counter(str1[:l//2])==Counter(str1[l//2+1:]):
            c=1
            print("YES")
        if(c==0):
            print("NO")
    t-=1