'''define a class royal_enfield and have constructor take values for model_name,color and mileage.
Also,create 3 objects for this class and print all three properties of objects outside the class
(print function should be outside the class)'''
class royal_enfield:
    def __init__(self,model_name,color,mileage):
        self.mod=model_name
        self.c=color
        self.m=mileage
print("Model 1:")
mod1=input()
cl1=input()
mil1=int(input())
print("Model 2:")
mod2=input()
cl2=input()
mil2=int(input())
print("Model 3:")
mod3=input()
cl3=input()
mil3=int(input())
ob1=royal_enfield(mod1,cl1,mil1)
ob2=royal_enfield(mod2,cl2,mil2)
ob3=royal_enfield(mod3,cl3,mil3)
print(ob1.mod,ob1.c,ob1.m)
print(ob2.mod,ob2.c,ob2.m)
print(ob3.mod,ob3.c,ob3.m)