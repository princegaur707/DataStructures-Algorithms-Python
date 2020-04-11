class Solution:
    def findClosestElements(self, arr, k, x):
        res = []
        for i in arr:
            res.append((i,abs(i-x)))
        res.sort(key = lambda x:[x[1],x[0]])
        print(res)
        returnres = []
        for i in range(k):
            returnres.append(res[i][0])
        returnres.sort()
        return returnres
obj=Solution()
print(obj.findClosestElements([1,2,3,4,5], 4, 3))