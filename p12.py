def fun(x):
    n=x
    while(x>1):
        x=x-1
        n=n*x
        
    print("factorial of the given number is: ",n)
    
a=int(input("enter number: "))
fun(a)