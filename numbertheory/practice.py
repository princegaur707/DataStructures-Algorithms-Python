def fractionSubtraction(a, b):
    cnt1=(a[0]*b[1]-a[1]*b[0])
    cnt2=(a[1]*b[1])
    def gcd(cnt1,cnt2):
        if(cnt2==0):
            return cnt1
        return gcd(cnt2,cnt1%cnt2)
    g=gcd(cnt1,cnt2)
    return([cnt1/g,cnt2/g])

p=fractionSubtraction([7,10],[3,10])
print(p)