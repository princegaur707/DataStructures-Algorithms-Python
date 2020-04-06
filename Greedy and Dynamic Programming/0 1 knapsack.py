# return max profit
# T.C O(n^2)
# rows -> wt of items with their values
# cols -> total wt
# i == 0 or j==0 base condition
# dp[i-1][j] if we dont take that item and previous value is added
# maxval() -> maxval(if we take that item and it's val is added and ...
# value of wt left is also added,dp[i-1][j])
def knapSack(W,wt,val,n):
    dp=[[0]*(W+1) for i in range(n+1)]
    for i in range(0,n+1):
        for j in range(0,W+1):
            if i == 0 or j== 0:
                dp[i][j] = 0
            elif wt[i-1]<=j:
                dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
                
    return dp[-1][-1] 

val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapSack(W, wt, val, n))
val = [1,4,5,7]
wt = [1,3,4,5]
W = 7
print(knapSack(W, wt, val, n))

