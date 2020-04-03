'''
https://leetcode.com/problems/subsets/
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
# T.C and S.C O(N*2^N)
'''
class Solution:
    def subsets(self, nums):
        n = len(nums)
        output = []
        for i in range(2**n,2**(n+1)):       # Why not 0,2**n: b/c if we take 0 it will directly take only 0 which will make index out of range 
            bitmask = bin(i)[3:]             # from 3: as it will be starting from 16 which is 1000 so to make it 1 
            print(bitmask)
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])  # It will become index out of range if not taken from 16
        return output
ob=Solution()
print(ob.subsets([1,2,3]))
