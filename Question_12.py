#Operaions performed: insert beginning, insert end, traverse, count no of nodes, reverse linked list
class Node:
    def __init__(self,data=None,address=None):
        self.data=data
        self.address=None
class Linklist:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,data):
        temp=Node(data)
        if self.head==None:
            self.head=temp
            return
        else:
            temp.address=self.head
            self.head=temp
    
    def insert_end(self,data):
        if self.head==None:
            self.head=Node(data,None)
            return
        temp=self.head
        while temp.address:
            temp=temp.address
        temp.address=Node(data,None)
            
    def printdata(self):
        count=0
        if self.head is None:
            print("Empty linked list")
            return
        temp=self.head 
        while temp:
            count=count+1
            print(temp.data," ")
            temp=temp.address 
            
    def reverse(self):
        prev=None
        curr=self.head
        while curr:
            next=curr.address
            curr.address=prev
            prev=curr
            curr=next
        self.head=prev
            
obj=Linklist()
obj2=Linklist()

status=1
while status==1:
    obj.insert_end(int(input("Enter data : ")))
    status=int(input("Enter status 0 for exit and 1 for addin data to linked list : "))
obj.printdata()
status=1
while status==1:
    obj2.insert_at_beginning(int(input("Enter data : ")))
    status=int(input("Enter status 0 for exit and 1 for addin data to linked list : "))
obj2.printdata()

obj.reverse()
print("reverse : ")
obj.printdata()



    