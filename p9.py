x=int(input("enter x value:"))
y=int(input("enter y value:"))

def fun(x,y):
    c=x
    x=y
    y=c
    print("after swapping:- x =",x," y = ",y)
    
fun(x,y)

#Output :
#enter x value:15
#enter y value:165
#after swapping:- x = 165  y =  15
