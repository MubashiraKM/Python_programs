# recursion- factorial of a number.
def fun(n):
    if n==1:
        return 1
    return n*fun(n-1)
print(fun(5))

#or
def fun(n):
    if n==0:
        return 1
    return n*fun(n-1)
print(fun(5))