# https://leetcode.com/problems/unique-paths/
# total ways to reach from top left to right bottom in a matrix
# you can only move bottom,right at a time and path should be unique
class Solution:
    def uniquePaths(self, r: int, c: int) -> int:
        dp = [[0]*c for i in range(r)]
        for i in range(r):
            for j in range(c):
                if i==0 or j==0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
                
        return dp[-1][-1]
    

