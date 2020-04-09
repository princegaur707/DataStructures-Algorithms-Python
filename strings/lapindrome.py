t=int(input())
while t:
    str1=input()
    l=len(str1)
    c=0
    if l%2==0:
        if set(str1[:l//2])==set(str1[l//2:]):
            c=1
            print("YES")
        if(c==0):
            print("NO")
    else:
        if set(str1[:l//2])==set(str1[l//2+1:]):
            c=1
            print("YES")
        if(c==0):
            print("NO")
    t-=1