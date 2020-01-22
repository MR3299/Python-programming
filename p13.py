def fun(x):
    if(x == 1): print("nor prime nor composite")
    return
    for i in range(x-1,1,-1):
        if(x%i==0):
            print(x," is not a prime number")
            return
    print(x," is a prime number")
            
a=int(input("enter number: "))
fun(a)