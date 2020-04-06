# nth fibonacci using memo
# https://leetcode.com/problems/fibonacci-number/
# T.C O(n)
class Solution:
    fibonacci = [0,1]
    def fib(self, n: int) -> int:
        try:
            return self.fibonacci[n]
        except:
            for i in range(len(self.fibonacci),n+1):
                self.fibonacci.append(self.fibonacci[-1]+self.fibonacci[-2])
            print(self.fibonacci)
            return self.fibonacci[n]
