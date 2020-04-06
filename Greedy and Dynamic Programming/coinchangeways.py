# https://leetcode.com/problems/coin-change-2/
# Number of ways/combination that make the amount
# T.C O(n^2)
# rows represent the total
# cols represent the denomination
# 0 1 KnapSack Problem
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0]*(amount+1) for i in range(len(coins)+1)]
        for i in range(len(coins)+1):
            for j in range(amount+1):
                if j == 0:
                    dp[i][j] = 1
                elif i==0:
                    dp[i][j]=0
                elif j>=coins[i-1]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
