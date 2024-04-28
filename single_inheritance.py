class a:
    def fun1(self):
        print("fun1")
    def fun2(self):
        print("fun2")
class b(a):
    def fun3(self):
        print("fun3")
    def fun4(self):
        print("fun4")
o=a()
p=b()
p.fun1()