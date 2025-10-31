n=int(input("Enter a number: "))
c=0
while n>0:
    c=c*10+n%10
    n=n//10
print(c)
