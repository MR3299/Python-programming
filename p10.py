x=int(input("enter 1st value:"))
y=int(input("enter 2nd value:"))
z=int(input("enter 3rd value:"))

def fun(x,y,z):
   
    if(x>y):
        if(x>z):
            print(x," is greatest")
        else:
            print(z," is greatest")
    elif(y>z):
        print(y," is greatest")
    else:
        print(z," is greatest")
    
fun(x,y,z)

#Output : 
#enter 1st value:7
#enter 2nd value:5
#enter 3rd value:6
#7  is greatest
