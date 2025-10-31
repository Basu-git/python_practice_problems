n=int(input("Enter a number: "))
factorial=1
for i in range (2,n+1):
    if n!=1:
        factorial*=i
    else:
        print("Factorial = 1")
print(factorial)

n=int(input("Enter  ; "))
i=2
f=1
while i<=n:
   if n!=1:
       f*=i
       i+=1
   else:
       print("Factorial=1")
print(f)