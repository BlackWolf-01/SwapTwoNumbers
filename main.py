#Program to swap two numbers without using a third variable
def swapone(a,b):
    #Code to swap a and b
    a=a^b
    b=a^b
    a=a^b
    print('After swapping a=',a,'b=',b)
def swaptwo(a,b):  
    a=(a&b)+(a|b)
    b=a+(~b)+1
    a=a+(~b)+1
    print('After swapping a=',a,'b=',b)
swapone(4,7)
swaptwo(7,1)       