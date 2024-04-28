y=int(input())
'''if(y%4==0):
    if(y%100==0):
        if(y%400==0):
         print("leap year")
        else:
           print("Not leap year")
    else:
       print("leap year")
else:
    print("Not leap year")'''

"""
if(y%100==0 and y%400==0):
    print("Leap year")
elif(y%100!=0 and y%4==0):
    print("Leap year")
else:
    print("not leap year")"""

if(y%400==0 or y%100!=0 and y%4==0):
    print("Leap year")
else:
    print("Not leap year")