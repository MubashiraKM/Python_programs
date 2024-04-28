class circle:
    def __init__(self,r):
        self.r=r
    def printing(self):
        print("Area of circle is:",3.14*r**2)#or import math (module) and use print(math.pi*self.r)
class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def printing(self):
        print("Area of rectangle is:",l*b)#print(self.l*self.b)
l=float(input())
b=float(input())
r=float(input())
o=circle(r)
o1=rectangle(l,b)
o.printing()
o1.printing()