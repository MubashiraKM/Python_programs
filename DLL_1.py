class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class dll:
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
    def insertatend(self,data):
        if self.head==None:
            self.head=node(data)
            self.tail=self.head
        else:
            new=node(data)
            self.tail.next=new
            new.prev=self.tail
            self.tail=new
    def printing(self):
        if self.head==None:
            return
        else:
            i=self.head
            while i:
                print(i.data)
                i=i.next
    def delatbeg(self):#deleting at the beginning
        if self.head==None:
            return
        self.head=self.head.next
        self.head.prev=None
    def delatend(self):
        if self.head==None:
            return
        self.tail=self.tail.prev
        self.tail.next=None
o=dll()
for i in range(1,6):
    o.insertatend(i)
o.printing()
o.delatbeg()
print("del at beg:")
o.printing()
o.delatend()
print("del at end:")
o.printing()