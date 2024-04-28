class ab:
    branch="cse" #inst var
    def __init__(self,a) -> None:
        ab.x=10 
        self.a=a
    def fun(self):
        print("fun1",self.branch,self.x)
        print("fun1",ab.branch,ab.x)
o=ab(3)
o.fun()#fun1 cse 10 \n fun1 cse 10
