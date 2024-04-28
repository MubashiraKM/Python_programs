class a:
    def fun(self):
        print("fun1")
    def fun2(self):
        print("fun2")
class b(a):
    def fun(self):
        print("fun3")
    def fun4(self):
        print("fun4")
class c(b):
    def fun(self):
        print("fun5")
    def fun6(self):
        print("fun6")
o=a()
p=b()
d=c()
p.fun()#fun3
d.fun()#fun3- importance to function of the same class
d.fun2()