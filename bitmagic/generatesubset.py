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
        for i in range(2**n):       # Why not 0,2**n why only this
            bitmask = bin(i)[2:]             # Why from 3: 
            print(bitmask)
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        return output
ob=Solution()
print(ob.subsets([1,2,3]))
