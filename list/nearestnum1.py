class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int):
        if len(arr) == k:
            return arr
        
        start, end = 0, len(arr)-k
        while start+1 < end:
            mid = start+(end-start)//2
            if abs(x-arr[mid]) <= abs(arr[mid+k]-x): # start is more preferred
                end = mid
            else: # end is more preferred
                start = mid
        
        if abs(x-arr[start]) <= abs(arr[start+k]-x):
            return arr[start:start+k]
       	else:
            return arr[end:end+k]
    