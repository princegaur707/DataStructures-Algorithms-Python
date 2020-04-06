# for n = 1 {1} -> 1
# for n = 2 {1,1},{2} -> 2
# for n = 3 {1,1,1} {2,1} {1,2} -> 3
# for n = 4 {1,1,1,1,} {2,1,1} {1,2,1} {1,1,2} {2,2} -> 5
# f(n) = f(n-1) + f(n-2) -> two steps
# f(n) = f(n-1) + fi(n-2) + f(n-3) -> three steps
# https://leetcode.com/problems/climbing-stairs/
class Solution:
    res = []
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        self.res=[0]*(n+1)
        self.res[1],self.res[2] = 1,2
        for i in range(3,n+1):
            self.res[i] = self.res[i-1] + self.res[i-2]
        return self.res[n]
