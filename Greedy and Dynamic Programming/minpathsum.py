'''
https://leetcode.com/problems/minimum-path-sum/
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        r,c = len(grid),len(grid[0])
        for i in range(1,r):
            grid[i][0]+=grid[i-1][0]
        for j in range(1,c):
            grid[0][j]+=grid[0][j-1]
        for i in range(1,r):
            for j in range(1,c):
                grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]