class a:
    def __init__(self,a) -> None:
        self.a=a
    def fun(self,x):
        self.x=x
        print("fun1")
o=a(3)
o.p=10
print(o.a,o.p)#3 10
o.fun(3)#fun1
a.fun(o,3)#fun1
#a.fun(3)-error, 1 argument missing