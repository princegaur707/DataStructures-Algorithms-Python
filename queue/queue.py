class Queue:
    def __init__(self,maxsize):
        self.front = -1 # used to pop/delete/dequeue
        self.rear = -1 # used to push/insert/enqueue
        self.maxsize = maxsize
        self.queue = [None]*maxsize # [0]*maxsize # [0]*self.maxsize
    
    def isEmpty(self):
        if self.front == -1 and self.rear == -1:
            return True
        else:
            return False
    
    def isFull(self):
        if self.rear == self.maxsize - 1:
            return True
        else:
            return False
        
    def enque(self,element):
        if self.isFull():
            return False
        elif self.isEmpty():
            self.rear = self.front = 0
            self.queue[self.rear] = element
            return True
        else:
            self.rear = self.rear + 1
            self.queue[self.rear] = element
            return True
    
    def deque(self):
        if self.isEmpty():
            return False
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            print("Element Dequed",self.queue[self.front])
            self.front = self.front + 1
            return True       
    
    def printQueue(self):
        if self.isEmpty():
            pass
        else:
            tmp1 = self.front
            tmp2 = self.rear
            while tmp1!=tmp2+1:
                print(self.queue[tmp1],end=" ")
                tmp1=tmp1+1
            
            
        