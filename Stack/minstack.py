#https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/529/week-2/3292/
class MinStack(object):
    
    def __init__(self):
        self.stack = []
        
    def push(self, x):
        self.stack.append((x, min(self.getMin(), x))) 
        #print(self.stack)
    def pop(self):
        self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        
    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return sys.maxsize