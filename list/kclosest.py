class Solution:
    def findClosestElements(self, arr, k, x) :
        left,right=0,len(arr)-k
        while left<right:
            mid=(left+right)//2
            if x-arr[mid]<arr[mid+k]-x:
                left=mid+1
            else:
                right=mid
        return arr[left:left+k]
obj=Solution()
print(obj.findClosestElements([1,2,3,4,5],4,3))
