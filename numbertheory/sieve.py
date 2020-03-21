# T.C n*log(log(n))
def generatePrimes(n):
    res = [True]*(n+1)
    res[0] = False
    res[1] = False
    p = 2
    while p*p <= n:
        if res[p] == True:
            i = p*p
            while i <= n:
                res[i] = False
                i=i+p
