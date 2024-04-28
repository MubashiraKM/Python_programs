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
        self.tail.next=self.head
        self.head.prev=self.tail
    def printing(self):
        if self.head==None:
            return
        else:
            i=self.head.next
            print(self.head.data)
            while i!=self.head:
                print(i.data)
                i=i.next
                # OR
            # i=self.head
            # while i.next!=self.head or :
            #     print(i.data)
            #     i=i.next
            # print(i.data)
o=dll()
for i in range(1,6):
    o.insertatbeg(i)
o.printing()