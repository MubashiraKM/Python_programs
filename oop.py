class cse:
    #constructor
    def __init__(self,name,rollno):
        self.n=name
        self.rn=rollno
        print("constructor")
    def fun(self):
        print(self.n,self.rn)
s1=cse('rahul',34)
s2=cse('raghu',36)
s1.fun()
s2.fun()
#properties can be accessed outside the class
print(s1.n,s2.n)