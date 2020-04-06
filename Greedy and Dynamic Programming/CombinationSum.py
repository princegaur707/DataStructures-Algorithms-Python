# https://leetcode.com/problems/combination-sum-iv/submissions/
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        if nums == []:
            return 0
        nums = sorted(nums)
        dp = [0]*(target+1)
        dp[0] = 1
        for sm in range(0,target+1):
            for num in nums:
                if num > sm:
                    break
                if num == sm:
                    dp[sm]+=1
                if num < sm:
                    dp[sm]+=dp[sm-num]                    
        return dp[target]
        
