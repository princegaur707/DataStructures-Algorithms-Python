# https://leetcode.com/problems/longest-increasing-subsequence/
# T.C O(n^2)
def longestincsubseq(arr,n):
    inc = [1]*(n)
    for i in range(1,n):
        for j in range(0,i+1):
            if arr[j] < arr[i]:
                inc[i]=max(inc[i],inc[j]+1)
    return inc

arr = [1,3,6,7,9,4,10,5,6]
print(longestincsubseq(arr,len(arr)))
