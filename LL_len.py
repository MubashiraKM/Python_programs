class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self) -> None:
        self.head=None
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            i=self.head
            while i.next:
                i=i.next
            i.next=new
    def printing(self):
        if self.head==None:
            return
        i=self.head
        c=0
        while i:
            #print(i.data)
            i=i.next
            c=c+1
        print("length of LL:",c)
l=[1,2,3,4,5]
o=sll()
for i in l:
    o.insertatend(i)
o.printing()