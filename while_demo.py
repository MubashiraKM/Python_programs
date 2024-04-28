s="abcd efghsf debgmrg"
i=0
print(len(s))
while i<len(s) and s[i]!=" ":
    print(s[i],end=" ")
    i+=1

#another method
s="abcd efghsf debgmrg"
for i in range(len(s)):
    if s[i]==' ':
        break
    print(s[i])