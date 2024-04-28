#take a sentence input from user and reverse the sentence word by word
#ip- programming in python
#op- python in programming
s=input()
s=s.split()
s=s[::-1]
s=" ".join(s)
print(s)