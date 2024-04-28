class node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=node(1) 
a.next=node(2) #b=node(2) a.next=b
a.next.next=node(3) #c=node(3) b.next=c
print(a,a.data,a.next)
print(a.next,a.next.data,a.next.next)
print(a.next.next,a.next.next.data,a.next.next.next)
