class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class revsll:
    def __init__(self) -> None:
        self.head=None
    def insertatbeg(self,data):#insertion at the beginning
        if self.head==None:
            self.head=node(data)
        else:
            new=node(data)
            new.next=self.head
            self.head=new
    def printing(self):#printing the list
        if self.head==None:
            return
        else:
            i=self.head
            while i:
                print(i.data)
                i=i.next
    def reverse_sll(self):#reversing a list
            print("Reverse of sll:")
            prev=None
            curr=self.head
            nxt=self.head.next
            while curr:
                curr.next=prev
                prev=curr
                curr=nxt
                if nxt:
                    nxt=nxt.next
            self.head=prev
    def delatbeg(self):#deleting at the beginning
        if self.head==None:
            return
        self.head=self.head.next
    def delatend(self):#deleting at the end
        if self.head==None:
            return
        if self.head.next==None:
            self.head=None
        i=self.head
        while i.next.next:
            i=i.next
        i.next=None
        #insert in the middle
    def insatmid(self,data,c):
        new=node(data)
        i=self.head
        a=1
        while a!=c-1:
            i=i.next
            a+=1
        new.next=i.next
        i.next=new
l=[2,4,6,7,8,9]
o=revsll()
print("SLL:")
for i in l:
    o.insertatbeg(i)
o.printing()
# print("Reverse of the list:")
o.reverse_sll()
o.printing()
o.delatbeg()
print("del at beg:")
o.printing()
o.delatend()
print("del at end:")
o.printing()
print("insert at mid:")
o.insatmid(10,2)
o.printing()