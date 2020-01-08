8.1)
n=int(input("enter value: "))
for i in range(1,n+1):
    for j in range(i):
        print("*", end =" ")
    print()
		
#Output :enter value: 5
#  * 
#  * * 
#  * * * 
#  * * * * 
#  * * * * * 

8.2)
n=int(input("enter value: "))
for i in range(1,n+1):
    for j in range(i):
        print(j+1, end =" ")
    print()
	

#Output :
#enter value: 5
#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5 

8.3)
n=int(input("enter value: "))
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ", end =" ")
    for k in range(i):
        print(" * ", end =" ")
    print()

#Output :
#enter value: 5
#         *  
#       *   *  
#     *   *   *  
#   *   *   *   *  
# *   *   *   *   *  

8.4)
n=int(input("enter value: "))
for i in range(1,n+1):
    for j in range(n,i,-1):
        print(" ", end =" ")
    for k in range(i):
        print(i, end =" ")
    print()

#Output : 
#enter value: 5
#        1 
#      2 2 
#    3 3 3 
#  4 4 4 4 
#5 5 5 5 5 
