#https://leetcode.com/problems/happy-number/
class Solution:
    def squaresum(self,n):
        sm = 0
        while n!=0:
            dig = n%10
            sm = sm + dig**2
            n=n//10
        return sm
    
    def isHappy(self, n: int) -> bool:
        memo = set()
        while n != 1:
            n = self.squaresum(n)
            if n in memo:
                return False
            else:
                memo.add(n)
        return True
