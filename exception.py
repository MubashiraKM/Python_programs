def fun(l,ind):
    try:
        a=l.copy()
        a[0]=l[0]/l[ind]
    except ValueError:
        print("Value Error")
    finally:
        print("end of fun")
l=[1,2,3,4,5]
try:
    fun(l,5)
    #raise IndexError("abcd") #raise errorname
except IndexError:
    print("Index error")
finally:
    print("End of block")