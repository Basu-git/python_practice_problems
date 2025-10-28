n=int(input("Enter how many  fib number: "))
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,b+a
    
