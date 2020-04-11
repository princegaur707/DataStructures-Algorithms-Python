class Solution:
    def findClosestElements(self, arr, k, x):
        arr1=[]
        i=j=n=arr.index(x)
        arr1.append(arr[n])
        l=len(arr)
        while len(arr1)!=k:
            if i-1>=0:
                arr1.append(arr[i-1])
                i-=1
            if j+1<l and len(arr1)!=k:
                arr1.append(arr[j+1])
                j+=1
        arr1.sort()
        return arr1
obj=Solution()
print(obj.findClosestElements([1,2,3,4,5], 4, 3))