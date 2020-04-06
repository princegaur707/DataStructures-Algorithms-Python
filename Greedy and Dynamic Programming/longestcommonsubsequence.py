# https://leetcode.com/problems/longest-common-subsequence/
# T.C O(n*m)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        x = text1
        y = text2
        n = len(text1)
        m = len(text2)
        mat = [[0]*(m+1) for i in range(n+1)]
        print(mat)
        for i in range(0,n+1):
            for j in range(0,m+1):
                if i == 0 or j == 0:
                    mat[i][j]=0
                elif x[i-1] == y[j-1]:
                    mat[i][j] = mat[i-1][j-1]+1
                else:
                    mat[i][j] = max(mat[i-1][j],mat[i][j-1])
        #print(mat[n][m])
        return mat[n][m]
