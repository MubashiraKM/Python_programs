s1=int(input("Sub1:"))
s2=int(input("Sub2:"))
s3=int(input("Sub3:"))
s4=int(input("Sub4:"))
s5=int(input("Sub5:"))
p=((s1+s2+s3+s4+s5)/500)*100
if(p>=75):
    print("Grade A")
elif(p>=60 and p<75):
    print("Grade B")
elif(p>=35 and p<60):
    print("Grade C")
else:
    print("Fail")
    if(p<35):
        print(True)
    elif(p!=35):
        print("no")