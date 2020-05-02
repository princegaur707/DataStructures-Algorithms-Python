#deletefirst,deletelast,deleteany(count can also be defined),insert,view
class node():
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist():
    def __init__(self):
        self.start=None
    def insert(self,value):
        newNode=node(value)
        if self.start==None:
            self.start=newNode
        else:
            temp=self.start
            while temp.next!=None:
                temp=temp.next
            temp.next=newNode
    def deletefirst(self):
        print("Deleting first node........")
        if self.start==None:
            print("Linked list is empty!")
        else:
            self.start=self.start.next
    def deletelast(self):
        print("Deleting last node.........")
        if self.start==None:
            print("Linked list is empty!")
        else:
            temp=self.start
            while temp.next.next!=None:
                temp=temp.next
            temp.next=None
    def deleteany(self,value,count):
        print(f"Deleting {value},{count} no. of times")
        c=0
        if self.start==None:
            print("Linked list is empty!")
        else:
            temp=self.start
            if temp.data==value:
                c+=1
                self.start=self.start.next
            while temp!=None and c<=count:
                if temp.next!=None:
                    if temp.next.data==value:
                        c+=1
                        print("We have found it and so we are deleting.......")
                        temp.next=temp.next.next
                temp=temp.next
            if c==0:
                print("No such number exists in linked list!")
    def viewlist(self):
        if self.start==None:
            print("Linked list is empty!")
        else:
            temp=self.start
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.next
        print("\n")
obj=linkedlist()
obj.insert(1);obj.insert(2);obj.insert(3);obj.insert(4);obj.insert(2);obj.insert(2);obj.insert(1);obj.insert(5);obj.insert(6)
obj.viewlist()
obj.deletefirst()
obj.viewlist()
obj.deletelast()
obj.viewlist()
obj.deleteany(2,2)
obj.viewlist()
