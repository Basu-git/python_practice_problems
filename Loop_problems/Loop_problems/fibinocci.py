n=int(input("Enter a number: "))
a=0
b=1
digit=0
while digit<n:
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    digit+=1
    
    