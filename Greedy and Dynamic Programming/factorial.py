# nth factorial using memo
# T.C O(n)
fact = [1,1]

t = int(input())
while t:
    n = int(input())
    try:
        print(fact[n])
    except:
        for i in range(len(fact),n+1):
            fact.append(fact[-1]*i)
        print(fact[n])
    t=t-1
