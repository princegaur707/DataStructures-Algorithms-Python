'''
Write a program to check whether a given number is an ugly number.
https://leetcode.com/problems/ugly-number/
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.'''
class Solution:
    def maxDivide(self,a,b):
        while a%b == 0:
            a = a // b
        return a
    def isUgly(self, num: int) -> bool:
        if num<=0:
            return False
        num = self.maxDivide(num,2)
        num = self.maxDivide(num,3)
        num = self.maxDivide(num,5)
