# https://leetcode.com/problems/coin-change/
# T.C O(n^2)
# rows -> represent denominations
# cols -> represent amount
def mincoinsneeded(coins,target):
    dp = [[0]*(target+1) for i in range(len(coins)+1)]
    for i in range(0,len(coins)+1):
        dp[i][0]=1
    for i in range(1,len(coins)+1):
        for j in range(1,target+1):
            if i==1:
                dp[i][j]=j            
            elif j>=coins[i-1]:
                dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i-1]])
            else:
                dp[i][j]=dp[i-1][j]
    dp[-1][-1]


coins = [1,5,6,9]
target = 10
mincoinsneeded(coins,target)
