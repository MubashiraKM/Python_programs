class node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        self.prev=None
class rev_dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatbeg(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            new.next=self.head
            self.head.prev=new
            self.head=new
    def reverse_dll(self):
       curr=self.head
       while curr:
           if curr.next==None:
               self.head=curr
           curr.next,curr.prev=curr.prev,curr.next
           curr=curr.prev
    def printing(self):
        if self.head==None:
            return
        else:
            i=self.head
            while i:
                print(i.data)
                i=i.next
o=rev_dll()
for i in range(1,6):
    o.insertatbeg(i)
print("DLL:")
o.printing()
o.reverse_dll()
print("reverse:")
o.printing()