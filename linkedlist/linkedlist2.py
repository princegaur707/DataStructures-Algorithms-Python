class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.start=None
    def insertatlast(self,value):
        newNode=node(value)
        if self.start==None:
            self.start=newNode
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
    def view(self):
        if self.start==None:
            print("Linked list is empty!")
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.next
    def insertatfront(self,value):
        newNode=node(value)
        if self.start==None:
            self.start=newNode
        else:
            newNode.next=start
            start=newNode
obj=linkedlist()
