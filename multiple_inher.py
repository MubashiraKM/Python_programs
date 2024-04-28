class a:
    def fun(self):
        print("fun1")
    def fun2(self):
        print("fun2")
class b():
    def fun(self):
        print("fun3")
    def fun4(self):
        print("fun4")
class c(a,b):
    def fun5(self):
        print("fun5")
o=a()
p=b()
d=c()
p.fun()#fun3-b
d.fun()#fun1-a
d.fun2()#fun2-a
d.fun4()#fun4-b
#function overriding-2 functions of same name in same class is not supported in python.