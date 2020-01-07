X=int(input("Enter first number: "))
Y=int(input("Enter second number: "))
c=[]
print("Even Numbers between ",X,"And ",Y," :")
X=X+1
while (X<Y):
    if(X%2==0):
        c=c+[X]
        X=X+1
    else: X=X+1

print(c)
