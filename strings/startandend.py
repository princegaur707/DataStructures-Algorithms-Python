#Check all the variations of string(not subset which start and end with 1)
from itertools import combinations,chain
t=int(input())
while t:
    def powerset(str1):
        str1=list(str1)
        return chain.from_iterable(combinations(str1,r) for r in range(len(str1)+1))
    n=int(input())
    str1=input()
    p=list(powerset(str1))
    print(p)
    cnt=0
    for i in p:
        try:
            if i[0]=='1' and i[-1]=='1':
                cnt+=1
        except:
            pass
    print(cnt)
    t-=1