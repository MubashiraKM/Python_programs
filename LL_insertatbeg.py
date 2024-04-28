class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self) -> None:
        self.head=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
l=[1,2,3,4,5]
o=sll()
for i in l:
    o.insertatbeg(i)
#print(head.data,head.next.data,head.next.next.data)