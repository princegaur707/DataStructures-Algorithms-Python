''' Stack
LIFO / FILO
push(), pop(), isEmpty() and peek() all take O(1) time. We do not run any loop in any of these operations.
Push Adds an item in the stack. If the stack is full, then it is said to be an Overflow condition.
Pop: Removes an item from the stack. The items are popped in the reversed order in which they are pushed. If the stack is empty, then it is said to be an Underflow condition.
Peek or Top: Returns top element of stack.
isEmpty: Returns true if stack is empty, else false.'''
class Stack:
    def __init__(self,maxsize):
        self.top = -1
        self.maxsize = maxsize
        self.stack = [0]*maxsize
    
    def push(self,element):
        if self.isFull():
            return False
        else:
            self.top=self.top+1
            self.stack[self.top]=element
            return True
    
    def pop(self):
        if self.isEmpty():
            return False
        else:
            var = self.stack[self.top]
            self.top = self.top - 1
            print("Popped element is",var) 
            return var  # equivalent to return True  
        
    def peek(self):
        if self.isEmpty():
            return False
        else:
            return self.stack[self.top]
    
    def isEmpty(self):
        if self.top < 0:
            print("Stack Empty")
            return True
        else:
            print("Stack is not Empty")
            return False
        
    def printStack(self):
        if self.isEmpty():
            return False
        else:
            tmp = self.top
            while tmp != -1:
                print(self.stack[tmp])
                tmp=tmp-1
            return True
                
    def isFull(self):
        if self.top >= self.maxsize -1:
            print("Stack Overflow")
            return True
        else:
            print("Stack is not Overflow")
            return False