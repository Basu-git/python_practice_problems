n=int(input("Enter a number: "))
m=n
s=0
while n>0:
    c=n%10
    s=s*10+c
    n=n//10
if s==m:
    print("Given number is a palindrome number")
else:
    print("Given number is not a palindrome number number")