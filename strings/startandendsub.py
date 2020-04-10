#Check all the variations of string(not subset which start and end with 1)
from itertools import combinations
t=int(input())
while t:
    def powerset(str1):
        res = [str1[x:y] for x, y in combinations(range(len(str1) + 1), r = 2)] 
        return res
    n=int(input())
    str1=input()
    p=list(powerset(str1))
    cnt=0
    for i in p:
        try:
            if i[0]=='1' and i[-1]=='1':
                cnt+=1
        except:
            pass
    print(cnt)
    t-=1