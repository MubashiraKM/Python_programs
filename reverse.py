'''a=int(input())
t=a
r=0
s=0
while t>0:
    r=t%10
    t=t//10
    s=s*10+r
print(s)
#palindrome
n=input()
if n==n[::-1]:
    print("Palindrome")
else:
    print("not palindrome")'''
#reverse
n=input()
n=n[::-1]
print(n)