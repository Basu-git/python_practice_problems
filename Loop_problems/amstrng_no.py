n=int(input("Enter a number: "))
m=n
ang=len(str(n))
sum=0
while n>0:
    c=n%10
    sum+=c**ang
    n=n//10
    
if sum==m:
    print('Given number is a angstrom number')
else:
    print("Given number is not a angstrom number")