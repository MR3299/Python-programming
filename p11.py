a=int(input("enter value of a"))
b=int(input("enter value of b"))
c=int(input("enter value of c"))


def root(a,b,c):

    d=(b**2)-(4*a*c)
    k=d**(0.5)
    x=((-b)+k)/(2*a)
    y=((-b)-k)/(2*a)

    print("first root= ",x)
    print("second root= ",y)
    
root(a,b,c)