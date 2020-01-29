n=int(input("enter steps for fibonacci: "))

def fibo(n):
        s=[]
        s.append(1)
        s.append(1)
        print(s[0],s[1],end=' ')
        for i in range(2,n):
            s.append(s[i-1]+s[i-2])
            print(s[i],end=" ") 
            i=i+1      
fibo(n)