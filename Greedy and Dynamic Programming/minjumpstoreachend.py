# https://leetcode.com/problems/jump-game-ii/
# T.C O(n^2) / Dynamic
# Naive Soln 90/92 Test Cases
class Solution:
    def jump(self, nums: List[int]) -> int:
        from sys import maxsize
        if len(set(nums))==1:
            return len(nums)-1
        jumps = [100]*(len(nums))
        jumps[0] = 0
        for i in range(1,len(jumps)):
            for j in range(0,i):
                if j+nums[j] >= i:
                    jumps[i] = min(jumps[i],jumps[j]+1)
        return jumps[-1]
# T.C O(n)
# greedy approach
'''
The main idea is based on greedy. Let's say the range of the current jump is [curBegin, curEnd], curFarthest is the farthest point that all points in [curBegin, curEnd] can reach.
Once the current point reaches curEnd, then trigger another jump, and set the new curEnd with curFarthest, then keep the above steps, as the following:'''
class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps , curend , curfarthest = 0,0,0
        for i in range(0,len(nums)-1):
            curfarthest = max(curfarthest,i+nums[i])
            if i==curend:
                jumps=jumps+1
                curend = curfarthest  
        return jumps
